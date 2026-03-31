CREATE OR REPLACE VIEW `omnisource-analytics.staging_layer.stg_transactions` AS
SELECT
    -- 1. تنظيف المعرفات 
    TRIM(transaction_id) AS transaction_id,
    TRIM(customer_id) AS customer_id,
    TRIM(product_id) AS product_id,

    -- 2. تحويل التواريخ 
    CAST(transaction_date AS DATE) AS transaction_date,

    -- 3. حماية الأرقام 
    ABS(CAST(quantity AS INT64)) AS quantity,
    ABS(CAST(price AS FLOAT64)) AS unit_price,

    -- 4. مصدر واحد للحقيقة (SSOT)
    ROUND(ABS(CAST(quantity AS INT64)) * ABS(CAST(price AS FLOAT64)), 2) AS calculated_total_amount,

    -- 5. علم الجودة (Data Quality Flag)
    CASE 
        WHEN ABS(CAST(total_amount AS FLOAT64)) != ROUND(ABS(CAST(quantity AS INT64)) * ABS(CAST(price AS FLOAT64)), 2) 
        THEN 'Mismatch - Needs Review' 
        ELSE 'Correct' 
    END AS data_quality_status

FROM
    `omnisource-analytics.raw_layer.raw_transactions`
WHERE
    transaction_id IS NOT NULL;