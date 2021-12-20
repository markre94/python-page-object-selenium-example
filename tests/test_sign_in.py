from time import sleep

from pages.sign_in_page import SignInPage
from utils.users_data import get_user


def test_sign_in_standard_user(init_driver):
    us = get_user('standard')
    sign_in = SignInPage(init_driver)
    sign_in.sign_in(us)

    assert init_driver.current_url == 'https://www.saucedemo.com/inventory.html'


def test_sign_in_locked_user(init_driver):
    user = get_user('locked_out')
    page = SignInPage(init_driver)
    page.sign_in(user)
    assert page.get_url() == page.url
    assert "Epic sadface: Sorry, this user has been locked out." == page.get_error_msg()
    page.close_error_login_msg_box()