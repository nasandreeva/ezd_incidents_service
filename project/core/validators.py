import re
from cerberus import Validator


class CustomValidator(Validator):
    def _validate_is_uuid(self, is_uuid, field, value):
        re_uuid = re.compile(
            r'[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}', re.I)
        if is_uuid and not re_uuid.match(value):
            self._error("Value for field '%s' must be valid UUID" % field)


class Validators:
    def cursor_value_validator(cursor_value):
        v = Validator({'cursor_value': {'type': 'string'}})
        return v.validate({'cursor_value': cursor_value})

    def limit_validator(limit):
        v = Validator({'limit': {'type': 'string'}})
        return v.validate({'limit': limit})

    def incident_id_validator(incident_id):
        v = Validator({'incident_id': {'type': 'string'}})
        return v.validate({'incident_id': incident_id})

    def incident_name_validator(incident_name):
        v = Validator({'incident_name': {'type': 'string'}})
        return v.validate({'incident_name': incident_name})

    def user_id_validator(user_id):
        v = Validator({'user_id': {'type': 'string'}})
        return v.validate({'user_id': user_id})

    def started_at_validator(started_at):
        v = Validator({'started_at': {'type': 'string'}})
        return v.validate({'started_at': started_at})

    def from_notification_id_validator(from_notification_id):
        v = Validator({'from_notification_id': {'type': 'string'}})
        return v.validate({'from_notification_id': from_notification_id})

    def from_report_id_validator(from_report_id):
        v = Validator({'from_report_id': {'type': 'string'}})
        return v.validate({'from_report_id': from_report_id})
