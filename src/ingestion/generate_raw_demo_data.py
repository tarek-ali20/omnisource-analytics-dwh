import csv
import random
import sqlite3
from datetime import date, datetime, timedelta, timezone
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT_DIR / "data" / "raw"
CUSTOMER_COUNT = 1000
TRANSACTION_COUNT = 1000
ORDER_COUNT = 1000
PRICE_SNAPSHOT_COUNT = 1000
FX_ROW_COUNT = 1000
SEED = 42


FIRST_NAMES = [
    "Ahmed", "Sara", "John", "Fatima", "Omar", "Lina", "Mona", "Yousef", "Noor", "Ali",
    "Mariam", "Hassan", "Layla", "David", "Ethan", "Sophia", "Zain", "Leen", "Khalid", "Ava",
]
LAST_NAMES = [
    "Ali", "Khalid", "Smith", "Hassan", "Brown", "Johnson", "Mansour", "Saleh", "Miller", "Clark",
    "Wilson", "Taylor", "Thomas", "Martin", "Anderson", "White", "Moore", "Young", "Hill", "King",
]
COUNTRY_CITY = {
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah"],
    "KSA": ["Riyadh", "Jeddah", "Dammam"],
    "Egypt": ["Cairo", "Alexandria", "Giza"],
    "USA": ["New York", "Chicago", "Austin"],
    "UK": ["London", "Manchester", "Birmingham"],
    "Qatar": ["Doha", "Al Rayyan"],
    "Kuwait": ["Kuwait City", "Hawalli"],
    "Bahrain": ["Manama", "Riffa"],
}
SEGMENTS = ["Basic", "Premium", "VIP", "Enterprise"]
STATUSES = ["Active", "Active", "Active", "Inactive", "Suspended"]
LANGUAGES = ["Arabic", "English", "Bilingual"]
CHANNELS = ["Organic", "Paid Search", "Referral", "Partner", "Social Media", "Direct"]
LOYALTY_TIERS = ["Bronze", "Silver", "Gold", "Platinum"]
GENDERS = ["Male", "Female"]
PRODUCTS = [
    ("P101", "Wireless Mouse", "Accessories", "LogiTech", "SKU-P101"),
    ("P102", "Mechanical Keyboard", "Accessories", "KeyCraft", "SKU-P102"),
    ("P103", "USB-C Hub", "Connectivity", "DockPro", "SKU-P103"),
    ("P104", "Laptop Stand", "Office", "ErgoLift", "SKU-P104"),
    ("P105", "27-inch Monitor", "Displays", "VisionTech", "SKU-P105"),
    ("P106", "Noise-Cancelling Headset", "Audio", "SoundPeak", "SKU-P106"),
    ("P107", "Webcam 4K", "Video", "ClearView", "SKU-P107"),
    ("P108", "Portable SSD 1TB", "Storage", "FlashCore", "SKU-P108"),
    ("P109", "Desk Lamp", "Office", "BrightNest", "SKU-P109"),
    ("P110", "Tablet Stand", "Accessories", "FlexMount", "SKU-P110"),
]
CAMPAIGNS = [
    ("CMP-001", "Google Ads", "Search", "Acquisition"),
    ("CMP-002", "Meta Ads", "Social", "Acquisition"),
    ("CMP-003", "TikTok Ads", "Social", "Awareness"),
    ("CMP-004", "LinkedIn Ads", "B2B", "Lead Generation"),
    ("CMP-005", "Email Nurture", "CRM", "Retention"),
    ("CMP-006", "Affiliate Network", "Partner", "Acquisition"),
]
STORES = [
    ("STR-001", "Dubai Mall Flagship", "UAE", "Dubai"),
    ("STR-002", "Mall of the Emirates", "UAE", "Dubai"),
    ("STR-003", "Riyadh Park", "KSA", "Riyadh"),
    ("STR-004", "Cairo Festival City", "Egypt", "Cairo"),
    ("STR-005", "Doha Festival City", "Qatar", "Doha"),
    ("STR-006", "Kuwait Avenues", "Kuwait", "Kuwait City"),
]
PAYMENT_METHODS = ["Credit Card", "Apple Pay", "Google Pay", "Bank Transfer", "Cash"]
ORDER_STATUSES = ["Completed", "Completed", "Processing", "Shipped", "Cancelled", "Returned"]
TRANSACTION_STATUSES = ["Completed", "Completed", "Completed", "Refunded", "Pending"]
FULFILLMENT_STATUSES = ["Delivered", "Packed", "In Transit", "Returned"]
SHIPPING_METHODS = ["Standard", "Express", "Same Day"]
WAREHOUSE_CODES = ["WH-DXB", "WH-RUH", "WH-CAI", "WH-NYC"]
SALES_REPS = ["SR-101", "SR-102", "SR-103", "SR-104", "SR-105"]
SUPPLIERS = ["Alpha Supply", "Delta Trade", "Vertex Global", "Prime Distribution"]
SOURCE_SITES = ["shop-alpha.example", "shop-beta.example", "shop-gamma.example"]
FX_CURRENCIES = ["AED", "SAR", "EGP", "GBP", "QAR", "KWD", "EUR", "BHD"]
FX_BASE_RATES = {
    "AED": 3.67,
    "SAR": 3.75,
    "EGP": 50.10,
    "GBP": 0.79,
    "QAR": 3.64,
    "KWD": 0.31,
    "EUR": 0.92,
    "BHD": 0.38,
}


