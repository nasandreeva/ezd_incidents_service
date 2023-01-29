from datetime import *
import __main__
import uuid

from app.__main__ import db_conn
from app.data_structures.incident import Incident


def parse_row(row) -> Incident:
    return Incident(row)


def list_incidents(from_incident_id: str, limit: int):
    if from_incident_id == '':
        result = db_conn().execute('SELECT * FROM incidents LIMIT ?',
                                   [limit]).fetchall()
    else:
        first = get_incident(from_incident_id)
        result = db_conn().execute('SELECT * FROM incidents WHERE sequence  >= ? LIMIT ?',
                                   [first.sequence, limit]).fetchall()

    incidents = []
    for row in result:
        incidents.append(parse_row(row))

    return incidents


def get_incident(incident_id: str) -> Incident:
    result = db_conn().execute(
        'SELECT * FROM incidents WHERE incident_id = ?', [incident_id]).fetchone()
    return parse_row(result)


def create_incident(incident: Incident) -> Incident:
    incident_id = str(uuid.uuid4())
    result = db_conn().execute(
        'INSERT INTO incidents (incident_id, incident_name, user_id, started_at) VALUES  (?,?,?,?)',
        [
            incident_id,
            incident.incident_name,
            incident.user_id,
            incident.started_at
        ]
    )

    return get_incident(incident_id)


def update_incident(incident_id: str, attrs: dict):
    attrs_list = []
    for attr_name, attr_value in attrs.items():
        attrs_list.append(f'{attr_name} = \'{attr_value}\'')

    values_set = ', '.join(attrs_list)

    result = db_conn().execute(
        f'UPDATE incidents SET {values_set} WHERE incident_id = ?', [incident_id])
    return result


def increment_positive_reports_count(incident_id: str):
    return db_conn().execute(
        f'UPDATE incidents SET positive_reports_count = positive_reports_count + 1 WHERE incident_id = ?', [incident_id])


def increment_negative_reports_count(incident_id: str):
    return db_conn().execute(
        f'UPDATE incidents SET negative_reports_count = negative_reports_count + 1 WHERE incident_id = ?', [incident_id])


def increment_resolved_notifications_count(incident_id: str):
    return db_conn().execute(
        f'UPDATE incidents SET resolved_notifications_count = resolved_notifications_count + 1 WHERE incident_id = ?', [incident_id])
