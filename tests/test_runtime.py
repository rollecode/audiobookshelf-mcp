import json

import httpx
import pytest

from audiobookshelf_mcp import runtime


@pytest.fixture(autouse=True)
def reset_client(monkeypatch):
    monkeypatch.setenv("AUDIOBOOKSHELF_TOKEN", "k")
    monkeypatch.setenv("AUDIOBOOKSHELF_URL", "http://audiobookshelf.test")
    runtime._http = None
    yield
    runtime._http = None


def install(handler):
    runtime._http = httpx.Client(
        base_url="http://audiobookshelf.test",
        headers={"Authorization": "Bearer k"},
        transport=httpx.MockTransport(handler),
    )


def test_missing_api_key_says_where_to_find_it(monkeypatch):
    monkeypatch.delenv("AUDIOBOOKSHELF_TOKEN", raising=False)
    runtime._http = None
    result = json.loads(runtime.call("GET", "/api/libraries"))
    assert result["status"] == "error"
    assert "AUDIOBOOKSHELF_TOKEN" in result["message"]


def test_none_query_values_are_dropped():
    seen = {}

    def handler(request):
        seen["url"] = str(request.url)
        return httpx.Response(200, json=[])

    install(handler)
    runtime.call("GET", "/api/libraries", query={"page": None, "pageSize": 10})
    assert "pageSize=10" in seen["url"]
    assert "page=" not in seen["url"].replace("pageSize=", "")


def test_empty_body_is_success_not_a_parse_error():
    install(lambda request: httpx.Response(204))
    assert json.loads(runtime.call("DELETE", "/api/libraries/1")) == {
        "status": "success",
        "result": None,
    }


def test_non_json_response_is_returned_as_text():
    install(lambda request: httpx.Response(200, text="pong"))
    assert json.loads(runtime.call("GET", "/ping"))["result"] == "pong"


def test_validation_errors_carry_the_detail():
    install(
        lambda request: httpx.Response(
            400, json=[{"propertyName": "title", "errorMessage": "must not be empty"}]
        )
    )
    message = json.loads(runtime.call("POST", "/api/libraries", body={}))["message"]
    assert "must not be empty" in message


def test_bad_api_key_names_the_variable():
    install(lambda request: httpx.Response(401))
    message = json.loads(runtime.call("GET", "/api/libraries"))["message"]
    assert "AUDIOBOOKSHELF_TOKEN" in message


def test_connection_failure_explains_the_url_variable():
    def handler(request):
        raise httpx.ConnectError("refused", request=request)

    install(handler)
    message = json.loads(runtime.call("GET", "/api/libraries"))["message"]
    assert "AUDIOBOOKSHELF_URL" in message


def test_the_bearer_token_is_sent():
    seen = {}

    def handler(request):
        seen["key"] = request.headers.get("Authorization")
        return httpx.Response(200, json={})

    install(handler)
    runtime.call("GET", "/api/libraries")
    assert seen["key"] == "Bearer k"


def test_every_tool_registers():
    import asyncio

    from audiobookshelf_mcp import extras, tools  # noqa: F401 -- registers the tools

    registered = asyncio.run(runtime.mcp.list_tools())
    assert len(registered) == 211
