"""
exception_handling.py
---------------------
Error and exception handling, including custom exceptions.
"""

def exception_examples():
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        result = str(e)
    finally:
        cleanup = 'Done'
    return result, cleanup

class CustomError(Exception):
    pass
