# Execution Order

This document defines the recommended SQL execution order for BigQuery.

## 1. Raw Layer

Load the source datasets into the `raw_layer` dataset.

Expected raw tables:

- `raw_customers_master`
- `raw_orders`
- `raw_transactions`
- `raw_scraped_prices`
- `raw_exchange_rates`
- `raw_campaigns`
- `raw_stores`
- `raw_inventory_snapshots`
- `raw_web_events`

## 2. Staging Layer

Run staging views after the raw tables exist.

Recommended order:

1. `stg_customers`
2. `stg_orders`
3. `stg_campaigns`
4. `stg_stores`
5. `stg_web_events`
6. `stg_inventory_snapshots`
7. `stg_exchange_rates`
8. `stg_transactions`

## 3. Warehouse Dimensions

Run dimension models before fact models.

Recommended order:

1. `warehouse_dim_date`
2. `warehouse_dim_store`
3. `warehouse_dim_campaign`
4. `warehouse_dim_customer`
5. `warehouse_dim_product`

## 4. Warehouse Facts

Run fact models after all required dimensions are available.

Recommended order:

1. `warehouse_fact_inventory`
2. `warehouse_fact_web_events`
3. `warehouse_fact_transactions`

## 5. Marts Layer

Run marts after the warehouse layer is fully built.

Recommended order:

1. `mart_sales_performance`
2. `mart_customer_360`
3. `mart_marketing_roi`

## Validation After Each Layer

- Confirm successful creation in BigQuery
- Check row counts
- Spot-check key columns
- Verify joins do not create unexpected fan-out
- Confirm BI-facing metrics match expectations
