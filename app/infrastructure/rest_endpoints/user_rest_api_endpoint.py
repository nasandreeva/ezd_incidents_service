from flask import Flask, request
import flask
import app.api.user_api as user_api
from app.core.exceptions import ForbiddenException, InvalidInputException, NotFoundException
from app.data_structures.notification import Notification
import app.infrastructure.rest_endpoints.helpers.rest_endpoint_helper as rest_api
from app.infrastructure.rest_endpoints.adapters.json_api_adapter import JsonApiError, JsonApiResponse

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
    try:
        raise ForbiddenException("User can not recall incident")
    except ForbiddenException:
        return rest_api.response(403, JsonApiError(403, 'Forbidden').render())
    except InvalidInputException:
        return rest_api.response(422, JsonApiError(422, 'Forbidden').render())
    except NotFoundException:
        return rest_api.response(404, JsonApiError(404, 'Forbidden').render())


@ app.route('/incidents', methods=['POST'])
def register_incident():
    incident = user_api.register_incident(request.form.get('incident_name'),
                                          request.form.get(
        'user_id'),
        request.form.get('started_at'))
    return rest_api.response(200, JsonApiResponse(incident).render())


@ app.route('/incidents/<incident_id>/confirmed', methods=['POST'])
def report_incident_confirmed(incident_id):
    incident = user_api.report_incident_confirmed(
        incident_id, request.form.get('user_id'))
    return rest_api.response(200, JsonApiResponse(incident).render())


@ app.route('/incidents/<incident_id>/not_confirmed', methods=['POST'])
def report_incident_not_confirmed(incident_id):
    incident = user_api.report_incident_not_confirmed(
        incident_id, request.form.get('user_id'))
    return rest_api.response(200, JsonApiResponse(incident).render())


@ app.route('/incidents/<incident_id>/recall', methods=['PATCH'])
def recall_incident(incident_id):
    incident = user_api.recall_incident(
        incident_id, request.form.get('user_id'))
    return rest_api.response(200, JsonApiResponse(incident).render())


@ app.route('/incidents/<incident_id>/mark_as_ended', methods=['PATCH'])
def mark_incident_as_ended(incident_id):
    user_id = request.form.get('user_id')
    incident = user_api.mark_incident_as_ended(
        incident_id, user_id)
    return rest_api.response(200, JsonApiResponse(incident).render())


@ app.route('/incidents/<incident_id>/resolved', methods=['PATCH'])
def notify_incident_resolved(incident_id):
    incident = user_api.notify_incident_resolved(
        incident_id, request.form.get('user_id'))
    return rest_api.response(200, JsonApiResponse(incident).render())


@ app.route('/incidents/<incident_id>/reports', methods=['GET'])
def list_incident_reports(incident_id):
    reports = user_api.list_incident_reports(incident_id, '10')
    return rest_api.response(200, JsonApiResponse(reports).render())


@ app.route('/incidents/<incident_id>/notifications', methods=['GET'])
def list_incident_notifications(incident_id):
    notifications = user_api.list_incident_notifications(incident_id, '10')
    return rest_api.response(200, JsonApiResponse(notifications).render())
