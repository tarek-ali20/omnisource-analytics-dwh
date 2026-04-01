-- Dimension model: store
-- Purpose:
-- Build the branch/store dimension from the staging layer using a surrogate key.
-- BigQuery execution target:
-- `omnisource-analytics.warehouse_layer.warehouse_dim_store`

CREATE OR REPLACE TABLE `omnisource-analytics.warehouse_layer.warehouse_dim_store` AS
SELECT
    GENERATE_UUID() AS store_sk,
    store_id,
    store_name,
    store_type,
    country,
    city,
    area_sq_m,
    phone_number
FROM `omnisource-analytics.staging_layer.stg_stores`;
