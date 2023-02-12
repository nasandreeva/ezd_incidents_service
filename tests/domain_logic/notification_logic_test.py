
from datetime import *
import project.domain_logic.notification_logic as notification_logic
import uuid
import project.tests.fixture.domain_logic.notification_logic_test_fixture as notification_logic_test_fixture


def create_sample_notification():
    return notification_logic.create_notification(
        str(uuid.uuid4()), 'user123', datetime.now())


def parse_row():
    assert True == False


def test_list_notifications():
    notification_logic_test_fixture.list_notifications()

    notifications = notification_logic.list_notifications('', 10)

    assert len(notifications) == 10


def test_list_incident_notifications():
    fixture = notification_logic_test_fixture.list_incident_notifications()

    result = notification_logic.list_incident_notifications(
        fixture['first_incident_id'], 10)

    assert len(result) == 5


def test_get_notification():
    fixture = notification_logic_test_fixture.get_notification()

    result = notification_logic.get_notification(
        fixture.notification_id)

    assert result.user_id == 'user123'


def test_create_notification():
    fixture = notification_logic_test_fixture.create_notification()

    result = notification_logic.create_notification(fixture)

    assert result.user_id == 'user123'
    assert result.incident_id != ''
