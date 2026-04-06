# Завдання 01: Технічне завдання — Google Ads інтеграція

## Короткий опис (TL;DR для ледачих)

Треба зробити так, щоб коли користувач клікнув нашу рекламу в Google, потім пішов на партнерський сайт і там зареєструвався — ми знали про це і передали в Google Ads як конверсію. Плюс збираємо всю статистику до себе в сховище, щоб потім аналізувати.

**Що отримуємо:**
- Google Ads бачить конверсії і оптимізує кампанії
- Ми бачимо повну картину в своїй аналітиці
- Партнери отримують якісний трафік

---

## Загальна схема інтеграції

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           USER JOURNEY                                       │
└─────────────────────────────────────────────────────────────────────────────┘

     ┌──────────┐
     │  Google  │
     │   Ads    │──────┐
     └──────────┘      │ gclid=xxx
                       ▼
              ┌────────────────┐
              │  Our Landing   │◄──────┐
              │     Page       │       │
              └───────┬────────┘       │
                      │                │
    ┌─────────────────┼────────────────┤
    │                 │                │
    ▼                 ▼                ▼
┌──────────┐  ┌──────────────┐  ┌──────────┐
│ Store    │  │  User clicks │  │ Session  │
│ GCLID +  │  │  partner link│  │ data     │
│ User ID  │  └──────┬───────┘  └──────────┘
└──────────┘         │
                     ▼
              ┌──────────────┐
              │ Partner Site │
              └──────┬───────┘
                     │
                     ▼ conversion
              ┌──────────────┐
              │   Postback   │──────────────────┐
              └──────────────┘                   │
                                                 ▼
                                    ┌──────────────────────┐
                                    │  Our Backend         │
                                    │  - Match click_id    │
                                    │  - Get GCLID         │
                                    │  - Send to Google Ads│
                                    │  - Store in DB       │
                                    └──────────────────────┘
                                                 │
                    ┌────────────────────────────┼────────────────────────────┐
                    │                            │                            │
                    ▼                            ▼                            ▼
            ┌──────────────┐           ┌──────────────┐              ┌──────────────┐
            │ Google Ads   │           │  Data Lake/  │              │  Internal    │
            │ Conversion   │           │  Warehouse   │              │  Dashboard   │
            └──────────────┘           └──────────────┘              └──────────────┘
```

---

## Логічна схема з ідентифікаторами

### Крок 1: Клік з реклами
**Де:** Google Ads → Landing Page  
**Що ловимо:**
```
URL: https://oursite.com/landing?gclid=CjwKCAjw...xyz&utm_campaign=dating_us
       │
       └─► gclid: CjwKCAjw...xyz (Google Click ID)
           utm_campaign: dating_us (для зведення аналітики)
