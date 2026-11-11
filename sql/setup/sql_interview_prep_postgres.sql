/*
DATA ENGINEERING INTERVIEW PREP — POSTGRESQL PRACTICE DATASET

Run this in a disposable local PostgreSQL practice database using DataGrip.

IMPORTANT: This script drops and recreates ONLY the schema `interview_prep`.
It deletes objects/data inside that schema. It does not touch other schemas.
*/

-- =====================================================
-- STEP 1: Create database
-- Run this statement separately while connected to
-- an existing database, e.g. postgres.
-- =====================================================
CREATE DATABASE sql_interview_prep;

-- =====================================================
-- STEP 2: Run everything below after connecting to
-- sql_interview_prep
-- =====================================================
DROP SCHEMA IF EXISTS interview_prep CASCADE;
CREATE SCHEMA interview_prep;
SET search_path TO interview_prep;

-- 1. Departments and employees: joins, self-joins, hierarchy, salary ranking.
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL UNIQUE,
    location VARCHAR(50)
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(80) NOT NULL,
    department_id INT REFERENCES departments(department_id),
    manager_id INT REFERENCES employees(employee_id),
    salary NUMERIC(12,2),
    hire_date DATE NOT NULL,
    email VARCHAR(120) UNIQUE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

INSERT INTO departments VALUES
(10,'Engineering','Bengaluru'),(20,'HR','Gurugram'),
(30,'Finance','Mumbai'),(40,'Marketing','Pune'),
(50,'Analytics','Hyderabad'),(60,'Legal','Delhi');

INSERT INTO employees VALUES
(100,'Asha',10,NULL,200000,'2018-04-10','asha@example.com',TRUE),
(200,'Rohan',20,NULL,160000,'2019-06-15','rohan@example.com',TRUE),
(300,'Meera',30,NULL,180000,'2017-02-20','meera@example.com',TRUE),
(400,'Kabir',40,NULL,150000,'2020-01-05','kabir@example.com',TRUE),
(500,'Ishita',50,NULL,190000,'2018-11-12','ishita@example.com',TRUE),
(600,'Dev',10,100,150000,'2020-03-01','dev@example.com',TRUE),
(601,'Nina',10,100,150000,'2021-07-19','nina@example.com',TRUE),
(602,'Arjun',10,100,120000,'2022-01-10','arjun@example.com',TRUE),
(603,'Tara',10,600,95000,'2023-08-01','tara@example.com',TRUE),
(604,'Vikram',10,600,95000,'2023-09-11','vikram@example.com',TRUE),
(201,'Priya',20,200,130000,'2021-02-01','priya@example.com',TRUE),
(202,'Neel',20,200,110000,'2022-05-16','neel@example.com',TRUE),
(203,'Sara',20,200,110000,'2022-08-23','sara@example.com',TRUE),
(301,'Omar',30,300,140000,'2020-10-10','omar@example.com',TRUE),
(302,'Pooja',30,300,120000,'2021-12-01','pooja@example.com',TRUE),
(401,'Anil',40,400,100000,'2021-04-14','anil@example.com',TRUE),
(402,'Leena',40,400,100000,'2022-03-09','leena@example.com',TRUE),
(501,'Farah',50,500,145000,'2020-07-07','farah@example.com',TRUE),
(502,'Jay',50,500,125000,'2021-09-17','jay@example.com',TRUE),
(503,'Mohan',50,500,NULL,'2024-01-08','mohan@example.com',TRUE),
(700,'Ira',NULL,NULL,90000,'2024-02-01','ira@example.com',TRUE);

-- 2. E-commerce entities: joins, revenue, aggregation, anti-joins, CTEs.
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(120),
    city VARCHAR(60),
    signup_date DATE NOT NULL,
    referred_by INT REFERENCES customers(customer_id)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    list_price NUMERIC(10,2) NOT NULL CHECK (list_price >= 0),
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL REFERENCES customers(customer_id),
    order_date TIMESTAMP NOT NULL,
    status VARCHAR(20) NOT NULL,
    channel VARCHAR(20),
    shipping_fee NUMERIC(10,2) DEFAULT 0
);

CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT NOT NULL REFERENCES orders(order_id),
    product_id INT NOT NULL REFERENCES products(product_id),
    quantity INT NOT NULL CHECK (quantity > 0),
    unit_price NUMERIC(10,2) NOT NULL,
    discount NUMERIC(10,2) NOT NULL DEFAULT 0
);

CREATE TABLE payments (
    payment_id INT PRIMARY KEY,
    order_id INT NOT NULL REFERENCES orders(order_id),
    payment_date TIMESTAMP,
    amount NUMERIC(12,2),
    payment_method VARCHAR(30),
    payment_status VARCHAR(20)
);

