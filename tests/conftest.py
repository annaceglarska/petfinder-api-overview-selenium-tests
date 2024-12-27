import pytest

from utils.config import DEFAULT_BROWSER
from utils.driver_factory import create_driver, quit_driver


@pytest.fixture
def driver():
    driver = create_driver(browser=DEFAULT_BROWSER)
    yield driver
    quit_driver(driver)
