class CustomError(Exception):
    pass


class Error(Exception):
    """ Base class for other exceptions """
    pass


class ValueTooSmallError(Error):
    """ Raised when the input value is too small """
    pass


num = int(input())
if num < 10:
    raise ValueTooSmallError
