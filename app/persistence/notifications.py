from app.data_structures.notification import *
import uuid
from datetime import *
from app.__main__ import db_conn
from app.data_structures.incident import *


def parse_row(row) -> Notification:
    return Notification(row)


def list_notifications(from_notification_id: str, limit:int):
    if from_notification_id == '':
        result = db_conn().execute('SELECT * FROM notifications LIMIT ?',
                                   [limit]).fetchall()
    else:
        first = get_notification(from_notification_id)
        result = db_conn().execute('SELECT * FROM notifications WHERE sequence  >= ? LIMIT ?',
                                   [first.sequence, limit]).fetchall()

    notifications = []
    for row in result:
        notifications.append(parse_row(row))
    db_conn().commit()
    return notifications


def list_incident_notifications(incident_id: str, limit: int):
    result = db_conn().execute('SELECT * FROM notifications WHERE incident_id  = ? LIMIT ?',
                               [incident_id, limit]).fetchall()

    notifications = []
    for row in result:
        notifications.append(parse_row(row))
    db_conn().commit()
    return notifications


def create_notification(notification: Notification) -> Notification:
    notification_id = str(uuid.uuid4())
    result = db_conn().execute(
        'INSERT INTO notifications (notification_id, incident_id, user_id, at) VALUES (?,?,?,?)',
        [
            notification_id,
            notification.incident_id,
            notification.user_id,
            datetime.now()
        ]
    )
    db_conn().commit()
    return get_notification(notification_id)


def get_notification(notification_id: str) -> Notification:
    result = db_conn().execute(
        'SELECT * FROM notifications WHERE notification_id = ?', [notification_id]).fetchone()
    if result is None:
        return None
    else:   
        return parse_row(result)
