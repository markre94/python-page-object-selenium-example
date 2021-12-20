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


class MainPageHeaderLocators:
    pass
