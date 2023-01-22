from datetime import *

from app.data_structures.report import Report
import app.persistence.reports as persistence_reports


def list_reports(incident_id) -> list[Report]:
    return list_reports(incident_id)

def create_confirmation_report(positive_reports_count, incident_id, user_id):
    return persistence_reports.create_report(incident_id, user_id, positive_reports_count)

def create_not_confirmation_report(user_id, negative_reports_count, incident_id):
    return persistence_reports.create_report(incident_id, user_id, negative_reports_count)

def search_for_reports(positive_reports_count, negative_reports_count: int, incident_id, incident_name: str):
    return persistence_reports.check_no_reports_for_incident(positive_reports_count, negative_reports_count, incident_id, incident_name)