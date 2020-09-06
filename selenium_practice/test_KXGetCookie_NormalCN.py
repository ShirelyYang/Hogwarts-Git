from time import sleep

from base import Base


class TestGetCookie(Base):
    def test_get_cookie(self):
        self.driver.get("https://service.kangxin.com/platform/home?path=%2Fhome")
        sleep(30)
        cookies = self.driver.get_cookies()
        print(cookies)


