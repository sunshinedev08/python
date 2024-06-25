import allure
import pytest


class Test_Set:
    @staticmethod
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("This Testcase will check if the given set of items in the data Dictionary are correct Users "
                        "or not")
    @allure.epic("User Management")
    @allure.parent_suite("Dict Management")
    @pytest.mark.parametrize('user_data', [{
        "Name": "Admin",
        "Surname": "User",
        "Email Address": "admin.user@example.com",
        "username": "admin.user"
    }])
    def test_isUser(user_data):
        users = [{
            "Name": "Admin",
            "Surname": "User",
            "Email Address": "admin.user@example.com",
            "username": "admin.user"
        },
            {
                "Name": "Reader",
                "Surname": "User",
                "Email Address": "reader.user@example.com",
                "username": "reader.user"
            }
        ]
        assert user_data in users, f"{user_data['Name']} is not a valid User"
