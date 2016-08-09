# -*- coding: utf -*-
ERR_MES = 'Please enter a whole number from 1 to 30'


def fibonacci(n):
    """Return the nth value in the fibonacci series"""
    if type(n) != int or n not in range(1, 31):
        return ERR_MES
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """Return the nth value in the lucas series"""
    if type(n) != int or n not in range(1, 31):
        return ERR_MES
    elif n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, x=0, y=1):
    """Return the nth value in the series using fibonacci calculations with any starting values"""
    if type(n) != int or n not in range(1, 31):
        return ERR_MES
    elif n == 1:
        return x
    elif n == 2:
        return y
    else:
        return sum_series(n - 1, x, y) + sum_series(n - 2, x, y)

if __name__ == "__main__":
    print(u'This module defines functions that implement mathematical series\ \n...')
    print('fibonacci(n): \n', fibonacci.__doc__, '\n')
    print('lucas(n): \n', lucas.__doc__, '\n')
    print('sum_series(n, x=0, y=1): \n', sum_series.__doc__)
