def contains_duplicate(numbers: list[int]) -> bool:
    seen = set()
    for number in numbers:
        if number not in seen:
            seen.add(number)
        else:
            return True
    return False
