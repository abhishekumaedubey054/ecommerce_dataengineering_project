import json
import pandas as pd

# Load raw data
with open("data/raw/orders.json", "r") as f:
    orders = json.load(f)

# Transform: convert to DataFrame and add total_price
df = pd.DataFrame(orders)
df["total_price"] = df["quantity"] * df["price"]

# Save to CSV
df.to_csv("data/transformed_orders.csv", index=False)
print("Transformed data saved to data/transformed_orders.csv")
