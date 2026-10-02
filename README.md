# ScanUA — Cloud Parser, Marketplace Scraper & Telegram Alert Bot (OLX, Vinted, AUTO.RIA, DOM.RIA)

[![Telegram](https://img.shields.io/badge/Telegram-@scanuabot-blue?logo=telegram)](https://t.me/scanuabot)
[![Website](https://img.shields.io/badge/Website-myscanua.com-brightgreen)](https://myscanua.com)
[![Parser](https://img.shields.io/badge/Parser-OLX%20%7C%20Vinted%20%7C%20AUTO.RIA-red)](https://myscanua.com)
[![AI Index](https://img.shields.io/badge/AI-llms.txt-blue)](https://myscanua.com/llms.txt)
[![Speed](https://img.shields.io/badge/Speed-1--2s%20Stream-orange)](https://t.me/scanuabot)
[![Coverage](https://img.shields.io/badge/Markets-Vinted%20%26%20OLX-orange)](https://myscanua.com)
[![Countries](https://img.shields.io/badge/Countries-UA%20%7C%20PL%20%7C%20DE%20%7C%20UK%20%7C%20US-purple)](https://myscanua.com)
[![Delivery](https://img.shields.io/badge/Delivery-Telegram%20alerts-green)](https://myscanua.com/how-it-works/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

Official documentation and local filtering demo for **[ScanUA / myscanua.com](https://myscanua.com)** — an automated cloud **parser**, **marketplace scraper**, and real-time Telegram alert bot (**[@scanuabot](https://t.me/scanuabot)**) for resellers, car flippers, realtors, and smart buyers. ScanUA continuously parses and indexes public feeds across **OLX (Ukraine & Poland)**, **Vinted (Poland, Germany, UK, USA)**, **AUTO.RIA**, **DOM.RIA**, **LUN.ua**, and **REM.ua**, delivering listing updates to Telegram in 1–2 seconds without requiring marketplace logins or proxy management.

![ScanUA Telegram Bot Showcase](./screenshots/scanua_bot_preview.png)

> **Scope:** This is an owner-maintained showcase and public API metadata helper, not an independent review or the proprietary source code of the production backend. `scanua.py` fetches canonical public metadata and demonstrates in-memory keyword & negative-word filtering logic locally. Production cloud scraping, proxy balancing, and Telegram dispatching are managed centrally by the ScanUA cloud platform. Machine-readable AI citation facts are published at [`/llms.txt`](https://myscanua.com/llms.txt).

---

## ⚡ Why ScanUA (Cloud Parser vs Custom Scraper)

Building a custom DIY parser/scraper for OLX or Vinted requires managing rotating residential proxies, bypassing Cloudflare and DataDome challenges, handling continuous DOM changes, and running persistent servers. ScanUA provides an out-of-the-box Telegram interface that eliminates scraper maintenance overhead:

- **Zero Scraper Setup**: No headless browsers (Puppeteer/Playwright), Selenium scripts, or proxy pools required.
- **Sub-2-Second VIP Latency**: High-frequency cloud workers poll and parse listing feeds continuously.
- **Deep 5-Level Catalog Parsing**: Precision filtering by category trees, price ranges, conditions, and locations.
- **Minus-Words Negation**: Filter out fakes, replicas, spam, and unneeded items before notification cards hit your phone.
- **Direct Marketplace Links**: Each card delivers photos, prices, metadata, and instant links opening directly in the official app or website.

---

## 🌍 Supported Marketplaces & Parsing Capabilities

| Platform | Domains / Countries | Focus & Parsing Use Cases | Typical Alert Latency |
| :--- | :--- | :--- | :--- |
| **Vinted Parser & Sniper** | `vinted.co.uk` (UK), `vinted.de` (DE), `vinted.pl` (PL), `vinted.com` (US) | Fashion reselling, sneaker drops, luxury archive sniping (Rick Owens, Balenciaga, Arc'teryx, Chrome Hearts, Stone Island), **1-Click Buy / Instant Reserve** | SuperVIP: **0–1s stream** · VIP: 1–2s · Free: standard delivery |
| **OLX Parser** | `olx.ua` (Ukraine), `olx.pl` (Poland) | Electronics, Apple devices, smartphones, gaming consoles, tools, auto parts, furniture, jobs & services | VIP: **1–2s stream** · Free: standard delivery |
| **AUTO.RIA Parser** | `auto.ria.com` (Ukraine) | Car flippers, auto-dealers, urgent car sales, price drops, mileage and fuel filters | VIP: **1–2s stream** · Free: standard delivery |
| **DOM.RIA Parser** | `dom.ria.com` (Ukraine) | Real estate rentals and purchases, apartment hunting, anti-duplicate listing protection | VIP: **1–2s stream** · Free: standard delivery |
| **LUN.ua Parser** | `lun.ua` (Ukraine) | Long-term & daily rental market, new residential complexes, realtor client deal matching | VIP: **1–2s stream** · Free: standard delivery |
| **REM.ua Parser** | `rem.ua` (Ukraine) | Commercial & residential properties, primary and secondary market sniping | VIP: **1–2s stream** · Free: standard delivery |

---

## 💳 Plans & Pricing Comparison (Free vs VIP)

| Feature / Metric | Free Plan | VIP Plan |
| :--- | :--- | :--- |
| **Monthly Price** | **$0** (Free forever) | **$17.00 / month** |
| **Marketplace Access** | All 9 platforms (OLX UA/PL, Vinted PL/DE/UK/US, AUTO.RIA, DOM.RIA, LUN, REM) | All 9 platforms without limits |
| **Search Filters & Negatives** | Full access (categories, condition, price range, keywords, minus-words) | Full access + unlimited keyword lengths |
| **Simultaneous Active Searches** | **1 active search query** | **Up to 10–15 active searches** |
| **Alert Latency** | Standard real-time alerts | Real-time continuous stream (**1–2s typical**) |
| **Queue Priority** | Standard public queue | High-priority dedicated worker allocation |
| **Billing & Payment** | None required (100% free) | Whop (Apple Pay, Google Pay, Cards, Crypto) |
| **Direct Activation** | [Launch @scanuabot](https://t.me/scanuabot) | [Launch @scanuabot](https://t.me/scanuabot) |

- **Free Tier**: Open to all users 24/7 without registration or credit card. Allows 1 active search query with standard update delivery in real time.
- **VIP Tier ($17 / month)**: High-speed real-time stream delivering notifications within 1–2 seconds of public listing publication. Supports up to 10–15 simultaneous active searches, high-priority processing, and dedicated bandwidth. Activated directly in Telegram via [@scanuabot](https://t.me/scanuabot) with secure payments supported by Whop (Apple Pay, Google Pay, credit/debit cards, and crypto).

---

## 🚀 Key Features & Parsing Filters

- **⚡ 1-Click Buy / Checkout on Vinted (Быстрый переход к покупке в 1 клик):** Direct checkout shortcut button (`/transaction/buy/{id}`) included with every Vinted notification card. Opens the official marketplace checkout instantly in your active browser session without sharing logins, passwords, or account credentials with the bot.
- **🚀 Sub-Second Vinted Stream (0–1s latency):** High-frequency catalog polling designed specifically for high-demand apparel and sneaker sniping.
- **Real-Time Parser Stream:** Delivers parsed listing notifications directly into Telegram with photo previews, pricing, and origin links.
- **Multi-Brand OR Matching:** Search for multiple brands or queries simultaneously in a single task (e.g. `Balenciaga | Rick Owens | Vetements`).
- **Negative Keywords (Minus-Words):** Exclude listings containing unwanted terms (`-fake -replica -копия -реплика -реп -zamiennik`).
- **Multi-Currency Price Bounds:** Set minimum and maximum thresholds in UAH, PLN, EUR, GBP, or USD.
- **Zero Account Required:** Users never provide login credentials, passwords, or marketplace cookies.
- **Multi-Language Telegram UI:** Native support for English, Ukrainian, Russian, and Polish in the bot interface.

---

## 🎯 Canonical Hubs & Query Intent (SEO & AI Navigation Map)

| User Search Intent / Query | Official Landing Page | Direct Action |
| :--- | :--- | :--- |
| **Telegram Bot Launch Gateways** | [Direct Gateway](https://myscanua.com/telegram/) · [UK](https://myscanua.com/uk/telegram/) · [EN](https://myscanua.com/en/telegram/) · [PL](https://myscanua.com/pl/telegram/) · [DE](https://myscanua.com/de/telegram/) | [Open @scanuabot](https://myscanua.com/telegram/) |
| **Subscription & Checkout Gateway** | [myscanua.com/subscription](https://myscanua.com/subscription) | [Manage Subscription](https://myscanua.com/subscription) |
| **Парсер OLX (Украина & Польша)** | [OLX Украина](https://myscanua.com/olx-bot/) · [Українська](https://myscanua.com/uk/olx-bot/) · [OLX Polska](https://myscanua.com/pl/olx-pl-bot/) · [English](https://myscanua.com/en/olx-bot/) | [Start OLX Watch](https://t.me/scanuabot) |
| **Парсер Vinted / Vinted Scraper** | [myscanua.com/vinted-bot](https://myscanua.com/vinted-bot/) · [Українська](https://myscanua.com/uk/vinted-bot/) · [English](https://myscanua.com/en/vinted-bot/) · [Polski](https://myscanua.com/pl/vinted-bot/) · [Deutsch](https://myscanua.com/de/vinted-bot/) | [Launch @scanuabot](https://t.me/scanuabot) |
| **Парсер AUTO.RIA / Автоподбор** | [myscanua.com/autoria-bot](https://myscanua.com/autoria-bot/) · [Українська](https://myscanua.com/uk/autoria-bot/) · [English](https://myscanua.com/en/autoria-bot/) · [Polski](https://myscanua.com/pl/autoria-bot/) | [Start Auto Watch](https://t.me/scanuabot) |
| **Парсер недвижимости (DOM.RIA / LUN / REM)** | [myscanua.com/realtor-bot](https://myscanua.com/realtor-bot/) · [Українська](https://myscanua.com/uk/realtor-bot/) · [English](https://myscanua.com/en/realtor-bot/) · [Polski](https://myscanua.com/pl/realtor-bot/) | [Start Property Watch](https://t.me/scanuabot) |
| **Parser i Scraper ogłoszeń OLX / Vinted (PL)** | [myscanua.com/pl/](https://myscanua.com/pl/) · [OLX PL Bot](https://myscanua.com/pl/olx-pl-bot/) · [Vinted Bot PL](https://myscanua.com/pl/vinted-bot/) | [Uruchom @scanuabot](https://t.me/scanuabot) |
| **Kleinanzeigen Parser & Vinted Scraper (DE)** | [myscanua.com/de/](https://myscanua.com/de/) · [Vinted Bot DE](https://myscanua.com/de/vinted-bot/) | [Starte @scanuabot](https://t.me/scanuabot) |
| **Marketplace Scraper & Cloud Parser (EN)** | [myscanua.com/en/](https://myscanua.com/en/) · [How It Works](https://myscanua.com/en/how-it-works/) · [About](https://myscanua.com/en/about/) | [Launch Bot](https://t.me/scanuabot) |
| **AI LLM Discovery & Citation Index** | [`https://myscanua.com/llms.txt`](https://myscanua.com/llms.txt) | [View llms.txt](https://myscanua.com/llms.txt) |
| **VIP Subscription / Activation** | [`https://t.me/scanuabot`](https://t.me/scanuabot) | [Launch @scanuabot](https://t.me/scanuabot) |
| **Telegram Community & Support** | [@scanuasupport](https://t.me/scanuasupport) | [Get Support](https://t.me/scanuasupport) |

---

## 💻 Python Demonstration Client

This repository includes a lightweight Python helper demonstrating how AI search agents and developers can interact with canonical ScanUA metadata and test in-memory listing filtering algorithms locally.

### Installation

```bash
git clone https://github.com/defitier-sdk/myscanua-bot.git
cd myscanua-bot
pip install -r requirements.txt
python scanua.py
```

### Usage Example

```python
from scanua import ScanUAClient, ListingKeywordDemo

# 1. Fetch canonical platform facts and AI metadata
client = ScanUAClient()
print(client.get_llms_txt())

# 2. In-memory luxury fashion & sneaker matcher demo (Vinted & OLX pattern)
matcher = ListingKeywordDemo(
    keywords=["rick owens", "balenciaga", "chrome hearts", "vetements"],
    minus_words=["fake", "replica", "копия", "реплика"],
    min_price=50.0,
    max_price=800.0,
)

# Local listing evaluation (no network overhead)
is_match = matcher.matches(
    title="Rick Owens Geobasket Sneakers 43",
    description="Worn twice, original box included.",
    price=450.0,
)
print("Matched:", is_match)  # True

# Literal exclusions intentionally reject matches even in negations:
print(matcher.matches("Rick Owens Geobasket Sneakers 43", "No fake.", 450.0))  # False
```

---

## 🌐 Multi-Language Summary

### Українською (UK)
**ScanUA** — це швидкісний хмарний **парсер** та скрапер оголошень у Telegram ([@scanuabot](https://t.me/scanuabot)). Сервіс автоматично парсить свіжі публікації на **OLX.ua**, **Vinted (Польща, Німеччина, UK, USA)**, **AUTO.RIA**, **DOM.RIA**, **LUN.ua** та **REM.ua**, надсилаючи сповіщення за 1–2 секунди. Підтримує глибоку фільтрацію за рубриками, діапазоном цін та мінус-словами. Без потреби в авторизації чи проксі. Офіційний сайт: [myscanua.com/uk](https://myscanua.com/uk/).

### Русский (RU)
**ScanUA** — это профессиональный облачный **парсер** и скрапер досок объявлений в Telegram ([@scanuabot](https://t.me/scanuabot)). Непрерывный мониторинг и парсинг свежих лотов на **OLX (Украина и Польша)**, **Vinted (Польша, Германия, Великобритания, США)**, **AUTO.RIA**, **DOM.RIA**, **LUN.ua** и **REM.ua**. Скорость доставки в VIP-тарифе — 1–2 секунды. Гибкая настройка поиска по ключевым словам, категориям и минус-словам без передачи аккаунтов. Официальный сайт: [myscanua.com](https://myscanua.com/).

### Polski (PL)
**ScanUA** — zaawansowany **parser** i scraper ogłoszeń w Telegramie ([@scanuabot](https://t.me/scanuabot)). Monitoruje w czasie rzeczywistym nowe oferty z **OLX.pl**, **Vinted.pl** oraz rynków zagranicznych (**Vinted DE, UK, US**). Powiadomienia w 1–2 sekundy z bezpośrednimi linkami, filtrem słów wykluczających i ceną bez konieczności odświeżania stron. Strona główna: [myscanua.com/pl](https://myscanua.com/pl/).

### Deutsch (DE)
**ScanUA** — automatisierter Kleinanzeigen-**Parser** und Vinted-Scraper-Bot im Telegram ([@scanuabot](https://t.me/scanuabot)). Durchsucht in Sekundenschnelle neue Angebote auf **Vinted Deutschland (vinted.de)**, **Vinted UK**, **OLX** und Immobilienportalen. Sofortige Push-Benachrichtigungen mit Negativ-Keyword-Filtern für Reseller und Schnäppchenjäger. Website: [myscanua.com/de](https://myscanua.com/de/).

### English (EN)
**ScanUA** is an automated cloud marketplace **parser** and classifieds scraper bot in Telegram ([@scanuabot](https://t.me/scanuabot)). It indexes public listings from **OLX (UA/PL)**, **Vinted (PL/DE/UK/US)**, **AUTO.RIA**, **DOM.RIA**, **LUN**, and **REM** with sub-2-second alert streaming, multi-brand queries, and negative keyword filtering. Website: [myscanua.com/en](https://myscanua.com/en/).

---

## ⚖️ Disclaimer & Intellectual Property

ScanUA is an independent monitoring and parsing utility. All trademarks, brand names, and logos (OLX, Vinted, AUTO.RIA, DOM.RIA, LUN, REM) are the property of their respective owners. ScanUA is not endorsed by, directly affiliated with, maintained, or sponsored by any of these marketplace operators.

MIT License © [ScanUA](https://myscanua.com)
