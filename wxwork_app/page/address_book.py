import pytest
import yaml
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from page.basepage import BasePage


class AddressBook(BasePage):
    def scroll(self, by, locator):
        action = TouchAction(self._driver)
        window_rect = self._driver.get_window_rect()
        width = window_rect["width"]
        height = window_rect["height"]
        x1 = width * 0.5
        y1 = height * 0.7
        y2 = height * 0.3
        i = 0
        while i < 10:
            try:
                self.find(by, locator).click()
                break
            except Exception as e:
                action.press(x=x1, y=y1).wait(200).move_to(x=x1, y=y2).release().perform()
                i += 1

    # @pytest.mark.parametrize("name, gender, phonenum", get_contact())
    def add(self, name, gender, phonenum):
        self.scroll(by="xpath", locator='//*[@text="添加成员"]')
        self.find(by="xpath", locator='//*[@text="手动输入添加"]').click()
        self.find(by="xpath", locator='//*[@resource-id="com.tencent.wework:id/em7"]//*[@resource-id="com.tencent.wework:id/b4t"]').send_keys(name)
        self.find(by="xpath", locator='//*[@resource-id="com.tencent.wework:id/d5l"]//*[@resource-id="com.tencent.wework:id/b5v"]').click()
        self.find(by="xpath", locator=f'//*[@text="{gender}"]').click()
        self.find(by="xpath", locator='//*[@text="手机号"]').send_keys(phonenum)
        self.find(by="id", locator="i6k").click()
        sleep(3)
        self.find(by="id", locator="i63").click()
        # toast 弹框，打印当前页面的布局结构  xml结构
        # print(self._driver.page_source)
        toast_text = self.find(by="xpath", locator='//*[@class="android.widget.Toast"]').text
        return toast_text

    def delete(self, name):
        self.find(by="xpath", locator=f'//*[@text="{name}"]').click()
        self.find(by="id", locator="i6d").click()
        self.find(by="id", locator="b_x").click()
        self.scroll(by="id", locator="elh")
        self.find(by="id", locator="blx").click()
        sleep(3)
        name_lists = self.finds(by="xpath", locator='//*[@class="android.view.ViewGroup"]//*[@class="android.widget.TextView"]')
        member = []
        for name in name_lists:
            member.append(name.text)
        return member



