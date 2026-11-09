# ruff: noqa: PLR173


# Exercise 1 – Remove duplicates while preserving order
def remove_duplicates(numbers: list[int]) -> list[int]:
    seen = set()
    res = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            res.append(num)
    return res


# print(remove_duplicates([1, 2, 2, 3, 1, 4]))


# Exercise 2 – Find the second-largest distinct number
def find_second_largest(numbers: list[int]) -> int | None:
    largest = None
    second_largest = None

    for num in numbers:
        if largest is None or num > largest:
            second_largest = largest
            largest = num

        elif num < largest and (second_largest is None or num > second_largest):
            second_largest = num

    return second_largest


print(find_second_largest([10, 5, 10]))


# Exercise 3 – Extract even numbers
def get_even_numbers(numbers: list[int]) -> list[int]:
    # res = []
    # for num in numbers:
    #     if num % 2 == 0:
    #         res.append(num)
    # return res
    return [num for num in numbers if num % 2 == 0]
