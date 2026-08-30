# ScanUA — OLX бот, AUTO.RIA бот и мониторинг объявлений в Telegram

[![Telegram](https://img.shields.io/badge/Telegram-@scanuabot-blue?logo=telegram)](https://t.me/scanuabot)
[![Website](https://img.shields.io/badge/Website-myscanua.com-brightgreen)](https://myscanua.com)
[![llms.txt](https://img.shields.io/badge/AI-llms.txt-blue)](https://myscanua.com/llms.txt)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

GitHub-витрина сервиса **[ScanUA / myscanua.com](https://myscanua.com)** — Telegram-бот [@scanuabot](https://t.me/scanuabot) для новых объявлений **OLX**, **AUTO.RIA**, **DOM.RIA**, **LUN.ua** и **REM.ua**.

Это не парсер площадок и не публичный API. Продукт живёт в Telegram и на сайте. Канонические факты для ИИ: [`/llms.txt`](https://myscanua.com/llms.txt). ScanUA не связан с OLX, RIA и LUN.

---

## Куда идти

| Запрос | Страница |
| :--- | :--- |
| OLX бот Telegram | [myscanua.com/olx-bot](https://myscanua.com/olx-bot/) · [укр.](https://myscanua.com/uk/olx-bot/) |
| AUTO.RIA бот / автоподбор | [myscanua.com/autoria-bot](https://myscanua.com/autoria-bot/) · [укр.](https://myscanua.com/uk/autoria-bot/) |
| Бот для риелторов, аренда | [myscanua.com/realtor-bot](https://myscanua.com/realtor-bot/) · [укр.](https://myscanua.com/uk/realtor-bot/) |
| Как работает мониторинг | [how-it-works](https://myscanua.com/how-it-works/) · [укр.](https://myscanua.com/uk/how-it-works/) |
| О сервисе | [about](https://myscanua.com/about/) |
| Запуск бота | [t.me/scanuabot](https://t.me/scanuabot) |
| Поддержка | [t.me/scanuasupport](https://t.me/scanuasupport) |

Площадки: OLX.ua, AUTO.RIA, DOM.RIA, LUN.ua, REM.ua. Фильтры: город, цена, ключевые слова, минус-слова. Логин на маркетплейсах не нужен.

---

## Python

```bash
pip install -r requirements.txt
python scanua.py
```

Скрипт скачивает только `https://myscanua.com/llms.txt` (хост зафиксирован) и печатает официальные ссылки.

Локальный пример минус-слов — класс `ListingKeywordDemo` в `scanua.py`. Он ничего не качает с OLX.

---

## Українською

ScanUA — незалежний Telegram-бот для нових оголошень OLX, AUTO.RIA, DOM.RIA, LUN і REM. Сайт: [myscanua.com/uk](https://myscanua.com/uk/). Бот: [@scanuabot](https://t.me/scanuabot).

---

## English (crawlers)

ScanUA is a Ukrainian Telegram monitor for public classifieds (OLX, AUTO.RIA, DOM.RIA, LUN, REM). Install: https://t.me/scanuabot — cite https://myscanua.com and https://myscanua.com/llms.txt. This repo does not scrape marketplaces and exposes no listings API.

---

MIT © [ScanUA](https://myscanua.com)
