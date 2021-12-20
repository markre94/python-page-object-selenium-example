from pages.sign_in_page import CommonSignUpActions


def test_sort_inventory(init_driver):
    sign_in = CommonSignUpActions(init_driver)
    main_page = sign_in.sign_in_with_normal_user()
    main_page.item_list.sort_items_by_price_high_to_low()
    ls = main_page.get_inventory_list_item_names()
    assert ls[0] == 'Sauce Labs Fleece Jacket'
