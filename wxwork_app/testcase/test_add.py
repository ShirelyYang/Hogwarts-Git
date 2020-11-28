import pytest
import yaml

from page.app import App


def get_contact():
    with open("../datas/contacts.yml") as f:
        datas = yaml.safe_load(f)
    print(datas)
    return datas


class TestAdd:
    def setup(self):
        self.main = App()

    def teardown(self):
        self.main.base_quit()

    @pytest.mark.parametrize("name, gender, phonenum", get_contact())
    def test_add(self, name, gender, phonenum):
        # lists = self.main.start().goto_address_book().add()
        # assert "亚历山大" in lists
        toast = self.main.start().goto_address_book().add(name, gender, phonenum)
        assert "添加成功" == toast
