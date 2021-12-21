from pages.base_page import BasePage
from utils.locators import MainPageHeaderLocators, MainPageItemListLocators, InventoryItemLocators
import pages.cart_page as cart_page


class MainPageHeader(BasePage):
    def __init__(self, driver):
        self.locators = MainPageHeaderLocators()
        super().__init__(driver, "https://www.saucedemo.com/invetory.html")

    def open_cart(self):
        self.find_element(*self.locators.SHOPPING_CART).click()

    def get_qty_of_items_in_the_cart(self):
        return int(self.find_element(*self.locators.ITEMS_QTY_IN_THE_CART).text)


class MainPageItemList(BasePage):
    def __init__(self, driver):
        self.locators = MainPageItemListLocators()
        super().__init__(driver, "https://www.saucedemo.com/invetory.html")

    def sort_items_by_give_value(self, value: str):
        self.select_item_by_value(*self.locators.SELECT_SORT_TYPE, value=value)

    def get_inventory_list_objects(self):
        return self.find_elements(*self.locators.INVENTORY_ITEM)

    def get_inventory_item_list(self):
        return self.find_elements(*self.locators.INVENTORY_ITEM_NAME)


class InventoryItemPage(BasePage):
    def __init__(self, driver):
        self.locators = InventoryItemLocators()
        super().__init__(driver, "https://www.saucedemo.com/invetory.html")

    def add_to_cart(self, idx):
        self.find_elements(*self.locators.ADD_TO_CARD_BTN)[idx].click()


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, "https://www.saucedemo.com/invetory.html")
        self.header = MainPageHeader(self.driver)
        self.item_list = MainPageItemList(self.driver)
        self.inventory_item = InventoryItemPage(self.driver)

    def get_inventory_list_item_names(self):
        items = self.item_list.get_inventory_item_list()
        return [item.text for item in items]

    def sort_items_in_page(self, value: str):
        self.item_list.sort_items_by_give_value(value)

    def add_item_to_cart_by_name(self, name: str):
        idx = self.get_inventory_list_item_names().index(name)
        self.inventory_item.add_to_cart(idx)

    def open_cart(self):
        self.header.open_cart()
        return cart_page.CartPage(self.driver)

    def get_qty_of_items_in_the_cart(self):
        return self.header.get_qty_of_items_in_the_cart()