def two_sum(numbers: list[int], target: int) -> list[int] | None:
    seen = {}
    for idx, number in enumerate(numbers):
        complement = target - number
        if complement in seen:
            return [seen[complement], idx]
        else:
            seen[number] = idx
    return None


print(two_sum(numbers=[2, 7, 11, 15], target=9))
