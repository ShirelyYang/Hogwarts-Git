from pageobject.app import App


class TestBase:
    app = None

    def setup(self):
        self.app = App()

    def teardown(self):
        self.app.base_quit()