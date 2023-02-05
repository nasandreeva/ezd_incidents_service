from datetime import *

from app.data_structures.report import Report
import app.persistence.reports as persistence_reports


def list_reports(from_report_id: str, limit: int):
    return persistence_reports.list_reports(from_report_id, limit)


def list_incident_reports(incident_id: str, limit: int):
    return persistence_reports.list_incident_reports(incident_id, limit)


def create_report(report: Report):
    return persistence_reports.create_report(report)


def check_no_reports_for_incident(incident_id: str):
    return persistence_reports.check_no_reports_for_incident(incident_id)


def get_report(report_id: str):
    return persistence_reports.get_report(report_id)


def check_if_user_can_create_report(user_id: str, incident_id: str):
    reports = persistence_reports.get_user_reports_count_for_incident(
        user_id, incident_id)
    if reports['positive_reports'] == 0 or reports['negative_reports'] == 0:
        return True
    else:
        return False
