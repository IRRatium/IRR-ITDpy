from __future__ import annotations

from ..models import Notifications
from ._common import build_query


def get_notifications(client, offset: int = 0, limit: int = 20) -> Notifications:
    query = build_query({"offset": offset, "limit": limit})
    response = client.get(f"/api/notifications/?{query}")
    response.raise_for_status()
    return Notifications.model_validate(response.json())


def mark_notification_read(client, notification_id: str) -> bool:
    response = client.post(f"/api/notifications/{notification_id}/read")
    response.raise_for_status()
    data = response.json()
    return bool(data.get("success", False))


def mark_all_notification_read(client, notification_ids=None) -> bool:
    """
    Отметить все уведомления как прочитанные.
    notification_ids — не используется, оставлен для совместимости.
    """
    response = client.post("/api/notifications/read-all")
    response.raise_for_status()
    return response.status_code in (200, 204)
