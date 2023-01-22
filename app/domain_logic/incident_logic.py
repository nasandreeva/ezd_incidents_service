from datetime import *

from app.data_structures.incident import Incident
import app.persistence.incidents as incident_persistence


def list_incidents(from_incident_id, limit) -> list[Incident]:
    return incident_persistence.list_incidents(from_incident_id, limit)


def get_info_about_incident(incident_id) -> Incident:
    return incident_persistence.info_about_incident(incident_id)


def get_incident(incident_id) -> Incident:
    return incident_persistence.get_incident(incident_id)


def create_incident(incident: Incident):
    return incident_persistence.create_incident(incident)


def update_incident(incident_id: str, attrs):
    return incident_persistence.update_incident(incident_id, attrs)


def mark_incident_as_recalled(incident_id, user_id: str) -> Incident:
    incident = incident.get_incident(incident_id)
    if incident.user_id == user_id:
        return incident_persistence.update_incident(incident_id, {'recalled': True})
    else:
        raise Exception("User can not recall incident")


def increment_all_reports_count(positive_reports_count: int, negative_reports_count: int):
    return incident_persistence.increment_all_reports_count(negative_reports_count, positive_reports_count)


def increment_positive_reports_count(positive_reports_count: int):
    return incident_persistence.increment_positive_reports_count(positive_reports_count)


def increment_negative_reports_count(negative_reports_count: int):
    return incident_persistence.increment_negative_reports_count(negative_reports_count)


def increment_resolved_notifications_count(incident_id):
    return incident_persistence.increment_resolved_notifications_count(incident_id)
