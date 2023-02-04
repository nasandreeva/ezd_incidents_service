import uuid
from datetime import *
from app.__main__ import db_conn
from app.data_structures.report import *


def parse_row(row) -> Report:
    return Report(row)


def list_reports(from_report_id: str, limit: int):
    if from_report_id == '':
        result = db_conn().execute('SELECT * FROM reports LIMIT ?',
                                   [limit]).fetchall()
    else:
        first = get_report(from_report_id)
        result = db_conn().execute('SELECT * FROM reports WHERE sequence  >= ? LIMIT ?',
                                   [first.sequence, limit]).fetchall()

    reports = []
    for row in result:
        reports.append(parse_row(row))
    db_conn().commit()
    return reports


def list_incident_reports(incident_id: str, limit: int) -> list[Report]:
    result = db_conn().execute('SELECT * FROM reports WHERE incident_id  = ? LIMIT ?',
                               [incident_id, limit]).fetchall()

    reports = []
    for row in result:
        reports.append(parse_row(row))
    db_conn().commit()
    return reports


def create_report(report: Report):
    report_id = str(uuid.uuid4())
    result = db_conn().execute(
        'INSERT INTO reports (report_id, incident_id, user_id, at, confirmed) VALUES  (?,?,?,?,?)',
        [
            report_id,
            report.incident_id,
            report.user_id,
            datetime.now(),
            report.confirmed
        ]
    )
    db_conn().commit()
    return get_report(report_id)


def check_no_reports_for_incident(incident_id: str):
    reports_in_incident = list_incident_reports(incident_id, 1)
    if len(reports_in_incident) > 0:
        db_conn().commit()
        return False
    else:
        db_conn().commit()
        return True


def get_report(report_id: str) -> Report:
    result = db_conn().execute(
        'SELECT * FROM reports WHERE report_id = ?', [report_id]).fetchone()
    if result is None:
        raise Exception('Report not found')
    else:
        return parse_row(result)


def get_user_reports_count_for_incident(user_id: str, incident_id: str):
    result_positive = db_conn().execute(
        'SELECT COUNT(DISTINCT report_id) as cnt FROM reports WHERE incident_id = ? and user_id = ? and confirmed == True', [incident_id, user_id])
    result_negative = db_conn().execute(
        'SELECT COUNT(DISTINCT report_id) as cnt FROM reports WHERE incident_id = ? and user_id = ? and confirmed == False', [incident_id, user_id])
    return {'positive_reports': result_positive.fetchall()[0]['cnt'], 'negative_reports': result_negative.fetchall()[0]['cnt']}
