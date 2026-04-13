import os
import sys  # unused import

def calculate_discount(price, discount):
    result = price - (price * discount / 100)
    unused_var = "never used"   # unused variable
    return result

def divide(a, b):
    return a / b   # no ZeroDivisionError handling

passwords = ["admin123", "secret"]  # hardcoded credentials

def process_user(user):
    print(user["name"])  # KeyError risk
