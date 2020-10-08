from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestTouchActionUnlock:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = "Android"
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = "emulator-5554"
        desired_caps['appPackage'] = 'cn.kmob.screenfingermovelock'
        desired_caps['appActivity'] = 'com.samsung.ui.MainActivity'
        desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_touch_action_unlock(self):
        print("解锁收拾密码")
        action = TouchAction(self.driver)
        action.press(x=116, y=187).wait(200).move_to(x=350,y=187).wait(200).move_to(x=586, y=187).wait(200).move_to(x=586, y=422)\
            .wait(200).move_to(x=586, y=655).wait(200).release().perform()