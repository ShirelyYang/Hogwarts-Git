from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from hamcrest import *


class TestParam:
    def setup(self):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["deviceName"] = "emulator-5554"
        desired_caps['platformVersion'] = "6.0"
        desired_caps['appPackage'] = 'com.xueqiu.android'
        # desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['appActivity'] = '.common.MainActivity'
        # 添加Android工作引擎，默认为 uiautomation2
        # desired_caps['automationName'] = 'uiautomation2'
        # 不对缓存进行处理 noReset
        desired_caps['noReset'] = True
        # 跳过一些安装，提高运行速度 skipServerInstallation
        desired_caps['skipServerInstallation'] = True
        desired_caps['dontStopAppOnReset'] = "true"
        # 支持输入中文：unicodeKeyBoard, resetKeyBoard
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.quit()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/action_close").click()

    @pytest.mark.parametrize('searchkey, type, expect_price', [
        ('alibaba', 'BABA', 280),
        ('xiaomi', '01810', 20)
    ])
    def test_param(self, searchkey, type, expect_price):
        """
        1.打开雪球应用
        2.点击搜索框
        3.输入 搜索词 'alibaba' or 'xiaomi'
        4.点击第一个搜索结果
        5.判断 股票价格
        :return:
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/name').click()
        locator = (MobileBy.XPATH,
                   f'//*[@resource-id="com.xueqiu.android:id/stockCode" and @text="{type}"]/../../..//'
                   '*[@resource-id="com.xueqiu.android:id/current_price"]')
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        ele = self.driver.find_element(*locator)
        current_price = float(ele.text)
        print(current_price)
        # expect_price = price
        assert_that(current_price, close_to(expect_price, expect_price*0.1))

