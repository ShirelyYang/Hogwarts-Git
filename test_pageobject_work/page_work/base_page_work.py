import shelve

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        self._driver = ""
        if driver is None:
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver

        db = shelve.open("../../test_project/cookie_db/weixin_cookie")
        cookies = db['cookie']
        db.close()

        if self._base_url != "":
            self._driver.get(self._base_url)

        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self._driver.add_cookie(cookie)

        if self._base_url != "":
            self._driver.get(self._base_url)

        self._driver.maximize_window()
        self._driver.implicitly_wait(3)

    def base_quit(self):
        return self._driver.quit()

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)
