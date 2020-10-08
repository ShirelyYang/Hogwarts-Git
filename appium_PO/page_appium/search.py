from page_appium.appium_base_page import AppiumBasePage


class Search(AppiumBasePage):
    def search(self, value):
        self._params["value"] = value
        self.steps("../page_appium/search.yaml")
        # result = self.steps("../page_appium/result.yaml")
        result = self.find(by="xpath", locator='//*[@text="京东"]')
        print(result.text)
        return result.text
