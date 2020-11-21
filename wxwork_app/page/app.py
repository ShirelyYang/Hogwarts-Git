from appium import webdriver

from page.address_book import AddressBook
from page.basepage import BasePage


class App(BasePage):
    def start(self):
        _package = "com.tencent.wework"
        _activity = ".launch.WwMainActivity"
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "emulator-5554"
            caps["appPackage"] = _package
            caps["appActivity"] = _activity
            caps["autoGrantPermissions"] = True
            caps["noReset"] = True
            caps['skipServerInstallation'] = True
            caps['skipDeviceInitialization'] = True
            self._driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
            self._driver.implicitly_wait(3)
        else:
            self._driver.start_activity(_package, _activity)
        return self

    def goto_address_book(self):
        self.find(by="xpath", locator='//*[@text="通讯录"]').click()
        return AddressBook(self._driver)