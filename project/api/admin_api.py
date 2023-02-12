import project.app_logic as app_logic
from datetime import *
from project.core.exceptions import ForbiddenException, InvalidInputException, NotFoundException
from project.data_structures.incident import Incident
from project.data_structures.notification import Notification
from project.data_structures.report import Report
from project.core.validators import Validators


def list_incidents(cursor_value: str, limit: str = '10') -> list[Incident]:
    if Validators.cursor_value_validator({'(cursor_value': cursor_value}) and Validators.limit_validator({'limit': limit}):
        return app_logic.list_incidents(cursor_value, int(limit))
    else:
        raise InvalidInputException('Invalid input')


def get_incident(incident_id: str) -> Incident:
    if Validators.incident_id_validator(incident_id):
        return app_logic.get_incident(incident_id)
    else:
        raise NotFoundException('Not Found')


def list_incident_reports(incident_id: str, limit: str = '10') -> list[Report]:
    if Validators.incident_id_validator({'incident_id': incident_id}) and Validators.limit_validator({'limit': limit}):
        return app_logic.list_incident_reports(incident_id, int(limit))
    else:
        raise InvalidInputException('Invalid input')


def list_incident_notifications(incident_id: str, limit: str = '10') -> list[Notification]:
    if Validators.incident_id_validator({'incident_id': incident_id}) and Validators.limit_validator({'limit': limit}):
        return app_logic.list_incident_notifications(incident_id, int(limit))
    else:
        raise InvalidInputException('Invalid input')


def list_reports(from_report_id: str, limit: str = '10'):
    if Validators.from_report_id_validator({'from_report_id': from_report_id}) and Validators.limit_validator({'limit': limit}):
        return app_logic.list_reports(from_report_id, int(limit))
    else:
        raise InvalidInputException('Invalid input')


def list_notifications(from_notification_id: str, limit: str = '10'):
    if Validators.from_notification_id_validator({'from_notification_id': from_notification_id}) and Validators.limit_validator({'limit': limit}):
        return app_logic.list_notifications(from_notification_id, int(limit))
    else:
        raise InvalidInputException('Invalid input')
