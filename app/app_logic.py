from ctypes import Union
from datetime import *

from app.data_structures.incident import Incident
from app.data_structures.notification import Notification
import app.domain_logic.incident_logic as incident_logic
import app.domain_logic.notification_logic as notification_logic
import app.domain_logic.report_logic as report_logic


def list_incidents(cursor_value: int, limit: int = 10) -> list[Incident]:
    return incident_logic.list_incidents(cursor_value, limit)


def get_incident_info(incident_id) -> Incident:
    notifications = notification_logic.list_notifications_about_ends_of_incidents(incident_id)
    reports = report_logic.list_reports(incident_id)
    incident = incident_logic.get_info_about_incident(incident_id)
    incident.notifications = notifications
    return embed_notifications_into_incident(incident, notifications, reports)

def embed_notifications_into_incident(incident: Incident, notifications_to_embed: list[Notification]):
    incident.notifications = notifications_to_embed
    return incident.notifications

def register_incident(incident_name: str, user_id: str, started_at: datetime) -> Incident:
    return incident_logic.create_incident(incident_name, user_id, started_at) 


def report_incident_confirmed(incident_id, user_id: str) -> Incident:
    return report_logic.create_confirmation_report(incident_id, user_id)


def report_incident_not_confirmed(incident_id, user_id: str) -> Incident:
    return report_logic.create_not_confirmation_report(user_id, incident_id)
    

def recall_incident(incident_id, user_id: str) -> Incident:
    incident = incident_logic.get_incident(incident_id)
    if incident.positive_reports_count == 0 and incident.negative_reports_count == 0:
        return incident_logic.mark_incident_as_recalled(incident_id, user_id)
    else:
        raise Exception("Incident can not be recalled")


def notify_incident_resolved(incident_id, user_id: str) -> Incident:
    return notification_logic.create_notification_about_end_of_incident(user_id, incident_id)