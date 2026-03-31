import sqlite3
import random
from datetime import datetime, timedelta

def create_operational_db():
    print("🚀 Simulating Operational Database (PostgreSQL Alternative)...")
    
    # سيقوم هذا الأمر بإنشاء ملف قاعدة البيانات في نفس المجلد
    conn = sqlite3.connect('operational_db.sqlite')
    cursor = conn.cursor()

    # إنشاء جدول الطلبات (Orders Table)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        order_id TEXT PRIMARY KEY,
        customer_id TEXT,
        order_status TEXT,
        order_date TEXT,
        shipping_cost REAL
    )
    ''')

    # مسح البيانات القديمة لو قمت بتشغيل السكريبت أكثر من مرة
    cursor.execute('DELETE FROM orders')

    # قائمة العملاء (نفس الـ IDs الموجودة في جدول العملاء للحفاظ على التكامل المرجعي)
    customers = [f"C{str(i).zfill(3)}" for i in range(1, 16)]
    statuses = ['Completed', 'Completed', 'Completed', 'Cancelled'] # جعلنا الأغلبية مكتملة

    # توليد 30 طلب وهمي
    orders_data = []
    base_date = datetime(2023, 1, 1)

    for i in range(1, 31):
        order_id = f"ORD-{str(i).zfill(4)}"
        customer_id = random.choice(customers)
        status = random.choice(statuses)
        
        # تواريخ عشوائية خلال السنتين الماضيتين
        random_days = random.randint(0, 400)
        order_date = (base_date + timedelta(days=random_days)).strftime('%Y-%m-%d')
        
        shipping_cost = round(random.uniform(10.0, 50.0), 2)

        orders_data.append((order_id, customer_id, status, order_date, shipping_cost))

    # إدخال البيانات في الجدول
    cursor.executemany('''
    INSERT INTO orders (order_id, customer_id, order_status, order_date, shipping_cost)
    VALUES (?, ?, ?, ?, ?)
    ''', orders_data)

    # حفظ التغييرات وإغلاق الاتصال
    conn.commit()
    conn.close()

    print("✅ Operational DB created successfully! File saved as 'operational_db.sqlite'")

if __name__ == "__main__":
    create_operational_db()