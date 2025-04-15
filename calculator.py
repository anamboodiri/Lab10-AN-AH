cd """
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def add(a, b):
    return (a + b)

def sub(a, b):
    return (a - b)

def mul(a, b):
    return (a * b)

def div(a, b):
    try:
        c = b/a
        return c
    except ZeroDivisionError:
        pass
    # raise ZeroDivisionError if a == 0

def log(a, b):
    try:
        log(b, a)
    except ValueError:
        pass

def exp(a, b):
    return (a^b)




