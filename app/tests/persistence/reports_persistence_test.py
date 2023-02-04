
from datetime import *
from app.data_structures.report import Report
import app.persistence.reports as reports_persistence
import uuid
import app.tests.fixture.persistence.reports_persistence_test_fixture as reports_persistence_test_fixture


def parse_row():
    assert True == False


def test_list_reports():
    reports_persistence_test_fixture.list_reports()

    result = reports_persistence.list_reports('', 10)

    assert len(result) == 10


def test_list_incident_reports():
    fixture = reports_persistence_test_fixture.list_incident_reports()
    result = reports_persistence.list_incident_reports(
        fixture['incident_id'], fixture['limit'])

    assert len(result) == 10


def test_get_report():

    fixture = reports_persistence_test_fixture.create_sample_report_for_random_incident()

    result = reports_persistence.get_report(fixture.report_id)

    assert result.user_id == 'user123'


def test_create_report():
    fixture = reports_persistence_test_fixture.create_report()

    result = reports_persistence.create_report(fixture)

    assert result.user_id == 'user123'


def test_get_user_reports_count_for_incident():
    fixture = reports_persistence_test_fixture.get_user_reports_count_for_incident()

    result = reports_persistence.get_user_reports_count_for_incident(
        fixture['user_id'], fixture['incident_id'])

    assert result == {'positive_reports': 1, 'negative_reports': 1}
