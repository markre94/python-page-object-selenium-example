import json
import os
from dataclasses import dataclass

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@dataclass
class TestConfig:
    browser: str
    implicit_wait: int
    headless: bool


@pytest.fixture(scope='session')
def config():
    config_file = os.path.join("/Users/marcin94/PycharmProjects/sauce_demo_ui_tests", 'config.json')
    with open(config_file) as f:
        return TestConfig(**json.load(f))


@pytest.fixture
def init_driver(config):
    """Fixture used for initializing of the driver."""

    if config.browser == "Chrome":

        options = Options()
        options.add_argument('--no-sandbox')  # # Bypass OS security model
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument("--start-fullscreen")
        options.add_argument('--disable-gpu')

        if config.headless:
            options.add_argument("--headless")

        driver_exec_path = ChromeDriverManager().install()
        s = Service(driver_exec_path)
        driver = webdriver.Chrome(service=s, options=options)

    else:
        raise Exception(f'Browser "{config.browser}" is not supported')

    yield driver

    driver.close()
