
-- ============================================================
-- SQL Window Functions
-- Topics: Ranking, Aggregate, LAG, LEAD, Window Frames
-- ============================================================


-- 1. ROW_NUMBER()
-- Assigns a unique sequential number to each row.
-- Example: Latest order per customer.

WITH ranked_orders AS (
    SELECT
        order_id,
        customer_id,
        order_date,
        amount,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY order_date DESC, order_id DESC
        ) AS row_num
    FROM orders
)
SELECT
    order_id,
    customer_id,
    order_date,
    amount
FROM ranked_orders
WHERE row_num = 1;


-- 2. RANK()
-- Assigns the same rank to tied values and leaves gaps.

SELECT
    emp_id,
    emp_name,
    emp_salary,
    RANK() OVER (
        ORDER BY emp_salary DESC
    ) AS salary_rank
FROM employees;


-- 3. DENSE_RANK()
-- Assigns the same rank to tied values without gaps.

SELECT
    emp_id,
    emp_name,
    emp_salary,
    DENSE_RANK() OVER (
        ORDER BY emp_salary DESC
    ) AS salary_rank
FROM employees;


-- 4. Second-highest distinct salary.

WITH ranked_employees AS (
    SELECT
        emp_id,
        emp_name,
        emp_salary,
        DENSE_RANK() OVER (
            ORDER BY emp_salary DESC
        ) AS salary_rank
    FROM employees
)
SELECT DISTINCT emp_salary
FROM ranked_employees
WHERE salary_rank = 2;


-- 5. Top 2 salary ranks per department.
-- Ties are retained.

WITH ranked_employees AS (
    SELECT
        emp_id,
        emp_name,
        department,
        emp_salary,
        DENSE_RANK() OVER (
            PARTITION BY department
            ORDER BY emp_salary DESC
        ) AS salary_rank
    FROM employees
)
SELECT
    emp_id,
    emp_name,
    department,
    emp_salary,
    salary_rank
FROM ranked_employees
WHERE salary_rank <= 2
ORDER BY department, salary_rank;


-- 6. Aggregate window function.
-- Department salary total while retaining employee rows.

SELECT
    emp_id,
    emp_name,
    department,
    emp_salary,
    SUM(emp_salary) OVER (
        PARTITION BY department
    ) AS department_total_salary
FROM employees;


-- 7. Running total using ROWS.

SELECT
    order_date,
    amount,
    SUM(amount) OVER (
        ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING
                 AND CURRENT ROW
    ) AS running_total
FROM orders;


-- 8. Running total using RANGE.
-- Rows with equal ordering values are treated as peers.

SELECT
    order_date,
    amount,
    SUM(amount) OVER (
        ORDER BY order_date
        RANGE BETWEEN UNBOUNDED PRECEDING
                  AND CURRENT ROW
    ) AS running_total
FROM orders;


-- 9. Moving average over the current and previous two rows.

SELECT
    order_date,
    amount,
    AVG(amount) OVER (
        ORDER BY order_date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_average
FROM orders;


-- 10. LAG()
-- Compare current order amount with previous order amount.

WITH customer_orders AS (
    SELECT
        customer_id,
        order_date,
        amount,
        LAG(amount) OVER (
            PARTITION BY customer_id
            ORDER BY order_date
        ) AS previous_amount
    FROM orders
)
SELECT
    customer_id,
    order_date,
    amount,
    previous_amount
FROM customer_orders
WHERE amount > previous_amount;


-- 11. LEAD()
-- Retrieve the next order amount.

SELECT
    customer_id,
    order_date,
    amount,
    LEAD(amount) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
    ) AS next_amount
FROM orders;
