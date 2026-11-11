# You're given an integer array height, where each element represents the height of a vertical line.


# Find two lines that, together with the x-axis, form a container that holds the maximum amount of water.
def max_area(height: list[int]) -> int:
    left, right, max_area = 0, len(height) - 1, 0
    while left < right:
        current_area = (right - left) * min(height[left], height[right])
        max_area = max(current_area, max_area)
        if height[left] < height[right]:
            left += 1
        else:
            left += 1
    return max_area


# print(max_area(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
