import requests
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    TIME_OUT = 10

    def __init__(self, driver, url: str):
        self.url = url
        self.driver = driver

    def open(self):
        if self.driver.current_url == self.url:
            print("Wychodze z funkcji")
            return
        self.driver.get(self.url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def get_title(self) -> str:
        return self.driver.title

    def get_url(self) -> str:
        return self.driver.current_url

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, self.TIME_OUT).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print(f"\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> {locator[1]}")

    def select_item_by_value(self, *locator, value: str):
        select = Select(self.driver.find_element(*locator))
        select.select_by_value(value)

    def is_link_broken(self, *locator) -> bool:
        link = self.driver.find_element(*locator).get_attribute('src')
        response = requests.head(link)
        return response.status_code != 200
