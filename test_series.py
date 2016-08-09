# -*- coding: utf -*-
import pytest

FIB_TABLE = [
    (-1, 'Please enter a whole positive number'),
    (0, 'Please enter a whole positive number'),
    (1, 0),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 3),
    (6, 5),
    (7, 8),
    (8, 13),
    (9, 21),
    (10, 34),
    (11, 55),
    (12, 89)
]


@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_fibonacci(n, result):
    from series import fibonacci
    assert fibonacci(n) == result


LUCAS_TABLE = [
    (1, 2),
    (2, 1),
    (3, 3),
    (4, 4),
    (5, 7),
    (6, 11),
    (7, 18),
    (8, 29),
    (9, 47),
    (10, 76),
]


@pytest.mark.parametrize('n, result', LUCAS_TABLE)
def test_lucas(n, result):
    from series import lucas
    assert lucas(n) == result
