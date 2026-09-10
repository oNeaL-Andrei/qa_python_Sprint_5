from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from helpers import generate_random_email, generate_random_password

# Базовый URL учебного стенда
BASE_URL = "https://stellarburgers.education-services.ru"

class TestRegistration:

    # Тест: успешная регистрация
    def test_registration_success(self):
        driver = webdriver.Chrome()  # Запускаем браузер
        driver.get(f"{BASE_URL}/register")  # Открываем страницу регистрации
        driver.find_element(*Locators.NAME_INPUT_FIELD).send_keys("Иван")  # Вводим имя, email и пароль
        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(generate_random_email()) # генерируем email
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(generate_random_password()) # генерируем пароль
        driver.find_element(*Locators.REG_BUTTON).click()  # Нажимаем кнопку регистрации
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_HEADER))  # Делаем задержку
        assert driver.find_element(*Locators.LOGIN_HEADER).is_displayed()  # Проверяем,что после успешной регистрации отображается заголовок «Вход»
        driver.quit()  # Закрываем браузер

    # Тест: ошибка при коротком пароле
    def test_registration_short_password_error(self):
        driver = webdriver.Chrome()  # Запускаем браузер
        driver.get(f"{BASE_URL}/register")  # Открываем страницу регистрации

        # Вводим имя, email и короткий пароль
        driver.find_element(*Locators.NAME_INPUT_FIELD).send_keys("Иван")
        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(generate_random_email())
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys("12345")
        driver.find_element(*Locators.REG_BUTTON).click()  # Нажимаем кнопку регистрации
        error_element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REG_ERROR_PASSWORD))  # Делаем задержку
        assert error_element.text == "Некорректный пароль"  # Проверяем текст ошибки
        driver.quit()  # Закрываем браузер