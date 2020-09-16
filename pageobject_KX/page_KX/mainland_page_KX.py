import os
from time import sleep
from selenium.webdriver.common.by import By

from page_KX.basepage_KX import BasePageKX


class MainlandPageKX(BasePageKX):
    def mainland_registration(self):
        self.find(By.CSS_SELECTOR, ".el-input__inner").send_keys("大陆注册测试")
        self.find(By.CSS_SELECTOR, ".el-upload-dragger").click()
        os.system(r"../tools/uploadchrome.exe")
        sleep(5)
        self.find(By.CSS_SELECTOR, ".first-nice li:nth-child(3)").click()
        self.find(By.CSS_SELECTOR, ".second-nice li:nth-child(1)").click()
        self.find(By.CSS_SELECTOR, ".third-nice li:nth-child(1)").click()
        self.find(By.CSS_SELECTOR, ".save-button button").click()
        sleep(3)
        self.find(By.XPATH, '//div[@slot="bottom"]/button').click()
        sleep(3)
        self.find(By.CSS_SELECTOR, ".next-preview button").click()
        sleep(3)
        self._driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.find(By.CSS_SELECTOR, ".buttons button:last-child").click()

        # 上传文件
        self.find(By.CSS_SELECTOR, ".upload-div-en").click()
        os.system(r"../tools/uploadchromeIDcard.exe")
        sleep(5)
        # 下载文件
        self.find(By.CSS_SELECTOR, ".downPOA").click()
        os.system(r"../tools/downloadchrome.exe")
        sleep(5)
        self.find(By.CSS_SELECTOR, ".upload-div-en").click()
        os.system(r"../tools/uploadPOA.exe")
        sleep(10)

        self.find(By.CSS_SELECTOR, ".save-button button").click()
        return self.find(By.CSS_SELECTOR, ".subconfirm span")

