CREATE OR REPLACE TABLE `omnisource-analytics.warehouse_layer.warehouse_dim_date` AS
WITH date_spine AS (
  SELECT date_day
  FROM UNNEST(GENERATE_DATE_ARRAY(DATE('2020-01-01'), DATE('2030-12-31'), INTERVAL 1 DAY)) AS date_day
)
SELECT
  CAST(FORMAT_DATE('%Y%m%d', date_day) AS INT64) AS date_key,
  date_day AS full_date,
  EXTRACT(YEAR FROM date_day) AS year,
  EXTRACT(QUARTER FROM date_day) AS quarter,
  EXTRACT(MONTH FROM date_day) AS month,
  FORMAT_DATE('%B', date_day) AS month_name,
  EXTRACT(WEEK FROM date_day) AS week_of_year,
  EXTRACT(DAY FROM date_day) AS day_of_month,
  EXTRACT(DAYOFWEEK FROM date_day) AS day_of_week,
  FORMAT_DATE('%A', date_day) AS day_name,
  CASE 
    WHEN EXTRACT(DAYOFWEEK FROM date_day) IN (6, 7) THEN TRUE 
    ELSE FALSE 
  END AS is_weekend,
  CONCAT(CAST(EXTRACT(YEAR FROM date_day) AS STRING), '-Q', CAST(EXTRACT(QUARTER FROM date_day) AS STRING)) AS year_quarter
FROM date_spine;