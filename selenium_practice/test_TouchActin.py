import pytest
from selenium.webdriver import TouchActions
from selenium import webdriver


class TestTouchAction(Base):
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("w3c", False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_touch_action(self):
        self.driver.get("https://www.baidu.com/")
        ele_input = self.driver.find_element_by_id("kw")
        ele_search = self.driver.find_element_by_id("su")
        action = TouchActions(self.driver)
        ele_input.send_keys("selenium测试")
        # TouchActions的点击操作
        action.tap(ele_search)
        action.perform()
        action.scroll_from_element(ele_input, 0, 10000).perform()


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_TouchAction.py'])
