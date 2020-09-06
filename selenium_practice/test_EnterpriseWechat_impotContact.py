import os
import shelve
import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from time import sleep


class TestEnteriseWechat:
    def setup(self):
        self.driver = webdriver.Chrome()
        # 浏览器最大化
        self.driver.maximize_window()
        # 每次操作隐式等待3秒
        self.driver.implicitly_wait(3)

    def teardown(self):
        # 测试用例执行完成后，退出浏览器
        self.driver.quit()

    def test_import_contact(self):
        # 从shelve   小型数据库中  读取数据
        db = shelve.open("../test_project/cookie_db/weixin_cookie")
        # db = shelve.open("../test_project/cookie_db/weixin_cookie")
        cookies = db["cookie"]
        db.close()
        # 获取登录前网址
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 复用cookie
        for cookie in cookies:
            # 去掉cookie中的expiry键值对
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            # 循环读取cookies列表，添加到cookie中
            self.driver.add_cookie(cookie)
        # 利用从shelve中读取的cookie，再次访问网址
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # CSS定位导入元素
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        # ID定位上传文件按钮，并实现上传操作
        self.driver.find_element(By.ID, "js_upload_file_input").send_keys("/Users/yang/Documents/test.xlsx")
        # 通过获取导入文件名称元素的text属性，断言文件是否导入成功
        assert self.driver.find_element(By.ID, "upload_file_name").text == "test.xlsx"
        # 强制等待3秒，加强效果
        sleep(3)

    def test_cookie(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(10)
        cookies = self.driver.get_cookies()
        # print(cookies)
        # cookies = [
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
        #      'value': '17162754233138488'}, {'domain': 'work.weixin.qq.com', 'expiry': 1599334674, 'httpOnly': True,
        #                                      'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '287vv9r'}, {
        #         'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
        #         'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'expiry': 1630839138, 'httpOnly': False,
        #                              'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {
        #         'domain': '.work.weixin.qq.com', 'expiry': 1601895139, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
        #         'path': '/', 'secure': False, 'value': 'zh-cn'}]
        db = shelve.open("../test_project/cookie_db/weixin_cookie")
        db['cookie'] = cookies
        db.close()
