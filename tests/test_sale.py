from decimal import Decimal

import pytest

from pages.sign_in_page import CommonSignUpActions
from utils.client_data import load_client_data


@pytest.fixture()
def data():
    return [dict(name='Sauce Labs Backpack', price=Decimal('29.99')),
            dict(name='Sauce Labs Bike Light', price=Decimal('15.99'))]


@pytest.fixture
def client_test_data(data):
    return {
        "client": load_client_data(),
        "items": data
    }


def test_sale_inventory_items(init_driver, client_test_data):
    sale_items_data = client_test_data['items']

    sign_in = CommonSignUpActions(init_driver)
    main_page = sign_in.sign_in_with_normal_user()

    main_page.add_item_to_cart_by_name(sale_items_data[0]['name'])
    main_page.add_item_to_cart_by_name(sale_items_data[1]['name'])

    assert 2 == main_page.get_qty_of_items_in_the_cart(), 'Number of items added to the cart differs from actual.'

    cart = main_page.open_cart()
    assert init_driver.current_url == "https://www.saucedemo.com/cart.html"
    cart_data = cart.get_all_cart_data()

    assert sale_items_data[0]['name'] in cart_data
    assert sale_items_data[1]['name'] in cart_data

    checkout_step_one = cart.click_checkout()
    checkout_step_one.fill_user_data(client_test_data['client'])
    checkout_overview = checkout_step_one.click_continue()
    checkout_complete = checkout_overview.click_finish()

    assert "THANK YOU FOR YOUR ORDER" == checkout_complete.get_header_complete(), "Wrong complete header msg."
    assert False is checkout_complete.is_image_broken(), "Image is broken."
    assert "Your order has been dispatched, and will arrive" \
           " just as fast as the pony can get there!" == checkout_complete.get_complete_text_msg()

    checkout_complete.click_back_home()


def test_abort_sale_inventory_remove_items_from_cart(init_driver, client_test_data):
    sale_items_data = client_test_data['items']

    sign_in = CommonSignUpActions(init_driver)
    main_page = sign_in.sign_in_with_normal_user()

    main_page.add_item_to_cart_by_name(sale_items_data[0]['name'])
    cart = main_page.open_cart()
    assert init_driver.current_url == "https://www.saucedemo.com/cart.html"
    assert sale_items_data[0]['name'] in cart.get_all_cart_data()

    cart.click_continue_shopping()

    main_page.add_item_to_cart_by_name(sale_items_data[1]['name'])
    cart = main_page.open_cart()
    assert init_driver.current_url == "https://www.saucedemo.com/cart.html"
    assert sale_items_data[1]['name'] in cart.get_all_cart_data()

    checkout_step_one = cart.click_checkout()
    cart = checkout_step_one.click_cancel()
    cart.remove_item_from_cart_by_name(sale_items_data[0]['name'])
    assert sale_items_data[0]['name'] not in cart.get_all_cart_data()

    cart.remove_item_from_cart_by_name(sale_items_data[1]['name'])
    assert sale_items_data[1]['name'] not in cart.get_all_cart_data()
    cart.click_continue_shopping()


def test_abort_sale_inventory_remove_item_from_main_page(init_driver, client_test_data):
    items = client_test_data['items']

    sign_in = CommonSignUpActions(init_driver)
    main_page = sign_in.sign_in_with_normal_user()
    main_page.add_item_to_cart_by_name(items[0]['name'])
    main_page.add_item_to_cart_by_name(items[1]['name'])
    assert 2 == main_page.get_qty_of_items_in_the_cart()
    cart = main_page.open_cart()

    assert items[0]['name'] in cart.get_all_cart_data()
    assert items[1]['name'] in cart.get_all_cart_data()
    main_page = cart.click_continue_shopping()
    main_page.remove_items_from_cart()

    assert 0 == main_page.get_qty_of_items_in_the_cart()
