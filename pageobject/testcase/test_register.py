from main import Main


class TestRegister:
    def setup(self):
        self.main = Main()

    def test_register(self):
        # assert self.main.goto_register().register() == None
        assert self.main.goto_login().register().register() == None

