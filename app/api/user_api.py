import app.app_logic as app_logic
from datetime import *
from app.data_structures.incident import Incident
from app.data_structures.notification import Notification
from app.data_structures.report import Report


def list_incidents(cursor_value: str, limit: str = '10') -> list[Incident]:
    return app_logic.list_incidents(cursor_value, int(limit))


def get_incident(incident_id: str) -> Incident:
    return app_logic.get_incident(incident_id)


def register_incident(incident_name: str,
                      user_id: str,
                      started_at: str) -> Incident:

    return app_logic.register_incident(dict([('incident_name', incident_name),
                                             ('user_id', user_id),
                                             ('started_at', datetime.fromisoformat(started_at))]))


def report_incident_confirmed(incident_id: str, user_id: str) -> Incident:
    return app_logic.report_incident_confirmed(incident_id, user_id)


def report_incident_not_confirmed(incident_id: str, user_id: str) -> Incident:
    return app_logic.report_incident_not_confirmed(incident_id, user_id)


def recall_incident(incident_id: str, user_id: str) -> Incident:
    return app_logic.recall_incident(incident_id, user_id)


def mark_incident_as_ended(incident_id: str, user_id: str) -> Incident:
    return app_logic.mark_incident_as_ended(incident_id, user_id)


def notify_incident_resolved(incident_id: str, user_id: str) -> Incident:
    return app_logic.notify_incident_resolved(incident_id, user_id)


def list_incident_reports(incident_id: str, limit: str = '10') -> list[Report]:
    return app_logic.list_incident_reports(incident_id, int(limit))


def list_incident_notifications(incident_id: str, limit: str = '10') -> list[Notification]:
    return app_logic.list_incident_notifications(incident_id, int(limit))
