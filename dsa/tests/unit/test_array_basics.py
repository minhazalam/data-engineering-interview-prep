from dsa.arrays.array_basics import find_max


def test_find_max():
    assert find_max([10, 5, 30, 20]) == 30


def test_find_max_single_element():
    assert find_max([5]) == 5


def test_find_max_negative_numbers():
    assert find_max([-10, -5, -20]) == -5


def test_find_max_duplicate_maximum():
    assert find_max([10, 30, 20, 30]) == 30


def test_find_max_empty_list():
    assert find_max([]) is None
