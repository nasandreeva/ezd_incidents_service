from sqlite3 import Connection

def drop_all(conn: Connection):
    conn.execute('DROP TABLE IF EXISTS incidents;')
    conn.execute('DROP TABLE IF EXISTS notifications;')
    conn.execute('DROP TABLE IF EXISTS reports;')


def create_all(conn: Connection):
    conn.execute('''CREATE TABLE incidents (
        sequence INT PRIMARY KEY NOT NULL, 
        incident_id CHAR(36) NOT NULL, 
        incident_name TEXT,
        user_id CHAR(36),
        started_at timestamp,
        ended_at timestamp,
        positive_reports_count INT NOT NULL,
        negative_reports_count INT NOT NULL,
        resolved_notifications_count INT NOT NULL,
        recalled BOOL
        );''')

    conn.execute('''CREATE TABLE notifications (
        sequence INT PRIMARY KEY NOT NULL, 
        notification_id CHAR(36) NOT NULL, 
        incident_id  INT NOT NULL,
        user_id  CHAR(36) NOT NULL,
        at  timestamp NOT NULL
        );''')

    conn.execute('''CREATE TABLE reports (
        sequence INT PRIMARY KEY NOT NULL, 
        report_id CHAR(36) NOT NULL, 
        incident_id INT NOT NULL,
        user_id CHAR(36) NOT NULL,
        confirmed BOOL,
        at timestamp NOT NULL
        );''')
