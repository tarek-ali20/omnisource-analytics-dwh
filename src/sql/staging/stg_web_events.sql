-- Staging model: web events
-- Purpose:
-- Simplify clickstream data into the key fields most useful for web-behavior analysis.
-- BigQuery execution target:
-- `omnisource-analytics.staging_layer.stg_web_events`

CREATE OR REPLACE VIEW `omnisource-analytics.staging_layer.stg_web_events` AS
SELECT
    CAST(session_id AS STRING) AS session_id,
    CAST(customer_id AS STRING) AS customer_id,
    TRIM(page_visited) AS page_visited,
    SAFE_CAST(time_spent_seconds AS INT64) AS time_spent_seconds,
    SAFE_CAST(event_timestamp AS TIMESTAMP) AS event_timestamp
FROM `omnisource-analytics.raw_layer.raw_web_events`
WHERE session_id IS NOT NULL;
