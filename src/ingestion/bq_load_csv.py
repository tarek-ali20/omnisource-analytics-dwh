from google.cloud import bigquery
import os
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT_DIR / "data" / "raw"

def load_csv_to_bq():
    print("🚀 Starting Batch Load to BigQuery Raw Layer...")
    
    # تهيئة الاتصال بالسحابة (سيستخدم هويتك المخفية تلقائياً)
    project_id = 'omnisource-analytics' # تأكد أن هذا هو الـ Project ID الخاص بك
    client = bigquery.Client(project=project_id)
    dataset_id = f"{project_id}.raw_layer"

    # قاموس يربط اسم الملف المحلي باسم الجدول الذي سيتم إنشاؤه في BigQuery
    files_to_load = {
        RAW_DIR / 'transactions.csv': 'raw_transactions',
        RAW_DIR / 'scraped_prices_automated.csv': 'raw_scraped_prices',
        RAW_DIR / 'api_exchange_rates.csv': 'raw_exchange_rates',
        RAW_DIR / 'customers_master.csv': 'raw_customers_master',
        RAW_DIR / 'campaigns.csv': 'raw_campaigns',
        RAW_DIR / 'stores.csv': 'raw_stores',
        RAW_DIR / 'inventory_snapshots.csv': 'raw_inventory_snapshots',
        RAW_DIR / 'web_events.csv': 'raw_web_events'
    }

    # إعدادات وظيفة الرفع (Job Configuration)
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1, # تجاهل الصف الأول لأنه يحتوي على أسماء الأعمدة
        autodetect=True,     # دع BigQuery يكتشف نوع البيانات (نص، رقم، تاريخ) تلقائياً
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE # لو الجدول موجود، قم بمسحه ووضع البيانات الجديدة
    )

    for filepath, table_name in files_to_load.items():
        table_id = f"{dataset_id}.{table_name}"
        
        # التأكد من أن الملف موجود على جهازك قبل محاولة رفعه
        if not os.path.exists(filepath):
            print(f"⚠️ File '{filepath}' not found in the raw directory. Skipping...")
            continue
            
        print(f"⏳ Uploading '{filepath.name}' to BigQuery table '{table_name}'...")
        
        # فتح الملف ورفعه للسحابة
        with open(filepath, "rb") as source_file:
            job = client.load_table_from_file(source_file, table_id, job_config=job_config)
        
        job.result()  # انتظار اكتمال عملية الرفع
        
        # التحقق من عدد الصفوف التي تم رفعها بنجاح
        table = client.get_table(table_id)
        print(f"✅ Success! Loaded {table.num_rows} rows into {table_name}.")

    print("🎉 All CSV files processed successfully!")

if __name__ == "__main__":
    load_csv_to_bq()
