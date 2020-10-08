from appium import webdriver
from time import sleep


class TestAttr:
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
        self.driver.quit()

    def test_attr(self):
        """
        1.打开【雪球】应用首页
        2.定位首页的搜索框
        3.判断搜索框是否可用，并查看搜索框name属性值
        4.打印搜索框这个元素的左上角坐标和它的宽高
        5.想搜索框输入：alibaba
        6.判断【阿里巴巴】是否可见
        7.如果可见，打印"搜索成功"点击，如果不可见，打印"搜索失败"
        :return:
        """
        search_inp = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        if search_inp.is_enabled():
            print(search_inp.get_attribute("name"))
            print(search_inp.location)
            print(search_inp.size)
            sleep(3)
            search_inp.click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        search_res = self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴" ]')
        if search_res.is_displayed():
            print("搜索成功")
        else:
            print("搜索失败")

