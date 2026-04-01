-- Fact model: transactions
-- Purpose:
-- Central sales fact table linking customer, product, campaign, store, time,
-- and core business dimensions.
-- BigQuery execution target:
-- `omnisource-analytics.warehouse_layer.warehouse_fact_transactions`
-- Note:
-- ANY_VALUE subqueries are used on dimensions to reduce accidental fan-out
-- when duplicate natural keys exist in dimension tables.

CREATE OR REPLACE TABLE `omnisource-analytics.warehouse_layer.warehouse_fact_transactions` AS
SELECT
    CAST(FORMAT_DATE('%Y%m%d', t.transaction_date) AS INT64) AS date_key,
    c.customer_sk,
    p.product_sk,
    camp.campaign_sk,
    s.store_sk,
    t.transaction_id,
    t.session_id,
    t.quantity,
    t.unit_price,
    t.calculated_total_amount
FROM `omnisource-analytics.staging_layer.stg_transactions` t
LEFT JOIN `omnisource-analytics.warehouse_layer.warehouse_dim_customer` c
    ON t.customer_id = c.customer_id
    AND t.transaction_date >= c.valid_from
    AND (t.transaction_date <= c.valid_to OR c.valid_to IS NULL)
LEFT JOIN (
    SELECT product_id, ANY_VALUE(product_sk) AS product_sk
    FROM `omnisource-analytics.warehouse_layer.warehouse_dim_product`
    GROUP BY product_id
) p
    ON t.product_id = p.product_id
LEFT JOIN (
    SELECT campaign_id, ANY_VALUE(campaign_sk) AS campaign_sk
    FROM `omnisource-analytics.warehouse_layer.warehouse_dim_campaign`
    GROUP BY campaign_id
) camp
    ON t.campaign_id = camp.campaign_id
LEFT JOIN (
    SELECT store_id, ANY_VALUE(store_sk) AS store_sk
    FROM `omnisource-analytics.warehouse_layer.warehouse_dim_store`
    GROUP BY store_id
) s
    ON t.store_id = s.store_id
WHERE t.data_quality_status = 'Passed';
