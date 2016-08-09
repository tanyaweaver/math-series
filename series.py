# -*- coding: utf -*-


def fibonacci(n):
    """Return the nth value in the fibonacci series"""
    if type(n) != int or n <= 0:
        return 'Please enter a whole positive number'
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """Return the nth value in the lucas series"""
    if type(n) != int or n <= 0:
        return 'Please enter a whole positive number'
    elif n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, x=0, y=1):
    """Return the nth value in the sum series"""
    if type(n) != int or n <= 0:
        return 'Please enter a whole positive number'
    elif n == 1:
        return x
    elif n == 2:
        return y
    else:
        return sum_series(n - 1, x, y) + sum_series(n - 2, x, y)
