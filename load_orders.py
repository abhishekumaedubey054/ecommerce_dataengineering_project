import pandas as pd

# Load transformed data
df = pd.read_csv("data/transformed_orders.csv")

# Load simulation
print("Loaded transformed orders:")
print(df.head())
