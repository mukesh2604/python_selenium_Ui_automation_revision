import pytest
from pages.login_page import LoginPage
from exceptions.login_exceptions import LoginFailedException
from Utils.config_reader import BASEURL, USERNAME, PASSWORD


def test_invalid_login(driver):
    driver.get(BASEURL)
    login_page = LoginPage(driver)

    with pytest.raises(LoginFailedException):
        login_page.login(USERNAME,PASSWORD)