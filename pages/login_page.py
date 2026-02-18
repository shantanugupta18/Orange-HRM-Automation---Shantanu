from playwright.sync_api import Page, expect

from config.settings import BASE_URL


class LoginPage:
    USERNAME_INPUT = "input[name='username']"
    PASSWORD_INPUT = "input[name='password']"
    SUBMIT_BUTTON = "button[type='submit']"
    MY_INFO_LINK = "role=link[name='My Info']"
    INVALID_CREDENTIALS = "text=Invalid credentials"

    def __init__(self, page: Page):
        self.page = page

    def open(self) -> None:
        for _ in range(2):
            try:
                self.page.goto(BASE_URL, timeout=45000, wait_until="domcontentloaded")
                return
            except Exception:
                continue
        self.page.goto(BASE_URL, timeout=60000, wait_until="load")

    def login(self, username: str, password: str) -> None:
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.SUBMIT_BUTTON, no_wait_after=True)

    def verify_login_success(self) -> None:
        expect(self.page.locator(self.MY_INFO_LINK)).to_be_visible()

    def verify_login_failure(self) -> None:
        expect(self.page.locator(self.INVALID_CREDENTIALS)).to_be_visible()
