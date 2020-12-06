from page.base_page import BasePage
from page.search import Search


class Main(BasePage):
    def goto_search(self):
        return Search(self._driver)
