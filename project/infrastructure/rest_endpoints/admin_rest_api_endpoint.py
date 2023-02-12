from flask import Flask, request
import flask
import project.api.admin_api as admin_api
from project.core.exceptions import ForbiddenException, InvalidInputException, NotFoundException
import project.infrastructure.rest_endpoints.helpers.rest_endpoint_helper as rest_api
from project.infrastructure.rest_endpoints.adapters.json_api_adapter import JsonApiError, JsonApiResponse

app = Flask(__name__)


@ project.route('/incidents', methods=['GET'])
def list_incidents():
    try:
        incidents = admin_api.list_incidents('', '10')
        return rest_api.response(200, JsonApiResponse(incidents).render())
    except ForbiddenException:
        return rest_api.response(403, JsonApiError(403, 'Forbidden').render())
    except InvalidInputException:
        return rest_api.response(422, JsonApiError(422, 'Forbidden').render())
    except NotFoundException:
        return rest_api.response(404, JsonApiError(404, 'Forbidden').render())


@ project.route('/incidents/<incident_id>', methods=['GET'])
def get_incident(incident_id):
    try:
        incident = admin_api.get_incident(incident_id)
        return rest_api.response(200, JsonApiResponse(incident).render())
    except ForbiddenException:
        return rest_api.response(403, JsonApiError(403, 'Forbidden').render())
    except InvalidInputException:
        return rest_api.response(422, JsonApiError(422, 'Forbidden').render())
    except NotFoundException:
        return rest_api.response(404, JsonApiError(404, 'Forbidden').render())


@ project.route('/incidents/<incident_id>/reports', methods=['GET'])
def list_incident_reports(incident_id):
    try:
        reports = admin_api.list_incident_reports(incident_id, '1000')
        return rest_api.response(200, JsonApiResponse(reports).render())
    except ForbiddenException:
        return rest_api.response(403, JsonApiError(403, 'Forbidden').render())
    except InvalidInputException:
        return rest_api.response(422, JsonApiError(422, 'Forbidden').render())
    except NotFoundException:
        return rest_api.response(404, JsonApiError(404, 'Forbidden').render())


@ project.route('/incidents/<incident_id>/notifications', methods=['GET'])
def list_incident_notifications(incident_id):
    try:
        notifications = admin_api.list_incident_notifications(incident_id, '1000')
        return rest_api.response(200, JsonApiResponse(notifications).render())
    except ForbiddenException:
        return rest_api.response(403, JsonApiError(403, 'Forbidden').render())
    except InvalidInputException:
        return rest_api.response(422, JsonApiError(422, 'Forbidden').render())
    except NotFoundException:
        return rest_api.response(404, JsonApiError(404, 'Forbidden').render())



@ project.route('/reports', methods=['GET'])
def list_reports():
    try:
        reports = admin_api.list_reports('', '10')
        return rest_api.response(200, JsonApiResponse(reports).render())
    except ForbiddenException:
        return rest_api.response(403, JsonApiError(403, 'Forbidden').render())
    except InvalidInputException:
        return rest_api.response(422, JsonApiError(422, 'Forbidden').render())
    except NotFoundException:
        return rest_api.response(404, JsonApiError(404, 'Forbidden').render())


@ project.route('/notifications', methods=['GET'])
def list_notifications():
    try:
        notifications = admin_api.list_notifications('', '10')
        return rest_api.response(200, JsonApiResponse(notifications).render())
    except ForbiddenException:
        return rest_api.response(403, JsonApiError(403, 'Forbidden').render())
    except InvalidInputException:
        return rest_api.response(422, JsonApiError(422, 'Forbidden').render())
    except NotFoundException:
        return rest_api.response(404, JsonApiError(404, 'Forbidden').render())