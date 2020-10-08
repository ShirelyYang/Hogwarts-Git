from appium import webdriver
import pytest
from hamcrest import *


class TestGetAttr:
    def setup(self):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["deviceName"] = "emulator-5554"
        desired_caps['platformVersion'] = "6.0"
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['dontStopAppOnReset'] = "true"
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_get_attr(self):
        search_ele = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(search_ele.get_attribute("text"))

    @pytest.mark.skip
    def test_assert(self):
        assert 'h' in 'this'

    def test_hamrest(self):
        assert_that(10, equal_to(10))
        assert_that(8, close_to(10, 2))

