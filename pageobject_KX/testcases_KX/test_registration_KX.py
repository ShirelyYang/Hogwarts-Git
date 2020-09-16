from page_KX.mainpage_KX import MainPageKX


class TestMainlandReg:
    def setup(self):
        self.main = MainPageKX()

    def teardown(self):
        self.main._base_quit()

    def test_mainland_registration(self):
        result = self.main.goto_mainland_registration().mainland_registration()
        assert result.text == "您的订单已提交！"
