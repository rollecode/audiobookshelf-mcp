"""Server instance, client and the call helper every generated tool uses."""

import importlib.metadata
import json
import logging
import os

import httpx
from mcp.server.fastmcp import FastMCP
from mcp.types import Icon

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

APP = "audiobookshelf"
TITLE = "Audiobookshelf"
ENV_URL = "AUDIOBOOKSHELF_URL"
ENV_KEY = "AUDIOBOOKSHELF_TOKEN"
DEFAULT_URL = "http://127.0.0.1:13378"
DEFAULT_PORT = 8570

try:
    __version__ = importlib.metadata.version(f"{APP}-mcp")
except importlib.metadata.PackageNotFoundError:  # running from a source tree
    __version__ = "0.0.0"

_ICON_BASE = os.getenv("MCP_PUBLIC_URL", "").rstrip("/")
_ICON_SIZES = (48, 96, 256)

mcp = FastMCP(
    APP,
    icons=(
        [
            Icon(
                src=f"{_ICON_BASE}/icon.png"
                if size == 256
                else f"{_ICON_BASE}/icon-{size}.png",
                mimeType="image/png",
                sizes=[f"{size}x{size}"],
            )
            for size in _ICON_SIZES
        ]
        if _ICON_BASE
        else None
    ),
    website_url=_ICON_BASE or None,
    instructions=(
        "Manage an Audiobookshelf server: libraries, books, podcasts, "
        "authors, series, collections, playlists, listening sessions and "
        "progress, users, backups and settings. Every route is a tool, named "
        "verb-first: list_* and get_* read, create_* posts, update_* patches "
        "and delete_* removes. "
        "Start with list_api_libraries to get a library id, then "
        "list_api_libraries_by_id_items to browse it. Playback position lives "
        "in the me/progress routes. Ids are strings, not numbers."
    ),
)

mcp._mcp_server.version = __version__

_READ = {
    "readOnlyHint": True,
    "destructiveHint": False,
    "idempotentHint": True,
    "openWorldHint": False,
}
_WRITE = {
    "readOnlyHint": False,
    "destructiveHint": False,
    "idempotentHint": True,
    "openWorldHint": False,
}
_DESTRUCTIVE = {**_WRITE, "destructiveHint": True}

_http: httpx.Client | None = None


def _client() -> httpx.Client:
    global _http
    if _http is None:
        api_key = os.getenv(ENV_KEY)
        if not api_key:
            raise RuntimeError(
                f"{ENV_KEY} is not set. Find your API token in "
                "Audiobookshelf under Settings, Users, your user."
            )
        _http = httpx.Client(
            base_url=(os.getenv(ENV_URL) or DEFAULT_URL).rstrip("/"),
            headers={"Authorization": f"Bearer {api_key}"},
            # A full library listing over a remote proxy genuinely
            # takes minutes; 60s times out on a few hundred items.
            timeout=httpx.Timeout(300.0, connect=15.0),
        )
    return _http


def _err(e: Exception) -> str:
    if isinstance(e, httpx.HTTPStatusError):
        status = e.response.status_code
        if status == 401:
            msg = f"{TITLE} rejected the token. Check {ENV_KEY}."
        elif status == 404:
            msg = "No such resource. Check the id."
        elif status == 400:
            # Servarr returns a validation array that says exactly which field
            # is wrong, which is far more useful than the status alone.
            msg = f"{TITLE} rejected the request: {_detail(e.response)}"
        else:
            msg = f"{TITLE} API error (HTTP {status}): {_detail(e.response)}"
    elif isinstance(e, httpx.ConnectError):
        msg = (
            f"Could not connect to {TITLE}. Check that it is running and "
            f"{ENV_URL} points at it."
        )
    elif isinstance(e, httpx.TimeoutException):
        msg = f"Request timed out. {TITLE} may be busy -- try again."
    else:
        msg = f"{type(e).__name__}: {e}"

    return json.dumps({"status": "error", "message": msg})


def _detail(response: httpx.Response) -> str:
    try:
        return json.dumps(response.json())[:800]
    except ValueError:
        return response.text[:400]


def call(
    method: str,
    path: str,
    query: dict | None = None,
    body: dict | None = None,
    form: dict | None = None,
) -> str:
    """Perform one API call and return its result as a JSON string."""
    try:
        params = {k: v for k, v in (query or {}).items() if v is not None}
        fields = {k: v for k, v in (form or {}).items() if v is not None}
        response = _client().request(
            method,
            path,
            params=params or None,
            json=body,
            data=fields or None,
        )
        response.raise_for_status()

        if not response.content:
            return json.dumps({"status": "success", "result": None})
        try:
            return json.dumps(
                {"status": "success", "result": response.json()}, indent=2
            )
        except ValueError:
            return json.dumps({"status": "success", "result": response.text})
    except Exception as e:
        return _err(e)


def main() -> None:
    import argparse

    from dotenv import find_dotenv, load_dotenv

    from . import extras, tools  # noqa: F401 -- importing registers every tool

    dotenv_path = find_dotenv(usecwd=True)
    if dotenv_path and load_dotenv(dotenv_path, override=False):
        logger.info("Loaded .env from %s", dotenv_path)

    parser = argparse.ArgumentParser(prog=f"{APP}-mcp")
    parser.add_argument(
        "--transport",
        choices=("stdio", "http"),
        default=os.getenv("MCP_TRANSPORT", "stdio"),
    )
    parser.add_argument("--host", default=os.getenv("MCP_HOST", "127.0.0.1"))
    parser.add_argument(
        "--port", type=int, default=int(os.getenv("MCP_PORT", str(DEFAULT_PORT)))
    )
    args = parser.parse_args()

    if args.transport == "stdio":
        mcp.run(transport="stdio")
        return

    if args.host not in ("127.0.0.1", "::1", "localhost"):
        raise SystemExit(
            f"refusing to listen on {args.host}: this server has no login of "
            "its own. Keep it on the local machine and put a proxy in front."
        )

    mcp.settings.host = args.host
    mcp.settings.port = args.port
    logger.info("Listening on http://%s:%d/mcp", args.host, args.port)
    mcp.run(transport="streamable-http")
