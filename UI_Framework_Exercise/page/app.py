from appium import webdriver

from page.base_page import BasePage
from page.main import Main


class App(BasePage):
    def start(self):
        _package = "com.xueqiu.android"
        _activity = ".view.WelcomeActivityAlias"
        caps = {}
        if self._driver is None:
            caps['platformName'] = "Android"
            caps['deviceName'] = "emulator-5554"
            caps['appPackage'] = _package
            caps['appActivity'] = _activity
            caps['noReset'] = True
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        else:
            self._driver.start_activity(_package, _activity)

    def stop(self):
        self._driver.quit()

    def bacK(self):
        self._driver.back()

    def goto_main(self):
        return Main(self._driver)