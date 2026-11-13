"""
Topic: List Comprehensions and Generator Expressions

Concepts covered:
    1. List comprehension syntax.
    2. Generator expression syntax.
    3. Eager vs lazy evaluation.
    4. Memory usage differences.
    5. Generator exhaustion after iteration.
    6. Using generators for memory-efficient data processing.

Practical example:
    Filtering orders based on their order amount.
"""

orders = [100, 250, 75, 400, 150, 50]

large_orders = (order for order in orders if order > 100)

print(large_orders)
print(list(large_orders))
print(list(large_orders))
