import logging

import yaml
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    logging.basicConfig(level=logging.INFO)
    _current_element: WebElement = None
    # _params = {}

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
        # read yaml
        with open('../datas/page_demo.yaml') as f:
            yaml_data = yaml.safe_load(f)
            # find search
            for step in yaml_data[po_method]:
                # find by click send_keys
                if isinstance(step, dict):
                   for key in step.keys():
                       if key == "id":
                           self.find((MobileBy.ID, step[key]))
                       elif key == "click":
                           self.click()
                       elif key == "send_keys":
                           content: str = step[key]
                           # for param in self._params:
                           #     content = content.replace("{%s}" % param, self._params[param])
                           for k,v in kwargs.items():
                               content = content.replace("${"+k+"}", v)
                           self.send_keys(content)
                        # todo: 更多关键词
                       else:
                           logging.error(f"don't know {step}")
