# import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# @pytest.fixture() DO NOT USE FIXTURES WITH A TEST
def test_title():
        driver = webdriver.Firefox()

        driver.get('https://www.saucedemo.com/')

        driver.implicitly_wait(0.8)
        driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys('secret_sauce')
        driver.find_element(By.CLASS_NAME, 'submit-button').click()

        driver.implicitly_wait(1000)
        print(driver.title)

        assert driver.title == "Swag Labs"
       
        driver.quit()