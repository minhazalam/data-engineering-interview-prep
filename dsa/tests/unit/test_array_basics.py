from dsa.arrays.array_basics import find_max, most_frequent_number, two_sum_hashmap


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


def test_most_frequent_number():
    assert most_frequent_number([101, 102, 101, 103, 102, 101]) == 101
    assert most_frequent_number([4, 4, 2, 2]) == 4
    assert most_frequent_number([]) is None
    assert most_frequent_number([5]) == 5
    assert most_frequent_number([-1, -1, 2, 2, 2]) == 2


def test_two_sum_hashmap():
    assert two_sum_hashmap([3, 3], 6) == [0, 1]
    assert two_sum_hashmap([2, 5, 8, 12], 10) == [0, 2]
    assert two_sum_hashmap([1, 2, 3], 10) is None
    assert two_sum_hashmap([-3, 4, 3, 90], 0) == [0, 2]
    assert two_sum_hashmap([0, 4, 3, 0], 0) == [0, 3]
