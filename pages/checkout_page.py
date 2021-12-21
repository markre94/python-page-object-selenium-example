from pages.base_page import BasePage
from utils.locators import CheckoutStepOneLocators, CheckoutOverviewLocators, CheckoutCompleteLocators
from utils.client_data import Client


class CheckoutClientInfoPage(BasePage):
    def __init__(self, driver):
        self.locators = CheckoutStepOneLocators()
        super().__init__(driver, 'https://www.saucedemo.com/checkout-step-one.html')

    def type_in_first_name(self, name: str):
        self.find_element(*self.locators.FIRST_NAME_FORM).send_keys(name)

    def type_in_last_name(self, name: str):
        self.find_element(*self.locators.LAST_NAME_FROM).send_keys(name)

    def type_in_postal_code(self, code: int):
        self.find_element(*self.locators.POSTAL_CODE_FORM).send_keys(code)

    def fill_user_data(self, data: Client):
        self.type_in_first_name(data.first_name)
        self.type_in_last_name(data.last_name)
        self.type_in_postal_code(data.zip_code)

    def click_continue(self):
        self.find_element(*self.locators.CONTINUE_BTN).click()
        return CheckoutOverviewPage(self.driver)

    def click_cancel(self):
        self.find_element(*self.locators.CANCEL_BTN).click()


class CheckoutOverviewPage(BasePage):
    def __init__(self, driver):
        self.locators = CheckoutOverviewLocators()
        super().__init__(driver, 'https://www.saucedemo.com/checkout-step-two.html')

    def click_finish(self):
        self.find_element(*self.locators.FINISH_BTN).click()

    def click_cancel(self):
        self.find_element(*self.locators.CANCEL_BTN).click()

    def get_total_price_no_tax(self):
        return self.find_element(*self.locators.TOTAL_PRICE_NO_TAX).text

    def get_shipping_info(self):
        return self.find_element(*self.locators.SHIPPING_INFO).text


class CheckoutCompletePage(BasePage):
    def __init__(self, driver):
        self.locators = CheckoutCompleteLocators()
        super().__init__(driver, 'https://www.saucedemo.com/checkout-complete.html')

    def click_back_home(self):
        self.find_element(*self.locators.BACK_HOME_BTN).click()

    def get_header_complete(self):
        pass
