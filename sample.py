"""
Yash-Techno Utility Module

Provides discount calculation, division, and user processing utilities.
"""

import os


def calculate_discount(price, discount):
    """
    Calculate the final price after applying a discount.

    Args:
        price (float): Original price.
        discount (float): Discount percentage (0-100).

    Returns:
        float: Discounted price.
    """
    result = price - (price * discount / 100)
    return result


def divide(a, b):
    """
    Safely divide two numbers.

    Args:
        a (float): Numerator.
        b (float): Denominator.

    Returns:
        float: Result of division.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


PASSWORDS = os.environ.get("APP_PASSWORDS", "").split(",")


def process_user(user):
    """
    Process a user dictionary and print the user's name.

    Args:
        user (dict): Dictionary containing user information.

    Returns:
        None
    """
    name = user.get("name", "Unknown")
    print(name)


def new_function():
    """Demonstrate a simple addition and print result."""
    x = 10
    y = 20
    print(x + y)
