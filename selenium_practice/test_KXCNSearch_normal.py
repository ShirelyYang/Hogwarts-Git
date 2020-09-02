from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:
    def setup(self):
        option = Options()
        option.add_experimental_option("w3c", False)
        option.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_demo(self):
        self.driver.get("https://service.kangxin.com/platform/home")
        self.driver.find_element_by_xpath('//li[@id="sbcx"]/section[@class="original"]').click()
        self.driver.find_element_by_css_selector(".camera-btn").click()
        sleep(3)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((
            By.XPATH, '//div[@class="el-upload-dragger"]')))
        self.driver.find_element_by_xpath('//div[@class="el-upload-dragger"]').click()
        os.system(r'D:\workspace-Python\Hogwarts-Git\selenium_practice\uploadChrome.exe "D:\work\img\ab.jpg"')
        # r"D:\work\img\ab.jpg"
        sleep(6)
        self.driver.find_element_by_xpath('//button[@type="button"]').click()
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((
            By.XPATH, '//input[@placeholder="请输入商标名称"]')))
        input_ele = self.driver.find_element_by_xpath('//input[@placeholder="请输入商标名称"]')
        action = TouchActions(self.driver)
        action.scroll_from_element(input_ele, 0, 10000).perform()
