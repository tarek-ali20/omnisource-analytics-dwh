-- Staging model: inventory snapshots
-- Purpose:
-- Prepare daily inventory snapshot data for stock availability analysis.
-- BigQuery execution target:
-- `omnisource-analytics.staging_layer.stg_inventory_snapshots`

CREATE OR REPLACE VIEW `omnisource-analytics.staging_layer.stg_inventory_snapshots` AS
SELECT
    SAFE_CAST(snapshot_date AS DATE) AS snapshot_date,
    CAST(product_id AS STRING) AS product_id,
    CAST(store_id AS STRING) AS store_id,
    SAFE_CAST(stock_quantity AS INT64) AS stock_quantity
FROM `omnisource-analytics.raw_layer.raw_inventory_snapshots`
WHERE product_id IS NOT NULL;
