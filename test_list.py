import pytest


class Test_List:
    @staticmethod
    @pytest.mark.parametrize('list_data', ['Apple', 'Banana', 'Orange'])
    def test_isFruit(list_data):
        fruits = ['Apple', 'Mango', 'Banana', 'Orange']
        assert list_data in fruits, f"{list_data} is not a fruit"
