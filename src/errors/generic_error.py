import json


class GenericError(Exception):
    status_code = 400

    def __init__(self, message, status_code=400):
        self.status_code = status_code
        return super().__init__(message)

    def serialize_response(self):
        return {
            "statusCode": self.status_code,
            "body": json.dumps({"message": self.message}),
        }
