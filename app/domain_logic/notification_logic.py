from datetime import *

from app.data_structures.notification import Notification
import app.persistence.notifications as notification_persistence

def list_notifications(from_notification_id: str, limit: int):
    return notification_persistence.list_notifications(from_notification_id, limit)

def list_incident_notifications(incident_id: str, limit: int):
    return notification_persistence.list_incident_notifications(incident_id, limit)

def create_notification(notification: Notification) -> Notification:
    return notification_persistence.create_notification(notification) 

def get_notification(notification_id: str) -> Notification:
    return notification_persistence.get_notification(notification_id)