import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

import pytest
from selenium import webdriver
from locators import Locators
from urls import Urls

@pytest.fixture
def logged_in_user(driver):
    driver.get(Urls.LOGIN_URL)
    driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys("testtestov1984@yandex.ru")
    driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys("1234567")
    driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()
    return driver