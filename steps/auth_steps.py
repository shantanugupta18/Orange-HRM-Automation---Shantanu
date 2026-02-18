from pytest_bdd import given
from config import settings

@given("the user is logged in with valid ESS credentials")
def login(page):
    page.goto(settings.BASE_URL)
    page.fill('input[name="username"]', settings.USERNAME)
    page.fill('input[name="password"]', settings.PASSWORD)
    page.click('button[type="submit"]')
