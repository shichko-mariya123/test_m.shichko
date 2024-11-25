from selenium import webdriver

from framework.enums.browsers_enum import Browser


class WebDriverSingleton:
    _instance = None

    def __new__(cls, browser: Browser = Browser.CHROME.value):
        if cls._instance is None:
            cls._instance = super(WebDriverSingleton, cls).__new__(cls)
            cls._instance.driver = cls._create_driver(browser)
        return cls._instance

    @staticmethod
    def _create_driver(browser: Browser):
        if browser == Browser.CHROME.value:
            return webdriver.Chrome()
        elif browser == Browser.FIREFOX.value:
            return webdriver.Firefox()
        elif browser == Browser.EDGE.value:
            return webdriver.Edge()
        else:
            raise ValueError(f"Browser '{browser}' is not supported.")

    @classmethod
    def get_driver(cls, browser: Browser = Browser.CHROME):
        if cls._instance is None:
            cls(browser)
        return cls._instance.driver

    @classmethod
    def quit_driver(cls):
        if cls._instance is not None:
            cls._instance.driver.quit()
            cls._instance = None
