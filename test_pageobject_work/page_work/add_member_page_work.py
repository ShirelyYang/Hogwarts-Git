from selenium.webdriver.common.by import By
from time import sleep
from page_work.add_department_page_work import AddDepartmentPage
from page_work.base_page_work import BasePage


class AddMemberPage(BasePage):
    def goto_add_department(self):
        self.find(By.CSS_SELECTOR, ".member_colLeft_top_addBtnWrap").click()
        self.find(By.CSS_SELECTOR, ".jstree-contextmenu li:nth-child(1) a").click()
        sleep(3)
        return AddDepartmentPage(self._driver)

