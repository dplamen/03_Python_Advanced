class ValueCannotBeNegative(Exception):
    """Number is negative"""
    pass


for _ in range(5):
    if int(input()) < 0:
        raise ValueCannotBeNegative
