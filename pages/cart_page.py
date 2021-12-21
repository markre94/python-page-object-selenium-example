from pages.base_page import BasePage
from utils.locators import CartLocators
import pages.main_page as main_page


class CartPage(BasePage):
    def __init__(self, driver):
        self.locators = CartLocators()
        super().__init__(driver, 'https://www.saucedemo.com/cart.html')
        self.wait_for_cart_page_to_load()

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
        idx = self.find_elements(*self.locators.INVENTORY_ITEM_NAME).index(name)
        self.find_elements(*self.locators.REMOVE_BTN)[idx].click()

    def click_checkout(self):
        self.find_element(*self.locators.CHECKOUT_BTN)

    def click_continue_shopping(self):
        self.find_element(*self.locators.CONTINUE_SHOPPING_BTN).click()
        return main_page.MainPage(self.driver)

