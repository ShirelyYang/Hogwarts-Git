from appium.webdriver.common.mobileby import MobileBy

from pageobject.base_page import BasePage


class Main(BasePage):
    def goto_search(self):
        # self.find(MobileBy.ID, "tv_search").click()
        self.steps("../datas/main.yaml")