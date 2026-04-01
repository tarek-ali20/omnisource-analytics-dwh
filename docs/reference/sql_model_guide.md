# SQL Model Guide

This guide summarizes the responsibility of each SQL layer and the models inside it.

## Staging Layer

The staging layer is responsible for:

- Standardizing data types
- Cleaning text and identifiers
- Normalizing source fields
- Preparing stable upstream interfaces for the warehouse layer

Core models:

- `stg_customers`
- `stg_orders`
- `stg_transactions`
- `stg_campaigns`
- `stg_stores`
- `stg_inventory_snapshots`
- `stg_web_events`
- `stg_exchange_rates`

## Warehouse Dimensions

Dimensions provide descriptive business context used by downstream fact tables.

Core dimensions:

- `warehouse_dim_date`
- `warehouse_dim_customer`
- `warehouse_dim_product`
- `warehouse_dim_campaign`
- `warehouse_dim_store`

## Warehouse Facts

Fact tables store measurable business events and metrics.

Core facts:

- `warehouse_fact_transactions`
- `warehouse_fact_inventory`
- `warehouse_fact_web_events`

## Marts Layer

Marts reshape warehouse data into reporting-friendly views suitable for BI tools.

Current marts:

- `mart_sales_performance`
- `mart_customer_360`
- `mart_marketing_roi`

## Modeling Philosophy

This repository follows a layered analytics engineering approach:

- Raw data lands with minimal business logic
- Staging standardizes and cleans entities
- Warehouse models create reusable analytical foundations
- Marts serve reporting and dashboard needs
