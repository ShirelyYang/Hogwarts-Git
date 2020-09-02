import shelve

from selenium import webdriver
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
        db = shelve.open("mydb/logincookies")
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
