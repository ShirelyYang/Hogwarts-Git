from pages.base_page import BasePage


class Search(BasePage):
    def search(self, keyword):
        self.po_run("search", keyword=keyword)

    def back(self):
        self.po_run("back")
