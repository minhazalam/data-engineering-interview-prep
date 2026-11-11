import pytest

from dsa.arrays.largest_container import max_area


@pytest.mark.parametrize(
    "height, expected",
    [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 4, 4, 4], 12),
        ([1, 2], 1),
        ([1, 2, 1], 2),
        ([0, 0, 0, 0], 0),
        ([5, 1, 2, 3, 4], 16),
        ([1, 3, 2, 5, 25, 24, 5], 15),
    ],
)
def test_max_area(height, expected):
    assert max_area(height) == expected


@pytest.mark.parametrize(
    "height",
    [
        [],
        [5],
    ],
)
def test_max_area_with_insufficient_lines(height):
    assert max_area(height) == 0
