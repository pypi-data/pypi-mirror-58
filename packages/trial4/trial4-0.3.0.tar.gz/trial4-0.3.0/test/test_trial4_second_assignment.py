import pytest
from trail4_second_assignment import lengthoflist


@pytest.mark.parametrize(
    "x,expected", [([1, 2, 3], 3), (["Pooja", "Rihaan"], 2), ([], 0)]
)
def test_length(x, expected):
    assert lengthoflist(x) == expected
