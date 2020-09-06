from selenium.webdriver.common.by import By

from add_member_page_shizhan import AddMemberPage
from base_page_shizhan import BasePage
from contact_page_shizhan import ContactPage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def go_to_contact(self):
        return ContactPage(self._driver)

    def go_to_add_member(self):
        self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        return AddMemberPage(self._driver)
