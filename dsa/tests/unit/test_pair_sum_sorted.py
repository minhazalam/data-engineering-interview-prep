import pytest

from dsa.arrays.pair_sum_sorted import (
    pair_sum_sorted,
    pair_sum_sorted_brute_force,
)


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([1, 2, 4, 6, 8, 9], 10, [0, 5]),
        ([1, 2, 3, 4, 5], 6, [0, 4]),
        ([1, 2, 3, 4, 5], 9, [3, 4]),
        ([1, 1, 2, 3], 2, [0, 1]),
        ([], 10, []),
        ([1, 2, 3], 10, []),
        ([5], 10, []),
    ],
)
def test_pair_sum_sorted(nums, target, expected):
    assert pair_sum_sorted(nums, target) == expected


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([1, 2, 4, 6, 8, 9], 10, [0, 5]),
        ([1, 2, 3, 4, 5], 6, [0, 4]),
        ([1, 2, 3, 4, 5], 9, [3, 4]),
        ([1, 1, 2, 3], 2, [0, 1]),
        ([], 10, []),
        ([1, 2, 3], 10, []),
        ([5], 10, []),
    ],
)
def test_pair_sum_sorted_brute_force(nums, target, expected):
    assert pair_sum_sorted_brute_force(nums, target) == expected
