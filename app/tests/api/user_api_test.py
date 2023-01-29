import app.tests.fixture.app_logic_test_fixture as app_logic_test_fixture
import app.api.user_api as user_api


def test_list_incidents():
    fixture = app_logic_test_fixture.list_incidents()

    incidents = user_api.list_incidents('', '10')

    assert len(incidents) == 10


def test_get_incident():
    fixture = app_logic_test_fixture.get_incident()
    incident = user_api.get_incident(fixture.incident_id)

    assert incident.user_id == 'user123'


def test_register_incident():
    fixture = app_logic_test_fixture.register_incident()

    result = user_api.register_incident(fixture['incident_name'],
                                        fixture['user_id'],
                                        str(fixture['started_at']))

    assert result.user_id == 'user123'


def test_report_incident_confirmed():
    fixture = app_logic_test_fixture.report_incident_confirmed()

    user_api.report_incident_confirmed(fixture.incident_id, fixture.user_id)

    updated_incident = user_api.get_incident(fixture.incident_id)

    assert updated_incident.positive_reports_count == 1


def test_report_incident_not_confirmed():
    fixture = app_logic_test_fixture.report_incident_not_confirmed()

    user_api.report_incident_not_confirmed(
        fixture.incident_id, fixture.user_id)

    updated_incident = user_api.get_incident(fixture.incident_id)

    assert updated_incident.negative_reports_count == 1


def test_recall_incident():
    fixture = app_logic_test_fixture.recall_incident()

    user_api.recall_incident(fixture.incident_id, fixture.user_id)

    updated_incident = user_api.get_incident(fixture.incident_id)

    assert updated_incident.recalled == 'True'


def test_mark_incident_as_ended():
    fixture = app_logic_test_fixture.mark_incident_as_ended()

    user_api.mark_incident_as_ended(fixture.incident_id, fixture.user_id)

    updated_incident = user_api.get_incident(fixture.incident_id)

    assert updated_incident.ended_at != None


def test_notify_incident_resolved():
    fixture = app_logic_test_fixture.notify_incident_resolved()

    user_api.notify_incident_resolved(fixture.incident_id, fixture.user_id)

    updated_incident = user_api.get_incident(fixture.incident_id)

    assert updated_incident.resolved_notifications_count == 1


def test_list_incident_reports():
    fixture = app_logic_test_fixture.list_incident_reports()
    result = user_api.list_incident_reports(
        fixture['incident_id'], fixture['limit'])

    assert len(result) == 10


def test_list_incident_notifications():
    fixture = app_logic_test_fixture.list_incident_notifications()

    notifications = user_api.list_incident_notifications(fixture['first_incident_id'], '10')

    assert len(notifications) == 5
