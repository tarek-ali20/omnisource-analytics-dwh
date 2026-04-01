-- Staging model: customers
-- Purpose:
-- Normalize customer master data from the raw layer into a clean BI-friendly view.
-- BigQuery execution target:
-- `omnisource-analytics.staging_layer.stg_customers`

CREATE OR REPLACE VIEW `omnisource-analytics.staging_layer.stg_customers` AS
SELECT
    CAST(customer_id AS STRING) AS customer_id,
    TRIM(first_name) AS first_name,
    TRIM(last_name) AS last_name,
    LOWER(TRIM(email)) AS email,
    CAST(phone AS STRING) AS phone_number,
    UPPER(TRIM(country)) AS country,
    TRIM(city) AS city,
    SAFE_CAST(registration_date AS DATE) AS registration_date,
    COALESCE(TRIM(customer_segment), 'Unknown') AS customer_segment,
    COALESCE(TRIM(status), 'Active') AS status
FROM `omnisource-analytics.raw_layer.raw_customers_master`
WHERE customer_id IS NOT NULL;
