# BigQuery Readiness Warnings

## Runtime Syntax Risk

Local review alone does not guarantee that the SQL models will run successfully in BigQuery Standard SQL. Small issues such as table-path mismatches, unsupported expressions, or minor syntax mistakes can remain invisible until cloud execution.

## Required Validation Before Production Claims

1. Run every SQL model directly in BigQuery.
2. Verify dataset and table paths in the target GCP project.
3. Confirm BigQuery type inference after loading the widened raw datasets.
4. Spot-check joins and row counts between raw, staging, and warehouse layers.
5. Capture failures and adjust SQL before any production label is used.

## Mart Design Warning

Do not build the `mart` layer only because the warehouse is ready. The marts should be derived from explicit Power BI questions, approved KPI logic, grain definitions, and dashboard performance requirements. Otherwise, there is a high risk of building aggregates that nobody uses.
