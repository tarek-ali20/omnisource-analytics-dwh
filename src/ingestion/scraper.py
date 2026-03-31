import csv
import random
from datetime import datetime, timezone
import time

# 1. قائمة المنتجات الخاصة بنا (نفس الموجودة في جدول المبيعات)
PRODUCTS = [
    {"id": "P101", "name": "Wireless Mouse", "base_price": 50.0},
    {"id": "P102", "name": "Mechanical Keyboard", "base_price": 200.0},
    {"id": "P103", "name": "USB-C Hub", "base_price": 30.0},
    {"id": "P104", "name": "Laptop Stand", "base_price": 150.0},
    {"id": "P105", "name": "27-inch Monitor", "base_price": 500.0}
]

def simulate_scraping_api(product):
    """
    تحاكي هذه الدالة عملية الـ Scraping. 
    في الواقع، هنا نضع كود (requests.get) لجلب السعر من الموقع.
    نضيف تغيراً طفيفاً في السعر لمحاكاة تقلبات السوق.
    """
    fluctuation = random.uniform(-0.05, 0.05) # تذبذب السعر بنسبة 5% زيادة أو نقص
    current_price = round(product["base_price"] * (1 + fluctuation), 2)
    
    # استخدام التوقيت العالمي (UTC) المعيار الأهم في هندسة البيانات
    timestamp = datetime.now(timezone.utc).isoformat() 
    
    return {
        "product_id": product["id"],
        "product_name": product["name"],
        "price": current_price,
        "scrape_timestamp": timestamp
    }

def main():
    filename = "scraped_prices_automated.csv"
    
    print("🚀 Starting Web Scraping Pipeline...")
    
    # تجهيز الملف لتبدأ الكتابة فيه
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["product_id", "product_name", "price", "scrape_timestamp"])
        writer.writeheader()
        
        # محاكاة سحب البيانات للمنتجات
        for product in PRODUCTS:
            print(f"Scraping data for {product['name']}...")
            scraped_data = simulate_scraping_api(product)
            writer.writerow(scraped_data)
            
            # محاكاة وقت الانتظار لتجنب حظر الـ IP (Polite Scraping)
            time.sleep(1) 
            
    print(f"✅ Scraping completed successfully! Data saved to {filename}")

if __name__ == "__main__":
    main()