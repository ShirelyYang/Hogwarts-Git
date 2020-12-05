import pytest
from time import sleep
from page.app import App
from page.utils import Utils


class TestLogin:
    data = Utils.from_file("../datas/test_search.yaml")

    def setup_class(self):
        self.app = App()
        self.app.start()

    def teardown_class(self):
        self.app.stop()

    def setup(self):
        pass

    def teardown(self):
        self.app.goto_demopage().back()

    # todo: 测试数据的数据驱动
    @pytest.mark.parametrize('username, password', [
        ("user1", "password1"),
        ("user2", "password2")
    ])
    def test_login(self, username, password):
        # todo: 测试步骤的数据驱动
        self.app.goto_demopage().login(username, password)

    # @pytest.mark.parametrize('keyword', [
    #     'alibaba',
    #     # 'baidu',
    #     # 'jd'
    # ])
    @pytest.mark.parametrize(data['keys'], data['values'])
    def test_search(self, keyword):
        self.app.goto_demopage().search(keyword)
