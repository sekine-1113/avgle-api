
class AvgleError(Exception):
    pass


class HTTPException(Exception):
    pass


class BadRequest(HTTPException):
    pass


class NotFound(HTTPException):
    pass


class TooManyRequests(HTTPException):
    pass


class ServerError(HTTPException):
    pass