def daterange(start: date, count: int):
    for offset in range(count):
        yield start + timedelta(days=offset)


def ensure_raw_dir():
    RAW_DIR.mkdir(parents=True, exist_ok=True)


def build_customers():
    rows = []
    for idx in range(1, CUSTOMER_COUNT + 1):
        customer_id = f"C{idx:04d}"
        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)
        country = random.choice(list(COUNTRY_CITY.keys()))
        city = random.choice(COUNTRY_CITY[country])
        registration_date = date(2021, 1, 1) + timedelta(days=random.randint(0, 1500))
        last_login_at = datetime(2024, 1, 1, tzinfo=timezone.utc) + timedelta(
            days=random.randint(0, 720),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59),
        )
        avg_order_value = round(random.uniform(40, 1200), 2)
        lifetime_value = round(avg_order_value * random.randint(2, 30), 2)
        rows.append({
            "customer_id": customer_id,
            "first_name": first_name,
            "last_name": last_name,
            "email": f"{first_name.lower()}.{last_name.lower()}{idx}@example.com",
            "phone": f"+9715{random.randint(10000000, 99999999)}",
            "country": country,
            "city": city,
            "registration_date": registration_date.isoformat(),
            "customer_segment": random.choice(SEGMENTS),
            "status": random.choice(STATUSES),
            "loyalty_tier": random.choice(LOYALTY_TIERS),
            "gender": random.choice(GENDERS),
            "preferred_language": random.choice(LANGUAGES),
            "acquisition_channel": random.choice(CHANNELS),
            "marketing_opt_in": random.choice(["true", "false"]),
            "credit_score_band": random.choice(["Low", "Medium", "High"]),
            "birth_date": (date(1975, 1, 1) + timedelta(days=random.randint(0, 12000))).isoformat(),
            "last_login_at": last_login_at.isoformat(),
            "avg_order_value": f"{avg_order_value:.2f}",
            "lifetime_value": f"{lifetime_value:.2f}",
        })
    return rows


