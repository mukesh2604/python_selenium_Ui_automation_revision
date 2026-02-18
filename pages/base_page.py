from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    allure.step("Checking if alert is present within {timeout} seconds")
    def is_alert_present(self, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            return True
        except TimeoutException:
            return False


    allure.step("Accepting alert and returning its text")
    def accept_alert(self, timeout=5):
        alert = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        text = alert.text

        allure.attach(
            text,
            name="alert_text",
            attachment_type=allure.attachment_type.TEXT
        )

        alert.accept()
        return text