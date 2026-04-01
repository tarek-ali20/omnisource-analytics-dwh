# OmniSource Analytics DWH

OmniSource Analytics DWH is a portfolio-grade analytics engineering project that demonstrates how a modern business can centralize operational, marketing, inventory, and behavioral data into a BigQuery-powered analytics stack.

The repository showcases an end-to-end layered workflow from raw data generation and ingestion through staging, dimensional modeling, and BI-ready data marts.

## Project Highlights

- BigQuery-centered analytics architecture using `raw`, `staging`, `warehouse`, and `marts` layers
- Realistic linked datasets for customers, transactions, campaigns, stores, inventory, and web events
- Kimball-style dimensional modeling with surrogate keys and reporting-oriented marts
- SQL assets organized by execution layer for clarity and maintainability
- Documentation prepared for GitHub presentation and technical review

## Stakeholder Value

- Sales leaders can monitor revenue, units sold, pricing, and store performance
- Marketing teams can connect campaign spend to conversions and ROI
- Operations teams can track inventory pressure and store-level stock exposure
- Customer teams can analyze retention, recency, and customer lifetime value

## Technical Stack

- Google BigQuery
- SQL
- Python
- Pandas
- SQLite
- Power BI

## Business Questions This Project Can Answer

- Which store, product, and campaign combinations generate the highest revenue?
- Which customers are most valuable and how recently did they purchase?
- Which campaigns generate conversions and the strongest return on investment?
- Where is inventory under pressure across stores and products?
- How does website behavior connect to purchase activity?

## Architecture Overview

```text
Source Systems
    |
    v
Raw Layer
    |
    v
Staging Layer
    |
    v
Warehouse Layer
    |
    v
Marts Layer
    |
    v
Power BI / BI Consumption
```

## Repository Structure

```text
.
|-- data/
|   `-- raw/                          # local source files and SQLite demo source
|-- docs/
|   |-- architecture/                # architecture and domain modeling documentation
|   |-- plans/                       # roadmap, readiness notes, and checklists
|   |-- reference/                   # schemas, execution order, and project maps
|   `-- standards/                   # naming and design conventions
|-- src/
|   |-- ingestion/                   # Python ingestion and raw-data generation scripts
|   `-- sql/
|       |-- staging/                 # cleansing and standardization views
|       |-- warehouse/
|       |   |-- dimensions/          # dimension tables
|       |   `-- facts/               # fact tables
|       `-- marts/                   # Power BI-ready reporting views
|-- requirements.txt
`-- .gitignore
```

## SQL Layers

### Staging

Standardizes raw source data into cleaner analytical interfaces.

### Warehouse

Builds reusable dimensions and facts for analytics engineering.

### Marts

Publishes reporting-ready views for BI consumers and leadership dashboards.

Current marts:

- `mart_sales_performance`
- `mart_customer_360`
- `mart_marketing_roi`

## Quick Start

1. Create and activate a Python virtual environment.
2. Install dependencies with `pip install -r requirements.txt`.
3. Generate local demo raw data with `python src/ingestion/generate_raw_demo_data.py`.
4. Authenticate to Google Cloud using Application Default Credentials.
5. Load the raw datasets into BigQuery.
6. Execute SQL models in this order:
   - `src/sql/staging/`
   - `src/sql/warehouse/dimensions/`
   - `src/sql/warehouse/facts/`
   - `src/sql/marts/`

## Documentation Index

### Architecture

- `docs/architecture/architecture_layers.md`
- `docs/architecture/data_flow.md`
- `docs/architecture/expanded_domain_model.md`

### Reference

- `docs/reference/data_dictionary.md`
- `docs/reference/raw_layer_schemas.md`
- `docs/reference/project_structure.md`
- `docs/reference/sql_model_guide.md`
- `docs/reference/execution_order.md`
- `docs/reference/stakeholder_summary.md`

### Planning

- `docs/plans/advanced_development_plan.md`
- `docs/plans/bigquery_readiness_warnings.md`
- `docs/plans/completeness_checklist.md`

### Standards

- `docs/standards/naming_conventions.md`

## Validation Note

This repository is organized and documented as a professional analytics project, but production-readiness still depends on successful BigQuery execution, row-count validation, join checks, and KPI confirmation with actual BI requirements.

## Recommended Next Improvements

- Add automated BigQuery audit queries for dimensions, facts, and marts
- Add CI validation for SQL and documentation consistency
- Parameterize project and dataset names for environment portability
- Introduce orchestration for repeatable end-to-end execution
- Add Power BI dashboard specification documents for stakeholders
