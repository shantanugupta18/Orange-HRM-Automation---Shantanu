from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("ORANGEHRM_BASE_URL")
USERNAME = os.getenv("ESS_USERNAME")
PASSWORD = os.getenv("ESS_PASSWORD")
HEADLESS = os.getenv("HEADLESS") == "true"
BROWSER = os.getenv("BROWSER", "chromium")
