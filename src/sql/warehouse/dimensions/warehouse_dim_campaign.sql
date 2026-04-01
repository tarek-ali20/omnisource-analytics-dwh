-- Dimension model: campaign
-- Purpose:
-- Build the marketing campaign dimension with a surrogate key for fact-table joins.
-- BigQuery execution target:
-- `omnisource-analytics.warehouse_layer.warehouse_dim_campaign`

CREATE OR REPLACE TABLE `omnisource-analytics.warehouse_layer.warehouse_dim_campaign` AS
SELECT
    GENERATE_UUID() AS campaign_sk,
    campaign_id,
    platform_name,
    budget,
    start_date
FROM `omnisource-analytics.staging_layer.stg_campaigns`;
