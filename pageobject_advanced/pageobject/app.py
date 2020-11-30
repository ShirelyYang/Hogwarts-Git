from appium import webdriver

from pageobject.base_page import BasePage
from pageobject.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def start(self):
        if self._driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "emulator-5554"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps["autoGrantPermissions"] = True
            caps["noReset"] = True
            self._driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        else:
            self._driver.start_activity(self._package, self._activity)
        self._driver.implicitly_wait(3)
        return self

    def main(self) -> Main:
        return Main(self._driver)
