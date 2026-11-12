/*
Problem: Identify customers whose order amount increased compared
         to their previous order.

Requirements:
1. Calculate the total amount for each order using order_items.
   Order amount = SUM(quantity * unit_price).
2. Compare each customer's current order amount with their
   immediately preceding order.
3. Use the LAG() window function, partitioned by customer_id.
4. Order records chronologically using order_date and order_id.
5. Return only orders where the current amount is greater than
   the previous order amount.

Tables:
- orders
- order_items

Concepts:
- INNER JOIN
- GROUP BY and aggregation
- Common Table Expressions (CTEs)
- LAG() window function
- PARTITION BY and ORDER BY
*/
with cte_orders as (select o.customer_id,
                           o.order_id,
                           o.order_date,
                           sum(oi.quantity * oi.unit_price) as amount
                    from orders o
                             inner join order_items oi on o.order_id = oi.order_id
                    group by o.customer_id, o.order_id, o.order_date),
     cte_orders_with_prev_amt as (select customer_id,
                                         order_id,
                                         order_date,
                                         amount,
                                         lag(amount)
                                         over (partition by customer_id order by order_date ,order_id) as previous_amount
                                  from cte_orders)
select customer_id, order_id, order_date, amount, previous_amount
from cte_orders_with_prev_amt
where amount >= previous_amount