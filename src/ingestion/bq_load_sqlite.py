import sqlite3
import pandas as pd
from google.cloud import bigquery
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[2]
RAW_DB_PATH = ROOT_DIR / "data" / "raw" / "operational_db.sqlite"

def load_sqlite_to_bq():
    print("🚀 Starting Database Extraction (SQLite -> BigQuery)...")
    
    # الخطوة الأولى: الاتصال بقاعدة البيانات المحلية
    db_file = RAW_DB_PATH
    
    try:
        conn = sqlite3.connect(db_file)
        
        # استخراج البيانات باستخدام استعلام SQL وتحويلها فوراً إلى DataFrame في الذاكرة
        query = "SELECT * FROM orders"
        df = pd.read_sql_query(query, conn)
        conn.close()
        
        print(f"📦 Extracted {len(df)} rows from local operational database.")
        
    except Exception as e:
        print(f"❌ Error reading from SQLite: {e}")
        return

    # الخطوة الثانية: الاتصال بالسحابة (BigQuery)
    project_id = 'omnisource-analytics' # تأكد من اسم مشروعك
    client = bigquery.Client(project=project_id)
    table_id = f"{project_id}.raw_layer.raw_orders"

    # إعدادات الرفع
    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE", # مسح البيانات القديمة إن وجدت وكتابة الجديدة
    )

    print(f"⏳ Streaming DataFrame to BigQuery table 'raw_orders'...")
    
    # الخطوة الثالثة: رفع الـ DataFrame مباشرة إلى BigQuery
    try:
        job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
        job.result()  # انتظار اكتمال العملية
        
        table = client.get_table(table_id)
        print(f"✅ Success! Loaded {table.num_rows} rows into raw_orders.")
        
    except Exception as e:
        print(f"❌ Error uploading to BigQuery: {e}")

if __name__ == "__main__":
    load_sqlite_to_bq()
