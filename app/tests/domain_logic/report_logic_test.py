
from datetime import *
from app.data_structures.report import Report
import app.domain_logic.report_logic as report_logic
import uuid
import app.tests.fixture.domain_logic.report_logic_test_fixture as report_logic_test_fixture


def parse_row():
    assert True == False


def test_list_reports():
    report_logic_test_fixture.list_reports()

    result = report_logic.list_reports('', 10)

    assert len(result) == 10


def test_list_incident_reports():
    fixture = report_logic_test_fixture.list_incident_reports()
    result = report_logic.list_incident_reports(
        fixture['incident_id'], fixture['limit'])

    assert len(result) == 10


def test_get_report():

    fixture = report_logic_test_fixture.create_sample_report_for_random_incident()

    result = report_logic.get_report(fixture.report_id)

    assert result.user_id == 'user123'


def test_create_report():
    fixture = report_logic_test_fixture.create_report()
    result = report_logic.create_report(fixture)
    assert result.user_id == 'user123'


def test_check_no_reports_for_incident():
    fixture = report_logic_test_fixture.check_no_reports_for_incident()
    result = report_logic.check_no_reports_for_incident(fixture.incident_id)
    assert result == False


def test_check_if_user_can_create_report():
    fixture = report_logic_test_fixture.check_if_user_can_create_report()
    result = report_logic.check_if_user_can_create_report(
        fixture['user_id'], fixture['incident_id'])
    assert result == False
