import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# ==========================
# MySQL Connection
# ==========================
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="S1o2b3h4a5@",   # Replace with your password
    database="ecommerce"
)

# ==========================
# Revenue by Category
# ==========================

query = """
SELECT
c.category_name,
SUM(o.quantity * p.selling_price) AS Revenue
FROM orders o
JOIN products p
ON o.product_id = p.product_id
JOIN categories c
ON p.category_id = c.category_id
GROUP BY c.category_name
ORDER BY Revenue DESC;
"""

category = pd.read_sql(query, conn)

plt.figure(figsize=(8,5))
plt.bar(category["category_name"], category["Revenue"])
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()

# ==========================
# Payment Method Pie Chart
# ==========================

query = """
SELECT
payment_method,
COUNT(*) AS Orders
FROM orders
GROUP BY payment_method;
"""

payment = pd.read_sql(query, conn)

plt.figure(figsize=(6,6))
plt.pie(
    payment["Orders"],
    labels=payment["payment_method"],
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Payment Method Distribution")
plt.show()

# ==========================
# Monthly Revenue
# ==========================

query = """
SELECT
MONTH(order_date) AS Month,
SUM(o.quantity * p.selling_price) AS Revenue
FROM orders o
JOIN products p
ON o.product_id = p.product_id
GROUP BY MONTH(order_date)
ORDER BY Month;
"""

monthly = pd.read_sql(query, conn)

plt.figure(figsize=(10,5))
plt.plot(monthly["Month"], monthly["Revenue"], marker="o")
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()

conn.close()

print("Charts Generated Successfully!")