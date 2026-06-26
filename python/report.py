import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="S1o2b3h4a5@",
    database="ecommerce"
)

query = """
SELECT
c.category_name,
SUM(o.quantity*p.selling_price) Revenue
FROM orders o
JOIN products p
ON o.product_id=p.product_id
JOIN categories c
ON p.category_id=c.category_id
GROUP BY c.category_name;
"""

report = pd.read_sql(query, conn)

report.to_excel("reports/sales_report.xlsx", index=False)

print("Excel Report Created Successfully!")

conn.close()