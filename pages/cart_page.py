import pages.main_page as main_page
from pages.base_page import BasePage
from utils.locators import CartLocators
from pages.checkout_page import CheckoutClientInfoPage


class CartPage(BasePage):
    def __init__(self, driver):
        self.locators = CartLocators()
        super().__init__(driver, 'https://www.saucedemo.com/cart.html')

    def get_inventory_item_name_list_from_cart(self):
        items = self.find_elements(*self.locators.INVENTORY_ITEM_NAME)
        return [item.text for item in items]

    def get_item_names_added_to_basket(self):
        return self.find_elements(*self.locators.INVENTORY_ITEM_NAME)

    def get_all_cart_data(self):
        names = self.get_item_names_added_to_basket()
        prices = self.find_elements(*self.locators.INVENTORY_ITEM_PRICE)
        quantities = self.find_elements(*self.locators.CART_QTY)

        return {n.text: {'price': p.text, 'qty': q.text} for n, p, q in zip(names, prices, quantities)}

    def wait_for_cart_page_to_load(self):
        self.wait_element(*self.locators.CART_CONTENTS)

    def remove_item_from_cart_by_name(self, name):
        idx = self.get_inventory_item_name_list_from_cart().index(name)
        self.find_elements(*self.locators.REMOVE_BTN)[idx].click()

    def click_checkout(self):
        self.find_element(*self.locators.CHECKOUT_BTN).click()
        return CheckoutClientInfoPage(self.driver)

    def click_continue_shopping(self):
        self.find_element(*self.locators.CONTINUE_SHOPPING_BTN).click()
        return main_page.MainPage(self.driver)
