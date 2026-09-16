"""Hand-written tools for the routes the generator cannot express.

`POST /api/upload` takes multipart form data with the audio files attached, so
the generated tool, which sends a JSON body, always fails with 400. This is the
only way to get a book into Audiobookshelf that is not already sitting in a
library folder, so it is worth writing properly.
"""

import json
import mimetypes
import pathlib

from .runtime import _WRITE, _client, _err, mcp

# What Audiobookshelf accepts as book or podcast media, from its own
# upload validation. Anything else is rejected before the request is sent.
AUDIO_SUFFIXES = {
    ".m4b", ".mp3", ".m4a", ".flac", ".opus", ".ogg", ".oga", ".mp4", ".aac",
    ".wma", ".aiff", ".wav", ".webm", ".webma", ".mka", ".awb", ".caf",
}
EXTRA_SUFFIXES = {".pdf", ".epub", ".mobi", ".azw3", ".cbr", ".cbz", ".jpg",
                  ".jpeg", ".png", ".webp", ".txt", ".nfo"}


def _ok(data: dict) -> str:
    return json.dumps({"status": "success", **data}, indent=2)


@mcp.tool(annotations=_WRITE)
def upload_book(
    library_id: str,
    folder_id: str,
    title: str,
    files: list[str],
    author: str | None = None,
    series: str | None = None,
) -> str:
    """Upload audio files as a new book, creating the library item.

    This is how a book that is not already on the server gets in. Audiobookshelf
    has no wishlist and cannot fetch a book from a title alone: the files have
    to exist somewhere this machine can read, and they are sent to the server
    here.

    Args:
        library_id: Target library, from list_libraries.
        folder_id: Folder within that library, from the library's `folders`.
        title: Book title, which becomes the item name and its folder name.
        files: Absolute paths to the audio files on this machine, plus any
            cover, ebook or PDF to sit alongside them.
        author: Author name, used for the folder structure.
        series: Series name, if it belongs to one.
    """
    try:
        if not files:
            raise ValueError("No files given. Upload needs at least one file.")

        payload, handles = [], []
        for raw in files:
            path = pathlib.Path(raw).expanduser()
            if not path.is_file():
                raise ValueError(f"Not a file: {path}")
            suffix = path.suffix.lower()
            if suffix not in AUDIO_SUFFIXES | EXTRA_SUFFIXES:
                raise ValueError(
                    f"{path.name}: Audiobookshelf does not accept {suffix} files."
                )
            handle = path.open("rb")
            handles.append(handle)
            kind = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
            payload.append(("files", (path.name, handle, kind)))

        if not any(
            pathlib.Path(f).suffix.lower() in AUDIO_SUFFIXES for f in files
        ):
            raise ValueError("At least one audio file is required.")

        fields = {"title": title, "library": library_id, "folder": folder_id}
        if author:
            fields["author"] = author
        if series:
            fields["series"] = series

        try:
            response = _client().post("/api/upload", data=fields, files=payload)
        finally:
            for handle in handles:
                handle.close()

        if response.status_code == 403:
            raise PermissionError(
                "This API key's user does not have upload permission. Enable it "
                "in Audiobookshelf under Settings, Users."
            )
        response.raise_for_status()

        return _ok(
            {
                "uploaded": title,
                "files": [pathlib.Path(f).name for f in files],
                "library_id": library_id,
                "folder_id": folder_id,
                "next_step": "Run create_libraries_by_id_scan if the item does "
                "not appear straight away.",
            }
        )
    except Exception as e:
        return _err(e)


@mcp.tool(annotations=_WRITE)
def add_podcast_from_feed(
    library_id: str,
    folder_id: str,
    feed_url: str,
    auto_download: bool = False,
) -> str:
    """Add a podcast by RSS feed, which the server fetches itself.

    Unlike a book, a podcast needs no local file: give the feed and
    Audiobookshelf pulls the episodes.

    Args:
        library_id: A podcast-type library, from list_libraries.
        folder_id: Folder within that library.
        feed_url: The RSS feed URL.
        auto_download: Keep downloading new episodes as they appear.
    """
    try:
        client = _client()
        feed = client.post("/api/podcasts/feed", json={"rssFeed": feed_url})
        feed.raise_for_status()
        meta = (feed.json() or {}).get("podcast", {})

        created = client.post(
            "/api/podcasts",
            json={
                "libraryId": library_id,
                "folderId": folder_id,
                "media": meta.get("media", {}),
                "autoDownloadEpisodes": auto_download,
            },
        )
        created.raise_for_status()
        return _ok({"added": (meta.get("media") or {}).get("metadata", {}).get("title"),
                    "feed": feed_url})
    except Exception as e:
        return _err(e)
