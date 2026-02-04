from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def wait_for_visible(driver,locator,timeout=10):
    """
    Waits for an element to be present on the page.

    :param driver: The WebDriver instance.
    :param locator: A tuple containing the locator strategy and locator value (e.g., (By.ID, 'element_id')).
    :param timeout: Maximum time to wait for the element to be present.
    :return: The WebElement if found within the timeout period, else raises TimeoutException.
    """
    try:
        element=WebDriverWait(driver,timeout).until(EC.presence_of_element_located(locator))
        return element
    except TimeoutException:
        raise TimeoutException(f"Element with locator {locator} not found within {timeout} seconds.")