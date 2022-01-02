from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from utils.link_response import LinkResponse
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
        if elem:
            logger.info(f"Found element with {elem}. Element location {elem.location}.")
        else:
            logger.error(f"Element searched by {locator[0]} not found with {locator[1]}.")

        return elem

    def find_elements(self, *locator):
        elements = self.driver.find_elements(*locator)
        if elements:
            logger.info(f"Found elements: {elements}")
        else:
            logger.error(f"Elements searched by {locator[0]} not found.")
        return elements

    def get_title(self) -> str:
        title = self.driver.title
        if title:
            logger.info(f"Current page title {title}")
        else:
            logger.error(f"Title of the page unknown.")
        return title

    def get_url(self) -> str:
        url = self.driver.current_url
        if url:
            logger.info(f"Current drivers url {url}")
        else:
            logger.error(f"Current drivers url unknown.")
        return url

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, self.TIME_OUT).until(EC.presence_of_element_located(locator))
            logger.info(f"Presence of the element {locator[1]} searched by {locator[0]} detected.")
        except TimeoutException:
            logger.error(f"Element {locator[1]} searched by {locator[0]} not found at the given time.")

    def select_item_by_value(self, *locator, value: str) -> None:
        select = Select(self.driver.find_element(*locator))
        options = select.options
        select.select_by_value(value)
        logger.info(f"Selecting {value} 'by_value' from Select Object of the given options {options}")

    def is_link_element_broken(self, *locator, attribute: str = 'src') -> bool:
        link = LinkResponse(self.driver.find_element(*locator).get_attribute(attribute))
        link.request_head()
        return link.is_link_broken()