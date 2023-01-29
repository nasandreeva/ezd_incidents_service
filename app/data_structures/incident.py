from datetime import *
import inspect
import json
from app.core.base_class import BaseClass

from app.data_structures.notification import Notification
from app.data_structures.report import Report

# incident_a.embed_notifications(notifications)


class Incident(BaseClass):
    incident_id: str
    sequence: int
    incident_name: str
    user_id: str
    started_at: datetime
    ended_at: datetime
    notifications: list[Notification]
    reports: list[Report]
    positive_reports_count: int
    negative_reports_count: int
    resolved_notifications_count: int
    recalled: bool

    def __init__(self, attrs: dict):
        self.init_attribute_from(attrs, 'incident_id', None)
        self.init_attribute_from(attrs, 'sequence', None)
        self.init_attribute_from(attrs, 'incident_name', None)
        self.init_attribute_from(attrs, 'user_id', None)
        self.init_attribute_from(attrs, 'started_at', None)
        self.init_attribute_from(attrs, 'ended_at', None)
        self.init_attribute_from(attrs, 'positive_reports_count', None)
        self.init_attribute_from(attrs, 'negative_reports_count', None)
        self.init_attribute_from(attrs, 'resolved_notifications_count', None)
        self.init_attribute_from(attrs, 'recalled', None)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    # def embed_notifications(notifications: list[Notification]):
    #     self.notifications = notifications
    #     return self
