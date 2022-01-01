import requests
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from utils.log import setup_custom_logger


logger = setup_custom_logger()


class BasePage:
    TIME_OUT = 10

    def __init__(self, driver, url: str):
        self.url = url
        self.driver = driver

    def open(self):
        if self.driver.current_url == self.url:
            return
        self.driver.get(self.url)
        logger.info(f'Opening browser and navigating to {self.url}')

    def find_element(self, *locator):
        elem = self.driver.find_element(*locator)
        logger.info(f"Found element with {elem.accessible_name}. Element location {elem.location}. ")
        return elem

    def find_elements(self, *locator):
        elems = self.driver.find_elements(*locator)
        logger.info(f"Found elements {elems}")
        return elems

    def get_title(self) -> str:
        title = self.driver.title
        logger.info(f"Current page title {title}")
        return title

    def get_url(self) -> str:
        url = self.driver.current_url
        logger.info(f"Current drivers url {url}")
        return url

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, self.TIME_OUT).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            logger.info(f"ELEMENT NOT FOUND WITHIN GIVEN TIME! --> {locator[1]}")

    def select_item_by_value(self, *locator, value: str):
        select = Select(self.driver.find_element(*locator))
        select.select_by_value(value)
        logger.info(f"Selecting element by value {value}")

    def is_link_broken(self, *locator) -> bool:
        link = self.driver.find_element(*locator).get_attribute('src')
        response = requests.head(link)
        logger.info(f"Links response code: {response.status_code}")
        return response.status_code != 200
