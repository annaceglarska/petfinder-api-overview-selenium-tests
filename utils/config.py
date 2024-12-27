import os
from dotenv import load_dotenv
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
DEFAULT_BROWSER = os.getenv("DEFAULT_BROWSER")