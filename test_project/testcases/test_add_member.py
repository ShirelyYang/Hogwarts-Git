from add_member_page_shizhan import AddMemberPage
from main_page_shizhan import MainPage
import pytest


class TestAddMember:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        # self.main._driver.quit()
        self.main.base_quit()

    def test_add_member(self):
        result = self.main.go_to_add_member().add_member("13588888888").get_member_list()
        assert "Shirely" in result

    def test_add_member_fail(self):
        self.main.go_to_add_member().add_member("ddffdsf")
        # result = self.main.go_to_add_member().get_phone_error_message()
        result = AddMemberPage(self.main._driver).get_phone_error_message()
        assert result == "请填写正确的手机号码"

    @pytest.mark.skip
    def test_contact_add_member(self):
        self.main.go_to_contact().go_to_add_member().add_member()