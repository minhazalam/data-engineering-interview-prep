import pytest

from dsa.arrays.triplet_sum import triplet_sum_all


@pytest.mark.parametrize(
    "numbers, target, expected",
    [
        (
            [-1, 0, 1, 2, -1, -4],
            0,
            [[-1, -1, 2], [-1, 0, 1]],
        ),
        (
            [-2, -2, -2, 0, 2, 2],
            0,
            [[-2, 0, 2]],
        ),
        (
            [0, 0, 0, 0],
            0,
            [[0, 0, 0]],
        ),
        (
            [1, 2],
            3,
            [],
        ),
        (
            [1, 2, 3, 4],
            20,
            [],
        ),
        (
            [-5, -2, 0, 2, 5],
            0,
            [[-5, 0, 5], [-2, 0, 2]],
        ),
    ],
)
def test_triplet_sum_all(numbers, target, expected):
    assert triplet_sum_all(numbers, target) == expected


def test_triplet_sum_all_does_not_modify_input():
    numbers = [-1, 0, 1, 2, -1, -4]
    original = numbers.copy()

    triplet_sum_all(numbers, 0)

    assert numbers == original
