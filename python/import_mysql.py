import pandas as pd
import mysql.connector
from pathlib import Path

# ==========================================
# MySQL Connection
# ==========================================

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="S1o2b3h4a5@",   # Your MySQL password
    database="ecommerce"
)

cursor = conn.cursor()

# ==========================================
# Read CSV Files
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET = BASE_DIR / "dataset"

customers = pd.read_csv(DATASET / "customers.csv")
products = pd.read_csv(DATASET / "products.csv")
orders = pd.read_csv(DATASET / "orders.csv")

# ==========================================
# Clean Existing Data
# ==========================================

cursor.execute("SET FOREIGN_KEY_CHECKS=0")

cursor.execute("DELETE FROM orders")
cursor.execute("DELETE FROM products")
cursor.execute("DELETE FROM customers")
cursor.execute("DELETE FROM categories")

cursor.execute("SET FOREIGN_KEY_CHECKS=1")

conn.commit()

print("Old data removed.")

# ==========================================
# Import Customers
# ==========================================

for _, row in customers.iterrows():

    cursor.execute("""
        INSERT INTO customers
        (customer_id, customer_name, gender, age,
         city, state, email, phone)

        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """,
    (
        int(row.customer_id),
        row.customer_name,
        row.gender,
        int(row.age),
        row.city,
        row.state,
        row.email,
        str(row.phone)
    ))

conn.commit()

print("✅ Customers Imported")

# ==========================================
# Import Categories
# ==========================================

categories = [
    (1, "Electronics"),
    (2, "Fashion"),
    (3, "Home"),
    (4, "Sports"),
    (5, "Books")
]

for category in categories:

    cursor.execute("""
        INSERT INTO categories
        (category_id, category_name)

        VALUES (%s,%s)
    """, category)

conn.commit()

print("✅ Categories Imported")

# ==========================================
# Import Products
# ==========================================

category_map = {
    "Electronics": 1,
    "Fashion": 2,
    "Home": 3,
    "Sports": 4,
    "Books": 5
}

for _, row in products.iterrows():

    cursor.execute("""
        INSERT INTO products
        (product_id,
         product_name,
         category_id,
         cost_price,
         selling_price,
         stock)

        VALUES (%s,%s,%s,%s,%s,%s)
    """,
    (
        int(row.product_id),
        row.product_name,
        category_map[row.category],
        float(row.cost_price),
        float(row.selling_price),
        int(row.stock)
    ))

conn.commit()

print("✅ Products Imported")

# ==========================================
# Import Orders
# ==========================================

for _, row in orders.iterrows():

    cursor.execute("""
        INSERT INTO orders
        (order_id,
         customer_id,
         product_id,
         quantity,
         payment_method,
         order_date)

        VALUES (%s,%s,%s,%s,%s,%s)
    """,
    (
        int(row.order_id),
        int(row.customer_id),
        int(row.product_id),
        int(row.quantity),
        row.payment_method,
        row.order_date
    ))

conn.commit()

print("✅ Orders Imported")

cursor.close()
conn.close()

print("\n🎉 ALL DATA IMPORTED SUCCESSFULLY!")