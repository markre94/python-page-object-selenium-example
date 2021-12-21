import pytest

from pages.sign_in_page import CommonSignUpActions
from decimal import Decimal


@pytest.fixture()
def data():
    item_1_data = dict(name='Sauce Labs Backpack', price=Decimal('29.99'))
    item_2_data = dict(name='Sauce Labs Bike Light', price=Decimal('15.99'))
    return [item_1_data, item_2_data]


def test_sale_inventory_items(init_driver, data):
    sale_items_data = data

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

    cart.click_continue_shopping()



