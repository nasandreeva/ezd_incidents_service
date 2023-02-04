from ctypes import Union
from datetime import *

from app.data_structures.incident import Incident
from app.data_structures.notification import Notification
from app.data_structures.report import Report
import app.domain_logic.incident_logic as incident_logic
import app.domain_logic.notification_logic as notification_logic
import app.domain_logic.report_logic as report_logic


def list_incidents(cursor_value: int, limit: int = 10) -> list[Incident]:
    return incident_logic.list_incidents(cursor_value, limit)


def get_incident(incident_id: str) -> Incident:
    return incident_logic.get_incident(incident_id)


def register_incident(attrs: dict) -> Incident:
    return incident_logic.create_incident(Incident(attrs))


def report_incident_confirmed(incident_id: str, user_id: str) -> Incident:
    report = report_logic.create_report(
        Report(dict([('incident_id', incident_id), ('user_id', user_id), ('confirmed', True)])))
    incident_logic.increment_positive_reports_count(incident_id)
    return incident_logic.get_incident(incident_id)


def report_incident_not_confirmed(incident_id: str, user_id: str) -> Incident:
    report = report_logic.create_report(
        Report(dict([('incident_id', incident_id), ('user_id', user_id), ('confirmed', False)])))
    incident_logic.increment_negative_reports_count(incident_id)
    return incident_logic.get_incident(incident_id)


def recall_incident(incident_id: str, user_id: str) -> Incident:
    incident = incident_logic.get_incident(incident_id)
    if incident.positive_reports_count == 0 and incident.negative_reports_count == 0:
        incident_logic.mark_incident_as_recalled(incident_id, user_id)
        return incident_logic.get_incident(incident_id)
    else:
        raise Exception("Incident can not be recalled")


def mark_incident_as_ended(incident_id: str, user_id: str) -> Incident:
    incident = incident_logic.get_incident(incident_id)
    incident_logic.mark_incident_as_ended(incident_id, user_id)
    return incident_logic.get_incident(incident_id)


def notify_incident_resolved(incident_id: str, user_id: str) -> Incident:
    notification_logic.create_notification(Notification(
        dict([('incident_id', incident_id), ("user_id", user_id)])))
    incident_logic.increment_resolved_notifications_count(incident_id)
    return incident_logic.get_incident(incident_id)


def list_incident_reports(incident_id: str, limit: int) -> list[Report]:
    return report_logic.list_incident_reports(incident_id, limit)


def list_incident_notifications(incident_id: str, limit: int) -> list[Notification]:
    return notification_logic.list_incident_notifications(incident_id, limit)

#
#  Administrative functions
#


def list_reports(from_report_id: str, limit: int):
    return report_logic.list_reports(from_report_id, limit)


def list_notifications(from_notification_id: str, limit: int):
    return notification_logic.list_notifications(from_notification_id, limit)