```

**Ідентифікатори для зберігання:**
| ID | Опис | Термін життя |
|----|------|--------------|
| `gclid` | Google Click Identifier | 90 днів (cookie) |
| `utm_source` | Джерело трафіку | Сесія |
| `utm_campaign` | Назва кампанії | Сесія |
| `utm_medium` | Медіа (cpc, display) | Сесія |
| `session_id` | Наша сесія | 30 хв бездіяльності |

### Крок 2: Перехід на партнера
**Де:** Our Site → Partner Offer  
**Що відбувається:**
```javascript
// При кліку на партнерський лінк
{
  "click_event": {
    "click_id": "clk_abc123",           // Наш внутрішній ID
    "user_id": "usr_789xyz",            // ID користувача (якщо є)
    "session_id": "sess_def456",        // ID сесії
    "gclid": "CjwKCAjw...xyz",          // З cookie/localStorage
    "partner_id": "partner_001",        // Який партнер
    "offer_id": "offer_dating_main",    // Який офер
    "timestamp": "2024-01-15T10:30:00Z",// Час кліка
    "ip_address": "203.0.113.42",       // IP (для fraud detection)
    "user_agent": "Mozilla/5.0...",     // Браузер
    "landing_page": "/landing/dating"   // З якої сторінки
  }
}
```

**Ідентифікатори для зведення аналітики:**
| ID | Опис | Навіщо потрібен |
|----|------|-----------------|
| `click_id` | Унікальний ID кліка | Зв'язуємо з postback |
| `user_id` | Наш ID користувача | LTV, ретеншен |
| `session_id` | ID сесії | Фанел аналіз |
| `gclid` | Google Click ID | Атрибуція в Google Ads |
| `partner_click_id` | ID від партнера (subid) | Деякі партнери передають свій |

### Крок 3: Конверсія на партнері
**Де:** Partner Site → Postback  
**Що приходить:**
```json
{
  "postback": {
    "click_id": "clk_abc123",           // ← Наш ID з кроку 2
    "partner_click_id": "pc_xyz789",    // ID партнера (опціонально)
    "conversion_type": "registration",  // Тип: registration | purchase | deposit
    "status": "approved",               // approved | pending | rejected
    "value": 0,                         // $ для purchase/deposit
    "currency": "USD",
    "timestamp": "2024-01-15T11:45:00Z",// Час конверсії
    "geo": "US",                        // Гео
    "device": "mobile"                  // Девайс
  }
}
```

### Крок 4: Відправка в Google Ads
**Що відправляємо:**
```json
{
  "conversion": {
    "gclid": "CjwKCAjw...xyz",          // ← Зі збереженого кроку 2
    "conversion_action": "customers/123/conversionActions/456",
    "conversion_date_time": "2024-01-15 11:45:00+02:00",
    "conversion_value": 0,
    "currency_code": "USD",
    "order_id": "clk_abc123",           // Для дедуплікації
    "user_identifiers": [               // Enhanced Conversions (опціонально)
      {
        "hashed_email": "a3f5..."       // SHA-256 хеш
      }
    ]
  }
}
```

---

## Які сервіси потрібні

### Основні:

| Сервіс | Для чого | Альтернативи |
|--------|----------|--------------|
| **Google Ads API** | Відправка конверсій | — (тільки офіційний) |
| **PostgreSQL / ClickHouse** | Зберігати кліки та конверсії | BigQuery, Redshift |
| **Redis** | Швидкий доступ до GCLID по session_id | Memcached |
| **Message Queue** | Надійна доставка postback'ів | RabbitMQ, Kafka, SQS |

### Допоміжні:

| Сервіс | Для чого |
|--------|----------|
| **BigQuery** (опціонально) | Довгострокове сховище + ML |
| **Grafana / Metabase** | Візуалізація аналітики |
| **Airflow** | ETL для Google Ads stats |

---

## Покрокова інструкція для розробки

### Фаза 1: Збір GCLID (1-2 дні)

**Задача:** Ловити і зберігати GCLID при вході на сайт

```javascript
// gclid-tracker.js

class GclidTracker {
  constructor() {
    this.STORAGE_KEY = 'gclid_data';
    this.TTL_DAYS = 90;
  }

  capture() {
    const urlParams = new URLSearchParams(window.location.search);
    const gclid = urlParams.get('gclid');
    
    if (gclid) {
      const data = {
        gclid: gclid,
        captured_at: new Date().toISOString(),
        landing_page: window.location.pathname,
        utm_source: urlParams.get('utm_source'),
        utm_campaign: urlParams.get('utm_campaign'),
        utm_medium: urlParams.get('utm_medium')
      };
      
      localStorage.setItem(this.STORAGE_KEY, JSON.stringify(data));
      
      // Також ставимо cookie (на випадок якщо localStorage очистять)
      document.cookie = `gclid=${gclid}; max-age=${this.TTL_DAYS * 24 * 60 * 60}; path=/; domain=.oursite.com`;
    }
  }

  get() {
    // Пробуємо спочатку localStorage
    const stored = localStorage.getItem(this.STORAGE_KEY);
    if (stored) {
      const data = JSON.parse(stored);
      // Перевіряємо чи не протух
      const age = (Date.now() - new Date(data.captured_at)) / (1000 * 60 * 60 * 24);
      if (age <= this.TTL_DAYS) {
        return data;
      }
    }
    
    // Fallback на cookie
    const match = document.cookie.match(/gclid=([^;]+)/);
    return match ? { gclid: match[1] } : null;
  }
}

// Ініціалізація
const tracker = new GclidTracker();
tracker.capture();
```

**API endpoint для створення сесії:**
```python
# POST /api/session/init
@app.route('/api/session/init', methods=['POST'])
def init_session():
    """Створює нову сесію з GCLID"""
    data = request.json
    
    session_id = generate_uuid()
    gclid_data = data.get('gclid_data')  # З фронта
    
    session = {
        'session_id': session_id,
        'user_id': data.get('user_id'),
        'gclid': gclid_data.get('gclid') if gclid_data else None,
        'utm_campaign': gclid_data.get('utm_campaign'),
        'landing_page': gclid_data.get('landing_page'),
        'ip_address': request.remote_addr,
        'user_agent': request.headers.get('User-Agent'),
        'created_at': datetime.utcnow(),
        'last_activity': datetime.utcnow()
    }
    
    db.sessions.insert_one(session)
    
    return jsonify({
        'session_id': session_id,
        'ttl_seconds': 1800  // 30 хв
    })
