"""
Problem: Top K Frequent Elements

Approach:
1. Count the frequency of each number using a dictionary.
2. Sort dictionary items by frequency in descending order.
3. Return the keys of the first k items.

Time Complexity: O(n + m log m)
Space Complexity: O(m)

n = number of input elements
m = number of distinct elements

Note: Heap-based optimization will be covered in Chapter 8.
"""


def top_k_frequent(numbers: list[int], k: int) -> list[int]:
    frequency = {}

    for number in numbers:
        if number not in frequency:
            frequency[number] = 1
        else:
            frequency[number] += 1

    sorted_items = sorted(
        frequency.items(),
        key=lambda item: item[1],
        reverse=True,
    )

    return [item[0] for item in sorted_items[:k]]


if __name__ == "__main__":
    print(top_k_frequent([1, 1, 1, 2, 2, 3, 3, 3, 3, 4], k=2))
