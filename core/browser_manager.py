from playwright.sync_api import sync_playwright

from config.settings import settings


class BrowserManager:
    def __init__(self) -> None:
        self._playwright = sync_playwright().start()
        browser_type = getattr(self._playwright, settings.browser)
        self._browser = browser_type.launch(headless=settings.headless)

    def context(self):
        return self._browser.new_context()

    def close(self) -> None:
        self._browser.close()
        self._playwright.stop()
