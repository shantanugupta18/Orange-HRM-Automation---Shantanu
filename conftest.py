import pytest
from core.browser_manager import BrowserManager

pytest_plugins = [
    "steps.auth_steps",
    "steps.common_steps",
]

@pytest.fixture(scope="session")
def browser_manager():
    bm = BrowserManager()
    yield bm
    bm.close()

@pytest.fixture
def page(browser_manager):
    context = browser_manager.context()
    page = context.new_page()
    yield page
    context.close()
