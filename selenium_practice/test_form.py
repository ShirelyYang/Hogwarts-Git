import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
from selenium_practice.base import Base


class TestForm(Base):
    def test_form(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element_by_link_text("登录").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, "user_login")))
        ele_usrname = self.driver.find_element_by_id("user_login")
        ele_pwd = self.driver.find_element_by_id("user_password")
        ele_label = self.driver.find_element_by_id("user_remember_me")
        ele_btn = self.driver.find_element_by_xpath('//input[@name="commit"]')
        ele_usrname.send_keys("yang")
        ele_pwd.send_keys("123456")
        ele_label.click()
        ele_btn.click()
        sleep(3)


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_form.py"])

