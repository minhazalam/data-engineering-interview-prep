"""
Problem: Pair Sum - Sorted
Pattern: Two Pointers
Difficulty: Easy

Problem:
Given a sorted array of integers and a target,
find the indices of two numbers that add up to the target.

Example:
Input:
    nums = [1, 2, 4, 6, 8, 9]
    target = 10

Expected:
    [2, 4]

Approach:
1. Brute force
2. Two pointers

Time Complexity:
Space Complexity:
"""


def pair_sum_sorted_brute_force(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def pair_sum_sorted(nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []


if __name__ == "__main__":
    nums = [1, 2, 4, 6, 8, 9]
    target = 10

    print(pair_sum_sorted_brute_force(nums, target))
    print(pair_sum_sorted(nums, target))
