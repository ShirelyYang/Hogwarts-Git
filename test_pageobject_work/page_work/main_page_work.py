from selenium.webdriver.common.by import By

from page_work.add_member_page_work import AddMemberPage
from page_work.contact_page_work import ContactPage
from page_work.base_page_work import BasePage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member(self):
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMemberPage(self._driver)

    def goto_contact(self):
        self.find(By.ID, "menu_contacts").click()
        return ContactPage(self._driver)
