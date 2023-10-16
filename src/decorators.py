import requests


def handle_req_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Request Failed: {e}")
        return None
    return wrapper


class CourseNotFound(Exception):

    def __init__(self, identifier):
        self.identifier = identifier
        message = f"Course {identifier} not found "
        super().__init__(message)
