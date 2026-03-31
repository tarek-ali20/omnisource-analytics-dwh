from google.cloud import bigquery
import os

def load_csv_to_bq():
    print("🚀 Starting Batch Load to BigQuery Raw Layer...")
    
    # تهيئة الاتصال بالسحابة (سيستخدم هويتك المخفية تلقائياً)
    project_id = 'omnisource-analytics' # تأكد أن هذا هو الـ Project ID الخاص بك
    client = bigquery.Client(project=project_id)
    dataset_id = f"{project_id}.raw_layer"

    # قاموس يربط اسم الملف المحلي باسم الجدول الذي سيتم إنشاؤه في BigQuery
    files_to_load = {
        'transactions.csv': 'raw_transactions',
        'scraped_prices_automated.csv': 'raw_scraped_prices',
        'api_exchange_rates.csv': 'raw_exchange_rates',
        'customers_master.csv': 'raw_customers_master' # <== السطر الجديد
    }

    # إعدادات وظيفة الرفع (Job Configuration)
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1, # تجاهل الصف الأول لأنه يحتوي على أسماء الأعمدة
        autodetect=True,     # دع BigQuery يكتشف نوع البيانات (نص، رقم، تاريخ) تلقائياً
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE # لو الجدول موجود، قم بمسحه ووضع البيانات الجديدة
    )

    for filename, table_name in files_to_load.items():
        table_id = f"{dataset_id}.{table_name}"
        
        # التأكد من أن الملف موجود على جهازك قبل محاولة رفعه
        if not os.path.exists(filename):
            print(f"⚠️ File '{filename}' not found in the directory. Skipping...")
            continue
            
        print(f"⏳ Uploading '{filename}' to BigQuery table '{table_name}'...")
        
        # فتح الملف ورفعه للسحابة
        with open(filename, "rb") as source_file:
            job = client.load_table_from_file(source_file, table_id, job_config=job_config)
        
        job.result()  # انتظار اكتمال عملية الرفع
        
        # التحقق من عدد الصفوف التي تم رفعها بنجاح
        table = client.get_table(table_id)
        print(f"✅ Success! Loaded {table.num_rows} rows into {table_name}.")

    print("🎉 All CSV files processed successfully!")

if __name__ == "__main__":
    load_csv_to_bq()