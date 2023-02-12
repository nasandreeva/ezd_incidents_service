import json


class JsonApiResponse:
    data: any

    def __init__(self, data):
        self.data = data

    def render(self):
        if isinstance(self.data, list):
            items = [(lambda item: item.__dict__)(item) for item in self.data]
            return json.dumps({"data": items})
        else:
            return json.dumps({"data": self.data.__dict__})


class JsonApiError:
    error: dict

    def __init__(self, code, message):
        self.error = {"code": code, "message": message}

    def render(self):
        json.dumps({"error": self.error})
