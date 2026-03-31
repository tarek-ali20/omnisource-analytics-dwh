CREATE OR REPLACE VIEW `omnisource-analytics.staging_layer.stg_exchange_rates` AS
WITH deduplicated_rates AS (
    SELECT 
        -- 1. توحيد التواريخ
        CAST(date AS DATE) AS exchange_date,
        
        -- 2. توحيد رموز العملات
        UPPER(TRIM(currency)) AS currency_code,
        
        -- 3. تأمين الأرقام
        ABS(CAST(rate AS FLOAT64)) AS exchange_rate,
        
        -- 4. منع التكرار (Deduplication)
        ROW_NUMBER() OVER(PARTITION BY CAST(date AS DATE), UPPER(TRIM(currency)) ORDER BY rate DESC) AS row_num

    FROM 
        `omnisource-analytics.raw_layer.raw_exchange_rates`
    WHERE 
        rate IS NOT NULL 
        AND currency IS NOT NULL
)

-- 5. استخراج النسخة النظيفة والفريدة فقط
SELECT 
    exchange_date,
    currency_code,
    exchange_rate
FROM 
    deduplicated_rates
WHERE 
    row_num = 1;