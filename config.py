import os

from dotenv import load_dotenv

from framework.enums.browsers_enum import Browser

load_dotenv()

URL = os.getenv('BASE_TASK_URL')
BROWSER = os.getenv('BROWSER', Browser.CHROME.value)