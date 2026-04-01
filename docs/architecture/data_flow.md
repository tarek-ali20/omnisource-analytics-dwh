# Data Flow

## Source To Warehouse Flow

- Google Sheets customer master data -> Python external-table setup -> `raw_customers_master`
- CSV transactions -> Python batch load -> `raw_transactions`
- Scraped product prices -> Python simulation output -> `raw_scraped_prices`
- Exchange-rate API -> Python API extraction -> `raw_exchange_rates`
- SQLite operational orders -> Python extraction -> `raw_orders`

## Transformation Path

```text
raw_* -> staging_* -> warehouse_* -> mart_* -> Power BI
```

## Design Intent

- Keep the raw layer close to source shape.
- Use staging for defensive SQL and data-quality enforcement.
- Build warehouse tables as stable, analytics-ready dimensional entities.
- Add marts later for KPI-specific and dashboard-optimized consumption.
