from datetime import *

from app.data_structures.notification import Notification
import app.persistence.notifications as notification_persistence

def list_notifications_about_ends_of_incidents(incident_id, incident_name: str, resolved_notifications_count: int) -> list[Notification]:
    return notification_persistence.list_notifications(incident_id, incident_name, resolved_notifications_count)

def create_notification_about_end_of_incident(user_id: str, ended_at: datetime, incident_id, incident_name: str):
    return notification_persistence.create_notification(incident_id, incident_name, user_id, ended_at)
    