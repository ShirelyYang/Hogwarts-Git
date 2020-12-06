from pages.base_page import BasePage
from pages.search import Search


class Main(BasePage):
    def goto_search(self):
        return Search(self._driver)