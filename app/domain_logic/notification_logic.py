from datetime import *
from app.core.exceptions import NotFoundException

from app.data_structures.notification import Notification
import app.persistence.notifications as notification_persistence
import app.domain_logic.incident_logic as incident_logic

def list_notifications(from_notification_id: str, limit: int):
    return notification_persistence.list_notifications(from_notification_id, limit)


def list_incident_notifications(incident_id: str, limit: int):
    incident_logic.ensure_incident_exists(incident_id)
    return notification_persistence.list_incident_notifications(incident_id, limit)


def create_notification(notification: Notification) -> Notification:
    incident_logic.ensure_incident_exists(notification.incident_id)
    return notification_persistence.create_notification(notification) 


def get_notification(notification_id: str) -> Notification:
    ensure_notification_exists(notification_id)
    return notification_persistence.get_notification(notification_id)


def ensure_notification_exists(notification_id: str):
    notification = notification_persistence.get_notification(notification_id)
    if notification is None:
        raise NotFoundException('Notification not found')