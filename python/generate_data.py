import os

print("Current Folder:", os.getcwd())
import random
from faker import Faker
import pandas as pd

fake = Faker("en_IN")

# ----------------------------
# Customers
# ----------------------------

customers = []

cities = [
    "Delhi","Mumbai","Lucknow","Noida","Kanpur",
    "Jaipur","Pune","Hyderabad","Bhopal","Patna"
]

states = [
    "Delhi","Maharashtra","Uttar Pradesh",
    "Uttar Pradesh","Uttar Pradesh",
    "Rajasthan","Maharashtra",
    "Telangana","Madhya Pradesh","Bihar"
]

for i in range(1,1001):

    customers.append({

        "customer_id":i,

        "customer_name":fake.name(),

        "gender":random.choice(["Male","Female"]),

        "age":random.randint(18,60),

        "city":random.choice(cities),

        "state":random.choice(states),

        "email":fake.email(),

        "phone":fake.msisdn()[:10]

    })

customers = pd.DataFrame(customers)
categories = [

"Electronics",

"Fashion",

"Home",

"Sports",

"Books"

]

products=[]

for i in range(1,101):

    category=random.choice(categories)

    cost=random.randint(100,5000)

    sell=cost+random.randint(100,2000)

    products.append({

        "product_id":i,

        "product_name":f"{category} Product {i}",

        "category":category,

        "cost_price":cost,

        "selling_price":sell,

        "stock":random.randint(20,500)

    })

products=pd.DataFrame(products)
orders=[]

payment_methods=[

"UPI",

"Card",

"Cash",

"Net Banking"

]

for i in range(1,5001):

    product=random.randint(1,16)

    customer=random.randint(1,1000)

    quantity=random.randint(1,5)

    orders.append({

        "order_id":i,

        "customer_id":customer,

        "product_id":product,

        "quantity":quantity,

        "payment_method":random.choice(payment_methods),

        "order_date":fake.date_between(
            start_date="-2y",
            end_date="today"
        )

    })

orders=pd.DataFrame(orders)
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "dataset"

customers.to_csv(DATASET_DIR / "customers.csv", index=False)
products.to_csv(DATASET_DIR / "products.csv", index=False)
orders.to_csv(DATASET_DIR / "orders.csv", index=False)

print("Customers:", len(customers))
print("Products:", len(products))
print("Orders:", len(orders))
print("Saved to:", DATASET_DIR)

print("Dataset Generated Successfully")
