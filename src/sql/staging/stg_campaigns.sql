-- Staging model: campaigns
-- Purpose:
-- Provide a BI-friendly view for marketing campaign analysis and attribution.
-- BigQuery execution target:
-- `omnisource-analytics.staging_layer.stg_campaigns`
-- Note:
-- This version keeps the essential columns from your proposed SQL and retains
-- a few extra business-useful fields from the expanded raw schema.

CREATE OR REPLACE VIEW `omnisource-analytics.staging_layer.stg_campaigns` AS
SELECT
    CAST(campaign_id AS STRING) AS campaign_id,
    TRIM(platform_name) AS platform_name,
    SAFE_CAST(budget AS FLOAT64) AS budget,
    SAFE_CAST(start_date AS DATE) AS start_date,
    TRIM(campaign_name) AS campaign_name,
    TRIM(channel_group) AS channel_group,
    TRIM(campaign_objective) AS campaign_objective,
    SAFE_CAST(actual_spend AS FLOAT64) AS actual_spend,
    SAFE_CAST(end_date AS DATE) AS end_date,
    TRIM(status) AS campaign_status
FROM `omnisource-analytics.raw_layer.raw_campaigns`
WHERE campaign_id IS NOT NULL;
