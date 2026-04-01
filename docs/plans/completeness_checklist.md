# Completeness Checklist

## What Is Already Strong

- Multi-source raw layer with realistic linked datasets.
- Staging layer covering core commerce entities.
- Warehouse dimensions and facts for sales, web, inventory, store, and campaign analysis.
- First Power BI-ready marts for sales performance and customer 360.

## What Still Prevents "Full" Completion

- BigQuery runtime validation for every dimension, fact, and mart query.
- A third mart focused on either inventory health or marketing ROI.
- Data-quality tests for nulls, duplicates, and referential integrity.
- Environment-driven configuration instead of hardcoded project and dataset names.
- Orchestration for repeatable end-to-end runs.
- KPI definitions approved by business stakeholders.
- Documentation of dashboard questions, grain, and refresh logic.

## Marketing ROI Mart

`mart_marketing_roi` is now part of the recommended mart layer because it closes
the loop between campaign spend and realized sales conversions.

## Recommended SQL Scope After This

1. Validate all current SQL on BigQuery.
2. Validate `mart_marketing_roi`.
3. Add test queries for row-count and join-quality checks.
4. Add a runbook for execution order from raw to marts.
