import allure
import pytest


class Test_List:
    @staticmethod
    @allure.title("Fruits Check")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("This Testcase will check if the given set of items in the data list are fruits or not")
    @allure.epic("Fruits Management")
    @allure.parent_suite("Fruits Management")
    @pytest.mark.parametrize('list_data', ['Apple', 'Banana', 'Orange'])
    def test_isFruit(list_data):
        fruits = ['Apple', 'Mango', 'Banana', 'Orange']
        assert list_data in fruits, f"{list_data} is not a fruit"

    @staticmethod
    @allure.title("Birds Check")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("This Testcase will check if the given set of items in the data list are Vehicles or not")
    @allure.epic("Vehicles Management")
    @allure.parent_suite("Vehicles Management")
    @pytest.mark.parametrize('list_data', ['Bycycle', 'TriCycle', 'MotorCycle', 'Water Bottle'])
    def test_isFruit(list_data):
        vehicles = ['Bus', 'Car', 'ByCycle', 'TriCycle', 'MotorCycle']
        assert list_data in vehicles, f"{list_data} is not a fruit"
