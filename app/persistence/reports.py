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

    return reports


def list_incident_reports(incident_id: str, limit: int) -> list[Report]:
    result = db_conn().execute('SELECT * FROM reports WHERE incident_id  = ? LIMIT ?',
                               [incident_id, limit]).fetchall()

    reports = []
    for row in result:
        reports.append(parse_row(row))

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

    return get_report(report_id)


def check_no_reports_for_incident(incident_id: str):
    reports_in_incident = list_incident_reports(incident_id, 1)
    if len(reports_in_incident) > 0:
        return False
    else:
        return True


def get_report(report_id: str) -> Report:
    result = db_conn().execute(
        'SELECT * FROM reports WHERE report_id = ?', [report_id]).fetchone()
    if result is None:
        raise Exception('Report not found')
    else:
        return parse_row(result)
