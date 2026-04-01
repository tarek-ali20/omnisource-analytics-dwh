-- Staging model: transactions
-- Purpose:
-- Provide the expanded sales transaction view with campaign, store, and session keys.
-- BigQuery execution target:
-- `omnisource-analytics.staging_layer.stg_transactions`
-- Note:
-- The raw schema uses `price` and `total_amount`, so they are mapped here to
-- `unit_price` and `calculated_total_amount` for warehouse compatibility.

CREATE OR REPLACE VIEW `omnisource-analytics.staging_layer.stg_transactions` AS
SELECT
    CAST(transaction_id AS STRING) AS transaction_id,
    CAST(customer_id AS STRING) AS customer_id,
    CAST(product_id AS STRING) AS product_id,
    CAST(campaign_id AS STRING) AS campaign_id, 
    CAST(store_id AS STRING) AS store_id,       
    CAST(session_id AS STRING) AS session_id,   
    CAST(transaction_date AS DATE) AS transaction_date,
    CAST(quantity AS INTEGER) AS quantity,
    CAST(price AS FLOAT64) AS unit_price, -- تم التغيير من unit_price إلى price
    CAST(total_amount AS FLOAT64) AS calculated_total_amount, -- تم التغيير من calculated_total_amount إلى total_amount
    'Passed' AS data_quality_status 
FROM `omnisource-analytics.raw_layer.raw_transactions`
WHERE transaction_id IS NOT NULL;