# Data Dictionary

## Raw Layer

### `raw_transactions`

| Column | Type | Description |
| --- | --- | --- |
| `transaction_id` | STRING | Original transaction identifier |
| `customer_id` | STRING | Source customer identifier |
| `product_id` | STRING | Source product identifier |
| `transaction_date` | STRING/DATE | Source transaction date before standardization |
| `quantity` | INTEGER | Purchased quantity |
| `price` | FLOAT | Unit price from source |
| `total_amount` | FLOAT | Source-supplied total amount |

### `raw_customers_master`

| Column | Type | Description |
| --- | --- | --- |
| `customer_id` | STRING | Source customer identifier |
| `first_name` | STRING | Customer first name |
| `last_name` | STRING | Customer last name |
| `email` | STRING | Customer email |
| `phone` | STRING | Customer phone number |
| `country` | STRING | Customer country |
| `city` | STRING | Customer city |
| `registration_date` | DATE/STRING | Registration date |
| `customer_segment` | STRING | Business segmentation label |
| `status` | STRING | Customer account status |

### `raw_scraped_prices`

| Column | Type | Description |
| --- | --- | --- |
| `product_id` | STRING | Product identifier |
| `product_name` | STRING | Product display name |
| `price` | FLOAT | Scraped market price |
| `scrape_timestamp` | TIMESTAMP/STRING | Scrape execution time |

### `raw_exchange_rates`

| Column | Type | Description |
| --- | --- | --- |
| `date` | DATE/STRING | Exchange-rate snapshot date |
| `currency` | STRING | Currency code |
| `rate` | FLOAT | Rate returned by the upstream API |

### `raw_orders`

| Column | Type | Description |
| --- | --- | --- |
| `order_id` | STRING | Operational order identifier |
| `customer_id` | STRING | Customer identifier |
| `order_status` | STRING | Order status |
| `order_date` | DATE/STRING | Order date |
| `shipping_cost` | FLOAT | Shipping cost amount |

## Staging Layer

### `stg_transactions`

| Column | Type | Description |
| --- | --- | --- |
| `transaction_id` | STRING | Cleaned transaction identifier |
| `customer_id` | STRING | Cleaned customer identifier |
| `product_id` | STRING | Cleaned product identifier |
| `transaction_date` | DATE | Standardized transaction date |
| `quantity` | INT64 | Absolute quantity |
| `unit_price` | FLOAT64 | Absolute unit price |
| `calculated_total_amount` | FLOAT64 | Recalculated amount from quantity x unit price |
| `data_quality_status` | STRING | Quality result flag |

### `stg_exchange_rates`

| Column | Type | Description |
| --- | --- | --- |
| `exchange_date` | DATE | Standardized exchange-rate date |
| `currency_code` | STRING | Cleaned currency code |
| `exchange_rate` | FLOAT64 | Validated exchange rate |

## Warehouse Layer

### `warehouse_dim_customer`

| Column | Type | Description | Key Type |
| --- | --- | --- | --- |
| `customer_sk` | STRING | Surrogate customer key | Primary Key |
| `customer_id` | STRING | Natural customer identifier | Natural Key |
| `customer_name` | STRING | Combined customer full name | Attribute |
| `email` | STRING | Standardized email | Attribute |
| `phone_number` | STRING | Standardized phone number | Attribute |
| `customer_segment` | STRING | Customer segment | Attribute |
| `country` | STRING | Country | Attribute |
| `city` | STRING | City | Attribute |
| `account_status` | STRING | Current account status | Attribute |
| `valid_from` | DATE | SCD validity start | Metadata |
| `valid_to` | DATE | SCD validity end | Metadata |
| `is_current` | BOOL | Current-record indicator | Metadata |

### `warehouse_dim_product`

| Column | Type | Description | Key Type |
| --- | --- | --- | --- |
| `product_sk` | STRING | Surrogate product key | Primary Key |
| `product_id` | STRING | Natural product identifier | Natural Key |
| `product_name` | STRING | Latest known product name | Attribute |
| `product_source` | STRING | Product master source | Attribute |

### `warehouse_dim_date`

| Column | Type | Description | Key Type |
| --- | --- | --- | --- |
| `date_key` | INT64 | Calendar key in `YYYYMMDD` format | Primary Key |
| `full_date` | DATE | Calendar date | Natural Key |
| `year` | INT64 | Calendar year | Attribute |
| `quarter` | INT64 | Quarter number | Attribute |
| `month` | INT64 | Month number | Attribute |
| `month_name` | STRING | Month name | Attribute |
| `week_of_year` | INT64 | Week indicator | Attribute |
| `day_of_month` | INT64 | Day of month | Attribute |
| `day_of_week` | INT64 | Day-of-week number | Attribute |
| `day_name` | STRING | Day name | Attribute |
| `is_weekend` | BOOL | Weekend flag | Attribute |
| `year_quarter` | STRING | Year and quarter label | Attribute |

### `warehouse_fact_transactions`

| Column | Type | Description | Key Type |
| --- | --- | --- | --- |
| `date_key` | INT64 | Foreign key to date dimension | Foreign Key |
| `customer_sk` | STRING | Foreign key to customer dimension | Foreign Key |
| `product_sk` | STRING | Foreign key to product dimension | Foreign Key |
| `transaction_id` | STRING | Source transaction identifier | Degenerate Dimension |
| `quantity` | INT64 | Quantity sold | Fact |
| `unit_price` | FLOAT64 | Unit price at transaction time | Fact |
| `calculated_total_amount` | FLOAT64 | Trusted transaction amount | Fact |
