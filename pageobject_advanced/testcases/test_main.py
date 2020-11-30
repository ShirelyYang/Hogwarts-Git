from time import sleep

import pytest
import yaml

from pageobject.app import App
from testcases.test_base import TestBase


class TestMain(TestBase):
    @pytest.mark.parametrize("value1, value2", yaml.safe_load(open("../datas/test_main.yaml")))
    def test_main(self, value1, value2):
        self.app.start().main().goto_search()
        print(value1)
        print(value2)

    def test_windows(self):
        print(yaml.safe_load(open("../datas/main.yaml"))[0])
        self.app.start().main().goto_windows()
