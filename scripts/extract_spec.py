#!/usr/bin/env python3
"""Build an OpenAPI document from Audiobookshelf's Express routers.

Audiobookshelf ships `docs/openapi.json`, but it documents 65 of the 209
routes its routers actually register, so generating from it would cover under a
third of the API. The routers themselves are the complete list, and they are
declarative enough to read without running anything:

    this.router.get('/libraries/:id/items', LibraryController.getLibraryItems...)

Each such line becomes an operation. Where the published spec documents the
same route, its summary and parameters are borrowed so the generated tool
carries the real description rather than a derived one.

    python scripts/extract_spec.py /path/to/audiobookshelf openapi.json
"""

import json
import pathlib
import re
import sys

# Each router file and the prefix Server.js mounts it under.
ROUTERS = {
    "ApiRouter.js": "/api",
    "HlsRouter.js": "/hls",
    "PublicRouter.js": "/public",
}

ROUTE = re.compile(
    r"this\.router\.(get|post|patch|put|delete)\(\s*'([^']+)'",
)

# :id in an Express path is {id} in OpenAPI.
PARAM = re.compile(r":([A-Za-z_][A-Za-z0-9_]*)")


def load_published(root: pathlib.Path) -> dict:
    """The shipped spec, used only to borrow descriptions where they exist."""
    published = root / "docs" / "openapi.json"
    if not published.exists():
        return {}
    spec = json.loads(published.read_text())
    return spec.get("paths", {})


def to_openapi_path(path: str) -> str:
    return PARAM.sub(r"{\1}", path)


def path_parameters(path: str) -> list[dict]:
    return [
        {
            "name": name,
            "in": "path",
            "required": True,
            "description": "Path parameter.",
            "schema": {"type": "string"},
        }
        for name in PARAM.findall(path)
    ]


def summarise(method: str, path: str) -> str:
    """A readable summary from the route itself, for the undocumented majority."""
    segments = [s for s in path.strip("/").split("/") if s and not s.startswith(":")]
    subject = " ".join(segments[-2:]) if segments else "the API"
    verb = {
        "get": "Get",
        "post": "Create or act on",
        "patch": "Update",
        "put": "Replace",
        "delete": "Delete",
    }[method]
    return f"{verb} {subject}."


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2

    root = pathlib.Path(sys.argv[1])
    published = load_published(root)
    paths: dict[str, dict] = {}
    borrowed = 0

    for filename, prefix in ROUTERS.items():
        source = root / "server" / "routers" / filename
        if not source.exists():
            print(f"missing {source}", file=sys.stderr)
            return 1

        for method, route in ROUTE.findall(source.read_text()):
            full = prefix + "/" + route.lstrip("/")
            full = full.rstrip("/") or "/"
            openapi_path = to_openapi_path(full)

            documented = (published.get(openapi_path) or {}).get(method) or {}
            if documented:
                borrowed += 1

            parameters = list(documented.get("parameters") or [])
            known = {p.get("name") for p in parameters}
            parameters += [
                p for p in path_parameters(full) if p["name"] not in known
            ]

            operation = {
                "summary": documented.get("summary")
                or summarise(method, full),
                "tags": documented.get("tags") or [_tag(full)],
                "parameters": parameters,
            }
            # Anything that is not a GET may carry a body; the routers do not
            # say so, and sending none is harmless where none is wanted.
            if method != "get":
                operation["requestBody"] = documented.get("requestBody") or {
                    "required": False,
                    "content": {"application/json": {"schema": {"type": "object"}}},
                }

            paths.setdefault(openapi_path, {})[method] = operation

    spec = {
        "openapi": "3.0.2",
        "info": {
            "title": "Audiobookshelf API",
            "version": "1.0.0",
            "description": (
                "Extracted from Audiobookshelf's Express routers, with "
                "descriptions borrowed from the published docs where they exist."
            ),
        },
        "paths": paths,
    }

    with open(sys.argv[2], "w") as handle:
        json.dump(spec, handle, indent=1)

    operations = sum(len(methods) for methods in paths.values())
    print(
        f"{len(paths)} paths, {operations} operations "
        f"({borrowed} with published descriptions) -> {sys.argv[2]}"
    )
    return 0


def _tag(path: str) -> str:
    segments = [s for s in path.strip("/").split("/") if s and not s.startswith("{")]
    # Skip the mount prefix, which is the same for most of the surface.
    return segments[1] if len(segments) > 1 else (segments[0] if segments else "root")


if __name__ == "__main__":
    raise SystemExit(main())
