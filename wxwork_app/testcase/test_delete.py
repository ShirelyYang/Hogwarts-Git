from page.app import App


class TestDelete:
    def setup(self):
        self.main = App()

    def teardown(self):
        self.main.base_quit()

    def test_delete(self):
        name = self.main.start().goto_address_book().delete()
        assert "亚历山大" not in name
