from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from base_page_shizhan import BasePage
from contact_page_shizhan import ContactPage


class AddMemberPage(BasePage):
    _username = (By.ID, "username")

    def add_member(self, phone):
        # *self._username 为 解元祖 操作
        self.find(*self._username).send_keys("Amy")
        # self.find(By.ID, "username").send_keys("Shirely")
        self.find(By.ID, "memberAdd_english_name").send_keys("XUE")
        self.find(By.ID, "memberAdd_acctid").send_keys("123")
        self.find(By.CSS_SELECTOR, '[name="gender"]').click()
        phone_input = self.find(By.ID, "memberAdd_phone").send_keys(phone)
        action = ActionChains(self._driver)
        action.release(phone_input)
        self.finds(By.CSS_SELECTOR, '.js_btn_save:nth-child(2)')[1].click()
        sleep(5)
        return ContactPage(self._driver)

    def get_phone_error_message(self):
        return self.find(By.CSS_SELECTOR, ".ww_inputWithTips_WithErr .ww_inputWithTips_tips").text