```

### Фаза 2: Трекінг кліків на партнерів (2-3 дні)

**API endpoint:**
```python
# POST /api/click/track
@app.route('/api/click/track', methods=['POST'])
def track_click():
    """Реєструє клік на партнерський офер"""
    data = request.json
    
    click_id = generate_uuid()
    session_id = data['session_id']
    
    # Дістаємо сесію з БД
    session = db.sessions.find_one({'session_id': session_id})
    
    click = {
        'click_id': click_id,
        'session_id': session_id,
        'user_id': session.get('user_id'),
        'gclid': session.get('gclid'),
        'partner_id': data['partner_id'],
        'offer_id': data['offer_id'],
        'clicked_at': datetime.utcnow(),
        'destination_url': data['destination_url'],
        # ... інші поля
    }
    
    db.clicks.insert_one(click)
    
    # Генеруємо лінк для партнера з click_id як subid
    partner_url = build_partner_url(
        data['destination_url'], 
        subid=click_id
    )
    
    return jsonify({
        'click_id': click_id,
        'partner_url': partner_url
    })
```

### Фаза 3: Обробка postback'ів (2-3 дні)

```python
# POST /postback/{partner_id}
@app.route('/postback/<partner_id>', methods=['GET', 'POST'])
def handle_postback(partner_id):
    """Отримує конверсію від партнера"""
    
    # Парсимо параметри (залежить від партнера)
    click_id = request.args.get('click_id') or request.json.get('click_id')
    conversion_type = request.args.get('type') or request.json.get('conversion_type')
    value = float(request.args.get('value', 0))
    
    # Зберігаємо конверсію
    conversion = {
        'conversion_id': generate_uuid(),
        'click_id': click_id,
        'partner_id': partner_id,
        'type': conversion_type,  # registration | purchase | etc
        'value': value,
        'currency': request.args.get('currency', 'USD'),
        'received_at': datetime.utcnow(),
        'status': 'pending'  // буде updated після відправки в Google Ads
    }
    
    db.conversions.insert_one(conversion)
    
    # Додаємо в чергу для відправки в Google Ads
    queue.send({
        'task': 'send_to_google_ads',
        'conversion_id': conversion['conversion_id'],
        'click_id': click_id
    })
    
    return 'OK', 200
```

### Фаза 4: Відправка в Google Ads (2-3 дні)

```python
# worker/google_ads_sender.py

from google.ads.googleads.client import GoogleAdsClient

class GoogleAdsConversionSender:
    def __init__(self):
        self.client = GoogleAdsClient.load_from_env()
        self.customer_id = os.getenv('GOOGLE_ADS_CUSTOMER_ID')
        
    def send_conversion(self, click_id: str):
        # Дістаємо дані кліка
        click = db.clicks.find_one({'click_id': click_id})
        conversion = db.conversions.find_one({'click_id': click_id})
        
        if not click or not click.get('gclid'):
            logger.warning(f"No GCLID for click {click_id}")
            return
        
        # Формуємо запит
        conversion_action = self.get_conversion_action(conversion['type'])
        
        conversion_data = {
            'gclid': click['gclid'],
            'conversion_action': conversion_action,
            'conversion_date_time': conversion['received_at'].isoformat(),
            'conversion_value': conversion['value'],
            'currency_code': conversion['currency'],
            'order_id': click_id  # Дедуплікація
        }
        
        # Відправляємо
        try:
            response = self.upload_click_conversion(conversion_data)
            
            # Оновлюємо статус
            db.conversions.update_one(
                {'click_id': click_id},
                {'$set': {
                    'status': 'sent',
                    'sent_at': datetime.utcnow(),
                    'google_ads_response': str(response)
                }}
            )
            
        except Exception as e:
            logger.error(f"Failed to send conversion: {e}")
            # Retry логіка...

    def upload_click_conversion(self, data):
        service = self.client.get_service('ConversionUploadService')
        
        click_conversion = self.client.get_type('ClickConversion')
        click_conversion.gclid = data['gclid']
        click_conversion.conversion_action = data['conversion_action']
        click_conversion.conversion_date_time = data['conversion_date_time']
        click_conversion.conversion_value = data['conversion_value']
        click_conversion.currency_code = data['currency_code']
        click_conversion.order_id = data['order_id']
        
        request = self.client.get_type('UploadClickConversionsRequest')
        request.customer_id = self.customer_id
        request.conversions.append(click_conversion)
        
        return service.upload_click_conversions(request=request)
