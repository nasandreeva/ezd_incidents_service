from datetime import *
import uuid
from project.data_structures.report import Report
import project.domain_logic.report_logic as report_logic
import random as random


def create_reports(incident_id, quantity):
    for i in range(quantity):
        create_sample_report(incident_id)


def create_sample_report(incident_id):
    report = Report({'incident_id': incident_id, 'user_id': 'user123',
                    'at': datetime.now(), 'confirmed': bool(random.randint(0, 1))})
    return report_logic.create_report(report)


def create_sample_report_for_random_incident():
    return create_sample_report(str(uuid.uuid4()))


def create_report():
    return Report({'incident_id': str(uuid.uuid4()), 'user_id': 'user123',  'at': datetime.now(), 'confirmed': bool(random.randint(0, 1))})


def list_reports():
    create_reports(str(uuid.uuid4()), 10)


def list_incident_reports():
    incident_id = str(uuid.uuid4())
    create_reports(incident_id, 10)
    return dict({'incident_id': incident_id, 'limit': 10})


def check_no_reports_for_incident():
    return create_sample_report_for_random_incident()


def create_sample_positive_report(incident_id, user_id):
    report = Report({'incident_id': incident_id, 'user_id': user_id,
                    'at': datetime.now(), 'confirmed': True})
    return report_logic.create_report(report)


def create_sample_negative_report(incident_id, user_id):
    report = Report({'incident_id': incident_id, 'user_id': user_id,
                    'at': datetime.now(), 'confirmed': False})
    return report_logic.create_report(report)


def check_if_user_can_create_report():
    incident_id = str(1234)
    user_id = 'user123'
    create_sample_negative_report(incident_id, user_id)
    create_sample_positive_report(incident_id, user_id)

    return dict({'user_id': user_id, 'incident_id': incident_id})
