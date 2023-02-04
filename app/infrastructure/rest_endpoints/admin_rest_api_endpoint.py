from flask import Flask, request
import flask
import app.api.admin_api as admin_api
import app.infrastructure.rest_endpoints.helpers.rest_endpoint_helper as rest_api
from app.infrastructure.rest_endpoints.adapters.json_api_adapter import JsonApiResponse

app = Flask(__name__)


@ app.route('/incidents', methods=['GET'])
def list_incidents():
    incidents = admin_api.list_incidents('', '10')
    return rest_api.response(200, JsonApiResponse(incidents).render())


@ app.route('/incidents/<incident_id>', methods=['GET'])
def get_incident(incident_id):
    incident = admin_api.get_incident(incident_id)
    return rest_api.response(200, JsonApiResponse(incident).render())


@ app.route('/incidents/<incident_id>/reports', methods=['GET'])
def list_incident_reports(incident_id):
    reports = admin_api.list_incident_reports(incident_id, '1000')
    return rest_api.response(200, JsonApiResponse(reports).render())


@ app.route('/incidents/<incident_id>/notifications', methods=['GET'])
def list_incident_notifications(incident_id):
    notifications = admin_api.list_incident_notifications(incident_id, '1000')
    return rest_api.response(200, JsonApiResponse(notifications).render())



@ app.route('/reports', methods=['GET'])
def list_reports():
    reports = admin_api.list_reports('', '10')
    return rest_api.response(200, JsonApiResponse(reports).render())


@ app.route('/notifications', methods=['GET'])
def list_notifications():
    notifications = admin_api.list_notifications('', '10')
    return rest_api.response(200, JsonApiResponse(notifications).render())