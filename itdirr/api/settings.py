from __future__ import annotations

from ..models import PrivacySettings, NotificationSettings

def update_privacy(
    client,
    *,
    is_private: bool | None = None,
    wall_access: str | None = None,
    likes_visibility: str | None = None,
    show_last_seen: bool | None = None,
) -> PrivacySettings:

    payload: dict[str, object] = {}

    if is_private is not None:
        payload["isPrivate"] = is_private

    if wall_access is not None:
        payload["wallAccess"] = wall_access

    if likes_visibility is not None:
        payload["likesVisibility"] = likes_visibility

    if show_last_seen is not None:
        payload["showLastSeen"] = show_last_seen

    if not payload:
        raise ValueError("No privacy fields provided to update")

    response = client.put("/api/users/me/privacy", json=payload)
    response.raise_for_status()

    return PrivacySettings.model_validate(response.json())


def update_notification_settings(
    client,
    *,
    enabled: bool | None = None,
    comments: bool | None = None,
    follows: bool | None = None,
    likes: bool | None = None,
    mentions: bool | None = None,
    sound: bool | None = None,
    wall_posts: bool | None = None,
) -> NotificationSettings:

    payload: dict[str, object] = {}

    if enabled is not None:
        payload["enabled"] = enabled

    if comments is not None:
        payload["comments"] = comments

    if follows is not None:
        payload["follows"] = follows

    if likes is not None:
        payload["likes"] = likes

    if mentions is not None:
        payload["mentions"] = mentions

    if sound is not None:
        payload["sound"] = sound

    if wall_posts is not None:
        payload["wallPosts"] = wall_posts

    if not payload:
        raise ValueError("No notification fields provided to update")

    response = client.put("/api/notifications/settings", json=payload)
    response.raise_for_status()

    return NotificationSettings.model_validate(response.json())