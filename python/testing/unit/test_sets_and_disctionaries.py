from python.fundamentals.sets_and_disctionaries import find_common_elements


def test_find_common_elements():
    assert find_common_elements([1, 2, 3, 4, 5, 2], [3, 4, 5, 6, 7, 3]) == [3, 4, 5]
