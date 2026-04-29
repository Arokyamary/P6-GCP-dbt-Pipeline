# GCP BigQuery + dbt Cloud Data Pipeline

## Project Overview
An end-to-end production-grade data pipeline built using Google Cloud Platform, dbt Cloud, and Looker Studio. The pipeline ingests 500,000 e-commerce orders, transforms them using dbt models, and visualizes insights in a live dashboard.

**Tech Stack:** Python · Google BigQuery · dbt Cloud · Looker Studio

---

## Architecture

Python ETL → BigQuery (Raw) → dbt Cloud (Transform) → Looker Studio (Dashboard)
---

## Architecture Diagram

![Architecture Diagram](architecture.png)

---

## Project Structure
```
P6_GCP_dbt/
│
├── models/
│   ├── staging/
│   │   └── stg_orders.sql
│   └── marts/
│       ├── fct_daily_revenue.sql
│       ├── fct_product_performance.sql
│       └── dim_city_summary.sql
│
├── tests/
│   └── schema.yml
│
├── load_to_bigquery.py
├── requirements.txt
└── dbt_project.yml

```

---

## Data Pipeline Layers

| Layer | Component | Tool |
|-------|-----------|------|
| Ingestion | Python ETL script | load_to_bigquery.py |
| Raw Layer | BigQuery dataset | ecommerce_raw.orders (500K rows) |
| Staging | dbt view model | stg_orders (cleaned + validated) |
| Mart Layer | dbt table models (3) | fct_daily_revenue, fct_product_performance, dim_city_summary |
| Tests | dbt schema tests | unique, not_null on key columns |
| Docs | dbt docs generate | Lineage graph (DAG visualization) |
| Dashboard | Looker Studio | 5-chart auto-refresh report |

---

## Dataset Schema

**ecommerce_raw.orders (500K rows)**

| Column | Type | Description |
|--------|------|-------------|
| order_id | STRING | Unique order identifier |
| customer_id | INTEGER | Customer identifier |
| product | STRING | Product name |
| category | STRING | Product category |
| city | STRING | City of order |
| quantity | INTEGER | Units ordered |
| unit_price | FLOAT | Price per unit |
| total_amount | FLOAT | Total order value |
| order_date | TIMESTAMP | Order timestamp |
| device | STRING | Device type (mobile/desktop/tablet) |

---

## dbt Models

### stg_orders (View)
- Cleans and validates raw orders
- Casts data types, trims whitespace
- Filters null order_ids and invalid amounts

### fct_daily_revenue (Table)
- Daily revenue aggregated by category, city, device
- Metrics: total_orders, total_units_sold, gross_revenue, avg_order_value, max_order_value

### fct_product_performance (Table)
- Product-level revenue metrics
- RANK() window function to rank products within each category by revenue

### dim_city_summary (Table)
- City-level aggregation
- Metrics: unique_customers, total_orders, lifetime_revenue, avg_order_value, city_revenue_rank

---

## dbt Tests

| Model | Column | Test |
|-------|--------|------|
| stg_orders | order_id | unique, not_null |
| stg_orders | total_amount | not_null |

All tests passing.

---

## Screenshots

### BigQuery Table Preview (500K rows)
![BigQuery Preview](screenshots/bigquery_preview.png)

### dbt Lineage Graph (DAG)
![dbt Lineage](screenshots/dbt_lineage.png)

### Looker Studio Dashboard
![Dashboard](screenshots/looker_dashboard.png)

---

## Looker Studio Dashboard

**Public URL:** [Click here to view live dashboard](ADD_YOUR_LOOKER_STUDIO_URL_HERE)

**Dashboard contains:**
- Total Revenue Scorecard
- Total Orders Scorecard
- Revenue by Date — Line Chart
- Revenue by City — Bar Chart
- Revenue by Category — Donut Chart
- Date Range Filter (interactive)

---

## How to Reproduce

### Prerequisites
- Python 3.10+
- Google Cloud account (free sandbox)
- dbt Cloud account (free tier)
- Google Cloud CLI installed

### Step 1 — Clone the repo
```bash
git clone https://github.com/Arokyamry/P6-GCP-dbt-Pipeline.git
cd P6-GCP-dbt-Pipeline
```

### Step 2 — Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Step 3 — Authenticate GCP
```bash
gcloud auth application-default login
```

### Step 4 — Create BigQuery datasets
```bash
bq mk --dataset --location=asia-south1 arokyamary-analytics:ecommerce_raw
bq mk --dataset --location=asia-south1 arokyamary-analytics:ecommerce_marts
```

### Step 5 — Load 500K rows to BigQuery
```bash
python load_to_bigquery.py
```

### Step 6 — Run dbt models
- Connect dbt Cloud to BigQuery using service account JSON
- Set location to asia-south1 in connection settings
- Run the following commands in dbt Cloud IDE:

```bash
dbt run
dbt test
dbt docs generate
```

---

## Key Results

- 500,000 orders loaded to BigQuery
- 4 dbt models built and running
- 3 mart tables created in ecommerce_marts dataset
- All dbt schema tests passing
- Live Looker Studio dashboard with 5 charts

---

## Author

**Arokyamary**
[GitHub](https://github.com/Arokyamary) 
