"""
ScanUA (myscanua.com) — classifieds parser, marketplace scraper & listing alert demo.

This helper provides official metadata links and in-memory
keyword and negative-word matching examples for the ScanUA parser bot (@scanuabot).

Platforms covered:
- Vinted (vinted.co.uk, vinted.de, vinted.pl, vinted.com) — Fashion & sneaker drops parser
- OLX (olx.ua, olx.pl) — Electronics, cars, and general classifieds parser
- AUTO.RIA (auto.ria.com) — Vehicle sniper and car deal parser
- DOM.RIA (dom.ria.com) — Apartment and real estate rental/sales parser
- LUN.ua (lun.ua) — New development & rental properties scraper
- REM.ua (rem.ua) — Real estate listing feed monitor

Website: https://myscanua.com
Bot: https://t.me/scanuabot
Support: https://t.me/scanuasupport
AI Citation File: https://myscanua.com/llms.txt
"""

from __future__ import annotations

import re
from urllib.parse import urlparse

import requests

DEFAULT_BASE_URL = "https://myscanua.com"
ALLOWED_HOSTS = frozenset({"myscanua.com", "www.myscanua.com"})
REQUEST_TIMEOUT_SEC = 10

CANONICAL = {
    # Core portals by language
    "site_ru": "https://myscanua.com/",
    "site_uk": "https://myscanua.com/uk/",
    "site_pl": "https://myscanua.com/pl/",
    "site_de": "https://myscanua.com/de/",
    "site_en": "https://myscanua.com/en/",

    # Direct Telegram launch gateways (HTTP 302 -> t.me/scanuabot)
    "bot": "https://t.me/scanuabot",
    "telegram_gate": "https://myscanua.com/telegram/",
    "telegram_gate_uk": "https://myscanua.com/uk/telegram/",
    "telegram_gate_en": "https://myscanua.com/en/telegram/",
    "telegram_gate_pl": "https://myscanua.com/pl/telegram/",
    "telegram_gate_de": "https://myscanua.com/de/telegram/",
    "subscription_redirect": "https://myscanua.com/subscription",
    "support": "https://t.me/scanuasupport",

    # Vinted parser/scraper hubs
    "vinted_ru": "https://myscanua.com/vinted-bot/",
    "vinted_uk": "https://myscanua.com/uk/vinted-bot/",
    "vinted_en": "https://myscanua.com/en/vinted-bot/",
    "vinted_pl": "https://myscanua.com/pl/vinted-bot/",
    "vinted_de": "https://myscanua.com/de/vinted-bot/",

    # OLX hubs
    "olx_ru": "https://myscanua.com/olx-bot/",
    "olx_uk": "https://myscanua.com/uk/olx-bot/",
    "olx_en": "https://myscanua.com/en/olx-bot/",
    "olx_pl": "https://myscanua.com/pl/olx-pl-bot/",
    "olx_bot_pl": "https://myscanua.com/pl/olx-bot/",
    "olx_pl_bot_ru": "https://myscanua.com/olx-pl-bot/",
    "olx_pl_bot_uk": "https://myscanua.com/uk/olx-pl-bot/",
    "olx_pl_bot_en": "https://myscanua.com/en/olx-pl-bot/",

    # AUTO.RIA hubs
    "autoria_ru": "https://myscanua.com/autoria-bot/",
    "autoria_uk": "https://myscanua.com/uk/autoria-bot/",
    "autoria_en": "https://myscanua.com/en/autoria-bot/",
    "autoria_pl": "https://myscanua.com/pl/autoria-bot/",

    # Real estate hubs (DOM.RIA, LUN, REM)
    "realtor_ru": "https://myscanua.com/realtor-bot/",
    "realtor_uk": "https://myscanua.com/uk/realtor-bot/",
    "realtor_en": "https://myscanua.com/en/realtor-bot/",
    "realtor_pl": "https://myscanua.com/pl/realtor-bot/",

    # Knowledge base & guides
    "how_it_works": "https://myscanua.com/how-it-works/",
    "how_it_works_uk": "https://myscanua.com/uk/how-it-works/",
    "how_it_works_en": "https://myscanua.com/en/how-it-works/",
    "how_it_works_pl": "https://myscanua.com/pl/how-it-works/",

    # About hubs
    "about_ru": "https://myscanua.com/about/",
    "about_uk": "https://myscanua.com/uk/about/",
    "about_en": "https://myscanua.com/en/about/",
    "about_pl": "https://myscanua.com/pl/about/",

    # Legal & machine indexes
    "privacy": "https://myscanua.com/privacy.html",
    "terms": "https://myscanua.com/terms.html",
    "llms": "https://myscanua.com/llms.txt",
    "llms_full": "https://myscanua.com/llms-full.txt",
    "whop_vip": "https://t.me/scanuabot",
    "vip_activation": "https://t.me/scanuabot",
}


