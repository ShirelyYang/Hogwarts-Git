import shelve

from selenium import webdriver
from time import sleep


class GetCookie:
    def get_cookie(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(10)
        cookies = self.driver.get_cookies()
        db = shelve.open("../cookie_db/weixin_cookie")
        db['cookie'] = cookies
        db.close()


GetCookie().get_cookie()
