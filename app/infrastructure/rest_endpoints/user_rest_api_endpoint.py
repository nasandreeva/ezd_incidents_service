from flask import Flask, request
import flask
import app.api.user_api as user_api

app = Flask(__name__)


# def list_incidents(cursor_value: int, limit: str = '10') -> list[Incident]:
# def get_incident(incident_id: str) -> Incident:


# def register_incident(incident_name,
# def report_incident_confirmed(incident_id: str, user_id: str) -> Incident:
# def report_incident_not_confirmed(incident_id: str, user_id: str) -> Incident:
# def recall_incident(incident_id: str, user_id: str) -> Incident:
# def mark_incident_as_ended(incident_id: str, user_id: str) -> Incident:
# def notify_incident_resolved(incident_id: str, user_id: str) -> Incident:
# def list_incident_reports(incident_id: str, limit: str='10') -> list[Report]:
# def list_incident_notifications(incident_id: str, limit: str='10') -> list[Notification]:


@ app.route('/incidents', methods=['GET'])
def list_incidents():
    return flask.json.jsonify(user_api.list_incidents('', '10'))


@ app.route('/incidents', methods=['POST'])
def register_incident():
    incident = user_api.register_incident(request.form.get('incident_name'),
                                          request.form.get(
        'user_id'),
        request.form.get('started_at'))
    return incident.toJSON()


@ app.route('/incidents/incident_id/confirmed', methods=['POST'])
def report_incident_confirmed():
    pass


@ app.route('/incidents/incident_id/not_confirmed', methods=['POST'])
def report_incident_not_confirmed():
    pass


@ app.route('/incidents/incident_id/recall', methods=['PATCH'])
def recall_incident():
    pass


@ app.route('/incidents/incident_id/mark_as_ended', methods=['PATCH'])
def mark_incident_as_ended():
    pass


@ app.route('/incidents/incident_id/resolved', methods=['PATCH'])
def notify_incident_resolved():
    pass


@ app.route('/incidents/incident_id/reports', methods=['GET'])
def list_incident_reports():
    pass


@ app.route('/incidents/incident_id/notifications', methods=['GET'])
def list_incident_notifications():
    pass
