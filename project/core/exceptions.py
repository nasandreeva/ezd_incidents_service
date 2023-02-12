class ForbiddenException(Exception):
    def __init__(self, description, message="Forbidden"):
        self.description = description
        self.message = message
        super().__init__(self.message)


class InvalidInputException(Exception):
    def __init__(self, description, message="Invalid input values"):
        self.description = description
        self.message = message
        super().__init__(self.message)


class NotFoundException(Exception):
    def __init__(self, description, message="Object not found"):
        self.description = description
        self.message = message
        super().__init__(self.message)
