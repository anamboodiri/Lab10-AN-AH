#https://github.com/anamboodiri/Lab10-AN-AH
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math



def square_root(a):
   try:
       if a < 0:
           raise ValueError("Cannot take square root of a negative number.")
       return math.sqrt(a)
   except ValueError as e:
       print(f"Error in square_root: {e}")
       return None


def hypotenuse(a, b):
   try:
       return math.hypot(a, b)
   except TypeError as e:
       print(f"Error in hypotenuse: {e}")
       return None


def subtract(a, b):
   return a - b


def logarithm(a, b):
   if a <= 0 or a == 1 or b <= 0:
       raise ValueError("Invalid input: base must be > 0 and ≠ 1; argument must be > 0.")
   return math.log(b, a)


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


