import allure
import pytest


class Test_Set:
    @staticmethod
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("This Testcase will check if the given set of items in the data set are correct roles or not")
    @allure.epic("Roles Management")
    @allure.parent_suite("Set Management")
    @pytest.mark.parametrize('roles_data', {'Administrator', 'Reader', 'Documenter'})
    def test_isRole(roles_data):
        fruits = {'Administrator', 'Reader', 'Documenter', 'Non-Administrator'}
        assert roles_data in fruits, f"{roles_data} is not a role"
