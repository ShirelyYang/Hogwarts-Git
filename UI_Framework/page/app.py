from appium import webdriver

from page.base_page import BasePage
from page.demo_page import DemoPage


class App(BasePage):
    def start(self):
        _package = "com.xueqiu.android"
        _activity = ".view.WelcomeActivityAlias"
        caps = {}
        if self._driver is None:
            caps["platformName"] = "Android"
            caps["deviceName"] = "emulator-5554"
            caps["appPackage"] = _package
            caps["appActivity"] = _activity
            caps["autoGrantPermissions"] = True
            caps["noReset"] = True
            self._driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        else:
            self._driver.start_activity(_package, _activity)
        self._driver.implicitly_wait(3)
        return self

    def stop(self):
        self._driver.quit()

    def goto_demopage(self):
        return DemoPage(self._driver)