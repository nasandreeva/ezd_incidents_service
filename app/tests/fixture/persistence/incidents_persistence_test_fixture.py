from app.data_structures.incident import Incident
import app.persistence.incidents as incidents_persistence
from datetime import *
import uuid


def create_sample_incident_object():
    return Incident({'incident_name': 'test incident', 'user_id': 'user123', 'started_at': datetime.now()})


def create_sample_incident():
    incident = incidents_persistence.create_incident(
        create_sample_incident_object())
    return incident


def create_incident():
    return create_sample_incident_object()


def list_incidents():
    return create_sample_incident()


def get_incident():
    return create_sample_incident()


def update_incident():

    incident = create_sample_incident()

    print(incident)

    return dict({'incident_id': incident.incident_id, 'incident_name': 'abcd'})


def increment_positive_reports_count():
    return create_sample_incident()


def increment_negative_reports_count():
    return create_sample_incident()


def increment_resolved_notifications_count():
    return create_sample_incident()


def list_incidents():
    create_list_sample_incidents(str(uuid.uuid4()), 10)


def create_list_sample_incidents(incident_id, quantity):
    for i in range(quantity):
        create_sample_incident()


def get_user_id_from_incident():
    return create_sample_incident()