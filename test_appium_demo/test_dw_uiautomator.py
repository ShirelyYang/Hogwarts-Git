from appium import webdriver
from time import sleep
import pytest


class TestDwUiautomator:
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
    def test_dw_uiautomator(self):
        """
        1. 进入雪球，点击我的，进入到个人信息页面
        2. 点击登录，进入到登录页面
        3.输入用户名，输入密码
        4.点击登录
        :return:
        """
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("登录雪球")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId('
                                                        '"com.xueqiu.android:id/login_account")').send_keys(
            "yangcx0123@126.com"
        )
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId('
                                                        '"com.xueqiu.android:id/login_password")').send_keys(
            "abc13623544409"
        )
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId('
                                                        '"com.xueqiu.android:id/button_next")').click()
        msg = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("'
                                                              'com.xueqiu.android:id/md_content")')
        print(msg)
        assert msg.text == "请求太频繁，请稍后再试"

    def test_scroll_find_element(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/title_text")'
                                                        '.text("关注")').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                                                        '.scrollIntoView(new UiSelector().text("niliuyuyue").instance(0));')
