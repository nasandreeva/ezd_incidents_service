BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "reports" (
	"sequence"	INTEGER NOT NULL,
	"report_id"	CHAR(36) NOT NULL,
	"incident_id"	CHAR(36) NOT NULL,
	"user_id"	CHAR(36) NOT NULL,
	"confirmed"	BOOL,
	"at"	timestamp NOT NULL,
	PRIMARY KEY("sequence" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "notifications" (
	"sequence"	INTEGER NOT NULL,
	"notification_id"	CHAR(36) NOT NULL,
	"incident_id"	CHAR(36) NOT NULL,
	"user_id"	CHAR(36) NOT NULL,
	"at"	timestamp NOT NULL,
	PRIMARY KEY("sequence" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "incidents" (
	"sequence"	INTEGER NOT NULL,
	"incident_id"	CHAR(36) NOT NULL,
	"incident_name"	NUMERIC,
	"user_id"	CHAR(36),
	"started_at"	timestamp,
	"ended_at"	timestamp,
	"positive_reports_count"	INT DEFAULT 0,
	"negative_reports_count"	INT DEFAULT 0,
	"resolved_notifications_count"	INT DEFAULT 0,
	"recalled"	BOOL,
	PRIMARY KEY("sequence" AUTOINCREMENT)
);
COMMIT;
