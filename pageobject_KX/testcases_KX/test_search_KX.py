from page_KX.mainpage_KX import MainPageKX


class TestSearchKX:
    def setup(self):
        self.main = MainPageKX()

    def teardown(self):
        self.main._base_quit()

    def test_search_image_kx(self):
        result = self.main.goto_search().search_image()
        assert result.text == "31665893"

    def test_search_text_kx(self):
        result = self.main.goto_search().searh_text()
        assert result.text == "307809"
