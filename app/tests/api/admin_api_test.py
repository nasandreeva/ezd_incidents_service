import app.tests.fixture.app_logic_test_fixture as app_logic_test_fixture
import app.api.admin_api as admin_api

def test_list_incidents():
    fixture = app_logic_test_fixture.list_incidents()

    incidents = admin_api.list_incidents('', '10')

    assert len(incidents) == 10

def test_get_incident():
    fixture = app_logic_test_fixture.get_incident()
    incident = admin_api.get_incident(fixture.incident_id)

    assert incident.user_id == 'user123'

def test_list_incident_reports():
    fixture = app_logic_test_fixture.list_incident_reports()
    result = admin_api.list_incident_reports(
        fixture['incident_id'], fixture['limit'])

    assert len(result) == 10

def test_list_incident_notifications():
    fixture = app_logic_test_fixture.list_incident_notifications()

    notifications = admin_api.list_incident_notifications(fixture['first_incident_id'], '10')

    assert len(notifications) == 5

def test_list_reports():
    fixture = app_logic_test_fixture.list_reports()

    result = admin_api.list_reports('', '10')

    assert len(result) == 10

def test_list_notifications():
    fixture = app_logic_test_fixture.list_notifications()

    notifications = admin_api.list_notifications('', '10')

    assert len(notifications) == 10