INSERT INTO customers VALUES
(1,'Aarav Sharma','aarav@example.com','Bengaluru','2023-01-10',NULL),
(2,'Diya Patel','diya@example.com','Mumbai','2023-02-15',1),
(3,'Vivaan Rao','vivaan@example.com','Delhi','2023-03-20',1),
(4,'Ananya Iyer','ananya@example.com','Bengaluru','2023-04-05',2),
(5,'Ishaan Khan','ishaan@example.com','Pune','2023-05-12',2),
(6,'Myra Das','myra@example.com','Hyderabad','2023-06-18',NULL),
(7,'Reyansh Gupta','reyan@example.com','Mumbai','2023-07-22',3),
(8,'Saanvi Nair','saanvi@example.com','Chennai','2023-08-30',NULL),
(9,'Kabir Sen','kabir.s@example.com','Delhi','2023-09-11',4),
(10,'Aditi Bose',NULL,NULL,'2024-01-02',NULL),
(11,'Noah Thomas','noah@example.com','Kolkata','2024-02-14',NULL);

INSERT INTO products VALUES
(101,'Laptop Pro','Electronics',85000,TRUE),
(102,'Wireless Mouse','Accessories',1500,TRUE),
(103,'Mechanical KB','Accessories',4500,TRUE),
(104,'4K Monitor','Electronics',28000,TRUE),
(105,'USB-C Hub','Accessories',3200,TRUE),
(106,'Office Chair','Furniture',12000,TRUE),
(107,'Standing Desk','Furniture',30000,TRUE),
(108,'Webcam','Electronics',5500,TRUE),
(109,'Headphones','Electronics',8000,FALSE),
(110,'Notebook','Stationery',250,TRUE);

INSERT INTO orders VALUES
(1001,1,'2024-01-05 09:15:00','delivered','web',100),
(1002,1,'2024-01-12 14:30:00','delivered','mobile',100),
(1003,2,'2024-01-12 16:00:00','delivered','web',0),
(1004,2,'2024-02-03 11:00:00','cancelled','mobile',0),
(1005,3,'2024-02-10 10:20:00','delivered','web',150),
(1006,3,'2024-03-01 18:45:00','shipped','web',150),
(1007,4,'2024-03-01 18:45:00','delivered','mobile',100),
(1008,5,'2024-03-15 08:00:00','processing','web',100),
(1009,6,'2024-04-02 12:10:00','delivered','partner',0),
(1010,7,'2024-04-02 12:10:00','delivered','web',100),
(1011,1,'2024-04-15 20:00:00','delivered','mobile',100),
(1012,8,'2024-05-05 09:00:00','cancelled','web',0),
(1013,9,'2024-05-20 13:30:00','delivered','web',100),
(1014,2,'2024-05-20 13:30:00','delivered','mobile',0),
(1015,10,'2024-06-01 10:00:00','processing','web',0);

INSERT INTO order_items VALUES
(1,1001,101,1,82000,2000),(2,1001,102,2,1400,100),
(3,1002,103,1,4300,0),(4,1002,105,1,3000,200),
(5,1003,104,1,27000,1000),(6,1003,108,1,5200,0),
(7,1004,102,1,1500,0),(8,1005,101,1,85000,5000),
(9,1005,103,2,4500,500),(10,1006,104,2,28000,2000),
(11,1007,106,1,11500,500),(12,1007,102,2,1500,0),
(13,1008,107,1,30000,2000),(14,1009,110,5,250,0),
(15,1010,108,2,5500,500),(16,1011,101,1,83000,1000),
(17,1011,105,2,3200,200),(18,1012,109,1,8000,0),
(19,1013,106,2,12000,1000),(20,1014,103,1,4500,0),
(21,1014,110,4,250,0),(22,1015,104,1,28000,0);

INSERT INTO payments VALUES
(5001,1001,'2024-01-05 09:16:00',84000,'card','success'),
(5002,1002,'2024-01-12 14:31:00',7300,'upi','success'),
(5003,1003,'2024-01-12 16:01:00',32200,'card','success'),
(5004,1004,'2024-02-03 11:01:00',1500,'upi','refunded'),
(5005,1005,'2024-02-10 10:21:00',93500,'card','success'),
(5006,1006,'2024-03-01 18:46:00',54000,'netbanking','success'),
(5007,1007,'2024-03-01 18:46:00',12600,'upi','success'),
(5008,1008,'2024-03-15 08:01:00',28000,'card','pending'),
(5009,1009,'2024-04-02 12:11:00',1250,'upi','success'),
(5010,1010,'2024-04-02 12:11:00',10500,'card','success'),
(5011,1011,'2024-04-15 20:01:00',89400,'card','success'),
(5012,1012,'2024-05-05 09:01:00',8000,'card','refunded'),
(5013,1013,'2024-05-20 13:31:00',23000,'upi','success'),
(5014,1014,'2024-05-20 13:31:00',5500,'upi','success'),
(5015,1015,NULL,NULL,'card','pending');

-- 3. Classic SQL interview / LeetCode-style tables.
CREATE TABLE scores (id INT PRIMARY KEY, score NUMERIC(5,2) NOT NULL);
INSERT INTO scores VALUES
(1,3.50),(2,3.65),(3,4.00),(4,3.85),
(5,4.00),(6,3.65),(7,2.90),(8,4.20);

