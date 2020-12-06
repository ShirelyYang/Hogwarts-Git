import logging

import yaml
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
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
        with open("../datas/main_page.yaml") as f:
            yaml_data = yaml.safe_load(f)
            for step in yaml_data[po_method]:
                if isinstance(step, dict):
                    for key in step.keys():
                        if key == "id":
                            self.find((MobileBy.ID, step[key]))
                        elif key == "click":
                            self.click()
                        elif key == "send_keys":
                            content: str = step[key]
                            for k, v in kwargs.items():
                                content = content.replace('${'+k+'}', v)
                            self.send_keys(content)
                        else:
                            logging.error(f"don\'t know {key}")