def build_transactions(customers):
    rows = []
    start_date = date(2022, 1, 1)
    for idx in range(1, TRANSACTION_COUNT + 1):
        customer = random.choice(customers)
        product_id, _, _, _, _ = random.choice(PRODUCTS)
        campaign_id, _, _, _ = random.choice(CAMPAIGNS)
        store_id, _, _, _ = random.choice(STORES)
        month_date = start_date + timedelta(days=random.randint(0, 1100))
        quantity = random.randint(1, 6)
        unit_price = round(random.uniform(25, 1500), 2)
        discount = round(unit_price * quantity * random.uniform(0.0, 0.15), 2)
        tax_amount = round((unit_price * quantity - discount) * 0.05, 2)
        shipping_amount = round(random.uniform(0, 60), 2)
        total_amount = round(unit_price * quantity - discount + tax_amount + shipping_amount, 2)
        session_id = f"SES-{idx:06d}"
        rows.append({
            "transaction_id": f"T{idx:05d}",
            "customer_id": customer["customer_id"],
            "product_id": product_id,
            "campaign_id": campaign_id,
            "store_id": store_id,
            "session_id": session_id,
            "transaction_date": f"{month_date.month}/{month_date.day}/{month_date.year}",
            "quantity": quantity,
            "price": f"{unit_price:.2f}",
            "total_amount": f"{total_amount:.2f}",
            "order_id": f"ORD-{idx:05d}",
            "payment_method": random.choice(PAYMENT_METHODS),
            "currency_code": random.choice(FX_CURRENCIES),
            "country_code": customer["country"],
            "city": customer["city"],
            "sales_channel": random.choice(["Online", "Marketplace", "Retail"]),
            "device_type": random.choice(["Mobile", "Desktop", "Tablet"]),
            "promo_code": random.choice(["NONE", "WELCOME10", "VIP15", "RAMADAN20"]),
            "discount_amount": f"{discount:.2f}",
            "tax_amount": f"{tax_amount:.2f}",
            "shipping_amount": f"{shipping_amount:.2f}",
            "fulfillment_status": random.choice(FULFILLMENT_STATUSES),
            "transaction_status": random.choice(TRANSACTION_STATUSES)
        })
    return rows


def build_campaigns():
    rows = []
    base_start = date(2024, 1, 1)
    for idx in range(1000):
        campaign_id, platform_name, channel_group, objective = CAMPAIGNS[idx % len(CAMPAIGNS)]
        start_date = base_start + timedelta(days=(idx % 180))
        end_date = start_date + timedelta(days=random.randint(14, 120))
        budget = round(random.uniform(2000, 150000), 2)
        spent = round(budget * random.uniform(0.65, 1.05), 2)
        rows.append({
            "campaign_id": campaign_id,
            "campaign_name": f"{platform_name} {start_date.strftime('%b %Y')} {idx + 1}",
            "platform_name": platform_name,
            "channel_group": channel_group,
            "campaign_objective": objective,
            "budget": f"{budget:.2f}",
            "actual_spend": f"{spent:.2f}",
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
            "target_country": random.choice(list(COUNTRY_CITY.keys())),
            "target_segment": random.choice(SEGMENTS),
            "creative_type": random.choice(["Video", "Static", "Carousel", "Search Text"]),
            "owner_team": random.choice(["Growth", "CRM", "Brand", "Performance"]),
            "agency_name": random.choice(["InHouse", "MediaHub", "BlueFox", "AdSpark"]),
            "kpi_goal": random.choice(["ROAS", "CAC", "Leads", "Revenue"]),
            "status": random.choice(["Active", "Paused", "Completed"]),
            "currency_code": random.choice(FX_CURRENCIES),
            "impressions_target": random.randint(10000, 3000000),
            "clicks_target": random.randint(1000, 250000),
            "created_at": datetime(2024, 1, 1, tzinfo=timezone.utc).isoformat(),
        })
    return rows


def build_stores():
    rows = []
    for idx in range(1000):
        store_id, store_name, country, city = STORES[idx % len(STORES)]
        opening_date = date(2018, 1, 1) + timedelta(days=random.randint(0, 2400))
        rows.append({
            "store_id": store_id,
            "store_name": store_name,
            "store_type": random.choice(["Mall", "Street Retail", "Warehouse Outlet", "Dark Store"]),
            "country": country,
            "city": city,
            "district": random.choice(["Central", "North", "South", "West", "East"]),
            "manager_name": f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}",
            "manager_email": f"manager{idx + 1}@example.com",
            "phone_number": f"+9714{random.randint(1000000, 9999999)}",
            "area_sq_m": round(random.uniform(80, 2500), 2),
            "latitude": f"{random.uniform(24.0, 26.5):.6f}",
            "longitude": f"{random.uniform(54.0, 56.5):.6f}",
            "opening_date": opening_date.isoformat(),
            "closing_time": random.choice(["22:00", "23:00", "00:00"]),
            "opening_time": random.choice(["08:00", "09:00", "10:00"]),
            "region": random.choice(["GCC North", "GCC South", "Levant", "International"]),
            "warehouse_attached_flag": random.choice(["true", "false"]),
            "rent_cost_monthly": f"{round(random.uniform(10000, 180000), 2):.2f}",
            "staff_count": random.randint(8, 120),
            "store_status": random.choice(["Open", "Renovation", "Planned"]),
        })
    return rows


