CREATE OR REPLACE VIEW `omnisource-analytics.staging_layer.stg_exchange_rates` AS
WITH deduplicated_rates AS (
    SELECT
        SAFE_CAST(date AS DATE) AS exchange_date,
        UPPER(TRIM(currency)) AS currency_code,
        ABS(SAFE_CAST(rate AS FLOAT64)) AS exchange_rate,
        ROW_NUMBER() OVER (
            PARTITION BY SAFE_CAST(date AS DATE), UPPER(TRIM(currency))
            ORDER BY SAFE_CAST(rate AS FLOAT64) DESC
        ) AS row_num
    FROM `omnisource-analytics.raw_layer.raw_exchange_rates`
    WHERE rate IS NOT NULL
      AND currency IS NOT NULL
)
SELECT
    exchange_date,
    currency_code,
    exchange_rate
FROM deduplicated_rates
WHERE row_num = 1
  AND exchange_date IS NOT NULL
  AND exchange_rate IS NOT NULL;
