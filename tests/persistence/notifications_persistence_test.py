
from datetime import *
import project.persistence.notifications as notifications_persistence
import uuid
import project.tests.fixture.persistence.notifications_persistence_test_fixture as notifications_persistence_test_fixture


def create_sample_notification():
    return notifications_persistence.create_notification(
        str(uuid.uuid4()), 'user123', datetime.now())


def parse_row():
    assert True == False

 
def test_list_notifications():
    notifications_persistence_test_fixture.list_notifications()

    notifications = notifications_persistence.list_notifications('', 10)

    assert len(notifications) == 10


def test_list_incident_notifications():
    fixture = notifications_persistence_test_fixture.list_incident_notifications_for_random_incidents()

    result = notifications_persistence.list_incident_notifications(
        fixture['first_incident_id'], 10)

    assert len(result) == 5


def test_get_notification():
    fixture = notifications_persistence_test_fixture.get_notification()

    result = notifications_persistence.get_notification(
        fixture.notification_id)

    assert result.user_id == 'user123'


def test_create_notification():
    fixture = notifications_persistence_test_fixture.create_notification()

    result = notifications_persistence.create_notification(fixture)

    assert result.user_id == 'user123'
    assert result.incident_id != ''
