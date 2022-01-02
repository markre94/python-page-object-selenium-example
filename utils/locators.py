from selenium.webdriver.common.by import By


class SignInPageLocators:
    USERNAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.ID, 'login-button')
    LOG_CREDS = (By.ID, 'log_credentials')
    LOGIN_PASSWD = (By.ID, 'login_password')
    ERROR_BOX = (By.CLASS_NAME, 'error-message-container')
    ERROR_BOX_CLOSE_BTN = (By.CLASS_NAME, 'error-button')


class MainPageItemListLocators:
    INVENTORY_ITEM = (By.CLASS_NAME, 'inventory_item')
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, 'inventory_item_name')
    SELECT_SORT_TYPE = (By.CLASS_NAME, 'product_sort_container')
    INVENTORY_BTN = (By.CLASS_NAME, 'btn_inventory')


class MainPageHeaderLocators:
    SHOPPING_CART = (By.CLASS_NAME, 'shopping_cart_link')
    ITEMS_QTY_IN_THE_CART = (By.CLASS_NAME, 'shopping_cart_badge')
    SIDE_BAR = (By.ID, 'react-burger-menu-btn')


class SideBarLocators:
    INVENTORY_LINK = (By.ID, 'inventory_sidebar_link')
    ABOUT_SIDEBAR_LINK = (By.ID, 'about_sidebar_link')
    LOGOUT_SIDEBAR = (By.ID, 'logout_sidebar_link')
    RESET_APP = (By.ID, 'reset_sidebar_link')


class InventoryItemLocators:
    PRICE = (By.CLASS_NAME, 'inventory_item_price')
    ADD_TO_CARD_BTN = (By.CLASS_NAME, 'btn_inventory')
    ITEM_DESCRIPTION = (By.CLASS_NAME, 'inventory_item_desc')
    REMOVE_FROM_CART = (By.XPATH, '//button[text()="Remove"]')


class FooterMainPageLocators:
    SOCIAL_LINKS = (By.CLASS_NAME, 'social')
    FOOTER_COPYRIGHTS = (By.CLASS_NAME, 'footer_copy')
    FOOTER_ROBOT_IMG = (By.CLASS_NAME, 'footer_robot')


class CartLocators:
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, 'inventory_item_name')
    CART_QTY = (By.CLASS_NAME, 'cart_quantity')
    INVENTORY_ITEM_PRICE = (By.CLASS_NAME, 'inventory_item_price')
    CART_CONTENTS = (By.ID, 'cart_contents_container')
    CONTINUE_SHOPPING_BTN = (By.ID, 'continue-shopping')
    CHECKOUT_BTN = (By.ID, 'checkout')
    REMOVE_BTN = (By.CLASS_NAME, 'cart_button')


class CheckoutStepOneLocators:
    FIRST_NAME_FORM = (By.ID, 'first-name')
    LAST_NAME_FROM = (By.ID, 'last-name')
    POSTAL_CODE_FORM = (By.ID, 'postal-code')
    CANCEL_BTN = (By.ID, 'cancel')
    CONTINUE_BTN = (By.ID, 'continue')
    ERROR_MSG = (By.CLASS_NAME, 'error-message-container')


class CheckoutOverviewLocators:
    FINISH_BTN = (By.ID, 'finish')
    CANCEL_BTN = (By.ID, 'cancel')
    INVENTORY_ITEM_PRICE = (By.CLASS_NAME, 'inventory_item_price')
    TOTAL_PRICE_NO_TAX = (By.CLASS_NAME, 'summary_subtotal_label')
    TOTAL_TAX = (By.CLASS_NAME, 'summary_tax_label')
    SUMMARY_TOTAL = (By.CLASS_NAME, 'summary_total_label')
    SHIPPING_INFO = (By.CLASS_NAME, 'summary_value_label')


class CheckoutCompleteLocators:
    BACK_HOME_BTN = (By.ID, 'back-to-products')
    COMPLETE_HEADER = (By.CLASS_NAME, 'complete-header')
    COMPLETE_TEXT = (By.CLASS_NAME, 'complete-text')
    PONY_IMG = (By.CLASS_NAME, 'pony_express')
