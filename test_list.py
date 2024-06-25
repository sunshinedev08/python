import allure
import pytest


class Test_List:
    @staticmethod
    @allure.title("Fruits Check")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("This Testcase will check if the given set of items in the data list are fruits or not")
    @allure.epic("Fruit Management")
    @allure.parent_suite("List Management")
    @pytest.mark.parametrize('fruits_data', ['Apple', 'Banana', 'Orange'])
    def test_isFruit(fruits_data):
        fruits = ['Apple', 'Mango', 'Banana', 'Orange']
        assert fruits_data in fruits, f"{fruits_data} is not a fruit"

    @staticmethod
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("This Testcase will check if the given set of items in the data list are Vehicles or not")
    @allure.epic("Vehicles Management")
    @allure.parent_suite("List Management")
    @pytest.mark.parametrize('vehicles_data', ['ByCycle', 'TriCycle', 'MotorCycle', 'Water Bottle'])
    def test_isVehicle(vehicles_data):
        vehicles = ['Bus', 'Car', 'ByCycle', 'TriCycle', 'MotorCycle']
        assert vehicles_data in vehicles, f"{vehicles_data} is not a Vehicle"
