import logging

from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _current_element: WebElement = None
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, by):
        self._current_element = self._driver.find_element(*by)
        return self._current_element

    def click(self):
        self._current_element.click()
        return self

    def send_keys(self, text):
        self._current_element.send_keys(text)
        return self

    def po_run(self, po_method, **kwargs):
        pass
