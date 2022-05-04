from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


import pages.cart_page as cart_page
import pages.sign_in_page as sign_in_page
from pages.base_page import BasePage
from utils.locators import MainPageHeaderLocators, MainPageItemListLocators, InventoryItemLocators, \
    FooterMainPageLocators, SideBarLocators
from utils.link_response import LinkResponse


class MainPageHeader(BasePage):
    def __init__(self, driver):
        self.locators = MainPageHeaderLocators()
        self.side_bar_locators = SideBarLocators()
        super().__init__(driver, "https://www.saucedemo.com/invetory.html")

    def open_cart(self):
        self.find_element(*self.locators.SHOPPING_CART).click()

    @property
    def cart_items_qty(self):
        try:
            element = self.find_element(*self.locators.ITEMS_QTY_IN_THE_CART)
        except NoSuchElementException:
            return 0
        else:
            return int(element.text)

    def open_sidebar(self):
        self.find_element(*self.locators.SIDE_BAR).click()


class MainPageSideBar(BasePage):
    def __init__(self, driver):
        self.locators = SideBarLocators()
        super().__init__(driver, "https://www.saucedemo.com/invetory.html")

    def log_out(self):
        self.wait_element(*self.locators.LOGOUT_SIDEBAR, EC.element_to_be_clickable)
        self.find_element(*self.locators.LOGOUT_SIDEBAR).click()
        return sign_in_page.SignInPage(self.driver)


class MainPageItemList(BasePage):
    def __init__(self, driver):
        self.locators = MainPageItemListLocators()
        self.inv_item_locators = InventoryItemLocators()
        super().__init__(driver, "https://www.saucedemo.com/invetory.html")

    def sort_items_by_give_value(self, value: str):
        self.selection_base.select_by_value(*self.locators.SELECT_SORT_TYPE, value=value)

    def get_inventory_list_objects(self):
        return self.find_elements(*self.locators.INVENTORY_ITEM)

    def get_inventory_item_list(self):
        return self.find_elements(*self.locators.INVENTORY_ITEM_NAME)

    def get_inventory_remove_buttons(self):
        return self.find_elements(*self.inv_item_locators.REMOVE_FROM_CART)


class InventoryItemPage(BasePage):
    def __init__(self, driver):
        self.locators = InventoryItemLocators()
        super().__init__(driver, "https://www.saucedemo.com/invetory.html")

    def add_to_cart(self, idx):
        self.find_elements(*self.locators.ADD_TO_CARD_BTN)[idx].click()

    def remove_from_cart(self, idx):
        self.find_elements(*self.locators.REMOVE_FROM_CART)[idx].click()


class FooterMainPage(BasePage):
    def __init__(self, driver):
        self.locators = FooterMainPageLocators()
        super().__init__(driver, "https://www.saucedemo.com/invetory.html")

    def get_links_responses(self):
        responses = {}
        element = self.find_element(*self.locators.SOCIAL_LINKS)
        links = element.find_elements(By.TAG_NAME, 'a')
        for link in links:
            link_res = LinkResponse(link.get_attribute('href'))
            responses[link] = link_res.get_link_response()
        return responses


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, "https://www.saucedemo.com/invetory.html")
        self.header = MainPageHeader(self.driver)
        self.sidebar = MainPageSideBar(self.driver)
        self.item_list = MainPageItemList(self.driver)
        self.inventory_item = InventoryItemPage(self.driver)
        self.footer = FooterMainPage(self.driver)

    def get_inventory_list_item_names(self):
        items = self.item_list.get_inventory_item_list()
        return [item.text for item in items]

    def sort_items_in_page(self, value: str):
        self.item_list.sort_items_by_give_value(value)

    def add_item_to_cart_by_name(self, name: str):
        idx = self.get_inventory_list_item_names().index(name)
        self.inventory_item.add_to_cart(idx)

    def remove_items_from_cart(self):
        items_to_remove = self.item_list.get_inventory_remove_buttons()
        for item in items_to_remove:
            item.click()

    def open_cart(self):
        self.header.open_cart()
        return cart_page.CartPage(self.driver)

    def get_qty_of_items_in_the_cart(self):
        return self.header.cart_items_qty

    @property
    def cart_items_qty(self):
        return self.header.cart_items_qty

    def get_footer_link_responses(self):
        return self.footer.get_links_responses()

    def are_inventory_items_visible(self):
        items = self.item_list.get_inventory_item_list()
        for item in items:
            if not item.is_displayed():
                return False
        return True

    def side_bar_log_out(self):
        self.header.open_sidebar()
        return self.sidebar.log_out()