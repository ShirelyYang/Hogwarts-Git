import pytest

from page_work.add_department_page_work import AddDepartmentPage
from page_work.main_page_work import MainPage


class TestAddDepartment:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.base_quit()

    @pytest.mark.skip
    def test_from_member_add_department(self):
        self.main.goto_add_member().goto_add_department().add_department()

    def test_from_contact_add_department(self):
        result = self.main.goto_contact().goto_add_department().add_department("XX测试中心").get_department()
        print(result)
        assert 'XX测试中心' in result

    def test_from_contact_add_department_fail(self):
        self.main.goto_contact().goto_add_department().add_department("")
        result = AddDepartmentPage(self.main._driver).get_error_message()
        print(result)
        assert result == "请输入部门名称"
