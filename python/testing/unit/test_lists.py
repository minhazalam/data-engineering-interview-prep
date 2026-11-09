from python.fundamentals.lists import (
    find_second_largest,
    get_even_numbers,
    remove_duplicates,
)


def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4]
    assert remove_duplicates([1, 1, 1]) == [1]
    assert remove_duplicates([]) == []


def test_find_second_largest():
    assert find_second_largest([10, 5, 20, 8, 20]) == 10
    assert find_second_largest([10, 10]) is None
    assert find_second_largest([5, 5, 5]) is None
    assert find_second_largest([-5, -10, -2]) == -5
    assert find_second_largest([7]) is None
    assert find_second_largest([]) is None


def test_get_even_numbers():
    assert get_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert get_even_numbers([1, 3, 5]) == []
    assert get_even_numbers([]) == []
    assert get_even_numbers([2, 4, 6]) == [2, 4, 6]
