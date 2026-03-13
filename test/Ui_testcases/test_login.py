import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys
import os
import allure

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pages.login_page import LoginPage
from exceptions.login_exceptions import LoginFailedException
from Utils.config_reader import BASEURL, USERNAME, PASSWORD
from Utils.logger import get_logger

logger = get_logger(__name__)


@pytest.mark.usefixtures("driver")  # ensures driver fixture is available
class TestLogin:

    @allure.feature("Login Functionality")
    @allure.story("Valid Login")
    @allure.severity(allure.severity_level.CRITICAL)
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

    @allure.feature("Login Functionality")
    @allure.story("Invalid Login")
    @allure.severity(allure.severity_level.NORMAL)
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

    @allure.feature("Login Functionality")
    @allure.story("Blank Credentials")
    @allure.severity(allure.severity_level.NORMAL)
    def test_blank_username(self, driver):
        """Test login with invalid username should fail """
        logger.info("starting test: test_invalid_username")
        driver.get(BASEURL)
        logger.info(f"navigated to {BASEURL}")
        login_page = LoginPage(driver)
        login_page.login("", PASSWORD)

        expected_error = "Epic sadface: Username is required"
        actual_error = login_page.get_error_message()
        logger.info(f"Actual error message: {actual_error}")

        assert expected_error in actual_error, f"Expected error message not displayed. Got: '{actual_error}'"
        logger.info("Invalid username correctly showed expected error message")

    @allure.feature("Login Functionality")
    @allure.story("Blank Credentials")
    @allure.severity(allure.severity_level.NORMAL)
    def test_blank_password(self, driver):
        """Test login with invalid password should fail """
        logger.info("starting test: test_invalid_password")
        driver.get(BASEURL)
        logger.info(f"navigated to {BASEURL}")
        login_page = LoginPage(driver)
        login_page.login(USERNAME, "")

        expected_error = "Epic sadface: Password is required"
        actual_error = login_page.get_error_message()
        logger.info(f"Actual error message: {actual_error}")

        assert expected_error in actual_error, f"Expected error message not displayed. Got: '{actual_error}'"
        logger.info("Invalid password correctly showed expected error message")

    @allure.feature("Login Functionality")
    @allure.story("Blank Credentials")
    @allure.severity(allure.severity_level.NORMAL)
    def test_blank_credentials(self, driver):
        """Test login with blank credentials should fail """
        logger.info("starting test: test_blank_credentials")
        driver.get(BASEURL)
        logger.info(f"navigated to {BASEURL}")
        login_page = LoginPage(driver)
        login_page.login("", "")

        expected_error = "Epic sadface: Username is required"
        actual_error = login_page.get_error_message()
        logger.info(f"Actual error message: {actual_error}")

        assert expected_error in actual_error, f"Expected error message not displayed. Got: '{actual_error}'"
        logger.info("Blank credentials correctly showed expected error message")

    @allure.feature("Login Functionality")
    @allure.story("Login Button State")
    @allure.severity(allure.severity_level.MINOR)
    def test_login_btn_enabled(self, driver):
        """Test login button is enabled when username and password are entered"""
        logger.info("starting test: test_login_btn_enabled")
        driver.get(BASEURL)
        logger.info(f"navigated to {BASEURL}")
        login_page = LoginPage(driver)

        login_page.login_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        assert login_page.login_btn.is_enabled(), ("Login button should be enabled before username and password are "
                                                   "entered")
        logger.info("Login button is enabled before username and password are entered")
