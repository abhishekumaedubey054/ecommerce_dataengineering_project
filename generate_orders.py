# This script was used to generate sample order data.
# It's already been executed, and the data is in data/raw/orders.json

import json
import random
from datetime import datetime, timedelta

products = ["Laptop", "Smartphone", "Tablet", "Headphones", "Monitor"]
orders = []

for i in range(50):
    orders.append({
        "order_id": f"ORD{1000 + i}",
        "customer_id": f"CUST{random.randint(100, 999)}",
        "product": random.choice(products),
        "quantity": random.randint(1, 5),
        "price": round(random.uniform(100.0, 1000.0), 2),
        "order_date": (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")
    })

with open("data/raw/orders.json", "w") as f:
    json.dump(orders, f, indent=2)