def build_scraped_prices():
    rows = []
    start_ts = datetime(2024, 1, 1, 9, 0, tzinfo=timezone.utc)
    for idx in range(PRICE_SNAPSHOT_COUNT):
        product_id, product_name, category, brand, sku = PRODUCTS[idx % len(PRODUCTS)]
        supplier = random.choice(SUPPLIERS)
        country = random.choice(list(COUNTRY_CITY.keys()))
        original_price = round(random.uniform(30, 1800), 2)
        discount_pct = round(random.uniform(0, 18), 2)
        price = round(original_price * (1 - discount_pct / 100), 2)
        rating = round(random.uniform(3.2, 5.0), 1)
        rows.append({
            "scrape_id": f"SCR-{idx + 1:05d}",
            "product_id": product_id,
            "sku": sku,
            "product_name": product_name,
            "category": category,
            "brand": brand,
            "supplier_name": supplier,
            "supplier_country": country,
            "price": f"{price:.2f}",
            "original_price": f"{original_price:.2f}",
            "discount_pct": f"{discount_pct:.2f}",
            "currency_code": random.choice(FX_CURRENCIES),
            "availability_status": random.choice(["In Stock", "Low Stock", "Out of Stock"]),
            "stock_qty": random.randint(0, 250),
            "rating": f"{rating:.1f}",
            "review_count": random.randint(5, 5000),
            "scrape_timestamp": (start_ts + timedelta(hours=idx * 3)).isoformat(),
            "source_site": random.choice(SOURCE_SITES),
            "page_url": f"https://{random.choice(SOURCE_SITES)}/products/{product_id.lower()}",
            "crawl_region": random.choice(["GCC", "EMEA", "Global"]),
        })
    return rows


