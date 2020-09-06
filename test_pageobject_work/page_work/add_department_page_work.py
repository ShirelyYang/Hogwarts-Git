from selenium.webdriver.common.by import By
from time import sleep
from page_work.contact_page_work import ContactPage
from page_work.base_page_work import BasePage


class AddDepartmentPage(BasePage):
    def add_department(self, dp_name):
        self.find(By.CSS_SELECTOR, ".inputDlg_item:nth-child(1) input").send_keys(dp_name)
        self.find(By.CSS_SELECTOR, ".qui_dialog_body .js_parent_party_name").click()
        # self.finds(By.CSS_SELECTOR, '.ww_dialog_body [role="treeitem"]')[0].click()
        self.finds(By.CSS_SELECTOR, ".ww_dialog_body .jstree-anchor")[0].click()
        self.find(By.CSS_SELECTOR, ".ww_dialog_foot .ww_btn_Blue").click()
        sleep(5)
        return ContactPage(self._driver)

    def get_error_message(self):
        # msg = self.find(By.ID, "js_tips")
        # .style.display = "block"
        msg = self._driver.execute_script('return msg=document.getElementById("js_tips").innerText')
        return msg