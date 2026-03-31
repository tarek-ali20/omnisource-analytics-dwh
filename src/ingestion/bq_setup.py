from google.cloud import bigquery
from google.cloud.exceptions import NotFound

def setup_raw_layer():
    print("🚀 Initializing BigQuery Connection...")
    
    # السحر هنا: بايثون سيتعرف تلقائياً على حسابك بفضل الـ gcloud CLI الذي استخدمته
    # فقط تأكد من استبدال 'omnisource-analytics' بـ Project ID الخاص بك إذا كان مختلفاً
    project_id = 'omnisource-analytics' 
    client = bigquery.Client(project=project_id)
    
    # اسم الـ Dataset الذي سننشئه
    dataset_id = f"{project_id}.raw_layer"
    
    print(f"🎯 Target Dataset: {dataset_id}")
    
    try:
        # محاولة التحقق مما إذا كان الـ Dataset موجوداً بالفعل
        client.get_dataset(dataset_id)
        print("✅ Dataset 'raw_layer' already exists. We are good to go!")
        
    except NotFound:
        # إذا لم يكن موجوداً، سنقوم بإنشائه
        print("⚠️ Dataset not found. Creating 'raw_layer' now...")
        
        # إعداد خصائص الـ Dataset
        dataset = bigquery.Dataset(dataset_id)
        dataset.location = "US" # نختار منطقة السيرفرات (المعيار الأمريكي هو الأرخص للتدريب)
        
        # تنفيذ أمر الإنشاء
        dataset = client.create_dataset(dataset, timeout=30)
        print(f"✅ Successfully created dataset: {dataset.dataset_id} in {dataset.location}")

if __name__ == "__main__":
    setup_raw_layer()