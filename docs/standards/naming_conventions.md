# Naming Conventions

## Table Naming

- `raw_<source_or_entity>` for landing tables in the raw layer
- `stg_<entity>` for cleansed staging views
- `warehouse_dim_<entity>` for dimension tables
- `warehouse_fact_<entity>` for fact tables
- `mart_<business_area>` for business-facing marts

## Examples

- `raw_transactions`
- `raw_customers_master`
- `stg_transactions`
- `warehouse_dim_customer`
- `warehouse_fact_transactions`
- `mart_sales_performance`

## Dataset Strategy

- `raw_layer`
- `staging_layer`
- `warehouse_layer`
- `mart_layer`

## Recommended File Naming

- Python ingestion scripts: `verb_object.py`
- SQL models: align file name with produced table or view name
- Documentation: lowercase snake_case Markdown files
