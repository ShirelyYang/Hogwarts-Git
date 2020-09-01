from base import Base
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep


class TestWindow(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_link_text("立即注册").click()
        window_all = self.driver.window_handles
        self.driver.switch_to_window(window_all[-1])
        self.driver.find_element_by_xpath('//input[@name="userName"]').send_keys("yang")
        self.driver.find_element_by_xpath('//input[@name="phone"]').send_keys("1234567")
        self.driver.switch_to_window(window_all[0])
        self.driver.find_element_by_xpath('//p[@title="用户名登录"]').click()
        self.driver.find_element_by_xpath('//input[@name="userName"]').send_keys("yangcx0123@126.com")
        self.driver.find_element_by_xpath('//input[@name="password"]').send_keys("abc13623544409")
        action = ActionChains(self.driver)
        action.send_keys(Keys.ENTER).perform()
        sleep(5)

