CREATE OR REPLACE TABLE `omnisource-analytics.warehouse_layer.warehouse_dim_customer` AS
SELECT
    -- 1. Surrogate Key
    GENERATE_UUID() AS customer_sk,
    
    -- 2. Natural Key (تحويل آمن لنص قبل القص)
    TRIM(CAST(customer_id AS STRING)) AS customer_id,
    
    -- 3. دمج الاسم الأول والأخير
    INITCAP(CONCAT(TRIM(CAST(first_name AS STRING)), ' ', TRIM(CAST(last_name AS STRING)))) AS customer_name,
    
    -- 4. SCD Type 1 Attributes
    LOWER(TRIM(CAST(email AS STRING))) AS email,
    TRIM(CAST(phone AS STRING)) AS phone_number,
    TRIM(CAST(customer_segment AS STRING)) AS customer_segment,
    
    -- 5. SCD Type 2 Attributes
    UPPER(TRIM(CAST(country AS STRING))) AS country,
    INITCAP(TRIM(CAST(city AS STRING))) AS city,
    TRIM(CAST(status AS STRING)) AS account_status,
    
    -- 6. SCD Type 2 Metadata
    CURRENT_DATE() AS valid_from,
    CAST('9999-12-31' AS DATE) AS valid_to,
    TRUE AS is_current

FROM
    `omnisource-analytics.raw_layer.raw_customers_master`
WHERE
    customer_id IS NOT NULL;