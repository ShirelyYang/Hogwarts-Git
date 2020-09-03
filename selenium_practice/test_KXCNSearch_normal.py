import os
import shelve

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSearch:
    def setup(self):
        option = Options()
        option.add_experimental_option("w3c", False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        db = shelve.open("mydb/KXCN_Normal_cookies")
        cookies = db['cookie']
        db.close()
        self.driver.get("https://service.kangxin.com/platform/home?path=%2Fhome")
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get("https://service.kangxin.com/platform/home?path=%2Fhome")
        self.driver.find_element(By.CSS_SELECTOR, ".el-dialog__headerbtn").click()
        self.driver.find_element(By.XPATH, '//li[@id="sbcx"]/section[1]').click()
        self.driver.find_element(By.CSS_SELECTOR, ".camera-btn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-upload-dragger").click()
        os.system(r'D:\workspace-Python\Hogwarts-Git\selenium_practice\uploadChrome.exe "D:\work\img\ab.jpg"')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((
            By.CSS_SELECTOR, '.search button')))
        btn = self.driver.find_element(By.CSS_SELECTOR, '.search button').click()
        action = TouchActions(self.driver)
        action.scroll_from_element(btn, 0, 10000)
