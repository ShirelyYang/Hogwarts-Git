from selenium.webdriver.common.by import By

from page_KX.basepage_KX import BasePageKX
from page_KX.search_KX import SearchKX


class MainPageKX(BasePageKX):
    _base_url = "https://testservice.kangxin.com/platform/home?path=%2Fhome"

    def goto_search(self):
        self.find(By.ID, "sbcx").click()
        return SearchKX(self._driver)

    def goto_mainland_registration(self):
        self.find(By.ID, "dlzc").click()

    def goto_mainlan_renew(self):
        pass