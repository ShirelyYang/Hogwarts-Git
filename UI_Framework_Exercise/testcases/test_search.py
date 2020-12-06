import pytest

from pages.app import App
from pages.utils import Utils


class TestSearch:
    data = Utils.from_file("../datas/test_search.yaml")

    def setup_class(self):
        self.app = App()
        self.app.start()

    def teardown_class(self):
        self.app.stop()

    def setup(self):
        pass

    def teardown(self):
        self.app.goto_main().goto_search().back()

    @pytest.mark.parametrize(data['keys'], data['values'])
    def test_search(self, keyword):
        self.app.goto_main().goto_search().search(keyword)
