-- Dimension model: customer
-- Purpose:
-- Build the customer dimension with surrogate keys and SCD Type 2 tracking fields.
-- BigQuery execution target:
-- `omnisource-analytics.warehouse_layer.warehouse_dim_customer`
-- Note:
-- `valid_from` is intentionally backdated to 1900-01-01 so historical
-- transactions always find a matching current customer record.

CREATE OR REPLACE TABLE `omnisource-analytics.warehouse_layer.warehouse_dim_customer` AS
SELECT
    GENERATE_UUID() AS customer_sk,
    customer_id,
    first_name,
    last_name,
    CONCAT(first_name, ' ', last_name) AS full_name,
    email,
    phone_number,
    country,
    city,
    registration_date,
    customer_segment,
    status AS account_status,
    DATE('1900-01-01') AS valid_from,
    CAST(NULL AS DATE) AS valid_to,
    TRUE AS is_current
FROM `omnisource-analytics.staging_layer.stg_customers`;
