import pytest
from dsa.hashing.contains_duplicate import contains_duplicate
from dsa.hashing.two_sum import two_sum


def test_contains_duplicate():
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert contains_duplicate([1, 1, 1, 1]) is True
    assert contains_duplicate([1]) is False
    assert contains_duplicate([]) is False


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([-1, -2, -3, -4], -6) == [1, 3]
    assert two_sum([1, 2, 3], 10) is None
