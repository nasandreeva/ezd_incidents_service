from datetime import *
import json

from project.core.base_class import BaseClass


class Notification(BaseClass):
    notification_id: int
    incident_id: int
    user_id: str
    at: datetime

    def __init__(self, attrs: dict):
        self.init_attribute_from(attrs, 'sequence', None)
        self.init_attribute_from(attrs, 'notification_id', None)
        self.init_attribute_from(attrs, 'incident_id', None)
        self.init_attribute_from(attrs, 'user_id', None)
        self.init_attribute_from(attrs, 'at', None)


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)