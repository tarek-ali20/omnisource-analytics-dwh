-- Mart model: customer 360
-- Purpose:
-- Provide a customer-centric mart for marketing, retention, and CRM analysis.
-- BigQuery execution target:
-- `omnisource-analytics.marts_layer.mart_customer_360`

CREATE OR REPLACE VIEW `omnisource-analytics.marts_layer.mart_customer_360` AS
SELECT
    c.customer_id,
    c.full_name,
    c.customer_segment,
    c.country,
    COUNT(f.transaction_id) AS total_orders,
    SUM(f.calculated_total_amount) AS lifetime_value_ltv,
    MAX(d.full_date) AS last_purchase_date,
    DATE_DIFF(CURRENT_DATE(), MAX(d.full_date), DAY) AS days_since_last_purchase
FROM `omnisource-analytics.warehouse_layer.warehouse_fact_transactions` f
JOIN `omnisource-analytics.warehouse_layer.warehouse_dim_customer` c
    ON f.customer_sk = c.customer_sk
JOIN `omnisource-analytics.warehouse_layer.warehouse_dim_date` d
    ON f.date_key = d.date_key
GROUP BY 1, 2, 3, 4;
