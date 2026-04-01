# Architecture Layers

## Layered View

```text
[ Data Sources ]
        |
        v
[ Ingestion Layer ]
        |
        v
[ Raw Layer in BigQuery ]
        |
        v
[ Staging Layer ]
        |
        v
[ Warehouse Layer ]
        |
        v
[ Mart Layer ]
        |
        v
[ BI / Power BI ]
```

## Layer Responsibilities

- Data Sources: CSV, Google Sheets, SQLite, API, and scraped source outputs.
- Ingestion Layer: Python scripts that extract, simulate, and load data.
- Raw Layer: landing zone for source-shaped tables with minimal transformation.
- Staging Layer: type standardization, deduplication, cleansing, and quality flags.
- Warehouse Layer: dimensional models based on star-schema design.
- Mart Layer: future business-facing aggregated models.
- BI Layer: dashboards, KPIs, and reporting consumption.
