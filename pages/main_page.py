from pages.base_page import BasePage
from utils.locators import MainPageHeaderLocators, MainPageItemListLocators


class MainPageHeader(BasePage):
    def __init__(self, driver):
        self.locators = MainPageHeaderLocators()
        super().__init__(driver, "https://www.saucedemo.com/invetory.html")


class MainPageItemList(BasePage):
    def __init__(self, driver):
        self.locators = MainPageItemListLocators()
        super().__init__(driver, "https://www.saucedemo.com/invetory.html")

    def sort_items_a_to_z(self):
        self.select_item_by_value(*self.locators.SELECT_SORT_TYPE, value='az')

    def sort_items_z_to_a(self):
        self.select_item_by_value(*self.locators.SELECT_SORT_TYPE, value='za')

    def sort_items_by_price_low_to_high(self):
        self.select_item_by_value(*self.locators.SELECT_SORT_TYPE, value='lohi')

    def sort_items_by_price_high_to_low(self):
        self.select_item_by_value(*self.locators.SELECT_SORT_TYPE, value='hilo')

    def get_inventory_list_objects(self):
        return self.find_elements(*self.locators.INVENTORY_ITEM)

    def get_inventory_item_list(self):
        return self.find_elements(*self.locators.INVENTORY_ITEM_NAME)


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, "https://www.saucedemo.com/invetory.html")
        self.header = MainPageHeader(self.driver)
        self.item_list = MainPageItemList(self.driver)

    def get_inventory_list_item_names(self):
        items = self.item_list.get_inventory_item_list()
        return [item.text for item in items]
