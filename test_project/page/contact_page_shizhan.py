from selenium.webdriver.common.by import By

from base_page_shizhan import BasePage


class ContactPage(BasePage):
    def go_to_add_member(self):
        from add_member_page_shizhan import AddMemberPage
        return AddMemberPage(self._driver)

    def get_member_list(self):
        name_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        # print(name_list)
        lis = []
        for name in name_list:
            lis.append(name.text)
        return lis
