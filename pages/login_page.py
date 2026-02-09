from selenium.webdriver.common.by import By
from Utils.wait_utils import wait_for_visible
from exceptions.login_exceptions import LoginFailedException
from exceptions.dashboard_exceptions import dashboard_exception
from selenium.common.exceptions import TimeoutException
from Utils.logger import get_logger
from pages.base_page import BasePage

class LoginPage(BasePage):
    """Page Object Model for the Login Page of the application."""

    def __init__(self, driver):
        """
        Initializes the LoginPage with a WebDriver instance.

        :param driver: The WebDriver instance.
        """
        super().__init__(driver)

        self.logger = get_logger(__name__)

        self.username_input = (By.ID, 'user-name')
        self.password_input = (By.NAME, 'password')
        self.login_button = (By.ID, 'login-button')
        self.dashboard_element = (By.ID, "inventory_container")
        self.error_message_locator = (By.CSS_SELECTOR, "h3[data-test='error']")

    def enter_username(self, username):
        """
        Enters the username into the username input field.

        :param username: The username to be entered.
        """
        username_field = wait_for_visible(self.driver, self.username_input)
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        """
        Enters the password into the password input field.

        :param password: The password to be entered.
        """
        password_field = wait_for_visible(self.driver, self.password_input)
        self.logger.info("Entering password.")
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        """
        Clicks the login button to submit the login form.
        """
        self.logger.info("Clicking the login button.")
        login_btn = wait_for_visible(self.driver, self.login_button)
        login_btn.click()

    def login(self, username, password):
        """
        Performs the complete login action by entering the username,
        entering the password, and clicking the login button.

        :param username: The username to be entered.
        :param password: The password to be entered.
        :raises LoginFailedException: If login fails due to timeout.
        """

        self.logger.info("Starting login process.")
        try:


            self.enter_username(username)
            self.logger.info("Username entered successfully.")
            self.enter_password(password)
            self.logger.info("Password entered successfully.")
            self.click_login()
            self.logger.info("Login button clicked successfully.")
        except TimeoutException:
            self.logger.error("Login failed due to timeout while waiting for elements.")
            raise LoginFailedException("Login failed due to timeout while waiting for elements.")



    def is_login_successful(self):
        """
        Checks if login succeeded by checking alert OR dashboard element
        """
        self.logger.info("Checking if login was successful.")
        try:
            # ✅ Safe alert check
            if self.is_alert_present():
                self.logger.warning("Alert detected after login attempt.")
                alert_text = self.accept_alert()
                self.logger.warning(f"Alert text: {alert_text}")
                return False

            self.logger.info("No alert detected, checking dashboard element.")


            wait_for_visible(self.driver, self.dashboard_element)

            self.logger.info("Login successful")
            return True

        except TimeoutException:
            self.logger.error("Dashboard not found after login")
            raise dashboard_exception("Login failed: dashboard not visible")



    def get_error_message(self):
        """
        Retrieves the error message displayed on the login page after a failed login attempt.

        :return: The error message text.
        """

        try:
            error_element = wait_for_visible(self.driver, self.error_message_locator)
            return error_element.text
        except TimeoutException:
            self.logger.error("Error message not found after failed login attempt.")
            return ""  # Return empty string if no error message is found




