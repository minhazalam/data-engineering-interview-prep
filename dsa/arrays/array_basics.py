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
