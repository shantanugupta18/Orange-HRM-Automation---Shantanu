import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    base_url: str
    username: str
    password: str
    admin_username: str
    admin_password: str
    headless: bool
    browser: str

    @classmethod
    def from_env(cls) -> "Settings":
        def get_env(name: str, default: str = "") -> str:
            value = os.getenv(name)
            if value is None:
                return default
            value = value.strip()
            return value if value else default

        return cls(
            base_url=get_env(
                "ORANGEHRM_BASE_URL",
                "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",
            ),
            username=get_env("ESS_USERNAME"),
            password=get_env("ESS_PASSWORD"),
            admin_username=get_env("ADMIN_USERNAME"),
            admin_password=get_env("ADMIN_PASSWORD"),
            headless=get_env("HEADLESS", "true").lower() == "true",
            browser=get_env("BROWSER", "chromium").lower(),
        )


settings = Settings.from_env()

BASE_URL = settings.base_url
USERNAME = settings.username
PASSWORD = settings.password
ADMIN_USERNAME = settings.admin_username
ADMIN_PASSWORD = settings.admin_password
HEADLESS = settings.headless
BROWSER = settings.browser
