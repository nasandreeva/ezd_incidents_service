
from datetime import *
import project.domain_logic.incident_logic as incident_logic
import project.tests.fixture.domain_logic.incident_logic_test_fixture as incident_logic_test_fixture


def parse_row():
    assert True == False


def test_list_incidents():
    incident_logic_test_fixture.list_incidents()

    incidents = incident_logic.list_incidents('', 10)

    assert len(incidents) == 10


def test_get_incident():

    fixture = incident_logic_test_fixture.create_sample_incident()

    incident = incident_logic.get_incident(fixture.incident_id)

    assert incident.user_id == 'user123'


def test_create_incident():
    fixture = incident_logic_test_fixture.create_incident()

    result = incident_logic.create_incident(fixture)

    assert result.user_id == 'user123'


def test_update_incident():
    fixture = incident_logic_test_fixture.update_incident()

    incident_logic.update_incident(fixture.get('incident_id'), fixture)

    updated_incident = incident_logic.get_incident(
        fixture.get('incident_id'))

    assert updated_incident.incident_name == 'abcd'


def test_increment_positive_reports_count():
    fixture = incident_logic_test_fixture.create_sample_incident()
    attrs = dict([('positive_reports_count', 10)])
    incident_logic.update_incident(fixture.incident_id, attrs)

    incident_logic.increment_positive_reports_count(
        fixture.incident_id)

    updated_incident = incident_logic.get_incident(fixture.incident_id)

    assert updated_incident.positive_reports_count == 11


def test_increment_negative_reports_count():
    fixture = incident_logic_test_fixture.create_sample_incident()
    attrs = dict([('negative_reports_count', 4)])
    incident_logic.update_incident(fixture.incident_id, attrs)
    incident_logic.increment_negative_reports_count(
        fixture.incident_id)
    updated_incident = incident_logic.get_incident(fixture.incident_id)
    assert updated_incident.negative_reports_count == 5


def test_increment_resolved_notifications_count():
    fixture = incident_logic_test_fixture.create_sample_incident()
    attrs = dict([('resolved_notifications_count', 2)])
    incident_logic.update_incident(fixture.incident_id, attrs)
    incident_logic.increment_resolved_notifications_count(
        fixture.incident_id)
    updated_incident = incident_logic.get_incident(fixture.incident_id)
    assert updated_incident.resolved_notifications_count == 3
