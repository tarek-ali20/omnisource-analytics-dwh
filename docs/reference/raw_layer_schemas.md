# Raw Layer Schemas

This repository now ships with expanded raw datasets designed for more realistic BigQuery loading and profiling.

## Dataset Shape

| Source | Rows | Columns |
| --- | ---: | ---: |
| `customers_master.csv` | 1000 | 20 |
| `campaigns.csv` | 1000 | 20 |
| `stores.csv` | 1000 | 20 |
| `transactions.csv` | 1000 | 23 |
| `scraped_prices_automated.csv` | 1000 | 20 |
| `api_exchange_rates.csv` | 1000 | 20 |
| `inventory_snapshots.csv` | 1000 | 20 |
| `web_events.csv` | 1000 | 20 |
| `operational_db.sqlite.orders` | 1000 | 20 |

## `customers_master.csv`

`customer_id`, `first_name`, `last_name`, `email`, `phone`, `country`, `city`, `registration_date`, `customer_segment`, `status`, `loyalty_tier`, `gender`, `preferred_language`, `acquisition_channel`, `marketing_opt_in`, `credit_score_band`, `birth_date`, `last_login_at`, `avg_order_value`, `lifetime_value`

## `campaigns.csv`

`campaign_id`, `campaign_name`, `platform_name`, `channel_group`, `campaign_objective`, `budget`, `actual_spend`, `start_date`, `end_date`, `target_country`, `target_segment`, `creative_type`, `owner_team`, `agency_name`, `kpi_goal`, `status`, `currency_code`, `impressions_target`, `clicks_target`, `created_at`

## `stores.csv`

`store_id`, `store_name`, `store_type`, `country`, `city`, `district`, `manager_name`, `manager_email`, `phone_number`, `area_sq_m`, `latitude`, `longitude`, `opening_date`, `closing_time`, `opening_time`, `region`, `warehouse_attached_flag`, `rent_cost_monthly`, `staff_count`, `store_status`

## `transactions.csv`

`transaction_id`, `customer_id`, `product_id`, `campaign_id`, `store_id`, `session_id`, `transaction_date`, `quantity`, `price`, `total_amount`, `order_id`, `payment_method`, `currency_code`, `country_code`, `city`, `sales_channel`, `device_type`, `promo_code`, `discount_amount`, `tax_amount`, `shipping_amount`, `fulfillment_status`, `transaction_status`

## `scraped_prices_automated.csv`

`scrape_id`, `product_id`, `sku`, `product_name`, `category`, `brand`, `supplier_name`, `supplier_country`, `price`, `original_price`, `discount_pct`, `currency_code`, `availability_status`, `stock_qty`, `rating`, `review_count`, `scrape_timestamp`, `source_site`, `page_url`, `crawl_region`

## `api_exchange_rates.csv`

`snapshot_id`, `date`, `base_currency`, `currency`, `rate`, `inverse_rate`, `provider`, `rate_type`, `market_region`, `is_weekend`, `effective_from`, `effective_to`, `source_url`, `load_batch_id`, `load_timestamp`, `year`, `month`, `day`, `fx_status`, `volatility_bucket`

## `inventory_snapshots.csv`

`inventory_snapshot_id`, `snapshot_date`, `store_id`, `product_id`, `sku`, `product_name`, `category`, `brand`, `stock_quantity`, `reserved_quantity`, `available_quantity`, `reorder_point`, `safety_stock`, `inbound_quantity`, `outbound_quantity`, `unit_cost`, `inventory_value`, `supplier_name`, `snapshot_timestamp`, `stock_status`

## `web_events.csv`

`event_id`, `session_id`, `customer_id`, `campaign_id`, `store_id`, `product_id`, `event_timestamp`, `event_date`, `event_type`, `page_visited`, `page_category`, `traffic_source`, `device_type`, `browser_name`, `operating_system`, `time_spent_seconds`, `scroll_depth_pct`, `is_conversion`, `order_id`, `revenue_amount`

## `operational_db.sqlite.orders`

`order_id`, `customer_id`, `order_status`, `order_date`, `shipping_cost`, `payment_method`, `shipping_method`, `shipping_country`, `shipping_city`, `billing_country`, `billing_city`, `currency_code`, `subtotal_amount`, `discount_amount`, `tax_amount`, `total_amount`, `item_count`, `priority_flag`, `warehouse_code`, `sales_rep_id`
