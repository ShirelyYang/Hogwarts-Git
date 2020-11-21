from page.app import App


class TestAdd:
    def setup(self):
        self.main = App()

    def teardown(self):
        self.main.base_quit()

    def test_add(self):
        # lists = self.main.start().goto_address_book().add()
        # assert "亚历山大" in lists
        toast = self.main.start().goto_address_book().add()
        assert "添加成功" == toast
