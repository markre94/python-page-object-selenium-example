from pages.sign_in_page import CommonSignUpActions
import pytest


def test_sort_inventory_all_type(init_driver):
    sign_in = CommonSignUpActions(init_driver)
    main_page = sign_in.sign_in_with_normal_user()
    main_page.add_item_to_cart_by_name('Sauce Labs Backpack')