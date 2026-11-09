/*
===============================================================================
Day 02 - CASE WHEN, NULL Handling and Conditional Aggregation
===============================================================================

PROBLEM STATEMENT:

You are working as a Data Engineer for an e-commerce company.

The company maintains two tables:

1. customers
   - customer_id
   - customer_name
   - city
   - signup_date

2. orders
   - order_id
   - customer_id
   - order_date
   - amount
   - status

Business Requirement:

Generate a customer-level order summary report containing:

1. Customer ID
2. Customer Name
3. Total number of orders
4. Number of completed orders
5. Number of pending orders
6. Number of cancelled orders
7. Total revenue generated from completed orders

Technical Requirements:

- Include all customers, even those who have never placed an order.
- Use LEFT JOIN to combine customers and orders.
- Use conditional aggregation with CASE WHEN.
- Use COUNT appropriately to handle NULL values.
- Group results at the customer level.
- Sort the output by customer_id in ascending order.

Expected Output:

| customer_id | customer_name | total_orders | completed_orders |
|-------------|---------------|--------------|------------------|
| 1           | Amit          | 2            | 2                |
| 2           | Priya         | 1            | 0                |
| 3           | Rahul         | 2            | 1                |
| 4           | Sneha         | 1            | 1                |
| 5           | Karan         | 1            | 0                |

Additional Concepts Practised:
- CASE WHEN
- COUNT(*) vs COUNT(column)
- COALESCE and NULLIF
- LEFT JOIN and NULL handling
- Conditional aggregation using SUM(CASE WHEN...)
- GROUP BY and ORDER BY

===============================================================================
*/
-- Day 2: CASE WHEN, NULL handling and conditional aggregation

-- Customer-level order summary
SELECT
    c.customer_id,
    c.customer_name,
    COUNT(o.order_id) AS total_orders,
    SUM(CASE WHEN o.status = 'completed' THEN 1 ELSE 0 END)
        AS completed_orders,
    SUM(CASE WHEN o.status = 'pending' THEN 1 ELSE 0 END)
        AS pending_orders,
    SUM(CASE WHEN o.status = 'cancelled' THEN 1 ELSE 0 END)
        AS cancelled_orders,
    SUM(CASE WHEN o.status = 'completed' THEN o.amount ELSE 0 END)
        AS completed_revenue
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.customer_name
ORDER BY
    c.customer_id;