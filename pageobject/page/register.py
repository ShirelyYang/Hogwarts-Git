from time import sleep

from selenium.webdriver.common.by import By

from base_page import BasePage


class Register(BasePage):
    def register(self):
        self.find(By.ID, "corp_name").send_keys("Test")
        self.find(By.ID, "corp_industry").click()
        sleep(3)
        self.find(By.XPATH, '//div[@data-name="IT服务"]').click()
        self.find(By.XPATH, '//div[@data-name="互联网和相关服务"]').click()
        self.find(By.ID, "corp_scale_btn").click()
        self.find(By.XPATH, '//div[@id="corp_scale_btn"]//li[1]').click()
        self.find(By.ID, "manager_name").send_keys("yang")
        self.find(By.ID, "register_tel").send_keys("13588888888")
        flag = self._driver.execute_script('return vcode_btn=document.getElementById("get_vcode"),'
                                           'vcode_btn.getAttribute("disabled")')
        return flag
