employee = {"id": 101, "name": "Rahul", "salary": 120000}

employee["salary"] = 135000
employee["department"] = "Engineering"

print(employee)
print("location" in employee)
print("salary" in employee)

sales = {"Laptop": 5, "Mobile": 12, "Tablet": 8, "Monitor": 3}
# Print every product name.
for key in sales.keys():
    print(key)

# we can also write
for key in sales:
    print(key)

# Calculate the total units sold.
total_units_sold = sum(sales.values())
print(f"total_units_sold: {total_units_sold}")

# Print only products with sales greater than 5.
for key, val in sales.items():
    if val > 5:
        print(key)

# Calculate the total number of products (distinct keys).
total_number_of_products = len(sales)
print(total_number_of_products)

print(hash(100))
print(hash("employee"))
print(hash((1, 2, 3)))
# non hashable
# print(hash([1, 2, 3]))
# print(hash({"id": 101}))
# print(hash((1, [2, 3])))

words = ["python", "sql", "python", "spark", "sql", "python", "kafka", "spark"]


def word_frequency(words: list[str]) -> dict[str, int]:
    res = {}
    for word in words:
        if word not in res:
            res[word] = 1
        else:
            res[word] += 1
        # res[word] = res.get(word, 0) + 1
    return res


print(word_frequency(words))
# Group records by department
employees = [
    ("Alice", "Engineering"),
    ("Bob", "HR"),
    ("Charlie", "Engineering"),
    ("David", "Finance"),
    ("Eva", "HR"),
    ("Frank", "Engineering"),
]


# {
#     "Engineering": ["Alice", "Charlie", "Frank"],
#     "HR": ["Bob", "Eva"],
#     "Finance": ["David"]
# }
def _group_employees(employees: list[tuple[str, str]]) -> dict[str, list[str]]:
    res = {}
    for employee, dept in employees:
        if dept not in res:
            res[dept] = [employee]
        else:
            res[dept].append(employee)
    return res


def group_employees(employees: list[tuple[str, str]]) -> dict[str, list[str]]:
    res = {}
    for employee, dept in employees:
        res.setdefault(dept, []).append(employee)
    return res
