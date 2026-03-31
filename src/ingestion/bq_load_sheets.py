from google.cloud import bigquery

def create_sheets_external_table():
    print("🚀 Setting up Live Connection to Google Sheets (Federated Query)...")
    
    project_id = 'omnisource-analytics'
    client = bigquery.Client(project=project_id)
    dataset_id = f"{project_id}.raw_layer"
    table_id = f"{dataset_id}.raw_customers_master"

    # ضع رابط الشيت الخاص بك هنا داخل علامتي التنصيص
    # يجب أن يكون الرابط كاملاً مثل: https://docs.google.com/spreadsheets/d/1abc.../edit
    SHEET_URL = "https://docs.google.com/spreadsheets/d/1i0vD9gAMn8Kl0xAySkoj2LS3P5Cl-kFaB01X5H5XvZg/edit?gid=0#gid=0"

    # إعدادات الجدول الخارجي (External Config)
    external_config = bigquery.ExternalConfig("GOOGLE_SHEETS")
    external_config.source_uris = [SHEET_URL]
    external_config.options.skip_leading_rows = 1  # تجاهل صف العناوين
    external_config.autodetect = True              # اكتشاف أنواع البيانات تلقائياً

    # إنشاء هيكل الجدول وربطه بالإعدادات الخارجية
    table = bigquery.Table(table_id)
    table.external_data_configuration = external_config

    try:
        # تنفيذ أمر إنشاء الجدول
        table = client.create_table(table, exists_ok=True)
        print(f"✅ Success! Live link established.")
        print(f"🔗 External Table created: {table.table_id}")
    except Exception as e:
        print(f"❌ Error creating external table: {e}")

if __name__ == "__main__":
    create_sheets_external_table()