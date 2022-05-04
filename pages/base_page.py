from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from utils.link_response import LinkResponse
from utils.log import setup_custom_logger

logger = setup_custom_logger()


class ItemSelectionBase:
    def __init__(self, driver):
        self.driver = driver

    def create_select(self, *locator):
        return Select(self.driver.find_element(*locator))

    def select_by_value(self, *locator, value: str):
        select = self.create_select(*locator)
        options = select.options
        select.select_by_value(value)
        logger.info(f"Selecting {value} 'by_value' from Select Object of the given options {options}")


class ErrorMsgHandler:
    def __init__(self, driver):
        self.driver = driver

    def get_error_message(self, *locator):
        try:
            return self.driver.find_element(*locator).text
        except NoSuchElementException:
            logger.warning("Not found message element. Returning ''")
            return ""


class LinkResponseHandler:
    def __init__(self, driver):
        self.driver = driver

    def is_link_element_broken(self, *locator, attribute: str = 'src') -> bool:
        link = LinkResponse(self.driver.find_element(*locator).get_attribute(attribute))
        link.request_head()
        return link.is_link_broken()


class BasePage:
    TIME_OUT = 10

    def __init__(self, driver, url: str):
        self._url = url
        self.driver = driver
        self.selection_base = ItemSelectionBase(self.driver)
        self.error_msg_handler = ErrorMsgHandler(self.driver)
        self.link_resp = LinkResponseHandler(self.driver)

    def open(self):
        if self.driver.current_url == self._url:
            return
        self.driver.get(self._url)
        logger.info(f'Opening browser and navigating to {self._url}')

    def find_element(self, *locator):
        elem = self.driver.find_element(*locator)
        if elem:
            logger.info(f"Found element with {locator[1]} {locator[0]}locator. Element location {elem.location}.")
        else:
            logger.error(f"Element searched by {locator[0]} not found with {locator[1]}.")

        return elem

    def find_elements(self, *locator):
        elements = self.driver.find_elements(*locator)
        if elements:
            logger.info(f"Found {len(elements)} elements with locator {locator[1]}.")
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

    @property
    def page_url(self) -> str:
        url = self.driver.current_url
        if url:
            logger.info(f"Current drivers url {url}")
        else:
            logger.error(f"Current drivers url unknown.")
        return url

    def wait_element(self, locator, condition=None):
        if condition is None:
            condition = EC.presence_of_element_located

        try:
            WebDriverWait(self.driver, self.TIME_OUT).until(condition(locator))
            logger.info(f"Presence of the element {locator[1]} searched by {locator[0]} detected.")
        except TimeoutException:
            logger.error(f"Element {locator[1]} searched by {locator[0]} not found at the given time.")