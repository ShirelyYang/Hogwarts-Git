from pageobject.app import App


class TestMain:
    def test_main(self):
        self.main = App()
        self.main.start()