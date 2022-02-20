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
                              "https://www.saucedemo.com/")),
    (UserTypes.NO_DATA, ("Epic sadface: Username is required", "https://www.saucedemo.com/"))
]


@pytest.mark.parametrize('user_type,expected_result', sign_in_user_data)
def test_sign_in_user(sign_in_page, user_type, expected_result):
    user = get_user(user_type)

    sign_in_page.sign_in(user)

    assert sign_in_page.page_url == expected_result[1]
    logger.info(f"Checking current page url.")
    assert expected_result[0] == sign_in_page.get_sign_in_error_msg()
    logger.info("Checking if error message appeared.")


def test_go_to_page_inventory_without_signing_in(init_driver):
    page = SignInPage(init_driver)
    init_driver.get("https://www.saucedemo.com/inventory.html")
    error_msg = "Epic sadface: You can only access '/inventory.html' when you are logged in."
    assert init_driver.current_url == "https://www.saucedemo.com/"
    assert page.get_sign_in_error_msg() == error_msg


def test_log_out(main_page):
    sign_in_page = main_page.side_bar_log_out()
    assert sign_in_page.page_url == "https://www.saucedemo.com/"
