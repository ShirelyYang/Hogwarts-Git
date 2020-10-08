from page_appium.app import App


class TestSearch:
    def test_search(self):
        result = App().start().main().goto_market().goto_search().search("jd")
        assert "京东" in result