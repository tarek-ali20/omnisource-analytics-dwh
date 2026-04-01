# Project Structure

This document explains how the repository is organized and how each major folder contributes to the overall analytics platform.

## Top-Level Layout

### `data/`

Contains local demo source data used to simulate upstream systems.

- `raw/`: CSV and SQLite inputs used before ingestion into BigQuery

### `docs/`

Contains all written project documentation.

- `architecture/`: system views, data flow, and domain design
- `plans/`: roadmap, warnings, and readiness planning
- `reference/`: practical references such as schemas and execution order
- `standards/`: naming and design conventions

### `src/`

Contains the executable project logic.

- `ingestion/`: Python scripts for data generation, extraction, and loading
- `sql/`: SQL models grouped by analytical layer

### `requirements.txt`

Lists Python dependencies used by local scripts and ingestion workflows.

## SQL Folder Breakdown

### `src/sql/staging/`

Staging views that clean and standardize raw source data.

Examples:

- `stg_customers.sql`
- `stg_transactions.sql`
- `stg_campaigns.sql`

### `src/sql/warehouse/dimensions/`

Dimension models that create descriptive analytical entities.

Examples:

- `warehouse_dim_customer.sql`
- `warehouse_dim_product.sql`
- `warehouse_dim_store.sql`

### `src/sql/warehouse/facts/`

Fact models that store measurable business events.

Examples:

- `warehouse_fact_transactions.sql`
- `warehouse_fact_inventory.sql`
- `warehouse_fact_web_events.sql`

### `src/sql/marts/`

Presentation-ready views intended for Power BI and business reporting.

Examples:

- `mart_sales_performance.sql`
- `mart_customer_360.sql`
- `mart_marketing_roi.sql`

## Why This Structure Works

- It mirrors how production analytics platforms are typically organized
- It makes execution order intuitive
- It separates transformation logic from reporting logic
- It improves readability for reviewers, recruiters, and hiring managers
