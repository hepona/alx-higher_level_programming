#!/usr/bin/python3
def safe_print_division(a, b):
    q = 0
    try:
        q = a / b
    except(ValueError, IndexError):
        q = None
    finally:
        print("Inside result: {}".format(q))
        return q
