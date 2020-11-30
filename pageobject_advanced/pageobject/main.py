import yaml
from appium.webdriver.common.mobileby import MobileBy
from time import sleep
from pageobject.base_page import BasePage


class Main(BasePage):
    def goto_search(self):
        self.find(MobileBy.ID, "tv_search").click()
        # search = yaml.safe_load(open("../datas/main.yaml"))[0]
        # self.steps("../datas/main.yaml")

    def goto_windows(self):
        self.find(MobileBy.ID, "post_status").click()
        sleep(3)
        self.find(MobileBy.ID, "tv_search").click()