from datetime import *
import uuid
from app.data_structures.notification import Notification
import app.domain_logic.notification_logic as notification_logic


def do_list_incident_notifications(first_incident_id, second_incident_id):

    create_incident_notifications(first_incident_id, 5)
    create_incident_notifications(second_incident_id, 5)

    return {'first_incident_id': first_incident_id, 'second_incident_id': second_incident_id}


def list_incident_notifications():
    first_incident_id = str(uuid.uuid4())
    second_incident_id = str(uuid.uuid4())
    return do_list_incident_notifications(first_incident_id, second_incident_id)


def create_incident_notifications(incident_id, quantity):
    for i in range(quantity):
        create_notification_for_incident(incident_id)


def create_notification_for_incident(incident_id):
    notification_logic.create_notification(
        Notification({'incident_id': incident_id,
                     'user_id': 'user123', 'at': datetime.now()}))


def get_notification():
    return notification_logic.create_notification(
        Notification({'incident_id': str(uuid.uuid4()), 'user_id': 'user123', 'at': datetime.now()}))


def list_notifications():
    create_incident_notifications(str(uuid.uuid4()), 10)


def create_notification():
    return Notification({'incident_id': str(uuid.uuid4()), 'user_id': 'user123', 'at': datetime.now()})
