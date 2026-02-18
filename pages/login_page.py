from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login(self, username, password):
        self.page.fill("input[name='username']", username)
        self.page.fill("input[name='password']", password)
        self.page.click("button[type='submit']")

    def verify_login_success(self):
        expect(self.page.locator("role=link[name='My Info']")).to_be_visible()

    def verify_login_failure(self):
        expect(self.page.locator("text=Invalid credentials")).to_be_visible()