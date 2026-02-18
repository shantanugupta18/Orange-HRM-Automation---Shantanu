from playwright.sync_api import Page

class MyInfoPage:
    def __init__(self, page: Page):
        self.page = page

    def open_my_info(self):
        self.page.click("role=link[name='My Info']")

    def open_section(self, section):
        self.page.click(f"role=link[name='{section}']")