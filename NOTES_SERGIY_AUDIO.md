# NOTES: Робота з SunoAPI для музичних каверів

## Дата створення
2026-03-15

## Контекст
Робота з upload-cover endpoint SunoAPI для створення AI-каверів на основі оригінальних вокальних треків.

---

## ⚠️ КРИТИЧНО ВАЖЛИВІ ПРОБЛЕМИ

### 1. Втрата оригінального вокалу
**Проблема:** SunoAPI `upload-cover` іноді генерує **тільки інструментал**, навіть з `instrumental: false`

**Причини:**
- Оригінальний вокал занадто тихий/нечіткий
- Suno не розпізнає вокал як окремий елемент
- Глюк системи (рандомний результат)

**Рішення:**
- Повторна генерація з тими ж параметрами (може спрацювати)
- Додавання тексту в `prompt` → Suno заспіває AI-вокалом (заміна оригіналу)
- Використання `/tools/separate` для розділення вокалу перед обробкою
- Ручний мікс в Audacity/Ableton (найнадійніше)

---

## ✅ ПРАВИЛЬНИЙ WORKFLOW

### Крок 1: Отримання файлу
```bash
# Завжди брати НАЙСВІЖІШИЙ файл
ls -lt /root/.openclaw/media/inbound/*.ogg /root/.openclaw/media/inbound/*.mp3 | head -1
```

### Крок 2: Конвертація (якщо OGG)
```bash
ffmpeg -i input.ogg -ar 44100 -ac 2 -b:a 192k output.mp3 -y
```

### Крок 3: Завантаження в Supabase
```bash
curl -s -X PUT "${SUPABASE_URL}/storage/v1/object/music/references/Sergiy/YYYY-MM-DD/Filename.mp3" \
  -H "Authorization: Bearer ${SUPABASE_SERVICE_KEY}" \
  -H "Content-Type: audio/mpeg" \
  --data-binary @file.mp3
```

### Крок 4: Генерація кавера

#### Варіант A: Зберегти оригінальний вокал (ризиковано)
```json
{
  "uploadUrl": "https://.../file.mp3",
  "customMode": true,
  "instrumental": false,
  "model": "V5",
  "callBackUrl": "https://httpbin.org/post",
  "prompt": "",
  "style": "Trip-hop, slow beats, minor key",
  "title": "Track Name",
  "audioWeight": 0.95,
  "styleWeight": 0.5
}
```
**Примітка:** Навіть з `audioWeight: 0.95` вокал може бути втрачено

#### Варіант B: AI-вокал з твоїм текстом (гарантовано)
```json
{
  "uploadUrl": "https://.../file.mp3",
  "customMode": true,
  "instrumental": false,
  "model": "V5",
  "callBackUrl": "https://httpbin.org/post",
  "prompt": "[Verse] Твій текст тут... [Chorus] Приспів тут...",
  "style": "Space rock, atmospheric synths",
  "title": "Track Name",
  "audioWeight": 0.6,
  "styleWeight": 0.5
}
```
**Примітка:** Suno заспіває твій текст AI-голосом, оригінальний вокал буде замінено

---

## 🎵 ПАРАМЕТРИ ТА ЇХ ЗНАЧЕННЯ

### `audioWeight` (0.0 - 1.0)
- **0.6** — Сильніше стилізація, менше оригіналу
- **0.95** — Максимальне збереження оригіналу (але вокал все одно може зникнути)

### `styleWeight` (0.0 - 1.0)
- **0.5** — Баланс між стилем і оригіналом

### `model`
- **"V5"** — Остання версія, найкраща якість

### `instrumental`
- **false** — Вокальний трек
- **true** — Інструментал

### `customMode`
- **true** — Детальний контроль через style/prompt

---

## 🚫 ОБМЕЖЕННЯ ТА ПОМИЛКИ

### SENSITIVE_WORD_ERROR
**Причина:** Назви відомих бендів (Pink Floyd, Death in Vegas) тригерять фільтр

**Рішення:** Описувати стиль іншими словами
- ❌ "Pink Floyd style"
- ✅ "Space rock, atmospheric synths, psychedelic echoes"

---

## 📋 ШАБЛОНИ ДЛЯ РІЗНИХ СЦЕНАРІЇВ

### Сценарій 1: Мінімальні зміни, зберегти вокал
```json
{
  "prompt": "",
  "style": "Slight reverb, warm production",
  "audioWeight": 0.95
}
```

### Сценарій 2: Сильна стилізація, зберегти вокал
```json
{
  "prompt": "",
  "style": "Trip-hop, slow beats, dark atmosphere",
  "audioWeight": 0.8
}
```

### Сценарій 3: AI-вокал з текстом
```json
{
  "prompt": "[Intro] ... [Verse] ... [Chorus] ...",
  "style": "Electronic, synth-driven",
  "audioWeight": 0.6
}
```

---

## 🔧 АЛЬТЕРНАТИВНІ ІНСТРУМЕНТИ

Якщо SunoAPI не підходить для збереження оригінального вокалу:

1. **Ultimate Vocal Remover (UVR)** — розділення вокалу та інструменталу
2. **Adobe Audition** — професійний мікс
3. **Ableton Live** — створення каверу вручну
4. **iZotope RX** — відновлення та обробка вокалу

---

## 📝 ЛОГ ГЕНЕРАЦІЙ

Див. файл: `/root/.openclaw/workspace/memory/music-log.jsonl`

---

## ⚡ ШВИДКІ КОМАНДИ

### Перевірка статусу генерації
```bash
curl -s "https://api.sunoapi.org/api/v1/generate/record-info?taskId=XXX" \
  -H "Authorization: Bearer API_KEY"
```

### Моніторинг у реальному часі
```bash
for i in {1..40}; do
  response=$(curl -s "https://api.sunoapi.org/api/v1/generate/record-info?taskId=XXX" \
    -H "Authorization: Bearer API_KEY")
  status=$(echo "$response" | grep -o '"status":"[^"]*"' | head -1 | cut -d'"' -f4)
  echo "$(date '+%H:%M:%S') - $status"
  [ "$status" = "SUCCESS" ] && break
  sleep 10
done
```

---

## 🔑 КЛЮЧОВІ ВИСНОВКИ

1. **SunoAPI upload-cover** — це AI-переробка, не "кавер" в класичному сенсі
2. Оригінальний вокал зберігається **випадково**, не гарантовано
3. Найнадійніший результат — AI-вокал з твоїм текстом
4. Для професійного результату потрібен ручний мікс

---

**Останнє оновлення:** 2026-03-15
**Автор:** Сергій Дубей + Kimi Claw
