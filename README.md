# ecommerce_dataengineering_project
I have made this project using pySpark which first generate ecommerce data and then transform it into a clean dataset.
This project simulates an e-commerce data pipeline with data generation, transformation, and loading steps.

## Project Structure

```
ecommerce_project/
├── data/
├── notebooks/
│   └── ecommerce_pipeline.ipynb
├── scripts/
│   ├── generate_orders.py
│   ├── transform_orders.py
│   └── load_orders.py
└── README.md
```

## How to Run

1. Install dependencies:
   ```bash
   pip install pandas
   ```

2. You can use the notebook to walk through the transformation and loading process:
   ```
   notebooks/ecommerce_pipeline.ipynb
   ```

3. Or run the scripts manually:
   ```bash
   python scripts/transform_orders.py
   python scripts/load_orders.py
   ```

Important thing to keep in mind:
You must have python, pyspark, jupyter notebook and hadoop bin made or installed and added to path. Errors can be raised if these apps or tools are not compatible with each other.

