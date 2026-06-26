import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# ==========================
# Connect to MySQL
# ==========================

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="S1o2b3h4a5@",   # Replace with your password
    database="ecommerce"
)

print("✅ Connected to MySQL")

# ==========================
# Total Revenue
# ==========================

query = """
SELECT SUM(o.quantity * p.selling_price) AS Total_Revenue
FROM orders o
JOIN products p
ON o.product_id = p.product_id;
"""

revenue = pd.read_sql(query, conn)

print("\n========== TOTAL REVENUE ==========")
print(revenue)

# ==========================
# Total Profit
# ==========================

query = """
SELECT
SUM(o.quantity*(p.selling_price-p.cost_price))
AS Total_Profit

FROM orders o
JOIN products p
ON o.product_id=p.product_id;
"""

profit = pd.read_sql(query, conn)

print("\n========== TOTAL PROFIT ==========")
print(profit)

# ==========================
# Top Products
# ==========================

query = """
SELECT
p.product_name,
SUM(o.quantity) Total_Sold

FROM orders o
JOIN products p

ON o.product_id=p.product_id

GROUP BY p.product_name

ORDER BY Total_Sold DESC

LIMIT 10;
"""

top_products = pd.read_sql(query, conn)

print("\n========== TOP PRODUCTS ==========")
print(top_products)

# ==========================
# Top Customers
# ==========================

query = """
SELECT
c.customer_name,
COUNT(*) Orders

FROM customers c
JOIN orders o

ON c.customer_id=o.customer_id

GROUP BY c.customer_name

ORDER BY Orders DESC

LIMIT 10;
"""

top_customers = pd.read_sql(query, conn)

print("\n========== TOP CUSTOMERS ==========")
print(top_customers)

# ==========================
# Payment Method Analysis
# ==========================

query = """
SELECT
payment_method,
COUNT(*) Orders

FROM orders

GROUP BY payment_method;
"""

payments = pd.read_sql(query, conn)

print("\n========== PAYMENT METHODS ==========")
print(payments)

conn.close()

print("\nDatabase Connection Closed")