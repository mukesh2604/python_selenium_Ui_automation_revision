import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.login_page import LoginPage
from exceptions.login_exceptions import LoginFailedException
from Utils.config_reader import BASEURL, USERNAME, PASSWORD
from Utils.logger import get_logger

logger = get_logger(__name__)

@pytest.mark.usefixtures("driver")  # ensures driver fixture is available
class TestLogin:

    def test_valid_login(self, driver):
        """Test valid login with correct credentials"""
        logger.info("Starting test: test_valid_login")
        driver.get(BASEURL)
        logger.info(f"Navigated to {BASEURL}")

        login_page = LoginPage(driver)
        try:
            login_page.login(USERNAME, PASSWORD)
        except Exception as e:
            logger.error(f"Login failed: {e}")
            raise

        assert login_page.is_login_successful(), "Login was not successful with valid credentials."
        logger.info("Login successful with valid credentials.")

    def test_invalid_login(self, driver):
        """Test login with invalid credentials should fail"""
        logger.info("Starting test: test_invalid_login")
        driver.get(BASEURL)
        logger.info(f"Navigated to {BASEURL}")

        login_page = LoginPage(driver)

        # Attempt login
        login_page.login(USERNAME, "wrong_password")

        expected_error = "Epic sadface: Username and password do not match any user in this service"
        actual_error = login_page.get_error_message()  # you should implement this method in LoginPage

        logger.info(f"Actual error message: {actual_error}")

        assert expected_error in actual_error, f"Expected error message not displayed. Got: '{actual_error}'"

        logger.info("Invalid login correctly showed expected error message")