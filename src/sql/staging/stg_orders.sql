-- Staging model: orders
-- Purpose:
-- Standardize operational order data loaded from SQLite into the staging layer.
-- BigQuery execution target:
-- `omnisource-analytics.staging_layer.stg_orders`

CREATE OR REPLACE VIEW `omnisource-analytics.staging_layer.stg_orders` AS
SELECT
    CAST(order_id AS STRING) AS order_id,
    CAST(customer_id AS STRING) AS customer_id,
    UPPER(TRIM(order_status)) AS order_status,
    SAFE_CAST(order_date AS DATE) AS order_date,
    SAFE_CAST(shipping_cost AS FLOAT64) AS shipping_cost
FROM `omnisource-analytics.raw_layer.raw_orders`
WHERE order_id IS NOT NULL;
