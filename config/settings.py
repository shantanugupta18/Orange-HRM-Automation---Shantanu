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
        return cls(
            base_url=os.getenv(
                "ORANGEHRM_BASE_URL",
                "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",
            ),
            username=os.getenv("ESS_USERNAME", ""),
            password=os.getenv("ESS_PASSWORD", ""),
            admin_username=os.getenv("ADMIN_USERNAME", ""),
            admin_password=os.getenv("ADMIN_PASSWORD", ""),
            headless=os.getenv("HEADLESS", "true").strip().lower() == "true",
            browser=os.getenv("BROWSER", "chromium").strip().lower(),
        )


settings = Settings.from_env()

BASE_URL = settings.base_url
USERNAME = settings.username
PASSWORD = settings.password
ADMIN_USERNAME = settings.admin_username
ADMIN_PASSWORD = settings.admin_password
HEADLESS = settings.headless
BROWSER = settings.browser
