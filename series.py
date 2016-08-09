# -*- coding: utf -*-


def fibonacci(n):
    """Return the nth value in the fibonacci series"""
    if n <= 0:
        return 'Please enter a whole positive number'
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """Return the nth value in the lucas series"""
    if n <= 0:
        return 'Please enter a whole positive number'
    elif n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)
