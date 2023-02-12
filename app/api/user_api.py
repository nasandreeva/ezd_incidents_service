import app.app_logic as app_logic
from datetime import *
from app.core.exceptions import ForbiddenException, InvalidInputException, NotFoundException
from app.core.validators import Validators
from app.data_structures.incident import Incident
from app.data_structures.notification import Notification
from app.data_structures.report import Report


def list_incidents(cursor_value: str, limit: str = '10') -> list[Incident]:
    if Validators.cursor_value_validator({'cursor_value': cursor_value}) and Validators.limit_validator({'limit': limit}):
        return app_logic.list_incidents(cursor_value, int(limit))
    else:
        raise InvalidInputException('Invalid input')


def get_incident(incident_id: str) -> Incident:
    if Validators.incident_id_validator({'incident_id': incident_id}):
        return app_logic.get_incident(incident_id)
    else:
        raise NotFoundException('Not Found')


def register_incident(incident_name: str,
                      user_id: str,
                      started_at: str) -> Incident:

    if Validators.incident_name_validator({'incident_name': incident_name}) and Validators.user_id_validator({'user_id': user_id}) and Validators.started_at_validator({'started_at': started_at}):
        return app_logic.register_incident(dict([('incident_name', incident_name),
                                                ('user_id', user_id),
                                                ('started_at', datetime.fromisoformat(started_at))]))
    else:
        raise ForbiddenException('Forbidden')


def report_incident_confirmed(incident_id: str, user_id: str) -> Incident:
    if Validators.incident_id_validator({'incident_id': incident_id}) and Validators.user_id_validator({'user_id': user_id}):
        return app_logic.report_incident_confirmed(incident_id, user_id)
    else:
        raise NotFoundException('Not Found')


def report_incident_not_confirmed(incident_id: str, user_id: str) -> Incident:
    if Validators.incident_id_validator({'incident_id': incident_id}) and Validators.user_id_validator({'user_id': user_id}):
        return app_logic.report_incident_not_confirmed(incident_id, user_id)
    else:
        raise NotFoundException('Not Found')


def recall_incident(incident_id: str, user_id: str) -> Incident:
    if Validators.incident_id_validator({'incident_id': incident_id}) and Validators.user_id_validator({'user_id': user_id}):
        return app_logic.recall_incident(incident_id, user_id)
    else:
        raise NotFoundException('Not Found')


def mark_incident_as_ended(incident_id: str, user_id: str) -> Incident:
    if Validators.incident_id_validator({'incident_id': incident_id}) and Validators.user_id_validator({'user_id': user_id}):
        return app_logic.mark_incident_as_ended(incident_id, user_id)
    else:
        raise NotFoundException('Not Found')


def notify_incident_resolved(incident_id: str, user_id: str) -> Incident:
    if Validators.incident_id_validator({'incident_id': incident_id}) and Validators.user_id_validator({'user_id': user_id}):
        return app_logic.notify_incident_resolved(incident_id, user_id)
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
