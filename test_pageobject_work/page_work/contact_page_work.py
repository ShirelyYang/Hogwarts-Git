import json

from selenium.webdriver.common.by import By

from page_work.base_page_work import BasePage


class ContactPage(BasePage):
    def goto_add_department(self):
        from page_work.add_department_page_work import AddDepartmentPage
        self.find(By.CSS_SELECTOR, ".member_colLeft_top_addBtnWrap").click()
        self.find(By.CSS_SELECTOR, ".jstree-contextmenu li:nth-child(1) a").click()
        return AddDepartmentPage(self._driver)

    def get_department(self):
        department_list = self.finds(By.CSS_SELECTOR, '.jstree-children a')
        # print(dp)
        departments = []
        for department in department_list:
            departments.append(department.text)
        return departments