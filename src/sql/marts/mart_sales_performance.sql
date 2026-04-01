-- Mart model: sales performance
-- Purpose:
-- Provide a Power BI-ready sales mart for leadership and sales managers.
-- BigQuery execution target:
-- `omnisource-analytics.marts_layer.mart_sales_performance`

CREATE OR REPLACE VIEW `omnisource-analytics.marts_layer.mart_sales_performance` AS
SELECT
    d.year,
    d.year_quarter,
    d.month_name,
    s.store_name,
    s.city AS store_city,
    p.product_name,
    camp.platform_name AS campaign_source,
    SUM(f.quantity) AS total_units_sold,
    SUM(f.calculated_total_amount) AS total_revenue,
    AVG(f.unit_price) AS avg_unit_price
FROM `omnisource-analytics.warehouse_layer.warehouse_fact_transactions` f
JOIN `omnisource-analytics.warehouse_layer.warehouse_dim_date` d
    ON f.date_key = d.date_key
JOIN `omnisource-analytics.warehouse_layer.warehouse_dim_store` s
    ON f.store_sk = s.store_sk
JOIN `omnisource-analytics.warehouse_layer.warehouse_dim_product` p
    ON f.product_sk = p.product_sk
LEFT JOIN `omnisource-analytics.warehouse_layer.warehouse_dim_campaign` camp
    ON f.campaign_sk = camp.campaign_sk
GROUP BY 1, 2, 3, 4, 5, 6, 7;