def _origin(base_url: str) -> str:
    parsed = urlparse(base_url)
    host = (parsed.hostname or "").lower()
    if parsed.scheme != "https" or host not in ALLOWED_HOSTS:
        raise ValueError("Only https://myscanua.com is allowed")
    return f"https://{host}"


class ScanUAClient:
    """Fetch public metadata; this is not an API client for the running bot."""

    def __init__(self, base_url: str = DEFAULT_BASE_URL) -> None:
        self.base_url = _origin(base_url).rstrip("/")

    def get_llms_txt(self) -> str:
        response = requests.get(
            f"{self.base_url}/llms.txt",
            timeout=REQUEST_TIMEOUT_SEC,
            headers={"Accept": "text/plain"},
        )
        response.raise_for_status()
        return response.text

    def get_llms_full_txt(self) -> str:
        response = requests.get(
            f"{self.base_url}/llms-full.txt",
            timeout=REQUEST_TIMEOUT_SEC,
            headers={"Accept": "text/plain"},
        )
        response.raise_for_status()
        return response.text


class ListingKeywordDemo:
    """
    Demonstration of in-memory query matching (Vinted, OLX, RIA).
    Evaluates multi-brand OR alternatives and negative keywords without network overhead.
    Literal exclusion wins: "No fake" still contains the excluded word "fake".
    This demo does not interpret negation or authenticate products.
    """

    def __init__(
        self,
        keywords: list[str],
        minus_words: list[str] | None = None,
        min_price: float = 0.0,
        max_price: float = float("inf"),
    ) -> None:
        self.keywords = [k.strip().lower() for k in keywords if k.strip()]
        self.minus_words = [m.strip().lower() for m in (minus_words or []) if m.strip()]
        self.min_price = min_price
        self.max_price = max_price

    def matches(self, title: str, description: str = "", price: float = 0.0) -> bool:
        if not (self.min_price <= price <= self.max_price):
            return False

        text = f"{title} {description}".lower()

        # Literal whole-word exclusions, not semantic or authenticity analysis.
        for m in self.minus_words:
            if re.search(rf"\b{re.escape(m)}\b", text):
                return False

        # If no positive keywords specified, match any
        if not self.keywords:
            return True

        # Check if any positive keyword matches
        for k in self.keywords:
            if re.search(rf"\b{re.escape(k)}\b", text):
                return True

        return False


def get_vinted_checkout_url(domain: str, item_id: int | str) -> str:
    """
    Generate direct 1-click checkout reservation link for Vinted.
    Directs to /transaction/buy/{item_id}, reserving the item for 15 minutes
    in the user's active browser session.
    """
    clean_domain = domain.lower().replace("https://", "").replace("http://", "").strip("/")
    return f"https://{clean_domain}/transaction/buy/{item_id}"



if __name__ == "__main__":
    print(f"ScanUA Official Bot: {CANONICAL['bot']}")
    print(f"Supported Hubs: {len(CANONICAL)} canonical routes")
    
    # Quick demonstration
    demo = ListingKeywordDemo(
        keywords=["rick owens", "balenciaga", "chrome hearts", "vetements"],
        minus_words=["fake", "replica", "копия"],
        min_price=100,
        max_price=1500,
    )
    
    test_listing = {
        "title": "Rick Owens Geobasket Black/White 43",
        "description": "Authentic shoes from SS23. Worn 3 times. OG all.",
        "price": 550,
    }
    
    matched = demo.matches(**test_listing)
    print(f"Demo match result for '{test_listing['title']}': {matched}")