CREATE TABLE persons (
    person_id INT PRIMARY KEY,
    last_name VARCHAR(60) NOT NULL,
    first_name VARCHAR(60) NOT NULL
);
CREATE TABLE addresses (
    address_id INT PRIMARY KEY,
    person_id INT REFERENCES persons(person_id),
    city VARCHAR(60),
    state VARCHAR(60)
);
INSERT INTO persons VALUES
(1,'Wang','Allen'),(2,'Alice','Bob'),(3,'Kumar','Ravi'),(4,'Shah','Mina');
INSERT INTO addresses VALUES
(101,1,'New York City','New York'),
(102,3,'Bengaluru','Karnataka'),
(103,NULL,'Unlinked City','NA');

-- 4. Time-series tables: running totals, moving averages, LAG/LEAD, date gaps.
CREATE TABLE daily_sales (sales_date DATE PRIMARY KEY, revenue NUMERIC(12,2) NOT NULL);
INSERT INTO daily_sales VALUES
('2024-01-01',1000),('2024-01-02',1200),('2024-01-03',900),
('2024-01-04',1500),('2024-01-05',1500),('2024-01-06',1800),
('2024-01-08',1100),('2024-01-09',1300);

CREATE TABLE weather (
    id INT PRIMARY KEY,
    record_date DATE NOT NULL UNIQUE,
    temperature INT NOT NULL
);
INSERT INTO weather VALUES
(1,'2024-01-01',20),(2,'2024-01-02',25),(3,'2024-01-03',23),
(4,'2024-01-04',26),(5,'2024-01-05',26),(6,'2024-01-06',19),
(7,'2024-01-07',30);

-- 5. Event data: event-time vs processing-time, ordering, deduplication, sessions.
CREATE TABLE activity_events (
    event_id BIGINT PRIMARY KEY,
    user_id INT NOT NULL,
    event_type VARCHAR(30) NOT NULL,
    event_time TIMESTAMP NOT NULL,
    received_time TIMESTAMP NOT NULL,
    session_id VARCHAR(30),
    event_value NUMERIC(12,2),
    source VARCHAR(30)
);
INSERT INTO activity_events VALUES
(1,1,'login','2024-06-01 09:00:00','2024-06-01 09:00:01','s1',NULL,'web'),
(2,1,'view_product','2024-06-01 09:02:00','2024-06-01 09:02:01','s1',NULL,'web'),
(3,1,'add_to_cart','2024-06-01 09:04:00','2024-06-01 09:04:03','s1',85000,'web'),
(4,1,'purchase','2024-06-01 09:08:00','2024-06-01 09:08:01','s1',85000,'web'),
(5,2,'login','2024-06-01 10:00:00','2024-06-01 10:00:01','s2',NULL,'mobile'),
(6,2,'view_product','2024-06-01 10:03:00','2024-06-01 10:03:01','s2',NULL,'mobile'),
(7,2,'login','2024-06-01 11:30:00','2024-06-01 11:30:01','s3',NULL,'mobile'),
(8,2,'purchase','2024-06-01 11:35:00','2024-06-01 11:40:00','s3',1200,'mobile'),
(9,3,'login','2024-06-02 08:00:00','2024-06-02 08:00:02','s4',NULL,'web'),
(10,3,'search','2024-06-02 08:01:00','2024-06-02 08:01:02','s4',NULL,'web'),
(11,3,'search','2024-06-02 08:01:00','2024-06-02 08:02:30','s4',NULL,'web'),
(12,3,'logout','2024-06-02 08:20:00','2024-06-02 08:20:01','s4',NULL,'web'),
(13,4,'login','2024-06-02 12:00:00','2024-06-02 12:00:01','s5',NULL,'mobile'),
(14,4,'purchase','2024-06-02 12:10:00','2024-06-02 12:10:01','s5',4500,'mobile');

-- Indexes for realistic query-planning exercises.
CREATE INDEX idx_employees_department_salary ON employees(department_id, salary DESC);
CREATE INDEX idx_orders_customer_date ON orders(customer_id, order_date DESC);
CREATE INDEX idx_order_items_order ON order_items(order_id);
CREATE INDEX idx_payments_order_status ON payments(order_id, payment_status);
CREATE INDEX idx_events_user_time ON activity_events(user_id, event_time);

-- Sanity check: expected row counts should match after successful execution.
SELECT 'departments' AS table_name, COUNT(*) AS row_count FROM departments
UNION ALL SELECT 'employees', COUNT(*) FROM employees
UNION ALL SELECT 'customers', COUNT(*) FROM customers
UNION ALL SELECT 'products', COUNT(*) FROM products
UNION ALL SELECT 'orders', COUNT(*) FROM orders
UNION ALL SELECT 'order_items', COUNT(*) FROM order_items
UNION ALL SELECT 'payments', COUNT(*) FROM payments
UNION ALL SELECT 'scores', COUNT(*) FROM scores
UNION ALL SELECT 'persons', COUNT(*) FROM persons
UNION ALL SELECT 'addresses', COUNT(*) FROM addresses
UNION ALL SELECT 'daily_sales', COUNT(*) FROM daily_sales
UNION ALL SELECT 'weather', COUNT(*) FROM weather
UNION ALL SELECT 'activity_events', COUNT(*) FROM activity_events
ORDER BY table_name;
