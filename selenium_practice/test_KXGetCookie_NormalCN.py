import shelve
from time import sleep
from selenium import webdriver


class TestGetCookie:
    def test_get_cookie(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://service.kangxin.com/platform/home?path=%2Fhome")
        sleep(30)
        cookies = self.driver.get_cookies()
        db = shelve.open("mydb/KXCN_Normal_cookies")
        db['cookie'] = cookies
        db.close()

