# OmniSource Analytics DWH 🚀

## 📌 Comprehensive Project Overview
The **OmniSource Analytics DWH** is a robust, end-to-end Data Engineering and Analytics Engineering solution designed to unify fragmented business data into a single, reliable source of truth (SSOT). 

Built with scalability and data quality in mind, this project demonstrates the complete lifecycle of modern data architecture, bridging the gap between raw data generation and business intelligence (BI) consumption.

### 🚀 Core Achievements & Technical Scope:
* **Multi-Source Data Ingestion (EL):** Engineered automated Python pipelines utilizing pandas and google-cloud-bigquery to extract data from diverse sources (CSV, SQLite, Google Sheets).
* **Cloud Security Best Practices:** Implemented zero-hardcoded-credentials architecture using Google Cloud Application Default Credentials (ADC).
* **Idempotent Data Loading:** Configured BigQuery load jobs with WRITE_TRUNCATE to guarantee pipeline idempotency and prevent data duplication.
* **Advanced SQL Transformations (Staging Layer):** Developed dynamic BigQuery VIEWS to act as a staging and cleansing layer applying defensive SQL techniques (Data Typing, Cleansing, Automated Quality Checks).
* **BI-Ready Architecture:** Set the foundational groundwork for a highly optimized Data Warehouse using Kimball's dimensional modeling (Star Schema), engineered specifically to maximize performance in BI tools like Power BI.
