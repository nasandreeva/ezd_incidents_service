from datetime import *

from app.data_structures.incident import Incident
import app.persistence.incidents as incident_persistence


def list_incidents(incident_id, started_at, ended_at) -> list[Incident]:
    return incident_persistence.list_incidents(incident_id, started_at, ended_at)


def get_info_about_incident(incident_id) -> Incident:
    return incident_persistence.info_about_incident(incident_id)


def get_incident(incident_id) -> Incident:
    return incident_persistence.get_incident(incident_id)


def create_incident(incident_name: str, user_id: str, started_at: datetime):
    return incident_persistence.create_incident(incident_name, user_id, started_at)


def mark_incident_as_recalled(incident_id, user_id: str) -> Incident:
    incident = incident.get_incident(incident_id)
    if incident.user_id == user_id:
        return incident_persistence.update_incident(incident_id, {'recalled': True})
    else:
        raise Exception("User can not recall incident")


def plus_one_meter_report(positive_reports_count: int, negative_reports_count: int):
    return incident_persistence.increment_all_reports_count(negative_reports_count, positive_reports_count)


def plus_one_meter_confirmed(positive_reports_count: int):
    return incident_persistence.increment_positive_reports_count(positive_reports_count)


def plus_one_meter_not_confirmed(negative_reports_count: int):
    return incident_persistence.increment_negative_reports_count(negative_reports_count)
