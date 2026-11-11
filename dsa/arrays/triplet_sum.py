# Given an integer array nums, determine whether there are three distinct elements whose sum equals a target value.
# nums = [1, 2, 3, 4, 5]
# target = 9

# One valid triplet is:
# [1, 3, 5]


# brute force solution
def brute_force_triplet_sum(numbers: list[int], target: int) -> bool:
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            for k in range(j + 1, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == target:
                    return True
    return False


# print(brute_force_triplet_sum([1, 2, 3, 4, 5], target=9))


def triplet_sum(numbers: list[int], target: int) -> bool:
    # if we are not given that the array is sorted then we will first sort it
    numbers.sort()
    for i in range(len(numbers) - 2):
        left = i + 1
        right = len(numbers) - 1
        while left < right:
            if numbers[i] + numbers[left] + numbers[right] == target:
                return True
            elif numbers[i] + numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
    return False


print(triplet_sum([4, 1, 2, 3, 5], target=20))


# Requirements:
# - Return all unique triplets.
# - Each triplet must sum to target.
# - Sort the input first.
# - Skip duplicate fixed values.
# - Skip duplicate left and right values after finding a triplet.
# - Do not modify the input list.
def triplet_sum_all(numbers: list[int], target: int) -> list[list[int]]:
    numbers = sorted(numbers)
    res = []
    for i in range(len(numbers) - 2):
        if i > 0 and numbers[i] == numbers[i - 1]:
            continue
        left = i + 1
        right = len(numbers) - 1
        while left < right:
            current_sum = numbers[i] + numbers[left] + numbers[right]
            if current_sum == target:
                res.append([numbers[i], numbers[left], numbers[right]])
                left += 1
                right -= 1
                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1
                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    return res


print(triplet_sum_all([-1, 0, 1, 2, -1, -4], target=0))
print(triplet_sum_all([-1, 0, 1, 2, -1, -4], 0))
# [[-1, -1, 2], [-1, 0, 1]]

print(triplet_sum_all([-2, -2, -2, 0, 2, 2], 0))
# [[-2, 0, 2]]

print(triplet_sum_all([0, 0, 0, 0], 0))
# [[0, 0, 0]]

print(triplet_sum_all([1, 2], 3))
# []
