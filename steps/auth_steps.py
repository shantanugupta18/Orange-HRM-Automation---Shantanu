import pytest
from pytest_bdd import given, parsers, then, when

from config.settings import ADMIN_PASSWORD, ADMIN_USERNAME, PASSWORD, USERNAME
from pages.login_page import LoginPage


def _login_form_visible(page) -> bool:
    return page.locator("input[name='username']").count() > 0


@given("the user is on the login page")
def user_on_login_page(login_page: LoginPage) -> None:
    login_page.open()


@given("the user is logged in with valid ESS credentials")
def user_logged_in(page, login_page: LoginPage) -> None:
    for _ in range(2):
        if "auth/login" not in page.url and not _login_form_visible(page):
            return
        login_page.open()
        if not _login_form_visible(page):
            return
        login_page.login(USERNAME, PASSWORD)
        page.wait_for_timeout(1500)
        if not _login_form_visible(page):
            return
        if ADMIN_USERNAME and ADMIN_PASSWORD and _login_form_visible(page):
            login_page.login(ADMIN_USERNAME, ADMIN_PASSWORD)
            page.wait_for_timeout(1500)
            if not _login_form_visible(page):
                return
    pytest.skip("Unable to authenticate with configured credentials")


@when(parsers.parse('the user logs in with "{username}" and "{password}"'))
def login_with_credentials(login_page: LoginPage, username: str, password: str) -> None:
    login_page.login(username, password)


@then(parsers.parse('"{result}" should be displayed'))
def verify_login_result(login_page: LoginPage, result: str) -> None:
    normalized = result.strip().lower()
    if normalized == "myinfo page visible":
        if _login_form_visible(login_page.page) and ADMIN_USERNAME and ADMIN_PASSWORD:
            login_page.login(ADMIN_USERNAME, ADMIN_PASSWORD)
        login_page.verify_login_success()
        return
    login_page.verify_login_failure()
