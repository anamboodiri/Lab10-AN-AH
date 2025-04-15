"""
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


def log(a, b):
    try:
        log(b, a)
    except ValueError:
        pass

def exp(a, b):
    return (a^b)

# First example
def add(a, b):
   return a + b


def subtract(a, b):
   return a - b


def multiply(a, b):
   return a * b


def divide(a, b):
   if a == 0:
       raise ZeroDivisionError("Cannot divide by zero.")
   return b / a


def logarithm(a, b):
   if a <= 0 or a == 1 or b <= 0:
       raise ValueError("Invalid input: base must be > 0 and ≠ 1; argument must be > 0.")
   return math.log(b, a)


def exponent(a, b):
   return a ** b



