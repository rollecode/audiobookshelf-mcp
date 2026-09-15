"""Generated from the OpenAPI document. Do not edit by hand.

Regenerate with:

    python scripts/generate_tools.py openapi.json src/audiobookshelf_mcp/tools.py

One tool per operation, 209 of them, covering the whole API.
"""

from .runtime import _DESTRUCTIVE, _READ, _WRITE, call, mcp


@mcp.tool(annotations=_WRITE)
def create_api_keys(body: dict) -> str:
    """Create or act on api api-keys.

    POST /api/api-keys

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/api-keys", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_authorize(body: dict) -> str:
    """Create or act on api authorize.

    POST /api/authorize

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/authorize", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_authors_by_id_image(id: str, body: dict) -> str:
    """Add an author image to the server.

    POST /api/authors/{id}/image

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/authors/{id}/image", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_authors_by_id_match(id: str, body: dict) -> str:
    """Match the author against Audible using quick match.

    POST /api/authors/{id}/match

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/authors/{id}/match", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_backups(body: dict) -> str:
    """Create or act on api backups.

    POST /api/backups

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/backups", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_backups_upload(body: dict) -> str:
    """Create or act on backups upload.

    POST /api/backups/upload

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/backups/upload", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_cache_items_purge(body: dict) -> str:
    """Create or act on items purge.

    POST /api/cache/items/purge

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/cache/items/purge", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_cache_purge(body: dict) -> str:
    """Create or act on cache purge.

    POST /api/cache/purge

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/cache/purge", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_collections(body: dict) -> str:
    """Create or act on api collections.

    POST /api/collections

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/collections", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_collections_by_id_batch_add(id: str, body: dict) -> str:
    """Create or act on batch add.

    POST /api/collections/{id}/batch/add

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/collections/{id}/batch/add", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_collections_by_id_batch_remove(id: str, body: dict) -> str:
    """Create or act on batch remove.

    POST /api/collections/{id}/batch/remove

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/collections/{id}/batch/remove", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_collections_by_id_book(id: str, body: dict) -> str:
    """Create or act on collections book.

    POST /api/collections/{id}/book

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/collections/{id}/book", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_custom_metadata_providers(body: dict) -> str:
    """Create or act on api custom-metadata-providers.

    POST /api/custom-metadata-providers

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/custom-metadata-providers", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_emails_ereader_devices(body: dict) -> str:
    """Update e-reader devices.

    POST /api/emails/ereader-devices

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/emails/ereader-devices", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_emails_send_ebook_to_device(body: dict) -> str:
    """Send ebook to device.

    POST /api/emails/send-ebook-to-device

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/emails/send-ebook-to-device", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_emails_test(body: dict) -> str:
    """Send test email.

    POST /api/emails/test

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/emails/test", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_feeds_by_id_close(id: str, body: dict) -> str:
    """Create or act on feeds close.

    POST /api/feeds/{id}/close

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/feeds/{id}/close", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_feeds_collection_by_collection_id_open(collection_id: str, body: dict) -> str:
    """Create or act on collection open.

    POST /api/feeds/collection/{collectionId}/open

    Args:
        collection_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/feeds/collection/{collection_id}/open", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_feeds_item_by_item_id_open(item_id: str, body: dict) -> str:
    """Create or act on item open.

    POST /api/feeds/item/{itemId}/open

    Args:
        item_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/feeds/item/{item_id}/open", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_feeds_series_by_series_id_open(series_id: str, body: dict) -> str:
    """Create or act on series open.

    POST /api/feeds/series/{seriesId}/open

    Args:
        series_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/feeds/series/{series_id}/open", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_filesystem_pathexists(body: dict) -> str:
    """Create or act on filesystem pathexists.

    POST /api/filesystem/pathexists

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/filesystem/pathexists", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_genres_rename(body: dict) -> str:
    """Create or act on genres rename.

    POST /api/genres/rename

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/genres/rename", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_items_batch_delete(body: dict) -> str:
    """Create or act on batch delete.

    POST /api/items/batch/delete

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/items/batch/delete", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_items_batch_get(body: dict) -> str:
    """Create or act on batch get.

    POST /api/items/batch/get

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/items/batch/get", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_items_batch_quickmatch(body: dict) -> str:
    """Create or act on batch quickmatch.

    POST /api/items/batch/quickmatch

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/items/batch/quickmatch", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_items_batch_scan(body: dict) -> str:
    """Create or act on batch scan.

    POST /api/items/batch/scan

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/items/batch/scan", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_items_batch_update(body: dict) -> str:
    """Create or act on batch update.

    POST /api/items/batch/update

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/items/batch/update", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_items_by_id_chapters(id: str, body: dict) -> str:
    """Create or act on items chapters.

    POST /api/items/{id}/chapters

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/items/{id}/chapters", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_items_by_id_cover(id: str, body: dict) -> str:
    """Create or act on items cover.

    POST /api/items/{id}/cover

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/items/{id}/cover", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_items_by_id_match(id: str, body: dict) -> str:
    """Create or act on items match.

    POST /api/items/{id}/match

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/items/{id}/match", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_items_by_id_play(id: str, body: dict) -> str:
    """Create or act on items play.

    POST /api/items/{id}/play

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/items/{id}/play", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_items_by_id_play_by_episode_id(id: str, episode_id: str, body: dict) -> str:
    """Create or act on items play.

    POST /api/items/{id}/play/{episodeId}

    Args:
        id: Path parameter.
        episode_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/items/{id}/play/{episode_id}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_items_by_id_scan(id: str, body: dict) -> str:
    """Create or act on items scan.

    POST /api/items/{id}/scan

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/items/{id}/scan", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_libraries(body: dict) -> str:
    """Create a new library on server.

    POST /api/libraries

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/libraries", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_libraries_by_id_remove_metadata(id: str, body: dict) -> str:
    """Create or act on libraries remove-metadata.

    POST /api/libraries/{id}/remove-metadata

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/libraries/{id}/remove-metadata", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_libraries_by_id_scan(id: str, body: dict) -> str:
    """Create or act on libraries scan.

    POST /api/libraries/{id}/scan

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/libraries/{id}/scan", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_libraries_order(body: dict) -> str:
    """Create or act on libraries order.

    POST /api/libraries/order

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/libraries/order", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_me_ereader_devices(body: dict) -> str:
    """Create or act on me ereader-devices.

    POST /api/me/ereader-devices

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/me/ereader-devices", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_me_item_by_id_bookmark(id: str, body: dict) -> str:
    """Create or act on item bookmark.

    POST /api/me/item/{id}/bookmark

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/me/item/{id}/bookmark", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_notifications(body: dict) -> str:
    """Create notification settings.

    POST /api/notifications

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/notifications", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_playlists(body: dict) -> str:
    """Create or act on api playlists.

    POST /api/playlists

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/playlists", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_playlists_by_id_batch_add(id: str, body: dict) -> str:
    """Create or act on batch add.

    POST /api/playlists/{id}/batch/add

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/playlists/{id}/batch/add", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_playlists_by_id_batch_remove(id: str, body: dict) -> str:
    """Create or act on batch remove.

    POST /api/playlists/{id}/batch/remove

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/playlists/{id}/batch/remove", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_playlists_by_id_item(id: str, body: dict) -> str:
    """Create or act on playlists item.

    POST /api/playlists/{id}/item

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/playlists/{id}/item", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_playlists_collection_by_collection_id(collection_id: str, body: dict) -> str:
    """Create or act on playlists collection.

    POST /api/playlists/collection/{collectionId}

    Args:
        collection_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/playlists/collection/{collection_id}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_podcasts(body: dict) -> str:
    """Create a new podcast.

    POST /api/podcasts

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/podcasts", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_podcasts_by_id_download_episodes(id: str, body: dict) -> str:
    """Download podcast episodes.

    POST /api/podcasts/{id}/download-episodes

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/podcasts/{id}/download-episodes", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_podcasts_by_id_match_episodes(id: str, body: dict, override: str | None = None) -> str:
    """Quick match podcast episodes.

    POST /api/podcasts/{id}/match-episodes

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        override: Override existing details if set to 1
    """
    return call("POST", f"/api/podcasts/{id}/match-episodes", query={"override": override}, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_podcasts_feed(body: dict) -> str:
    """Get podcast feed.

    POST /api/podcasts/feed

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/podcasts/feed", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_podcasts_opml_create(body: dict) -> str:
    """Bulk create podcasts from OPML feed URLs.

    POST /api/podcasts/opml/create

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/podcasts/opml/create", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_podcasts_opml_parse(body: dict) -> str:
    """Get feeds from OPML text.

    POST /api/podcasts/opml/parse

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/podcasts/opml/parse", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_session_by_id_close(id: str, body: dict) -> str:
    """Create or act on session close.

    POST /api/session/{id}/close

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/session/{id}/close", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_session_by_id_sync(id: str, body: dict) -> str:
    """Create or act on session sync.

    POST /api/session/{id}/sync

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/session/{id}/sync", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_session_local(body: dict) -> str:
    """Create or act on session local.

    POST /api/session/local

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/session/local", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_session_local_all(body: dict) -> str:
    """Create or act on session local-all.

    POST /api/session/local-all

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/session/local-all", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_sessions_batch_delete(body: dict) -> str:
    """Create or act on batch delete.

    POST /api/sessions/batch/delete

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/sessions/batch/delete", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_share_mediaitem(body: dict) -> str:
    """Create or act on share mediaitem.

    POST /api/share/mediaitem

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/share/mediaitem", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_tags_rename(body: dict) -> str:
    """Create or act on tags rename.

    POST /api/tags/rename

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/tags/rename", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_tools_batch_embed_metadata(body: dict) -> str:
    """Create or act on batch embed-metadata.

    POST /api/tools/batch/embed-metadata

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/tools/batch/embed-metadata", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_tools_item_by_id_embed_metadata(id: str, body: dict) -> str:
    """Create or act on item embed-metadata.

    POST /api/tools/item/{id}/embed-metadata

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/tools/item/{id}/embed-metadata", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_tools_item_by_id_encode_m4b(id: str, body: dict) -> str:
    """Create or act on item encode-m4b.

    POST /api/tools/item/{id}/encode-m4b

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/tools/item/{id}/encode-m4b", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_upload(body: dict) -> str:
    """Create or act on api upload.

    POST /api/upload

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/upload", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_users(body: dict) -> str:
    """Create or act on api users.

    POST /api/users

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/users", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_validate_cron(body: dict) -> str:
    """Create or act on api validate-cron.

    POST /api/validate-cron

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/validate-cron", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def create_watcher_update(body: dict) -> str:
    """Create or act on watcher update.

    POST /api/watcher/update

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/watcher/update", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_api_keys_by_id(id: str, body: dict | None = None) -> str:
    """Delete api api-keys.

    DELETE /api/api-keys/{id}

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", f"/api/api-keys/{id}", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_authors_by_id(id: str, body: dict | None = None) -> str:
    """Delete an author by ID.

    DELETE /api/authors/{id}

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", f"/api/authors/{id}", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_authors_by_id_image(id: str, body: dict | None = None) -> str:
    """Delete an author image by author ID.

    DELETE /api/authors/{id}/image

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", f"/api/authors/{id}/image", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_backups_by_id(id: str, body: dict | None = None) -> str:
    """Delete api backups.

    DELETE /api/backups/{id}

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", f"/api/backups/{id}", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_collections_by_id(id: str, body: dict | None = None) -> str:
    """Delete api collections.

    DELETE /api/collections/{id}

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", f"/api/collections/{id}", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_collections_by_id_book_by_book_id(id: str, book_id: str, body: dict | None = None) -> str:
    """Delete collections book.

    DELETE /api/collections/{id}/book/{bookId}

    Args:
        id: Path parameter.
        book_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", f"/api/collections/{id}/book/{book_id}", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_custom_metadata_providers_by_id(id: str, body: dict | None = None) -> str:
    """Delete api custom-metadata-providers.

    DELETE /api/custom-metadata-providers/{id}

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", f"/api/custom-metadata-providers/{id}", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_genres_by_genre(genre: str, body: dict | None = None) -> str:
    """Delete api genres.

    DELETE /api/genres/{genre}

    Args:
        genre: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", f"/api/genres/{genre}", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_items_by_id(id: str, body: dict | None = None) -> str:
    """Delete api items.

    DELETE /api/items/{id}

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", f"/api/items/{id}", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_items_by_id_cover(id: str, body: dict | None = None) -> str:
    """Delete items cover.

    DELETE /api/items/{id}/cover

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", f"/api/items/{id}/cover", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_items_by_id_file_by_fileid(id: str, fileid: str, body: dict | None = None) -> str:
    """Delete items file.

    DELETE /api/items/{id}/file/{fileid}

    Args:
        id: Path parameter.
        fileid: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", f"/api/items/{id}/file/{fileid}", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_libraries_by_id(id: str, body: dict | None = None) -> str:
    """Delete a single library by ID on server.

    DELETE /api/libraries/{id}

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", f"/api/libraries/{id}", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_libraries_by_id_issues(id: str, body: dict | None = None) -> str:
    """Delete items with issues in a library.

    DELETE /api/libraries/{id}/issues

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", f"/api/libraries/{id}/issues", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_libraries_by_id_narrators_by_narrator_id(id: str, narrator_id: str, body: dict | None = None) -> str:
    """Delete libraries narrators.

    DELETE /api/libraries/{id}/narrators/{narratorId}

    Args:
        id: Path parameter.
        narrator_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", f"/api/libraries/{id}/narrators/{narrator_id}", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_me_item_by_id_bookmark_by_time(id: str, time: str, body: dict | None = None) -> str:
    """Delete item bookmark.

    DELETE /api/me/item/{id}/bookmark/{time}

    Args:
        id: Path parameter.
        time: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", f"/api/me/item/{id}/bookmark/{time}", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_me_progress_by_id(id: str, body: dict | None = None) -> str:
    """Delete me progress.

    DELETE /api/me/progress/{id}

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", f"/api/me/progress/{id}", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_me_sessions_by_id(id: str, body: dict | None = None) -> str:
    """Delete me sessions.

    DELETE /api/me/sessions/{id}

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", f"/api/me/sessions/{id}", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_notifications_by_id(id: str, body: dict | None = None) -> str:
    """Delete a notification.

    DELETE /api/notifications/{id}

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", f"/api/notifications/{id}", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_playlists_by_id(id: str, body: dict | None = None) -> str:
    """Delete api playlists.

    DELETE /api/playlists/{id}

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", f"/api/playlists/{id}", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_playlists_by_id_item_by_library_item_id_by_episode_id(id: str, library_item_id: str, episode_id: str, body: dict | None = None) -> str:
    """Delete playlists item.

    DELETE /api/playlists/{id}/item/{libraryItemId}/{episodeId}?

    Args:
        id: Path parameter.
        library_item_id: Path parameter.
        episode_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", f"/api/playlists/{id}/item/{library_item_id}/{episode_id}?", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_podcasts_by_id_episode_by_episode_id(id: str, episode_id: str, body: dict | None = None, hard: str | None = None) -> str:
    """Remove a podcast episode.

    DELETE /api/podcasts/{id}/episode/{episodeId}

    Args:
        id: Path parameter.
        episode_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
        hard: Hard delete the episode if set to 1
    """
    return call("DELETE", f"/api/podcasts/{id}/episode/{episode_id}", query={"hard": hard}, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_sessions_by_id(id: str, body: dict | None = None) -> str:
    """Delete api sessions.

    DELETE /api/sessions/{id}

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", f"/api/sessions/{id}", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_share_mediaitem_by_id(id: str, body: dict | None = None) -> str:
    """Delete share mediaitem.

    DELETE /api/share/mediaitem/{id}

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", f"/api/share/mediaitem/{id}", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_tags_by_tag(tag: str, body: dict | None = None) -> str:
    """Delete api tags.

    DELETE /api/tags/{tag}

    Args:
        tag: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", f"/api/tags/{tag}", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_tools_item_by_id_encode_m4b(id: str, body: dict | None = None) -> str:
    """Delete item encode-m4b.

    DELETE /api/tools/item/{id}/encode-m4b

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", f"/api/tools/item/{id}/encode-m4b", query=None, body=body, form=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_users_by_id(id: str, body: dict | None = None) -> str:
    """Delete api users.

    DELETE /api/users/{id}

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("DELETE", f"/api/users/{id}", query=None, body=body, form=None)


@mcp.tool(annotations=_READ)
def get_authors_by_id(id: str, include: str | None = None) -> str:
    """Get an author by ID.

    GET /api/authors/{id}

    Args:
        id: Path parameter.
        include: A comma separated list of what to include with the author. The options are `items` and `series`. `series` will only have an effect if `items` is included. For example, the value `items,series` will include both library items and series.
    """
    return call("GET", f"/api/authors/{id}", query={"include": include}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_authors_by_id_image(id: str) -> str:
    """Get an author image by author ID.

    GET /api/authors/{id}/image

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/authors/{id}/image", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_backups_by_id_apply(id: str) -> str:
    """Get backups apply.

    GET /api/backups/{id}/apply

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/backups/{id}/apply", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_backups_by_id_download(id: str) -> str:
    """Get backups download.

    GET /api/backups/{id}/download

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/backups/{id}/download", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_collections_by_id(id: str) -> str:
    """Get api collections.

    GET /api/collections/{id}

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/collections/{id}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_hls_by_stream_by_file(stream: str, file: str) -> str:
    """Get hls.

    GET /hls/{stream}/{file}

    Args:
        stream: Path parameter.
        file: Path parameter.
    """
    return call("GET", f"/hls/{stream}/{file}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_items_by_id(id: str) -> str:
    """Get api items.

    GET /api/items/{id}

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/items/{id}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_items_by_id_cover(id: str) -> str:
    """Get items cover.

    GET /api/items/{id}/cover

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/items/{id}/cover", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_items_by_id_download(id: str) -> str:
    """Get items download.

    GET /api/items/{id}/download

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/items/{id}/download", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_items_by_id_ebook_by_fileid(id: str, fileid: str) -> str:
    """Get items ebook.

    GET /api/items/{id}/ebook/{fileid}?

    Args:
        id: Path parameter.
        fileid: Path parameter.
    """
    return call("GET", f"/api/items/{id}/ebook/{fileid}?", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_items_by_id_ffprobe_by_fileid(id: str, fileid: str) -> str:
    """Get items ffprobe.

    GET /api/items/{id}/ffprobe/{fileid}

    Args:
        id: Path parameter.
        fileid: Path parameter.
    """
    return call("GET", f"/api/items/{id}/ffprobe/{fileid}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_items_by_id_file_by_fileid(id: str, fileid: str) -> str:
    """Get items file.

    GET /api/items/{id}/file/{fileid}

    Args:
        id: Path parameter.
        fileid: Path parameter.
    """
    return call("GET", f"/api/items/{id}/file/{fileid}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_items_by_id_file_by_fileid_download(id: str, fileid: str) -> str:
    """Get file download.

    GET /api/items/{id}/file/{fileid}/download

    Args:
        id: Path parameter.
        fileid: Path parameter.
    """
    return call("GET", f"/api/items/{id}/file/{fileid}/download", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_items_by_id_metadata_object(id: str) -> str:
    """Get items metadata-object.

    GET /api/items/{id}/metadata-object

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/items/{id}/metadata-object", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_libraries_by_id(id: str, include: str | None = None) -> str:
    """Get a single library by ID on server.

    GET /api/libraries/{id}

    Args:
        id: Path parameter.
        include: Query parameter.
    """
    return call("GET", f"/api/libraries/{id}", query={"include": include}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_libraries_by_id_authors(id: str) -> str:
    """Get all authors in a library.

    GET /api/libraries/{id}/authors

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/libraries/{id}/authors", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_libraries_by_id_collections(id: str) -> str:
    """Get libraries collections.

    GET /api/libraries/{id}/collections

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/libraries/{id}/collections", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_libraries_by_id_download(id: str) -> str:
    """Get libraries download.

    GET /api/libraries/{id}/download

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/libraries/{id}/download", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_libraries_by_id_episode_downloads(id: str) -> str:
    """Get libraries episode-downloads.

    GET /api/libraries/{id}/episode-downloads

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/libraries/{id}/episode-downloads", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_libraries_by_id_filterdata(id: str) -> str:
    """Get libraries filterdata.

    GET /api/libraries/{id}/filterdata

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/libraries/{id}/filterdata", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_libraries_by_id_items(id: str, sort: str | None = None, filter: str | None = None, include: str | None = None, collapse_series: int | None = None) -> str:
    """Get items in a library.

    GET /api/libraries/{id}/items

    Args:
        id: Path parameter.
        sort: The field to sort by from the request.
        filter: The filter for the library.
        include: The fields to include in the response. The only current option is `rssfeed`.
        collapse_series: Whether to collapse series into a single cover
    """
    return call("GET", f"/api/libraries/{id}/items", query={"sort": sort, "filter": filter, "include": include, "collapseSeries": collapse_series}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_libraries_by_id_matchall(id: str) -> str:
    """Get libraries matchall.

    GET /api/libraries/{id}/matchall

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/libraries/{id}/matchall", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_libraries_by_id_narrators(id: str) -> str:
    """Get libraries narrators.

    GET /api/libraries/{id}/narrators

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/libraries/{id}/narrators", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_libraries_by_id_opml(id: str) -> str:
    """Get libraries opml.

    GET /api/libraries/{id}/opml

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/libraries/{id}/opml", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_libraries_by_id_personalized(id: str) -> str:
    """Get libraries personalized.

    GET /api/libraries/{id}/personalized

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/libraries/{id}/personalized", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_libraries_by_id_playlists(id: str) -> str:
    """Get libraries playlists.

    GET /api/libraries/{id}/playlists

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/libraries/{id}/playlists", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_libraries_by_id_podcast_titles(id: str) -> str:
    """Get libraries podcast-titles.

    GET /api/libraries/{id}/podcast-titles

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/libraries/{id}/podcast-titles", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_libraries_by_id_recent_episodes(id: str) -> str:
    """Get libraries recent-episodes.

    GET /api/libraries/{id}/recent-episodes

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/libraries/{id}/recent-episodes", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_libraries_by_id_search(id: str) -> str:
    """Get libraries search.

    GET /api/libraries/{id}/search

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/libraries/{id}/search", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_libraries_by_id_series(id: str, sort: str | None = None, filter: str | None = None, include: str | None = None) -> str:
    """Get library series.

    GET /api/libraries/{id}/series

    Args:
        id: Path parameter.
        sort: The field to sort by from the request.
        filter: The filter for the library.
        include: The fields to include in the response. The only current option is `rssfeed`.
    """
    return call("GET", f"/api/libraries/{id}/series", query={"sort": sort, "filter": filter, "include": include}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_libraries_by_id_series_by_series_id(id: str, series_id: str, sort: str | None = None, filter: str | None = None, include: str | None = None) -> str:
    """Get single series in library.

    GET /api/libraries/{id}/series/{seriesId}

    Args:
        id: Path parameter.
        series_id: Path parameter.
        sort: The field to sort by from the request.
        filter: The filter for the library.
        include: The fields to include in the response. The only current option is `rssfeed`.
    """
    return call("GET", f"/api/libraries/{id}/series/{series_id}", query={"sort": sort, "filter": filter, "include": include}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_libraries_by_id_stats(id: str) -> str:
    """Get libraries stats.

    GET /api/libraries/{id}/stats

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/libraries/{id}/stats", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_me_bookmarks_by_library_item_id(library_item_id: str) -> str:
    """Get me bookmarks.

    GET /api/me/bookmarks/{libraryItemId}

    Args:
        library_item_id: Path parameter.
    """
    return call("GET", f"/api/me/bookmarks/{library_item_id}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_me_item_listening_sessions_by_library_item_id_by_episode_id(library_item_id: str, episode_id: str) -> str:
    """Get item listening-sessions.

    GET /api/me/item/listening-sessions/{libraryItemId}/{episodeId}?

    Args:
        library_item_id: Path parameter.
        episode_id: Path parameter.
    """
    return call("GET", f"/api/me/item/listening-sessions/{library_item_id}/{episode_id}?", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_me_progress_by_id_by_episode_id(id: str, episode_id: str) -> str:
    """Get me progress.

    GET /api/me/progress/{id}/{episodeId}?

    Args:
        id: Path parameter.
        episode_id: Path parameter.
    """
    return call("GET", f"/api/me/progress/{id}/{episode_id}?", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_me_progress_by_id_remove_from_continue_listening(id: str) -> str:
    """Get progress remove-from-continue-listening.

    GET /api/me/progress/{id}/remove-from-continue-listening

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/me/progress/{id}/remove-from-continue-listening", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_me_series_by_id_readd_to_continue_listening(id: str) -> str:
    """Get series readd-to-continue-listening.

    GET /api/me/series/{id}/readd-to-continue-listening

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/me/series/{id}/readd-to-continue-listening", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_me_series_by_id_remove_from_continue_listening(id: str) -> str:
    """Get series remove-from-continue-listening.

    GET /api/me/series/{id}/remove-from-continue-listening

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/me/series/{id}/remove-from-continue-listening", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_me_stats_year_by_year(year: str) -> str:
    """Get stats year.

    GET /api/me/stats/year/{year}

    Args:
        year: Path parameter.
    """
    return call("GET", f"/api/me/stats/year/{year}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_notifications_by_id_test(id: str) -> str:
    """Send a test notification.

    GET /api/notifications/{id}/test

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/notifications/{id}/test", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_playlists_by_id(id: str) -> str:
    """Get api playlists.

    GET /api/playlists/{id}

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/playlists/{id}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_podcasts_by_id_checknew(id: str, limit: int | None = None) -> str:
    """Check and download new episodes.

    GET /api/podcasts/{id}/checknew

    Args:
        id: Path parameter.
        limit: Maximum number of episodes to download
    """
    return call("GET", f"/api/podcasts/{id}/checknew", query={"limit": limit}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_podcasts_by_id_clear_queue(id: str) -> str:
    """Clear episode download queue.

    GET /api/podcasts/{id}/clear-queue

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/podcasts/{id}/clear-queue", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_podcasts_by_id_downloads(id: str) -> str:
    """Get episode downloads.

    GET /api/podcasts/{id}/downloads

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/podcasts/{id}/downloads", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_podcasts_by_id_episode_by_episode_id(id: str, episode_id: str) -> str:
    """Get a specific podcast episode.

    GET /api/podcasts/{id}/episode/{episodeId}

    Args:
        id: Path parameter.
        episode_id: Path parameter.
    """
    return call("GET", f"/api/podcasts/{id}/episode/{episode_id}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_podcasts_by_id_search_episode(id: str, title: str | None = None) -> str:
    """Find episode by title.

    GET /api/podcasts/{id}/search-episode

    Args:
        id: Path parameter.
        title: Title of the episode to search for
    """
    return call("GET", f"/api/podcasts/{id}/search-episode", query={"title": title}, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_public_session_by_id_track_by_index(id: str, index: str) -> str:
    """Get session track.

    GET /public/session/{id}/track/{index}

    Args:
        id: Path parameter.
        index: Path parameter.
    """
    return call("GET", f"/public/session/{id}/track/{index}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_public_share_by_slug(slug: str) -> str:
    """Get public share.

    GET /public/share/{slug}

    Args:
        slug: Path parameter.
    """
    return call("GET", f"/public/share/{slug}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_public_share_by_slug_cover(slug: str) -> str:
    """Get share cover.

    GET /public/share/{slug}/cover

    Args:
        slug: Path parameter.
    """
    return call("GET", f"/public/share/{slug}/cover", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_public_share_by_slug_download(slug: str) -> str:
    """Get share download.

    GET /public/share/{slug}/download

    Args:
        slug: Path parameter.
    """
    return call("GET", f"/public/share/{slug}/download", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_public_share_by_slug_track_by_index(slug: str, index: str) -> str:
    """Get share track.

    GET /public/share/{slug}/track/{index}

    Args:
        slug: Path parameter.
        index: Path parameter.
    """
    return call("GET", f"/public/share/{slug}/track/{index}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_series_by_id(id: str) -> str:
    """Get series.

    GET /api/series/{id}

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/series/{id}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_session_by_id(id: str) -> str:
    """Get api session.

    GET /api/session/{id}

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/session/{id}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_stats_year_by_year(year: str) -> str:
    """Get stats year.

    GET /api/stats/year/{year}

    Args:
        year: Path parameter.
    """
    return call("GET", f"/api/stats/year/{year}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id(id: str) -> str:
    """Get api users.

    GET /api/users/{id}

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/users/{id}", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_listening_sessions(id: str) -> str:
    """Get users listening-sessions.

    GET /api/users/{id}/listening-sessions

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/users/{id}/listening-sessions", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def get_users_by_id_listening_stats(id: str) -> str:
    """Get users listening-stats.

    GET /api/users/{id}/listening-stats

    Args:
        id: Path parameter.
    """
    return call("GET", f"/api/users/{id}/listening-stats", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_api_keys() -> str:
    """Get api api-keys.

    GET /api/api-keys
    """
    return call("GET", "/api/api-keys", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_auth_settings() -> str:
    """Get api auth-settings.

    GET /api/auth-settings
    """
    return call("GET", "/api/auth-settings", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_backups() -> str:
    """Get api backups.

    GET /api/backups
    """
    return call("GET", "/api/backups", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_collections() -> str:
    """Get api collections.

    GET /api/collections
    """
    return call("GET", "/api/collections", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_custom_metadata_providers() -> str:
    """Get api custom-metadata-providers.

    GET /api/custom-metadata-providers
    """
    return call("GET", "/api/custom-metadata-providers", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_emails_settings() -> str:
    """Get email settings.

    GET /api/emails/settings
    """
    return call("GET", "/api/emails/settings", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_feeds() -> str:
    """Get api feeds.

    GET /api/feeds
    """
    return call("GET", "/api/feeds", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_filesystem() -> str:
    """Get api filesystem.

    GET /api/filesystem
    """
    return call("GET", "/api/filesystem", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_genres() -> str:
    """Get api genres.

    GET /api/genres
    """
    return call("GET", "/api/genres", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_libraries() -> str:
    """Get all libraries on server.

    GET /api/libraries
    """
    return call("GET", "/api/libraries", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_logger_data() -> str:
    """Get api logger-data.

    GET /api/logger-data
    """
    return call("GET", "/api/logger-data", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_me() -> str:
    """Get api me.

    GET /api/me
    """
    return call("GET", "/api/me", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_me_bookmarks() -> str:
    """Get me bookmarks.

    GET /api/me/bookmarks
    """
    return call("GET", "/api/me/bookmarks", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_me_items_in_progress() -> str:
    """Get me items-in-progress.

    GET /api/me/items-in-progress
    """
    return call("GET", "/api/me/items-in-progress", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_me_listening_sessions() -> str:
    """Get me listening-sessions.

    GET /api/me/listening-sessions
    """
    return call("GET", "/api/me/listening-sessions", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_me_listening_stats() -> str:
    """Get me listening-stats.

    GET /api/me/listening-stats
    """
    return call("GET", "/api/me/listening-stats", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_me_progress() -> str:
    """Get me progress.

    GET /api/me/progress
    """
    return call("GET", "/api/me/progress", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_me_sessions() -> str:
    """Get me sessions.

    GET /api/me/sessions
    """
    return call("GET", "/api/me/sessions", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_notificationdata() -> str:
    """Get notification event data.

    GET /api/notificationdata
    """
    return call("GET", "/api/notificationdata", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_notifications() -> str:
    """Get notification settings.

    GET /api/notifications
    """
    return call("GET", "/api/notifications", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_notifications_test(fail: int | None = None) -> str:
    """Send general test notification.

    GET /api/notifications/test

    Args:
        fail: Whether to intentionally cause the notification to fail. `0` for false, `1` for true.
    """
    return call("GET", "/api/notifications/test", query={"fail": fail}, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_playlists() -> str:
    """Get api playlists.

    GET /api/playlists
    """
    return call("GET", "/api/playlists", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_search_authors() -> str:
    """Get search authors.

    GET /api/search/authors
    """
    return call("GET", "/api/search/authors", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_search_books() -> str:
    """Get search books.

    GET /api/search/books
    """
    return call("GET", "/api/search/books", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_search_chapters() -> str:
    """Get search chapters.

    GET /api/search/chapters
    """
    return call("GET", "/api/search/chapters", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_search_covers() -> str:
    """Get search covers.

    GET /api/search/covers
    """
    return call("GET", "/api/search/covers", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_search_podcast() -> str:
    """Get search podcast.

    GET /api/search/podcast
    """
    return call("GET", "/api/search/podcast", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_search_providers() -> str:
    """Get search providers.

    GET /api/search/providers
    """
    return call("GET", "/api/search/providers", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_sessions() -> str:
    """Get api sessions.

    GET /api/sessions
    """
    return call("GET", "/api/sessions", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_sessions_open() -> str:
    """Get sessions open.

    GET /api/sessions/open
    """
    return call("GET", "/api/sessions/open", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_stats_server() -> str:
    """Get stats server.

    GET /api/stats/server
    """
    return call("GET", "/api/stats/server", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_tags() -> str:
    """Get api tags.

    GET /api/tags
    """
    return call("GET", "/api/tags", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_tasks() -> str:
    """Get api tasks.

    GET /api/tasks
    """
    return call("GET", "/api/tasks", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_users() -> str:
    """Get api users.

    GET /api/users
    """
    return call("GET", "/api/users", query=None, body=None, form=None)


@mcp.tool(annotations=_READ)
def list_users_online() -> str:
    """Get users online.

    GET /api/users/online
    """
    return call("GET", "/api/users/online", query=None, body=None, form=None)


@mcp.tool(annotations=_WRITE)
def patch_api_keys_by_id(id: str, body: dict) -> str:
    """Update api api-keys.

    PATCH /api/api-keys/{id}

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PATCH", f"/api/api-keys/{id}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def patch_auth_settings(body: dict) -> str:
    """Update api auth-settings.

    PATCH /api/auth-settings

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PATCH", "/api/auth-settings", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def patch_authors_by_id(id: str, body: dict) -> str:
    """Update an author by ID.

    PATCH /api/authors/{id}

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PATCH", f"/api/authors/{id}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def patch_backups_path(body: dict) -> str:
    """Update backups path.

    PATCH /api/backups/path

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PATCH", "/api/backups/path", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def patch_collections_by_id(id: str, body: dict) -> str:
    """Update api collections.

    PATCH /api/collections/{id}

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PATCH", f"/api/collections/{id}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def patch_emails_settings(body: dict) -> str:
    """Update email settings.

    PATCH /api/emails/settings

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PATCH", "/api/emails/settings", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def patch_items_by_id_cover(id: str, body: dict) -> str:
    """Update items cover.

    PATCH /api/items/{id}/cover

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PATCH", f"/api/items/{id}/cover", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def patch_items_by_id_ebook_by_fileid_status(id: str, fileid: str, body: dict) -> str:
    """Update ebook status.

    PATCH /api/items/{id}/ebook/{fileid}/status

    Args:
        id: Path parameter.
        fileid: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PATCH", f"/api/items/{id}/ebook/{fileid}/status", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def patch_items_by_id_media(id: str, body: dict) -> str:
    """Update items media.

    PATCH /api/items/{id}/media

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PATCH", f"/api/items/{id}/media", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def patch_items_by_id_tracks(id: str, body: dict) -> str:
    """Update items tracks.

    PATCH /api/items/{id}/tracks

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PATCH", f"/api/items/{id}/tracks", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def patch_libraries_by_id(id: str, body: dict) -> str:
    """Update a single library by ID on server.

    PATCH /api/libraries/{id}

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PATCH", f"/api/libraries/{id}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def patch_libraries_by_id_narrators_by_narrator_id(id: str, narrator_id: str, body: dict) -> str:
    """Update libraries narrators.

    PATCH /api/libraries/{id}/narrators/{narratorId}

    Args:
        id: Path parameter.
        narrator_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PATCH", f"/api/libraries/{id}/narrators/{narrator_id}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def patch_me_item_by_id_bookmark(id: str, body: dict) -> str:
    """Update item bookmark.

    PATCH /api/me/item/{id}/bookmark

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PATCH", f"/api/me/item/{id}/bookmark", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def patch_me_password(body: dict) -> str:
    """Update me password.

    PATCH /api/me/password

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PATCH", "/api/me/password", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def patch_me_progress_batch_update(body: dict) -> str:
    """Update batch update.

    PATCH /api/me/progress/batch/update

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PATCH", "/api/me/progress/batch/update", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def patch_me_progress_by_library_item_id_by_episode_id(library_item_id: str, episode_id: str, body: dict) -> str:
    """Update me progress.

    PATCH /api/me/progress/{libraryItemId}/{episodeId}?

    Args:
        library_item_id: Path parameter.
        episode_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PATCH", f"/api/me/progress/{library_item_id}/{episode_id}?", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def patch_notifications(body: dict) -> str:
    """Update select notification settings.

    PATCH /api/notifications

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PATCH", "/api/notifications", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def patch_notifications_by_id(id: str, body: dict) -> str:
    """Update a notification.

    PATCH /api/notifications/{id}

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PATCH", f"/api/notifications/{id}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def patch_playlists_by_id(id: str, body: dict) -> str:
    """Update api playlists.

    PATCH /api/playlists/{id}

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PATCH", f"/api/playlists/{id}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def patch_podcasts_by_id_episode_by_episode_id(id: str, episode_id: str, body: dict) -> str:
    """Update a podcast episode.

    PATCH /api/podcasts/{id}/episode/{episodeId}

    Args:
        id: Path parameter.
        episode_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PATCH", f"/api/podcasts/{id}/episode/{episode_id}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def patch_public_share_by_slug_progress(slug: str, body: dict) -> str:
    """Update share progress.

    PATCH /public/share/{slug}/progress

    Args:
        slug: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PATCH", f"/public/share/{slug}/progress", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def patch_series_by_id(id: str, body: dict) -> str:
    """Update series.

    PATCH /api/series/{id}

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PATCH", f"/api/series/{id}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def patch_settings(body: dict) -> str:
    """Update api settings.

    PATCH /api/settings

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PATCH", "/api/settings", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def patch_sorting_prefixes(body: dict) -> str:
    """Update api sorting-prefixes.

    PATCH /api/sorting-prefixes

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PATCH", "/api/sorting-prefixes", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def patch_users_by_id(id: str, body: dict) -> str:
    """Update api users.

    PATCH /api/users/{id}

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PATCH", f"/api/users/{id}", query=None, body=body, form=None)


@mcp.tool(annotations=_WRITE)
def patch_users_by_id_openid_unlink(id: str, body: dict) -> str:
    """Update users openid-unlink.

    PATCH /api/users/{id}/openid-unlink

    Args:
        id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PATCH", f"/api/users/{id}/openid-unlink", query=None, body=body, form=None)
