import pytest
import yaml

from pageobject.app import App


class TestMain:
    @pytest.mark.parametrize("value1, value2", yaml.safe_load(open("../datas/test_main.yaml")))
    def test_main(self, value1, value2):
        self.main = App()
        self.main.start()
        print(value1)
        print(value2)
