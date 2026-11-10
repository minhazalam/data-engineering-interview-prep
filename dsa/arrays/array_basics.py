# ruff: noqa: PLR1730
# find maximun
def find_max(numbers: list[int]) -> int:
    if len(numbers) == 0:
        return
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


# find maximun
def find_min(numbers: list[int]) -> int:
    if len(numbers) == 0:
        return
    min_number = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number
    return min_number


# calculate sum
def calculate_sum(numbers: list[int]) -> int:
    if len(numbers) == 0:
        return 0
    sum_of_numbers = 0
    for number in numbers:
        sum_of_numbers += number
    return sum_of_numbers


# linear search
def linear_search(numbers: list[int], target: int) -> int:
    for idx in range(len(numbers)):
        if numbers[idx] == target:
            return idx
    return -1


# reverse an array
def reverse_array(numbers: list[int]) -> list[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        numbers[left], numbers[right] = numbers[right], numbers[left]
        left += 1
        right -= 1
    return numbers


# array palindrome
def is_palindrome(numbers: list[int]) -> bool:
    left, right = 0, len(numbers) - 1
    while left < right:
        if numbers[left] == numbers[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


# move zeros
def move_zeros(numbers: list[int]) -> list[int]:
    left, right = 0, 1
    while right < len(numbers):
        if numbers[left] != 0:
            left += 1
        elif numbers[right] == 0:
            right += 1
        else:
            numbers[left], numbers[right] = numbers[right], numbers[left]
            left += 1
            right += 1
    return numbers


def find_duplicates(numbers: list[int]) -> list[int]:
    seen = set()
    duplicates = []
    duplicate_set = set()
    for number in numbers:
        if number not in seen:
            seen.add(number)
        elif number not in duplicate_set:
            duplicate_set.add(number)
            duplicates.append(number)
    return duplicates


print(find_duplicates(numbers=[4, 2, 2, 2, 4, 4]))


# Hash Maps and Frequency Counting
# Given an integer list, return a dictionary containing the frequency of each number.
# numbers = [1, 2, 2, 3, 1, 1, 4]
# {
#     1: 3,
#     2: 2,
#     3: 1,
#     4: 1
# }
def count_frequency(numbers: list[int]) -> dict[int, int]:
    res = {}
    # for number in numbers:
    #     if number in res:
    #         res[number] += 1
    #     else:
    #         res[number] = 1
    # return res

    for number in numbers:
        res[number] = res.get(number, 0) + 1
    return res


print(count_frequency([1, 2, 2, 3, 1, 1, 4]))


def most_frequent_number(numbers: list[int]) -> int | None:
    frequency = {}
    max_count = 0
    max_count_number = None

    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
        if frequency[number] > max_count:
            max_count = frequency[number]
            max_count_number = number

    return max_count_number


print(most_frequent_number([101, 102, 101, 103, 102, 101]))


def two_sum_hashmap(numbers: list[int], target: int) -> list[int] | None:
    seen = {}
    for index, number in enumerate(numbers):
        complement = target - number
        if complement in seen:
            return [seen[complement], index]
        else:
            seen[number] = index
    return None


print(two_sum_hashmap([2, 7, 11, 15], 9))
