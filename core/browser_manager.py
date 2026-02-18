from playwright.sync_api import sync_playwright
from config import settings

class BrowserManager:
    def __init__(self):
        self.pw = sync_playwright().start()
        self.browser = getattr(self.pw, settings.BROWSER).launch(headless=settings.HEADLESS)

    def context(self):
        return self.browser.new_context()

    def close(self):
        self.browser.close()
        self.pw.stop()
