"""Call real generated tools and check the requests they build.

The coverage tests read tools.py as text and the runtime tests exercise call()
directly, so without this nothing proves a generated function actually
produces the request its docstring claims.
"""

import json

import httpx
import pytest

from audiobookshelf_mcp import runtime, tools


@pytest.fixture(autouse=True)
def transport(monkeypatch):
    monkeypatch.setenv("AUDIOBOOKSHELF_TOKEN", "k")
    monkeypatch.setenv("AUDIOBOOKSHELF_URL", "http://abs.test")
    runtime._http = None
    seen: dict = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["method"] = request.method
        seen["path"] = request.url.path
        seen["query"] = dict(request.url.params)
        seen["body"] = json.loads(request.content) if request.content else None
        return httpx.Response(200, json={"ok": True})

    runtime._http = httpx.Client(
        base_url="http://abs.test",
        headers={"Authorization": "Bearer k"},
        transport=httpx.MockTransport(handler),
    )
    yield seen
    runtime._http = None


def test_a_collection_read_hits_the_collection(transport):
    result = json.loads(tools.list_libraries())
    assert result["status"] == "success"
    assert transport["method"] == "GET"
    assert transport["path"] == "/api/libraries"


def test_a_path_parameter_lands_in_the_url(transport):
    tools.get_libraries_by_id(42)
    assert transport["path"] == "/api/libraries/42"


def test_a_write_sends_its_payload(transport):
    tools.create_libraries({"name": "Books"})
    assert transport["path"] == "/api/libraries"
    assert transport["body"] == {"name": "Books"}



def test_a_delete_reaches_the_right_path(transport):
    tools.delete_libraries_by_id(7)
    assert transport["method"] == "DELETE"
    assert transport["path"] == "/api/libraries/7"


def test_a_failure_comes_back_as_a_structured_error():
    runtime._http = httpx.Client(
        base_url="http://abs.test",
        transport=httpx.MockTransport(lambda request: httpx.Response(404)),
    )
    result = json.loads(tools.list_libraries())
    assert result["status"] == "error"


def test_annotations_match_what_each_tool_does():
    import asyncio

    registered = {t.name: t for t in asyncio.run(runtime.mcp.list_tools())}
    assert registered["list_libraries"].annotations.readOnlyHint is True
    assert registered["delete_libraries_by_id"].annotations.destructiveHint is True
    assert registered["create_libraries"].annotations.readOnlyHint is False
