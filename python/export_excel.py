import pandas as pd
import mysql.connector
from pathlib import Path

# ==========================
# MySQL Connection
# ==========================
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="S1o2b3h4a5@",      # Your password
    database="ecommerce"
)

# ==========================
# Export Folder
# ==========================
BASE_DIR = Path(__file__).resolve().parent.parent
EXPORT_DIR = BASE_DIR / "exports"
EXPORT_DIR.mkdir(exist_ok=True)

# ==========================
# Export Tables
# ==========================
tables = ["customers", "categories", "products", "orders"]

for table in tables:
    df = pd.read_sql(f"SELECT * FROM {table}", conn)
    file_path = EXPORT_DIR / f"{table}.xlsx"
    df.to_excel(file_path, index=False)
    print(f"✅ {table}.xlsx exported")

conn.close()

print("\n🎉 All Excel files exported successfully!")