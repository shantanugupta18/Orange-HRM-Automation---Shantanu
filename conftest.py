import pytest

from core.browser_manager import BrowserManager
from pages.login_page import LoginPage
from pages.my_info_page import MyInfoPage, MyInfoWorkflowPage, UploadPage

pytest_plugins = [
    "steps.auth_steps",
    "steps.common_steps",
    "steps.navigation_steps",
    "steps.crud_steps",
    "steps.restricted_steps",
    "steps.upload_steps",
]


@pytest.fixture(scope="session")
def browser_manager() -> BrowserManager:
    manager = BrowserManager()
    yield manager
    manager.close()


@pytest.fixture
def page(browser_manager: BrowserManager):
    context = browser_manager.context()
    browser_page = context.new_page()
    yield browser_page
    context.close()


@pytest.fixture
def login_page(page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def my_info_page(page) -> MyInfoPage:
    return MyInfoPage(page)


@pytest.fixture
def context_page(page) -> MyInfoWorkflowPage:
    return MyInfoWorkflowPage(page)


@pytest.fixture
def upload_page(page) -> UploadPage:
    return UploadPage(page)
