from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

option=Options()
option.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=option)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()


driver.find_element(By.ID,'user-name').send_keys("standard_user")
driver.find_element(By.NAME,'password').send_keys("secret_sauce")

driver.find_element(By.CLASS_NAME,"btn_action").click()







