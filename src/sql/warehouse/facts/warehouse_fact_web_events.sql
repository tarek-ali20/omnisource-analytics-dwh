-- Fact model: web events
-- Purpose:
-- Store clickstream-style web interactions linked to the customer dimension
-- using SCD-aware joins.
-- BigQuery execution target:
-- `omnisource-analytics.warehouse_layer.warehouse_fact_web_events`

CREATE OR REPLACE TABLE `omnisource-analytics.warehouse_layer.warehouse_fact_web_events` AS
SELECT
    CAST(FORMAT_DATE('%Y%m%d', DATE(w.event_timestamp)) AS INT64) AS date_key,
    c.customer_sk,
    w.session_id,
    w.page_visited,
    w.time_spent_seconds,
    w.event_timestamp
FROM `omnisource-analytics.staging_layer.stg_web_events` w
LEFT JOIN `omnisource-analytics.warehouse_layer.warehouse_dim_customer` c
    ON w.customer_id = c.customer_id
    AND DATE(w.event_timestamp) >= c.valid_from
    AND (DATE(w.event_timestamp) <= c.valid_to OR c.valid_to IS NULL);
