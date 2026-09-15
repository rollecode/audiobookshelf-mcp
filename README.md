<center align="center" style="text-align: center;justify-content:center;">
<div align="center" style="text-align: center;justify-content:center;">
<h1 align="center" style="text-align: center;justify-content:center;">

Audiobookshelf MCP server

<img style="justify-content:center;text-align: center;width: 120px; height: auto;" alt="Audiobookshelf" src="public/logo.png" />

</h1>


![Version](https://img.shields.io/badge/version-1.0.0-blue.svg?style=for-the-badge) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Audiobookshelf](https://img.shields.io/badge/Audiobookshelf-82612C?style=for-the-badge&logo=audiobookshelf&logoColor=white) ![Coverage](https://img.shields.io/badge/API_coverage-209%2F209-brightgreen?style=for-the-badge)

</div>
</center>

<hr>

Run Audiobookshelf from Claude.ai and Claude Code. All 209 routes are tools. Not a curated subset: every endpoint the web interface can reach, this can reach.

<hr>

## Why not the other options

Audiobookshelf ships `docs/openapi.json`, but it documents 65 of the 209 routes its Express routers register, so anything generated from it covers under a third of the API. The routers are the complete list:

| Approach | Tools | Coverage |
| --- | --- | --- |
| Servers built on `docs/openapi.json` | up to 65 | 31 % |
| Hand-written subsets | a dozen or so | under 10 % |
| This one | **209** | **100 %** |

The published spec covers libraries, items and a few author and series routes. It leaves out playback sessions, progress, podcasts and their episode downloads, collections, playlists, users, backups, notifications, email and the whole settings surface.

## How it stays complete

`scripts/extract_spec.py` reads the routers and writes an OpenAPI document, borrowing summaries and parameters from the published docs wherever they exist. `scripts/generate_tools.py` then turns it into tools:

```bash
git clone --depth 1 https://github.com/advplyr/audiobookshelf.git /tmp/abs
python scripts/extract_spec.py /tmp/abs openapi.json
python scripts/generate_tools.py openapi.json src/audiobookshelf_mcp/tools.py
```

45 of the 209 operations carry the project's own descriptions; the rest are derived from the route.

A test compares every generated call against every operation in the extracted spec, in both directions. A route Audiobookshelf adds and this misses fails the build; so does a tool pointing at a route that does not exist.

## Tool names

Verb first, derived from the method and path, so the name says what it does:

| Pattern | Meaning | Example |
| --- | --- | --- |
| `list_*` | Read a collection | `list_api_libraries`, `list_api_me` |
| `get_*_by_id` | Read one record | `list_api_libraries_by_id` |
| `create_*` | POST | `create_api_libraries` |
| `update_*` | PATCH | `update_api_libraries_by_id` |
| `delete_*` | DELETE | `delete_api_libraries_by_id` |

209 tools is a lot to put in front of a model at once. If your client supports tool filtering, narrow it to the groups you use.

## What is covered

Every route the three routers register, across `/api`, `/public` and `/hls`: libraries and their items, books, podcasts and episode downloads, authors, series, collections, playlists, search, listening sessions and playback progress, `me`, users and API keys, notifications, email and ereader devices, RSS feeds and share links, the filesystem browser, caches, backups, logs, tools and the whole settings surface.

## Setup

```bash
git clone https://github.com/rollecode/audiobookshelf-mcp.git
cd audiobookshelf-mcp
uv venv && uv pip install -e .
```

```bash
export AUDIOBOOKSHELF_URL=http://127.0.0.1:13378
export AUDIOBOOKSHELF_TOKEN=...   # Settings, Users, your user, API token
```

### Claude Code

```bash
claude mcp add audiobookshelf -- /path/to/audiobookshelf-mcp/.venv/bin/audiobookshelf-mcp
```

## Writing

Audiobookshelf patches rather than replaces, so `body` needs only the fields you are changing. Ids are strings throughout, not numbers.

## Development

```bash
uv pip install -e . pytest ruff
.venv/bin/python -m pytest tests
.venv/bin/ruff check .
```

## Licence

MIT
