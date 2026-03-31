import requests
import csv
from datetime import datetime, timezone

def fetch_exchange_rates():
    """
    الاتصال بـ API حقيقي لجلب أسعار الصرف.
    نستخدم API مجاني ومفتوح لأغراض التدريب والتطوير.
    """
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    
    try:
        # إرسال طلب GET للخادم
        response = requests.get(url, timeout=10)
        response.raise_for_status() # للتحقق من نجاح الطلب (Status Code 200)
        return response.json() # إرجاع البيانات بصيغة JSON
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching data from API: {e}")
        return None

def main():
    print("🚀 Starting API Integration Pipeline...")
    
    api_data = fetch_exchange_rates()
    
    if not api_data:
        print("Pipeline aborted due to API failure.")
        return

    # العملات التي تهمنا بناءً على دول العملاء في نظامنا
    target_currencies = ['AED', 'SAR', 'EGP', 'GBP', 'QAR', 'KWD', 'EUR', 'BHD']
    
    # استخراج التاريخ من الـ API، أو استخدام توقيت UTC الحالي كبديل
    api_date = api_data.get('date', datetime.now(timezone.utc).strftime('%Y-%m-%d'))
    rates = api_data.get('rates', {})
    
    filename = "api_exchange_rates.csv"
    
    # تحويل بيانات الـ JSON إلى شكل مسطح (Flattening) وحفظها في CSV
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['date', 'currency', 'rate']) # كتابة أسماء الأعمدة (Headers)
        
        for currency in target_currencies:
            if currency in rates:
                # كتابة صف لكل عملة
                writer.writerow([api_date, currency, rates[currency]])
                print(f"Loaded: 1 USD = {rates[currency]} {currency}")
                
    print(f"✅ API data successfully flattened and saved to {filename}")

if __name__ == "__main__":
    main()