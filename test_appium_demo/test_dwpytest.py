import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from time import sleep


class TestDW:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = "Android"
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = "emulator-5554"
        desired_caps['appPackage'] = "com.xueqiu.android"
        desired_caps['appActivity'] = ".view.WelcomeActivityAlias"
        desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.back()
        self.driver.quit()

    def test_search(self):
        """
        1.打开 雪球 app
        2.点击搜索输入框
        3.向搜索输入框里面输入  "阿里巴巴"
        4.在搜索结果里面选择  "阿里巴巴"，然后进行点击
        5.获取  阿里巴巴 的股价，并判断  这只股价的价格>200
        :return:
        """
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]').click()
        price = float(self.driver.find_element(MobileBy.XPATH,
                                               '//*[@resource-id="com.xueqiu.android:id/current_price" and @text="271.61"]')
                      .text)
        assert price > 200
        sleep(3)


if __name__ == '__main__':
    pytest.main()