from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestToast:
    def setup(self):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["deviceName"] = "emulator-5554"
        desired_caps['platformVersion'] = "6.0"
        desired_caps['appPackage'] = 'com.touchboarder.android.api.demos'
        desired_caps['appActivity'] = 'com.example.android.apis.view.PopupMenu1'
        # 添加Android工作引擎，默认为 uiautomation2
        desired_caps['automationName'] = 'uiautomation2'
        desired_caps['dontStopAppOnReset'] = "true"
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_toast(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="Make a Popup!"]').click()
        self.driver.find_element_by_xpath('//*[@text="Search"]').click()
        # print(self.driver.page_source)
        # 通过class属性值定位
        # print(self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text)
        # 通过text属性值定位
        # print(self.driver.find_element(MobileBy.XPATH, '//*[@text="Clicked popup menu item Search"]').text)
        # contains 为包含的意思
        print(self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "Clicked popup")]').text)