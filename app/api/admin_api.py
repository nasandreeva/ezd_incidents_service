import app.app_logic as app_logic
from datetime import *
from app.data_structures.incident import Incident
from app.data_structures.notification import Notification
from app.data_structures.report import Report


def list_incidents(cursor_value: str, limit: str = '10') -> list[Incident]:
    return app_logic.list_incidents(cursor_value, int(limit))


def get_incident(incident_id: str) -> Incident:
    return app_logic.get_incident(incident_id)


def list_incident_reports(incident_id: str, limit: str = '10') -> list[Report]:
    return app_logic.list_incident_reports(incident_id, int(limit))


def list_incident_notifications(incident_id: str, limit: str = '10') -> list[Notification]:
    return app_logic.list_incident_notifications(incident_id, int(limit))


def list_reports(from_report_id: str, limit: str = '10'):
    return app_logic.list_reports(from_report_id, int(limit))


def list_notifications(from_notification_id: str, limit: str = '10'):
    return app_logic.list_notifications(from_notification_id, int(limit))
