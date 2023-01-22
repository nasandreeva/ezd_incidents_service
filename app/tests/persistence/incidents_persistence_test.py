
from datetime import *
import app.persistence.incidents as incidents_persistence
import app.tests.fixture.incidents_persistence_test_fixture as incidents_persistence_test_fixture


def parse_row():
    assert True == False


def test_list_incidents():
    incidents_persistence_test_fixture.list_incidents()

    incidents = incidents_persistence.list_incidents('', 10)

    assert len(incidents) == 10


def test_get_incident():

    incident = incidents_persistence_test_fixture.create_sample_incident()

    assert incident.user_id == 'user123'


def test_create_incident():
    fixture = incidents_persistence_test_fixture.create_incident()

    result = incidents_persistence.create_incident(fixture)

    assert result.user_id == 'user123'


def test_update_incident():
    fixture = incidents_persistence_test_fixture.update_incident()

    incidents_persistence.update_incident(fixture.get('incident_id'), fixture)

    updated_incident = incidents_persistence.get_incident(
        fixture.get('incident_id'))

    assert updated_incident.incident_name == 'abcd'


def test_increment_positive_reports_count():
    fixture = incidents_persistence_test_fixture.create_sample_incident()
    attrs = dict([('positive_reports_count', 10)])
    incidents_persistence.update_incident(fixture.incident_id, attrs)

    incidents_persistence.increment_positive_reports_count(
        fixture.incident_id)

    updated_incident = incidents_persistence.get_incident(fixture.incident_id)

    assert updated_incident.positive_reports_count == 11


def test_increment_negative_reports_count():
    fixture = incidents_persistence_test_fixture.create_sample_incident()
    attrs = dict([('negative_reports_count', 4)])
    incidents_persistence.update_incident(fixture.incident_id, attrs)
    incidents_persistence.increment_negative_reports_count(
        fixture.incident_id)
    updated_incident = incidents_persistence.get_incident(fixture.incident_id)
    assert updated_incident.negative_reports_count == 5


def test_increment_resolved_notifications_count():
    fixture = incidents_persistence_test_fixture.create_sample_incident()
    attrs = dict([('resolved_notifications_count', 2)])
    incidents_persistence.update_incident(fixture.incident_id, attrs)
    incidents_persistence.increment_resolved_notifications_count(
        fixture.incident_id)
    updated_incident = incidents_persistence.get_incident(fixture.incident_id)
    assert updated_incident.resolved_notifications_count == 3
