import pytest
import yaml

from page.app import App

def get_contact():
    with open("../datas/contacts.yml") as f:
        datas = yaml.safe_load(f)
    print(datas)
    return datas


class TestDelete:
    def setup(self):
        self.main = App()

    def teardown(self):
        self.main.base_quit()

    @pytest.mark.parametrize("name, gender, phonenum", get_contact())
    def test_delete(self, name, gender, phonenum):
        member = self.main.start().goto_address_book().delete(name)
        assert name not in member
