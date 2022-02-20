import json
import os
from dataclasses import dataclass

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.sign_in_page import SignInPage, CommonSignUpActions

from utils.log import setup_custom_logger

logger = setup_custom_logger()


@dataclass
class TestConfig:
    browser: str
    implicit_wait: int
    headless: bool


@allure.step("Load configuration data")
def config():
    config_file = os.path.join("/Users/marcin94/PycharmProjects/sauce_demo_ui_tests", 'config.json')
    with open(config_file) as f:
        return TestConfig(**json.load(f))


@allure.step("Browser config")
def browser_config():
    logger.info("Brower options configuration")
    options = Options()
    options.add_argument('--no-sandbox')  # # Bypass OS security model
    options.add_argument('disable-infobars')
    options.add_argument("--disable-extensions")
    options.add_argument("--start-fullscreen")
    options.add_argument('--disable-gpu')
    return options


@allure.step("Drivers setup changed")
def driver_setup(options):
    driver_exec_path = ChromeDriverManager().install()
    s = Service(driver_exec_path)
    driver = webdriver.Chrome(service=s, options=options)
    logger.info("ChromeDriver setup.")
    return driver


@pytest.fixture()
def init_driver():
    """Fixture used for initializing of the driver."""

    con = config()
    if con.browser == "Chrome":
        options = browser_config()

        if con.headless:
            options.add_argument("--headless")

        driver = driver_setup(options)
    else:
        raise Exception(f'Browser "{con.browser}" is not supported')

    yield driver

    logger.info("Closing driver.")
    driver.close()


@pytest.fixture()
def sign_in_page(init_driver):
    return SignInPage(init_driver)


@pytest.fixture()
def main_page(init_driver):
    return CommonSignUpActions(init_driver).sign_in_with_normal_user()
