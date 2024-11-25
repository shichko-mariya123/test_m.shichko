import pytest

from config import BROWSER, URL
from framework.web_driver import WebDriverSingleton


@pytest.fixture()
def browser():
    driver = WebDriverSingleton.get_driver(browser=BROWSER)
    driver.get(URL)
    yield driver
    WebDriverSingleton.quit_driver()
