import pytest

from pages.sign_in_page import SignInPage
from utils.log import setup_custom_logger
from utils.users_data import get_user, UserTypes

logger = setup_custom_logger()

sign_in_user_data = [
    (UserTypes.STANDARD, ("", "https://www.saucedemo.com/inventory.html")),
    (UserTypes.LOCKED_OUT, ("Epic sadface: Sorry, this user has been locked out.", "https://www.saucedemo.com/")),
    (UserTypes.PROBLEM, ("", "https://www.saucedemo.com/inventory.html")),
    (UserTypes.PERFORMANCE_GLITCH, ("", "https://www.saucedemo.com/inventory.html")),
    (UserTypes.INVALID_DATA, ("Epic sadface: Username and password do not match any user in this service",
                              "https://www.saucedemo.com/"))
]


@pytest.mark.parametrize('user_type,expected_result', sign_in_user_data)
def test_sign_in_user(init_driver, user_type, expected_result):
    user = get_user(user_type)

    page = SignInPage(init_driver)
    page.sign_in(user)

    assert page.page_url == expected_result[1]
    logger.info(f"Checking current page url.")
    assert expected_result[0] == page.get_error_msg()
    logger.info("Checking if error message appeared.")
