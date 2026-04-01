-- Fact model: inventory snapshots
-- Purpose:
-- Store daily inventory balances by product and store using surrogate keys.
-- BigQuery execution target:
-- `omnisource-analytics.warehouse_layer.warehouse_fact_inventory`

CREATE OR REPLACE TABLE `omnisource-analytics.warehouse_layer.warehouse_fact_inventory` AS
SELECT
    CAST(FORMAT_DATE('%Y%m%d', i.snapshot_date) AS INT64) AS date_key,
    p.product_sk,
    s.store_sk,
    i.stock_quantity
FROM `omnisource-analytics.staging_layer.stg_inventory_snapshots` i
LEFT JOIN `omnisource-analytics.warehouse_layer.warehouse_dim_product` p
    ON i.product_id = p.product_id
LEFT JOIN `omnisource-analytics.warehouse_layer.warehouse_dim_store` s
    ON i.store_id = s.store_id;
