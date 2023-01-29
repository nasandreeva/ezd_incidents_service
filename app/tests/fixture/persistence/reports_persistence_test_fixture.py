from datetime import *
import uuid
from app.data_structures.report import Report
import app.persistence.reports as reports_persistence
import random as random

 
def create_reports(incident_id, quantity):
    for i in range(quantity):
        create_sample_report(incident_id)


def create_sample_report(incident_id):
    report = Report({'incident_id': incident_id, 'user_id': 'user123',
                    'at': datetime.now(), 'confirmed': bool(random.randint(0, 1))})
    return reports_persistence.create_report(report)


def create_sample_report_for_random_incident():
    return create_sample_report(str(uuid.uuid4()))


def create_report():
    return Report({'incident_id': str(uuid.uuid4()), 'user_id': 'user123',  'at': datetime.now(), 'confirmed': bool(random.randint(0, 1))})


def list_reports():
    create_reports(str(uuid.uuid4()), 10)


def list_incident_reports():
    incident_id = str(uuid.uuid4())
    create_reports(incident_id, 10)
    return {'incident_id': incident_id, 'limit': 10}
