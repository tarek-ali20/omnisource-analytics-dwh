-- Dimension model: product
-- Purpose:
-- Build the product dimension from scraped raw data, keeping the latest known
-- product name per product_id.
-- BigQuery execution target:
-- `omnisource-analytics.warehouse_layer.warehouse_dim_product`

CREATE OR REPLACE TABLE `omnisource-analytics.warehouse_layer.warehouse_dim_product` AS
WITH ranked_products AS (
    SELECT
        CAST(product_id AS STRING) AS product_id,
        TRIM(product_name) AS product_name,
        ROW_NUMBER() OVER(PARTITION BY product_id ORDER BY scrape_timestamp DESC) AS rn
    FROM `omnisource-analytics.raw_layer.raw_scraped_prices`
    WHERE product_id IS NOT NULL
)
SELECT
    GENERATE_UUID() AS product_sk,
    product_id,
    product_name,
    'Scraped' AS product_source
FROM ranked_products
WHERE rn = 1;
