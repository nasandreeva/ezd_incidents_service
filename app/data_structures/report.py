from datetime import *
import json

from app.core.base_class import BaseClass


class Report(BaseClass):
    report_id: str
    incident_id: str
    user_id: str
    confirmed: bool
    at: datetime
    sequence: int

    def __init__(self, attrs: dict):
        self.init_attribute_from(attrs, 'report_id', None)
        self.init_attribute_from(attrs, 'incident_id', None)
        self.init_attribute_from(attrs, 'user_id', None)
        self.init_attribute_from(attrs, 'confirmed', None)
        self.init_attribute_from(attrs, 'at', None)
        self.init_attribute_from(attrs, 'sequence', None)        
        

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
