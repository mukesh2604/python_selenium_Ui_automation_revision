import pytest
from pages.login_page import LoginPage
from exceptions.login_exceptions import LoginFailedException
from Utils.config_reader import BASEURL, USERNAME, PASSWORD
from Utils.logger import get_logger

logger = get_logger(__name__)
def test_invalid_login(driver):
    logger.info("Starting test: test_invalid_login")
    driver.get(BASEURL)
    logger.info(f"Navigated to {BASEURL}")

    login_page = LoginPage(driver)

    with pytest.raises(LoginFailedException):
        login_page.login(USERNAME,PASSWORD)
        logger.info("Completed test: test_invalid_login")

