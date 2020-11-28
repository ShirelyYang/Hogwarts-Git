import logging

import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _error_count = 0
    _error_max = 10
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, by, locator=None):
        logging.info(locator)
        try:
            element = self._driver.find_elements(*by) if isinstance(by, tuple) else self._driver.find_element(by, locator)
            self._error_count = 0
            return element
        except Exception as e:
            self._error_count += 1
            if self._error_count >= self._error_max:
                raise e
            raise e

    def finds(self, by, locator):
        logging.info(locator)
        return self._driver.find_elements(by, locator)

    def base_quit(self):
        return self._driver.quit()

