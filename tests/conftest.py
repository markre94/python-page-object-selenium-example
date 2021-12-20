import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def init_driver():
    """Fixture used for initializing of the driver."""

    # options = Options()
    # options.add_argument('--no-sandbox')  # # Bypass OS security model
    # options.add_argument('disable-infobars')
    # options.add_argument("--disable-extensions")
    # options.add_argument("--start-fullscreen")
    # options.add_argument('--disable-gpu')

    driver_exec_path = ChromeDriverManager().install()
    s = Service(driver_exec_path)
    driver = webdriver.Chrome(service=s)

    yield driver

    driver.close()

