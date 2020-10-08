from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep


class TestTouchAction:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = "Android"
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = "emulator-5554"
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_touch_action(self):
        action = TouchAction(self.driver)
        sleep(3)
        # wait 200ms
        # 根据定位坐标点去实现滑动操作 不推荐
        # action.press(x=294, y=1050).wait(200).move_to(x=294, y=230).release().perform()
        # 方法二：实现滑动
        # 获取当前屏幕的尺寸
        # print(self.driver.get_window_rect())
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y_start = int(height * 4/5)
        y_end = int(height * 1/5)
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()

