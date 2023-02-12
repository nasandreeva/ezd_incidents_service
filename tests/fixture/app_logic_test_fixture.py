import uuid
from project.data_structures.incident import Incident
from datetime import *
import project.tests.fixture.app_logic_test_fixture as app_logic_test_fixture
import project.tests.fixture.domain_logic.incident_logic_test_fixture as incident_logic_test_fixture
import project.tests.fixture.domain_logic.report_logic_test_fixture as report_logic_test_fixture
import project.tests.fixture.domain_logic.notification_logic_test_fixture as notification_logic_test_fixture
import project.domain_logic.incident_logic as incident_logic


def create_sample_incident():
    incident = incident_logic.create_incident(Incident(
        dict([('incident_name', 'test incident'), ('user_id', 'user123'), ('started_at', datetime.now())])))
    print(vars(incident))
    return incident



def list_incidents():
    return incident_logic_test_fixture.list_incidents()


def get_incident():
    return create_sample_incident()


def register_incident():
    return dict([('incident_name', 'test incident'), ('user_id', 'user123'), ('started_at', datetime.now())])


def report_incident_confirmed():
    return create_sample_incident()


def report_incident_not_confirmed():
    return create_sample_incident()


def recall_incident():
    return create_sample_incident()


def mark_incident_as_ended():
    return create_sample_incident()


def notify_incident_resolved():
    return create_sample_incident()


def list_incident_reports():
    return report_logic_test_fixture.list_incident_reports()


def list_incident_notifications():
    return notification_logic_test_fixture.list_incident_notifications()


def list_reports():
    return report_logic_test_fixture.list_reports()


def list_notifications():
    return notification_logic_test_fixture.list_notifications()



def check_if_user_can_create_report():
    incident_id = str(1234)
    user_id = 'user123'
    report_logic_test_fixture.create_sample_negative_report(incident_id, user_id)
    report_logic_test_fixture.create_sample_positive_report(incident_id, user_id)

    return dict({'user_id': user_id, 'incident_id': incident_id})


def report_incident_not_confirmed():
    user_id = 'user123'
    incident_id = str(1234)
    report_logic_test_fixture.create_sample_negative_report(incident_id, user_id)
    return dict({'user_id': user_id, 'incident_id': incident_id})

def report_incident_confirmed():
    user_id = 'user123'
    incident_id = str(1234)
    report_logic_test_fixture.create_sample_positive_report(incident_id, user_id)
    return dict({'user_id': user_id, 'incident_id': incident_id})