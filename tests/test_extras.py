"""The upload path, which the generated tools cannot express."""

import json

import httpx
import pytest

from audiobookshelf_mcp import extras, runtime


@pytest.fixture(autouse=True)
def transport(monkeypatch):
    monkeypatch.setenv("AUDIOBOOKSHELF_TOKEN", "t")
    monkeypatch.setenv("AUDIOBOOKSHELF_URL", "http://abs.test")
    runtime._http = None
    seen: dict = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["path"] = request.url.path
        seen["type"] = request.headers.get("content-type", "")
        seen["body"] = request.content
        return httpx.Response(200, json={"ok": True})

    runtime._http = httpx.Client(
        base_url="http://abs.test",
        headers={"Authorization": "Bearer t"},
        transport=httpx.MockTransport(handler),
    )
    yield seen
    runtime._http = None


@pytest.fixture
def book(tmp_path):
    f = tmp_path / "chapter one.mp3"
    f.write_bytes(b"ID3audio")
    return f


def test_upload_sends_multipart_with_the_file(transport, book):
    result = json.loads(
        extras.upload_book("lib1", "fol1", "Empire of AI", [str(book)], author="Karen Hao")
    )
    assert result["status"] == "success"
    assert transport["path"] == "/api/upload"
    assert transport["type"].startswith("multipart/form-data")
    body = transport["body"]
    assert b"Empire of AI" in body
    assert b"Karen Hao" in body
    assert b"chapter one.mp3" in body
    assert b"ID3audio" in body


def test_upload_requires_at_least_one_audio_file(transport, tmp_path):
    cover = tmp_path / "cover.jpg"
    cover.write_bytes(b"\xff\xd8")
    result = json.loads(extras.upload_book("lib1", "fol1", "X", [str(cover)]))
    assert result["status"] == "error"
    assert "audio file" in result["message"]


def test_upload_rejects_an_unsupported_type(transport, tmp_path):
    bad = tmp_path / "notes.docx"
    bad.write_bytes(b"x")
    result = json.loads(extras.upload_book("lib1", "fol1", "X", [str(bad)]))
    assert result["status"] == "error"
    assert "does not accept" in result["message"]


def test_upload_reports_a_missing_file(transport):
    result = json.loads(extras.upload_book("lib1", "fol1", "X", ["/nope/a.mp3"]))
    assert result["status"] == "error"
    assert "Not a file" in result["message"]


def test_upload_needs_files(transport):
    result = json.loads(extras.upload_book("lib1", "fol1", "X", []))
    assert result["status"] == "error"
    assert "No files given" in result["message"]


def test_missing_upload_permission_is_explained(monkeypatch, book):
    runtime._http = httpx.Client(
        base_url="http://abs.test",
        transport=httpx.MockTransport(lambda request: httpx.Response(403)),
    )
    result = json.loads(extras.upload_book("lib1", "fol1", "X", [str(book)]))
    assert result["status"] == "error"
    assert "upload permission" in result["message"]


def test_podcast_is_created_from_its_feed(transport):
    result = json.loads(
        extras.add_podcast_from_feed("lib2", "fol2", "https://example.com/rss")
    )
    assert result["status"] == "success"
    assert transport["path"] == "/api/podcasts"