```

### Фаза 5: Збір статистики з Google Ads (2 дні)

```python
# etl/google_ads_stats.py

from google.ads.googleads.client import GoogleAdsClient

class GoogleAdsStatsCollector:
    """Збирає статистику з Google Ads в наш data lake"""
    
    def __init__(self):
        self.client = GoogleAdsClient.load_from_env()
        
    def fetch_campaign_stats(self, date_from: str, date_to: str):
        """Тягує статистику по кампаніях"""
        
        query = f"""
        SELECT
            campaign.id,
            campaign.name,
            segments.date,
            metrics.impressions,
            metrics.clicks,
            metrics.cost_micros,
            metrics.conversions,
            metrics.conversions_value
        FROM campaign
        WHERE segments.date BETWEEN '{date_from}' AND '{date_to}'
        """
        
        service = self.client.get_service('GoogleAdsService')
        response = service.search(customer_id=self.customer_id, query=query)
        
        stats = []
        for row in response:
            stats.append({
                'campaign_id': row.campaign.id,
                'campaign_name': row.campaign.name,
                'date': row.segments.date,
                'impressions': row.metrics.impressions,
                'clicks': row.metrics.clicks,
                'cost_usd': row.metrics.cost_micros / 1_000_000,
                'conversions': row.metrics.conversions,
                'conversion_value': row.metrics.conversions_value,
                'fetched_at': datetime.utcnow()
            })
        
        # Зберігаємо
        db.google_ads_stats.insert_many(stats)
        
        return len(stats)

# Запускаємо щодня через cron/airflow
def daily_sync():
    collector = GoogleAdsStatsCollector()
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    
    count = collector.fetch_campaign_stats(yesterday, yesterday)
    logger.info(f"Synced {count} records for {yesterday}")
```

---

## Схема бази даних

```sql
-- Користувачі
CREATE TABLE users (
    user_id UUID PRIMARY KEY,
    email VARCHAR(255),
    created_at TIMESTAMP,
    country VARCHAR(2),
    device_type VARCHAR(50)
);

-- Сесії
CREATE TABLE sessions (
    session_id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(user_id),
    gclid VARCHAR(255),
    utm_source VARCHAR(100),
    utm_campaign VARCHAR(255),
    utm_medium VARCHAR(100),
    landing_page VARCHAR(500),
    ip_address INET,
    user_agent TEXT,
    created_at TIMESTAMP,
    last_activity TIMESTAMP
);

-- Кліки на партнерів
CREATE TABLE clicks (
    click_id UUID PRIMARY KEY,
    session_id UUID REFERENCES sessions(session_id),
    user_id UUID REFERENCES users(user_id),
    gclid VARCHAR(255),
    partner_id VARCHAR(100),
    offer_id VARCHAR(100),
    clicked_at TIMESTAMP,
    destination_url TEXT,
    partner_click_id VARCHAR(255)  -- subid від партнера
);

-- Конверсії
CREATE TABLE conversions (
    conversion_id UUID PRIMARY KEY,
    click_id UUID REFERENCES clicks(click_id),
    partner_id VARCHAR(100),
    type VARCHAR(50),  -- registration, purchase, deposit
    status VARCHAR(50),  -- pending, sent, failed
    value DECIMAL(10,2),
    currency VARCHAR(3),
    received_at TIMESTAMP,
    sent_at TIMESTAMP,
    google_ads_response TEXT
);

-- Статистика Google Ads
CREATE TABLE google_ads_stats (
    id SERIAL PRIMARY KEY,
    campaign_id BIGINT,
    campaign_name VARCHAR(255),
    date DATE,
    impressions INT,
    clicks INT,
    cost_usd DECIMAL(10,2),
    conversions DECIMAL(10,2),
    conversion_value DECIMAL(10,2),
    fetched_at TIMESTAMP
);
```

---

## Корисні посилання

- [Google Ads API — Conversion Tracking](https://developers.google.com/google-ads/api/docs/conversion-tracking/overview)
- [Enhanced Conversions](https://support.google.com/google-ads/answer/9888145)
- [Click Attribution](https://support.google.com/google-ads/answer/3123169)
- [Google Ads API Python Client](https://github.com/googleads/google-ads-python)

---

*«Якщо щось не зарахувалось — не панікуй. Логи не вруть (якщо ти їх пишеш).»*
