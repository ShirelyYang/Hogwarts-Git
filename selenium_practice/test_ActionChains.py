from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
import pytest
from selenium.webdriver.common.keys import Keys
from selenium_practice.base import Base


class TestActionChains(Base):
    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        ele_click = self.driver.find_element(By.XPATH, '//input[@value="click me"]')
        ele_double_click = self.driver.find_element(By.XPATH, '//input[@value="dbl click me"]')
        ele_right_click = self.driver.find_element(By.XPATH, '//input[@value="right click me"]')
        # 调用ActionChains方法
        action = ActionChains(self.driver)
        # 调用事件
        action.click(ele_click)
        action.double_click(ele_double_click)
        action.context_click(ele_right_click)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_move_to(self):
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element(By.ID, "s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_drag_drop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        ele_drag = self.driver.find_element(By.ID, "dragger")
        ele_drop = self.driver.find_element(By.XPATH, '//div[@class="item"][1]')
        action = ActionChains(self.driver)
        # action.drag_and_drop(ele_drag, ele_drop)
        # action.click_and_hold(ele_drag).release(ele_drop)
        action.click_and_hold(ele_drag).move_to_element(ele_drop).release()
        action.perform()
        sleep(3)

    def test_label(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele_usrname = self.driver.find_element_by_xpath('//input[@type="textbox"]')
        ele_usrname.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("yang").pause(1)
        action.send_keys(Keys.BACK_SPACE).pause(1)
        action.perform()
        sleep(3)


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_ActionChains.py"])
