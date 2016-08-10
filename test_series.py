# -*- coding: utf -*-
import pytest

from series import ERR_MES

FIB_TABLE = [
    ('adsg', ERR_MES),
    (-1, ERR_MES),
    (0, ERR_MES),
    (31, ERR_MES),
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
    (12, 89),
]


@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_fibonacci(n, result):
    from series import fibonacci
    assert fibonacci(n) == result


LUCAS_TABLE = [
    ('adsg', ERR_MES),
    (-1, ERR_MES),
    (0, ERR_MES),
    (31, ERR_MES),
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


SUM_TABLE = [
    (1, 0, 1, 0),
    (2, 0, 1, 1),
    (3, 0, 1, 1),
    (1, 2, 1, 2),
    (2, 2, 1, 1),
    (3, 2, 1, 3),
    (1, 3, 2, 3),
    (2, 3, 2, 2),
    (3, 3, 2, 5),
    (4, 3, 2, 7),
]


@pytest.mark.parametrize('n, x, y, result', SUM_TABLE)
def test_sum(n, x, y, result):
    from series import sum_series
    assert sum_series(n, x, y) == result
