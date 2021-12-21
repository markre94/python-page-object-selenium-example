from pages.sign_in_page import CommonSignUpActions
import pytest

test_data = [('az', ['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt',
                     'Sauce Labs Fleece Jacket', 'Sauce Labs Onesie', 'Test.allTheThings() T-Shirt (Red)']),
             ('za', ['Test.allTheThings() T-Shirt (Red)', 'Sauce Labs Onesie', 'Sauce Labs Fleece Jacket',
                     'Sauce Labs Bolt T-Shirt', 'Sauce Labs Bike Light', 'Sauce Labs Backpack']),
             ('hilo', ['Sauce Labs Fleece Jacket', 'Sauce Labs Backpack', 'Sauce Labs Bolt T-Shirt',
                       'Test.allTheThings() T-Shirt (Red)', 'Sauce Labs Bike Light', 'Sauce Labs Onesie']),
             ('lohi', ['Sauce Labs Onesie', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt',
                       'Test.allTheThings() T-Shirt (Red)', 'Sauce Labs Backpack', 'Sauce Labs Fleece Jacket'])]


@pytest.mark.parametrize("sort_type,expected_sorted_item_list", test_data)
def test_sort_inventory_all_type(init_driver, sort_type, expected_sorted_item_list):
    sign_in = CommonSignUpActions(init_driver)
    main_page = sign_in.sign_in_with_normal_user()
    main_page.sort_items_in_page(sort_type)
    sorted_list = main_page.get_inventory_list_item_names()
    assert expected_sorted_item_list == sorted_list, "Item list don't match."


def test_inventory_page_smoke(init_driver):
    sign_in = CommonSignUpActions(init_driver)
    main_page = sign_in.sign_in_with_normal_user()



    assert True is main_page.are_inventory_items_visible()

    links = main_page.get_footer_link_responses()
    assert [200, 200, 999] == links
