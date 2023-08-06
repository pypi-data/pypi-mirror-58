import pytest
from trial4 import dividenum, multiplynum, addnumber, subnum


@pytest.mark.parametrize(
    "x,y,result",
    [(40, 10, 4), (49, 7, 7), pytest.param(90, 10, 9, marks=pytest.mark.xfail)],
)
def test_divide(x, y, result):
    assert dividenum(x, y) == result


@pytest.mark.parametrize(
    "x,y,expected",
    [(20, 10, 200), (5, 8, 40), pytest.param(90, 10, 110, marks=pytest.mark.xfail)],
)
def test_multiply(x, y, expected):
    assert multiplynum(x, y) == expected


@pytest.mark.parametrize(
    "x,y,expected",
    [(5, 4, 9), (3, 10, 13), pytest.param(90, 10, 110, marks=pytest.mark.xfail)],
)
def test_add(x, y, expected):
    assert addnumber(x, y) == expected


@pytest.mark.parametrize(
    "x,y,result",
    [(10, 8, 2), (100, 50, 50), pytest.param(90, 10, 110, marks=pytest.mark.xfail)],
)
def test_substract(x, y, result):
    assert subnum(x, y) == result
