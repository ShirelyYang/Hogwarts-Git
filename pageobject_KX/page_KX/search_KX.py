import os
from math import ceil

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_KX.basepage_KX import BasePageKX


class SearchKX(BasePageKX):
    def search_image(self):
        self._driver.find_element(By.CSS_SELECTOR, ".camera-btn").click()
        self._driver.find_element(By.CSS_SELECTOR, ".el-upload-dragger").click()
        sleep(3)
        os.system(r"D:\workspace-Python\Hogwarts-Git\selenium_practice\uploadchrome.exe")
        sleep(10)
        WebDriverWait(self._driver, 30).until(expected_conditions.element_to_be_clickable((
            By.CSS_SELECTOR, '.search button')))
        self.find(By.CSS_SELECTOR, '.search button').click()
        sleep(30)
        for i in range(int(ceil(1758/56))):
            self._driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            sleep(10)
        self._driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        return self.find(By.CSS_SELECTOR, '.trademark-reg')

    def searh_text(self):
        input_text = self.find(By.XPATH, '//input[@placeholder="请输入商标名称"]').send_keys("apple")
        # 点击查询按钮
        self.find(By.CSS_SELECTOR, ".el-button").click()
        sleep(10)
        # 回车进行查询操作
        # action = ActionChains(self._driver)
        # action.send_keys(input_text, Keys.ENTER)
        WebDriverWait(self._driver, 30).until(expected_conditions.element_to_be_clickable((
            By.CSS_SELECTOR, '.el-long-defalut-button')))
        # self.find(By.CSS_SELECTOR, '.el-long-defalut-button').click()
        sleep(30)
        total = self.find(By.CSS_SELECTOR, ".zTotal")
        for i in range(int(ceil(1051/56))):
            self._driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            sleep(10)
        self._driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        return self.find(By.CSS_SELECTOR, '.trademark-reg')
