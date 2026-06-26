-- =========================================
-- DATABASE
-- =========================================

DROP DATABASE IF EXISTS ecommerce;

CREATE DATABASE ecommerce;

USE ecommerce;
CREATE TABLE categories(

category_id INT AUTO_INCREMENT PRIMARY KEY,

category_name VARCHAR(50) NOT NULL

);
CREATE TABLE customers(

customer_id INT AUTO_INCREMENT PRIMARY KEY,

customer_name VARCHAR(100),

gender VARCHAR(20),

age INT,

city VARCHAR(100),

state VARCHAR(100),

email VARCHAR(100),

phone VARCHAR(20)

);
CREATE TABLE products(

product_id INT AUTO_INCREMENT PRIMARY KEY,

product_name VARCHAR(200),

category_id INT,

cost_price DECIMAL(10,2),

selling_price DECIMAL(10,2),

stock INT,

FOREIGN KEY(category_id)

REFERENCES categories(category_id)

);
CREATE TABLE orders(

order_id INT AUTO_INCREMENT PRIMARY KEY,

customer_id INT,

product_id INT,

quantity INT,

payment_method VARCHAR(30),

order_date DATE,

FOREIGN KEY(customer_id)

REFERENCES customers(customer_id),

FOREIGN KEY(product_id)

REFERENCES products(product_id)

);
INSERT INTO categories(category_name)

VALUES

('Electronics'),

('Fashion'),

('Home'),

('Sports'),

('Books'),

('Beauty'),

('Toys'),

('Groceries');
INSERT INTO products

(product_name,
category_id,
cost_price,
selling_price,
stock)

VALUES

('Laptop',1,42000,52000,50),

('Wireless Mouse',1,350,699,250),

('Mechanical Keyboard',1,900,1799,120),

('Gaming Headset',1,1500,2999,75),

('T-Shirt',2,250,699,400),

('Jeans',2,700,1499,220),

('Running Shoes',2,1800,3499,150),

('Sofa',3,12000,18999,20),

('Dining Table',3,9000,15999,18),

('Football',4,450,999,150),

('Cricket Bat',4,1200,2499,90),

('Python Programming Book',5,300,699,250),

('SQL Mastery Book',5,250,649,180),

('Face Wash',6,90,249,350),

('Toy Car',7,150,399,300),

('Rice 5Kg',8,300,499,500);
SHOW TABLES;

SELECT * FROM categories;

SELECT * FROM products;
