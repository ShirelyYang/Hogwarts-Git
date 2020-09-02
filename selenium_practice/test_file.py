from selenium import webdriver
from time import sleep


class TestFile:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_file(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_id("sttb").click()
        self.driver.find_element_by_id("stfile").send_keys(r"D:\work\img\ab.jpg")
        sleep(3)

