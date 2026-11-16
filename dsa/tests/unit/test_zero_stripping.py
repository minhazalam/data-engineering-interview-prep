import pytest

from dsa.hashing.zero_striping import zero_stripping


@pytest.mark.parametrize(
    ("matrix", "expected"),
    [
        (
            [[1, 2, 3], [4, 0, 6], [7, 8, 9]],
            [[1, 0, 3], [0, 0, 0], [7, 0, 9]],
        ),
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 0]],
            [[1, 2, 0], [4, 5, 0], [0, 0, 0]],
        ),
        (
            [[1, 2], [3, 4]],
            [[1, 2], [3, 4]],
        ),
        (
            [[0, 2], [3, 4]],
            [[0, 0], [0, 4]],
        ),
        (
            [[0, 0], [0, 0]],
            [[0, 0], [0, 0]],
        ),
    ],
)
def test_zero_stripping(matrix, expected):
    result = zero_stripping(matrix)
    assert result == expected
