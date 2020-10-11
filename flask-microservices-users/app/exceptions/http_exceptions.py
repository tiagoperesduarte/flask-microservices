class HttpException(Exception):
    """Http exception"""


class ResourceNotFoundException(HttpException):
    """Resource not found exception"""


class BadCredentialsException(HttpException):
    """Bad credentials exception"""


class ConflictException(HttpException):
    """Conflict exception"""
