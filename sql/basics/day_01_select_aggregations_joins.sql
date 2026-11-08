DROP TABLE IF EXISTS public.orders;
DROP TABLE IF EXISTS public.customers;
CREATE TABLE public.customers
(
    customer_id   INT PRIMARY KEY,
    customer_name VARCHAR(100),
    city          VARCHAR(50),
    signup_date   DATE
);
CREATE TABLE public.orders
(
    order_id    INT PRIMARY KEY,
    customer_id INT REFERENCES public.customers (customer_id),
    order_date  DATE,
    amount      DECIMAL(10, 2),
    status      VARCHAR(20)
);
INSERT INTO public.customers
VALUES (1, 'Amit', 'Bangalore', '2025-01-10'),
       (2, 'Priya', 'Mumbai', '2025-02-15'),
       (3, 'Rahul', 'Bangalore', '2025-03-20'),
       (4, 'Sneha', 'Delhi', '2025-04-05'),
       (5, 'Karan', 'Pune', '2025-05-12');

INSERT INTO public.orders
VALUES (101, 1, '2025-06-01', 2500, 'completed'),
       (102, 1, '2025-06-05', 1500, 'completed'),
       (103, 2, '2025-06-07', 3000, 'pending'),
       (104, 3, '2025-06-10', 4000, 'completed'),
       (105, 3, '2025-06-12', 2000, 'cancelled'),
       (106, 4, '2025-06-15', 5000, 'completed'),
       (107, 5, '2025-06-20', 1000, 'pending');
SELECT *
FROM public.customers;
SELECT *
FROM public.orders;

-- Retrieve all customers.
select *
from public.customers;
-- Find customers from Bangalore.
select *
from public.customers
where city = 'Bangalore';

-- Find orders with amount greater than ₹2,000.
select *
from public.orders
where amount > 2000;
-- Retrieve completed orders, sorted by amount descending.
select *
from public.orders
where status = 'completed'
order by amount desc;
-- Find all unique customer cities.
select distinct city
from public.customers;
-- Count the total number of orders.
select count(1)
from public.orders;
-- Calculate total revenue from completed orders.
select sum(orders.amount)
from public.orders
where status = 'completed';
-- Calculate total order amount for each customer.
select customer_id, sum(amount) as total_order_amount
from public.orders
group by orders.customer_id;
-- Find customers who have more than one order.
select customer_id
from public.orders
group by customer_id
having count(*) > 1;
-- Find the average order amount for each order status.
select orders.status, avg(orders.amount)
from public.orders
group by status;

-- Q11. Find customers who have at least one completed order.
select distinct customers.customer_id, customer_name
from public.customers
         inner join public.orders o on customers.customer_id = o.customer_id
WHERE o.status = 'completed';
-- Q12. Find customers whose completed order total exceeds ₹3,000.
select customers.customer_id, customer_name, sum(o.amount)
from public.customers
         inner join public.orders o on customers.customer_id = o.customer_id
where o.status = 'completed'
group by customers.customer_id, customer_name
having sum(o.amount) > 3000;
-- Q13. Find all customers, including those who have never placed an order.
select c.customer_id, customer_name
from public.customers c
         left join public.orders o on c.customer_id = o.customer_id;
--Find customers who have never placed an order.
select *
from public.customers c
         left join public.orders o on c.customer_id = o.customer_id
where o.order_id is null;