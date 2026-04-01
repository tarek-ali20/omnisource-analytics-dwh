# Expanded Domain Model

The project is now moving from a simple sales warehouse toward a broader commerce analytics platform.

## Core Business Domains

- Customers: who buys, returns, churns, and engages.
- Products: what is sold, viewed, and stocked.
- Campaigns: which marketing spend drives sessions, orders, and revenue.
- Stores: which branch or fulfillment location influences demand and inventory.
- Orders and Transactions: the monetized business outcome.
- Inventory: whether stock availability supports or blocks demand.
- Web Events: pre-purchase behavior and conversion flow.

## Key Relationships

- `raw_transactions.campaign_id` -> `warehouse_dim_campaign.campaign_id`
- `raw_transactions.store_id` -> `warehouse_dim_store.store_id`
- `raw_transactions.session_id` -> `raw_web_events.session_id`
- `raw_web_events.customer_id` -> `warehouse_dim_customer.customer_id`
- `raw_inventory_snapshots.product_id` -> `warehouse_dim_product.product_id`
- `raw_inventory_snapshots.store_id` -> `warehouse_dim_store.store_id`

## Why These Tables Matter

- `warehouse_dim_campaign` enables ROI, CAC, ROAS, and acquisition analysis.
- `warehouse_dim_store` enables branch performance and geo-operations analysis.
- `warehouse_fact_inventory` explains lost sales, stock pressure, and replenishment needs.
- `warehouse_fact_web_events` links behavior before purchase to campaign and revenue outcomes.

## Recommended Next Wave, Not Immediate

If the project needs to grow further, the next realistic domains are:

- `warehouse_fact_returns`
- `warehouse_fact_payments`
- `warehouse_dim_supplier`
- `warehouse_dim_employee`
- `warehouse_fact_customer_support`

These should be added only if they support actual leadership questions, operating KPIs, or Power BI dashboard requirements.
