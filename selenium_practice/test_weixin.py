import shelve

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

from selenium.webdriver.common.by import By


class TestDemo:
    def setup(self):
        # 复用浏览器
        # option = Options()
        # option.debugger_address = 'localhost:9222'
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_contact(self):
        sleep(3)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # self.driver.find_element_by_id("menu_contacts").click()

    def test_cookie(self):
        # cookies = self.driver.get_cookies()
        # print(cookies)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'QZM2zVaju8gicYIJvYPXyFHM7kNO9bU0-7pVw8uytCoY6GcZsXxtywUjtpieHo7bbtlqj_GF49Ub5vTkfTWM-esegkL2UbwxseYhi1sKZ1ydV0RrSW4dWKd971bR4kZsB6u6gCYdXYfJHG9FlzTnpJjeAGeyDQiG4mDZR4Cxx-IYCP4D3-lX-UxTIpSjkZ7YclXoZHhpcX6isc9kum2IorBwGp4jZkXCI_xfAjfohWmjDcmPVyG2dpFj3hTuY7Vkhh_uRRB4Ig0NGF0CVLBfrQ'}, {'domain': '.qq.com', 'expiry': 1599054933, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850770889759'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850770889759'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325048156169'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a7067712'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'uo-QflXh9v6QZB4C_gZdFZ5DsoB26Q4lmKnqXIXP62g9jN77VAiiNG7g6eND1iTr'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1630587157, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1598883133,1599051157'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1599051157'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '0315463'}, {'domain': '.qq.com', 'expiry': 1599138958, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1962883080.1598883134'}, {'domain': 'work.weixin.qq.com', 'expiry': 1599082436, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '4ua16an'}, {'domain': '.qq.com', 'expiry': 1662124558, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1850307641.1598883134'}, {'domain': '.work.weixin.qq.com', 'expiry': 1630419123, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1601646882, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}]
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        sleep(3)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_id("menu_contacts").click()

    def test_cookie1(self):
        # shelve  小型的数据库， 对象持久化保存方法
        # cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'QZM2zVaju8gicYIJvYPXyFHM7kNO9bU0-7pVw8uytCoY6GcZsXxtywUjtpieHo7bbtlqj_GF49Ub5vTkfTWM-esegkL2UbwxseYhi1sKZ1ydV0RrSW4dWKd971bR4kZsB6u6gCYdXYfJHG9FlzTnpJjeAGeyDQiG4mDZR4Cxx-IYCP4D3-lX-UxTIpSjkZ7YclXoZHhpcX6isc9kum2IorBwGp4jZkXCI_xfAjfohWmjDcmPVyG2dpFj3hTuY7Vkhh_uRRB4Ig0NGF0CVLBfrQ'}, {'domain': '.qq.com', 'expiry': 1599054933, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850770889759'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850770889759'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325048156169'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a7067712'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'uo-QflXh9v6QZB4C_gZdFZ5DsoB26Q4lmKnqXIXP62g9jN77VAiiNG7g6eND1iTr'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1630587157, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1598883133,1599051157'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1599051157'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '0315463'}, {'domain': '.qq.com', 'expiry': 1599138958, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1962883080.1598883134'}, {'domain': 'work.weixin.qq.com', 'expiry': 1599082436, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '4ua16an'}, {'domain': '.qq.com', 'expiry': 1662124558, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1850307641.1598883134'}, {'domain': '.work.weixin.qq.com', 'expiry': 1630419123, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1601646882, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}]
        db = shelve.open("mydb/logincookies")
        # db['cookie'] = cookies
        cookies = db['cookie']
        db.close()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        sleep(3)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_id("menu_contacts").click()

    def test_import_contact(self):
        db = shelve.open("mydb/logincookies")
        cookies = db['cookie']
        db.close()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(2)').click()
        self.driver.find_element(By.ID, 'js_upload_file_input').send_keys('/Users/yang/Documents/业务验证反馈表Feedback20200723.xlsx')
        sleep(3)
        assert self.driver.find_element(By.ID, "upload_file_name").text == "业务验证反馈表Feedback20200723.xlsx"