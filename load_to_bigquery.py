from google.cloud import bigquery
import pandas as pd
import numpy as np

client = bigquery.Client(project='arokyamary-analytics')
print('Generating 500,000 orders...')

np.random.seed(42)
n = 500_000
products = ['iPhone 15','Samsung TV','Nike Shoes','Dell Laptop','Rice 10kg','T-Shirt']
categories = ['Electronics','Electronics','Fashion','Electronics','Grocery','Fashion']
cities = ['Bengaluru','Mumbai','Delhi','Chennai','Hyderabad','Pune']
prod_idx = np.random.randint(0, len(products), n)

df = pd.DataFrame({
'order_id': [f'ORD{i:08d}' for i in range(n)],
'customer_id': np.random.randint(1000, 99999, n),
'product': [products[i] for i in prod_idx],
'category': [categories[i] for i in prod_idx],
'city': np.random.choice(cities, n),
'quantity': np.random.randint(1, 5, n),
'unit_price': np.random.choice([79999,45000,4999,65000,899,799], n).astype(float),
'total_amount': np.random.uniform(500, 100000, n),
'order_date': pd.date_range('2023-01-01', periods=n, freq='1min')[:n],
'device': np.random.choice(['mobile','desktop','tablet'], n),
})

table_id = 'arokyamary-analytics.ecommerce_raw.orders'
job_config = bigquery.LoadJobConfig(autodetect=True, write_disposition='WRITE_TRUNCATE')

print(f'Uploading {len(df):,} rows to BigQuery...')
job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
job.result()

table = client.get_table(table_id)
print(f'SUCCESS: Loaded {table.num_rows:,} rows to {table_id}')