def build_exchange_rates():
    rows = []
    start_date = date(2025, 1, 1)
    row_id = 1
    for fx_date in daterange(start_date, FX_ROW_COUNT // len(FX_CURRENCIES)):
        for currency in FX_CURRENCIES:
            rate = round(FX_BASE_RATES[currency] * random.uniform(0.96, 1.04), 4)
            rows.append({
                "snapshot_id": f"FX-{row_id:05d}",
                "date": fx_date.isoformat(),
                "base_currency": "USD",
                "currency": currency,
                "rate": f"{rate:.4f}",
                "inverse_rate": f"{(1 / rate):.6f}",
                "provider": "ExchangeRate-API",
                "rate_type": random.choice(["Spot", "Closing"]),
                "market_region": random.choice(["Middle East", "Europe", "Global"]),
                "is_weekend": str(fx_date.weekday() >= 5).lower(),
                "effective_from": f"{fx_date.isoformat()}T00:00:00+00:00",
                "effective_to": f"{fx_date.isoformat()}T23:59:59+00:00",
                "source_url": "https://api.exchangerate-api.com/v4/latest/USD",
                "load_batch_id": f"BATCH-{fx_date.strftime('%Y%m%d')}",
                "load_timestamp": datetime.combine(
                    fx_date, datetime.min.time(), tzinfo=timezone.utc
                ).isoformat(),
                "year": fx_date.year,
                "month": fx_date.month,
                "day": fx_date.day,
                "fx_status": "valid",
                "volatility_bucket": random.choice(["Low", "Medium", "High"]),
            })
            row_id += 1
    return rows[:FX_ROW_COUNT]


def build_orders(customers):
    rows = []
    start_date = date(2022, 1, 1)
    for idx in range(1, ORDER_COUNT + 1):
        customer = random.choice(customers)
        order_date = start_date + timedelta(days=random.randint(0, 1200))
        item_count = random.randint(1, 8)
        subtotal = round(random.uniform(60, 2500), 2)
        discount = round(subtotal * random.uniform(0.0, 0.12), 2)
        tax_amount = round((subtotal - discount) * 0.05, 2)
        shipping_cost = round(random.uniform(5, 75), 2)
        total = round(subtotal - discount + tax_amount + shipping_cost, 2)
        rows.append({
            "order_id": f"ORD-{idx:05d}",
            "customer_id": customer["customer_id"],
            "order_status": random.choice(ORDER_STATUSES),
            "order_date": order_date.isoformat(),
            "shipping_cost": shipping_cost,
            "payment_method": random.choice(PAYMENT_METHODS),
            "shipping_method": random.choice(SHIPPING_METHODS),
            "shipping_country": customer["country"],
            "shipping_city": customer["city"],
            "billing_country": customer["country"],
            "billing_city": customer["city"],
            "currency_code": random.choice(FX_CURRENCIES),
            "subtotal_amount": subtotal,
            "discount_amount": discount,
            "tax_amount": tax_amount,
            "total_amount": total,
            "item_count": item_count,
            "priority_flag": random.choice(["true", "false"]),
            "warehouse_code": random.choice(WAREHOUSE_CODES),
            "sales_rep_id": random.choice(SALES_REPS),
        })
    return rows


def build_inventory_snapshots():
    rows = []
    start_date = date(2025, 1, 1)
    for idx in range(1000):
        store_id, _, _, _ = random.choice(STORES)
        product_id, product_name, category, brand, sku = random.choice(PRODUCTS)
        snapshot_date = start_date + timedelta(days=idx % 120)
        stock_quantity = random.randint(0, 500)
        reserved_quantity = random.randint(0, min(stock_quantity, 60))
        inbound_quantity = random.randint(0, 120)
        outbound_quantity = random.randint(0, 100)
        available_quantity = stock_quantity - reserved_quantity
        unit_cost = round(random.uniform(15, 900), 2)
        inventory_value = round(available_quantity * unit_cost, 2)
        rows.append({
            "inventory_snapshot_id": f"INV-{idx + 1:06d}",
            "snapshot_date": snapshot_date.isoformat(),
            "store_id": store_id,
            "product_id": product_id,
            "sku": sku,
            "product_name": product_name,
            "category": category,
            "brand": brand,
            "stock_quantity": stock_quantity,
            "reserved_quantity": reserved_quantity,
            "available_quantity": available_quantity,
            "reorder_point": random.randint(20, 120),
            "safety_stock": random.randint(10, 80),
            "inbound_quantity": inbound_quantity,
            "outbound_quantity": outbound_quantity,
            "unit_cost": f"{unit_cost:.2f}",
            "inventory_value": f"{inventory_value:.2f}",
            "supplier_name": random.choice(SUPPLIERS),
            "snapshot_timestamp": datetime.combine(
                snapshot_date, datetime.min.time(), tzinfo=timezone.utc
            ).isoformat(),
            "stock_status": random.choice(["Healthy", "Low", "Out Of Stock"]),
        })
    return rows


def build_web_events(customers, transactions):
    rows = []
    event_types = ["page_view", "product_view", "add_to_cart", "checkout_start", "purchase"]
    pages = ["/home", "/category", "/product", "/cart", "/checkout", "/campaign-landing"]
    tx_index = {tx["session_id"]: tx for tx in transactions}
    session_ids = list(tx_index.keys())
    for idx in range(1000):
        session_id = session_ids[idx % len(session_ids)]
        tx = tx_index[session_id]
        customer = next(c for c in customers if c["customer_id"] == tx["customer_id"])
        event_time = datetime(2025, 1, 1, tzinfo=timezone.utc) + timedelta(minutes=idx * 7)
        is_conversion = "true" if random.random() < 0.18 else "false"
        rows.append({
            "event_id": f"WEB-{idx + 1:06d}",
            "session_id": session_id,
            "customer_id": customer["customer_id"],
            "campaign_id": tx["campaign_id"],
            "store_id": tx["store_id"],
            "product_id": tx["product_id"],
            "event_timestamp": event_time.isoformat(),
            "event_date": event_time.date().isoformat(),
            "event_type": random.choice(event_types),
            "page_visited": random.choice(pages),
            "page_category": random.choice(["Landing", "Catalog", "Product", "Checkout", "Support"]),
            "traffic_source": random.choice(CHANNELS),
            "device_type": random.choice(["Mobile", "Desktop", "Tablet"]),
            "browser_name": random.choice(["Chrome", "Safari", "Edge", "Firefox"]),
            "operating_system": random.choice(["iOS", "Android", "Windows", "macOS"]),
            "time_spent_seconds": random.randint(5, 900),
            "scroll_depth_pct": round(random.uniform(5, 100), 2),
            "is_conversion": is_conversion,
            "order_id": tx["order_id"] if is_conversion == "true" else "",
            "revenue_amount": tx["total_amount"] if is_conversion == "true" else "0.00",
        })
    return rows


def write_csv(path: Path, rows):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_orders_sqlite(path: Path, rows):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS orders")
    cur.execute(
        """
        CREATE TABLE orders (
            order_id TEXT PRIMARY KEY,
            customer_id TEXT,
            order_status TEXT,
            order_date TEXT,
            shipping_cost REAL,
            payment_method TEXT,
            shipping_method TEXT,
            shipping_country TEXT,
            shipping_city TEXT,
            billing_country TEXT,
            billing_city TEXT,
            currency_code TEXT,
            subtotal_amount REAL,
            discount_amount REAL,
            tax_amount REAL,
            total_amount REAL,
            item_count INTEGER,
            priority_flag TEXT,
            warehouse_code TEXT,
            sales_rep_id TEXT
        )
        """
    )
    cur.executemany(
        """
        INSERT INTO orders (
            order_id, customer_id, order_status, order_date, shipping_cost,
            payment_method, shipping_method, shipping_country, shipping_city,
            billing_country, billing_city, currency_code, subtotal_amount,
            discount_amount, tax_amount, total_amount, item_count,
            priority_flag, warehouse_code, sales_rep_id
        ) VALUES (
            :order_id, :customer_id, :order_status, :order_date, :shipping_cost,
            :payment_method, :shipping_method, :shipping_country, :shipping_city,
            :billing_country, :billing_city, :currency_code, :subtotal_amount,
            :discount_amount, :tax_amount, :total_amount, :item_count,
            :priority_flag, :warehouse_code, :sales_rep_id
        )
        """,
        rows,
    )
    conn.commit()
    conn.close()


def main():
    random.seed(SEED)
    ensure_raw_dir()

    customers = build_customers()
    campaigns = build_campaigns()
    stores = build_stores()
    transactions = build_transactions(customers)
    scraped_prices = build_scraped_prices()
    exchange_rates = build_exchange_rates()
    orders = build_orders(customers)
    inventory_snapshots = build_inventory_snapshots()
    web_events = build_web_events(customers, transactions)

    write_csv(RAW_DIR / "customers_master.csv", customers)
    write_csv(RAW_DIR / "campaigns.csv", campaigns)
    write_csv(RAW_DIR / "stores.csv", stores)
    write_csv(RAW_DIR / "transactions.csv", transactions)
    write_csv(RAW_DIR / "scraped_prices_automated.csv", scraped_prices)
    write_csv(RAW_DIR / "api_exchange_rates.csv", exchange_rates)
    write_csv(RAW_DIR / "inventory_snapshots.csv", inventory_snapshots)
    write_csv(RAW_DIR / "web_events.csv", web_events)
    write_orders_sqlite(RAW_DIR / "operational_db.sqlite", orders)

    print("Generated raw datasets:")
    print(f"- customers_master.csv: {len(customers)} rows, {len(customers[0])} columns")
    print(f"- campaigns.csv: {len(campaigns)} rows, {len(campaigns[0])} columns")
    print(f"- stores.csv: {len(stores)} rows, {len(stores[0])} columns")
    print(f"- transactions.csv: {len(transactions)} rows, {len(transactions[0])} columns")
    print(f"- scraped_prices_automated.csv: {len(scraped_prices)} rows, {len(scraped_prices[0])} columns")
    print(f"- api_exchange_rates.csv: {len(exchange_rates)} rows, {len(exchange_rates[0])} columns")
    print(f"- inventory_snapshots.csv: {len(inventory_snapshots)} rows, {len(inventory_snapshots[0])} columns")
    print(f"- web_events.csv: {len(web_events)} rows, {len(web_events[0])} columns")
    print(f"- operational_db.sqlite.orders: {len(orders)} rows, {len(orders[0])} columns")


if __name__ == "__main__":
    main()
