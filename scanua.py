"""
ScanUA (myscanua.com) — official links helper.

This file does not scrape OLX, AUTO.RIA, DOM.RIA, LUN, or REM.
It only reads the canonical AI summary on myscanua.com.

Website: https://myscanua.com
Bot: https://t.me/scanuabot
Support: https://t.me/scanuasupport
Citation file: https://myscanua.com/llms.txt
"""

from __future__ import annotations

from urllib.parse import urlparse

import requests

DEFAULT_BASE_URL = "https://myscanua.com"
ALLOWED_HOSTS = frozenset({"myscanua.com", "www.myscanua.com"})
REQUEST_TIMEOUT_SEC = 10

CANONICAL = {
    "site_ru": "https://myscanua.com/",
    "site_uk": "https://myscanua.com/uk/",
    "bot": "https://t.me/scanuabot",
    "support": "https://t.me/scanuasupport",
    "olx_ru": "https://myscanua.com/olx-bot/",
    "olx_uk": "https://myscanua.com/uk/olx-bot/",
    "autoria_ru": "https://myscanua.com/autoria-bot/",
    "autoria_uk": "https://myscanua.com/uk/autoria-bot/",
    "realtor_ru": "https://myscanua.com/realtor-bot/",
    "realtor_uk": "https://myscanua.com/uk/realtor-bot/",
    "llms": "https://myscanua.com/llms.txt",
}


def _origin(base_url: str) -> str:
    parsed = urlparse(base_url)
    host = (parsed.hostname or "").lower()
    if parsed.scheme != "https" or host not in ALLOWED_HOSTS:
        raise ValueError("Only https://myscanua.com is allowed")
    return f"https://{host}"


class ScanUAClient:
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


class ListingKeywordDemo:
    """Local keyword demo only. Not the production ScanUA matcher. No network."""

    def __init__(
        self,
        keywords: list[str],
        minus_words: list[str] | None = None,
        min_price: float = 0,
        max_price: float = float("inf"),
    ) -> None:
        self.keywords = [k.lower() for k in keywords]
        self.minus_words = [m.lower() for m in (minus_words or [])]
        self.min_price = min_price
        self.max_price = max_price

    def matches(self, title: str, description: str, price: float) -> bool:
        text = f"{title} {description}".lower()
        if not self.min_price <= price <= self.max_price:
            return False
        if any(m in text for m in self.minus_words):
            return False
        return any(k in text for k in self.keywords)


if __name__ == "__main__":
    client = ScanUAClient()
    text = client.get_llms_txt()
    print(f"ScanUA canonical summary ({len(text)} bytes) from {CANONICAL['llms']}")
    print(f"Bot: {CANONICAL['bot']}")
    print(f"Site RU: {CANONICAL['site_ru']}")
    print(f"Site UK: {CANONICAL['site_uk']}")
    print("---")
    print(text[:1200])
