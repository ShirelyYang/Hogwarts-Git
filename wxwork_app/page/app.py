from appium import webdriver

from page.address_book import AddressBook
from page.basepage import BasePage


class App(BasePage):
    def start(self):
        """
        启动应用：
        如果driver已经被实例化，就复用已有的driver
        如果driver=None，就要重新创建一个driver
        :return:
        """
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
            # 启动任何一个包和activity
            self._driver.start_activity(_package, _activity)
            # 启动 caps 里面设置的 appPackage appActivity
            # self._driver.launch_app()
        return self

    def restart(self):
        self._driver.close_app()
        self._driver.launch_app()

    def goto_address_book(self):
        self.find(by="xpath", locator='//*[@text="通讯录"]').click()
        return AddressBook(self._driver)