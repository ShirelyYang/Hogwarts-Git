from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage


class DemoPage(BasePage):
    _search_button = (MobileBy.ID, "home_search")
    # todo: po的数据驱动
    def login(self):
        pass

    def forget_password(self):
        pass

    def search(self, keyword):
        # self._params["value"] = keyword
        self.po_run("search", keyword=keyword)
        # self.find(self._search_button)
        # self.click()
        return self

    def back(self):
        self.po_run("back")
        return self
