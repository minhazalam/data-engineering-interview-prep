# Exercise 1: Find common elements
# Given two lists, return their common unique elements.
list1 = [1, 2, 3, 4, 5, 2]
list2 = [3, 4, 5, 6, 7, 3]

# Expected: [3, 4, 5]


def find_common_elements(list1: list[int], list2: list[int]) -> list[int]:
    # return list(set(list1) & set(list2))
    # preserving the order from list1
    list2 = set(list2)
    res = []
    for num in list1:
        if num in list2 and num not in res:
            res.append(num)
    return res


# grouping employees by department.
employees = [
    ("Amit", "Engineering"),
    ("Priya", "HR"),
    ("Rahul", "Engineering"),
    ("Sneha", "Finance"),
    ("Karan", "HR"),
]


def group_employees(employees: list[tuple[str, str]]) -> dict[str, list[str]]:
    result = {}
    for employee, department in employees:
        if department not in result:
            result[department] = [employee]
        else:
            result[department].append(employee)

    return result


print(group_employees(employees))
# Expected output
# {
#     "Engineering": ["Amit", "Rahul"],
#     "HR": ["Priya", "Karan"],
#     "Finance": ["Sneha"]
# }
