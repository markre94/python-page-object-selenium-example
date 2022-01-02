from pages.base_page import BasePage
from pages.main_page import MainPage
from utils.locators import SignInPageLocators
from utils.users_data import User, get_user, UserTypes


class SignInPage(BasePage):
    def __init__(self, driver):
        self.locators = SignInPageLocators()
        super().__init__(driver, "https://www.saucedemo.com/")
        self.open()

    def enter_user_name(self, user_name: str):
        self.find_element(*self.locators.USERNAME).send_keys(user_name)

    def enter_password(self, password: str):
        self.find_element(*self.locators.PASSWORD).send_keys(password)

    def click_login_btn(self):
        self.find_element(*self.locators.LOGIN_BTN).click()

    def sign_in(self, user: User):
        self.enter_user_name(user.name)
        self.enter_password(user.password)
        self.click_login_btn()

    def get_error_msg(self):
        return self.get_element_message(*self.locators.ERROR_BOX)

    def close_error_login_msg_box(self):
        self.find_element(*self.locators.ERROR_BOX_CLOSE_BTN).click()


class CommonSignUpActions:
    def __init__(self, driver):
        self.page = SignInPage(driver)

    def sign_in_with_normal_user(self):
        user = get_user(UserTypes.STANDARD)
        self.page.sign_in(user)
        return MainPage(self.page.driver)

    def sign_in_with_problem_user(self):
        user = get_user(UserTypes.PROBLEM)
        self.page.sign_in(user)
        return MainPage(self.page.driver)
