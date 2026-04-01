# Advanced Development Plan

## Executive Goal

Evolve the repository from a strong learning-oriented warehouse prototype into a production-grade analytics platform with reliable ingestion, governed modeling, automated testing, orchestration, observability, and BI-ready semantic outputs.

## Phase 1: Foundation Hardening

- Centralize configuration for project ID, dataset names, source paths, and environment selection.
- Standardize Python execution so every ingestion script reads from `data/raw/` and writes predictable outputs.
- Replace hardcoded identifiers with environment-driven configuration.
- Add consistent logging instead of `print`-only operational messages.
- Add a `src/sql/marts/` directory and establish an execution order contract.

## Phase 2: Data Modeling Maturity

- Add missing staging models for customers, products, and orders.
- Introduce a conformed product dimension and ensure fact tables always join on surrogate keys.
- Expand the warehouse to include order, shipping, campaign, store, inventory, and customer lifecycle analytics.
- Decide and document a true SCD strategy for customers, because the current model mimics SCD metadata without historical source snapshots.
- Add semantic marts such as `mart_sales_daily`, `mart_customer_retention`, and `mart_product_performance`.

## Phase 3: Data Quality And Testing

- Add schema tests for uniqueness, non-nullability, accepted values, and referential integrity.
- Add freshness checks for API and scraped data.
- Implement reconciliation tests between raw totals and warehouse totals.
- Create a small synthetic test dataset for deterministic local validation.
- Adopt a framework such as dbt tests, Great Expectations, or custom SQL assertions.

## Phase 4: Orchestration And Deployment

- Introduce orchestration with Airflow, Dagster, or Prefect.
- Define DAG dependencies from ingestion through marts.
- Add CI to lint Python, validate SQL, and run data-quality checks on pull requests.
- Add CD to deploy SQL models and scheduler artifacts to target environments.
- Separate `dev`, `test`, and `prod` BigQuery datasets.

## Phase 5: Observability And Operations

- Add structured run metadata for row counts, load duration, source freshness, and failure reasons.
- Publish operational audit tables such as `ops_pipeline_runs` and `ops_data_quality_results`.
- Add alerting for ingestion failures, abnormal row-count drops, and delayed upstream sources.
- Track data lineage from source file to warehouse table.

## Phase 6: Governance, Security, And Cost Control

- Define data classification for PII columns like email and phone.
- Add column-level security and access roles in BigQuery.
- Partition and cluster large fact tables to optimize cost and query performance.
- Document retention policy for raw snapshots and audit tables.
- Add naming, ownership, and stewardship metadata to all models.

## Recommended Delivery Sequence

1. Configuration layer + requirements + execution guide.
2. Staging completion for all entities and fact/dimension join consistency.
3. Automated tests and CI validation.
4. Orchestration and environment promotion.
5. Observability, governance, and BI semantic mart expansion.

## Highest-Priority Risks To Address

- Hardcoded cloud configuration makes promotion across environments fragile.
- Date parsing in source transactions is inconsistent and must be standardized defensively.
- The current customer dimension implies SCD2 behavior without historical source capture.
- Exchange-rate integration lacks an explicit transaction currency strategy.
- No automated tests currently protect against regressions or broken assumptions.
- New domains such as campaign attribution and web events require agreed business definitions before KPI publication.
