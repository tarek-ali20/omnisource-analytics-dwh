-- Staging model: stores
-- Purpose:
-- Standardize branch and store information for location-based analytics.
-- BigQuery execution target:
-- `omnisource-analytics.staging_layer.stg_stores`
-- Note:
-- The raw schema uses `city` and `area_sq_m`, so they are aliased here to match
-- your requested BI naming style.

CREATE OR REPLACE VIEW `omnisource-analytics.staging_layer.stg_stores` AS
SELECT
    CAST(store_id AS STRING) AS store_id,
    TRIM(store_name) AS store_name,
    TRIM(store_type) AS store_type,
    TRIM(country) AS country,
    TRIM(city) AS city,
    -- تحويل المساحة إلى FLOAT بناءً على الـ Schema
    CAST(area_sq_m AS FLOAT64) AS area_sq_m,
    -- تحويل رقم الهاتف لنص دفاعياً للحفاظ عليه
    CAST(phone_number AS STRING) AS phone_number
FROM `omnisource-analytics.raw_layer.raw_stores`
WHERE store_id IS NOT NULL;
