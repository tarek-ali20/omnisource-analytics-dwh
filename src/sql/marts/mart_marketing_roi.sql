-- Mart model: marketing ROI
-- Purpose:
-- Connect campaign cost to realized revenue and conversions for performance
-- marketing and leadership reporting.
-- BigQuery execution target:
-- `omnisource-analytics.marts_layer.mart_marketing_roi`

CREATE OR REPLACE VIEW `omnisource-analytics.marts_layer.mart_marketing_roi` AS
WITH campaign_revenue AS (
    SELECT
        campaign_sk,
        SUM(calculated_total_amount) AS total_revenue_generated,
        COUNT(transaction_id) AS total_conversions
    FROM `omnisource-analytics.warehouse_layer.warehouse_fact_transactions`
    WHERE campaign_sk IS NOT NULL
    GROUP BY 1
)
SELECT
    c.platform_name,
    c.campaign_id,
    c.budget AS campaign_cost,
    COALESCE(r.total_revenue_generated, 0) AS revenue,
    COALESCE(r.total_conversions, 0) AS conversions,
    CASE
        WHEN c.budget > 0 THEN (COALESCE(r.total_revenue_generated, 0) - c.budget) / c.budget
        ELSE 0
    END AS return_on_investment_roi
FROM `omnisource-analytics.warehouse_layer.warehouse_dim_campaign` c
LEFT JOIN campaign_revenue r
    ON c.campaign_sk = r.campaign_sk;
