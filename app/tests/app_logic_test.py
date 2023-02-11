from datetime import *
import app.app_logic as app_logic
import app.tests.fixture.app_logic_test_fixture as app_logic_test_fixture


def test_list_incidents():
    fixture = app_logic_test_fixture.list_incidents()

    incidents = app_logic.list_incidents('', 10)

    assert len(incidents) == 10


def test_get_incident():
    fixture = app_logic_test_fixture.get_incident()

    incident = app_logic.get_incident(fixture.incident_id)

    assert incident.user_id == 'user123'


def test_register_incident():
    fixture = app_logic_test_fixture.register_incident()

    result = app_logic.register_incident(fixture)

    assert result.user_id == 'user123'


def test_report_incident_confirmed():
    fixture = app_logic_test_fixture.report_incident_confirmed()

    app_logic.report_incident_confirmed(fixture.incident_id, fixture.user_id)

    updated_incident = app_logic.get_incident(fixture.incident_id)

    assert updated_incident.positive_reports_count == 1


def test_report_incident_not_confirmed():
    
    fixture = app_logic_test_fixture.report_incident_not_confirmed()

    app_logic.report_incident_not_confirmed(
        fixture.incident_id, fixture.user_id)

    updated_incident = app_logic.get_incident(fixture.incident_id)

    assert updated_incident.negative_reports_count == 1


def test_recall_incident():
    fixture = app_logic_test_fixture.recall_incident()

    app_logic.recall_incident(fixture.incident_id, fixture.user_id)

    updated_incident = app_logic.get_incident(fixture.incident_id)

    assert updated_incident.recalled == 'True'


def test_mark_incident_as_ended():
    fixture = app_logic_test_fixture.mark_incident_as_ended()

    app_logic.mark_incident_as_ended(fixture.incident_id, fixture.user_id)

    updated_incident = app_logic.get_incident(fixture.incident_id)

    assert updated_incident.ended_at != None


def test_notify_incident_resolved():
    fixture = app_logic_test_fixture.notify_incident_resolved()

    app_logic.notify_incident_resolved(fixture.incident_id, fixture.user_id)

    updated_incident = app_logic.get_incident(fixture.incident_id)

    assert updated_incident.resolved_notifications_count == 1


def test_list_incident_reports():
    fixture = app_logic_test_fixture.list_incident_reports()
    result = app_logic.list_incident_reports(
        fixture['incident_id'], fixture['limit'])

    assert len(result) == 10


def test_list_incident_notifications():
    fixture = app_logic_test_fixture.list_incident_notifications()

    result = app_logic.list_incident_notifications(
        fixture['first_incident_id'], 10)

    assert len(result) == 5


def test_list_reports():
    fixture = app_logic_test_fixture.list_reports()

    result = app_logic.list_reports('', 10)

    assert len(result) == 10


def test_list_notifications():
    fixture = app_logic_test_fixture.list_notifications()

    notifications = app_logic.list_notifications('', 10)

    assert len(notifications) == 10


def test_check_if_user_can_create_report():
    fixture = app_logic_test_fixture.check_if_user_can_create_report()
    result = app_logic.check_if_user_can_create_report(
        fixture['user_id'], fixture['incident_id'])
    assert result == False


def test_report_incident_not_confirmed():
    fixture = app_logic_test_fixture.report_incident_not_confirmed()
    result = app_logic.report_incident_not_confirmed(fixture['user_id'], fixture['incident_id'])
    updated_incident = app_logic.get_incident(fixture['incident_id'])

    assert updated_incident.negative_reports_count == 1 


def test_report_incident_confirmed():
    fixture = app_logic_test_fixture.report_incident_confirmed()
    result = app_logic.report_incident_confirmed(fixture['user_id'], fixture['incident_id'])
    updated_incident = app_logic.get_incident(fixture['incident_id'])

    assert updated_incident.negative_reports_count == 1 