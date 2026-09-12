from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from helpers import generate_random_email, generate_random_password
from urls import Urls  # Импортируем класс с константами URL. Изменено согласно комментариям.


class TestRegistration:

    # Тест: успешная регистрация
    def test_registration_success(self, driver): # изменино добавлен аргумент фикстуры
        driver.get(Urls.REGISTER_URL)  # Открываем страницу регистрации. Изменено согластно комментариям.
        driver.find_element(*Locators.NAME_INPUT_FIELD).send_keys("Иван")  # Вводим имя, email и пароль
        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(generate_random_email()) # генерируем email
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(generate_random_password()) # генерируем пароль
        driver.find_element(*Locators.REG_BUTTON).click()  # Нажимаем кнопку регистрации
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_HEADER))  # Делаем задержку
        assert driver.find_element(*Locators.LOGIN_HEADER).is_displayed()  # Проверяем,что после успешной регистрации отображается заголовок «Вход»
        

    # Тест: ошибка при коротком пароле
    def test_registration_short_password_error(self, driver): # изменино добавлен аргумент фикстуры
        driver.get(Urls.REGISTER_URL)  # Открываем страницу регистрации. Изменено согластно комментариям.

        # Вводим имя, email и короткий пароль
        driver.find_element(*Locators.NAME_INPUT_FIELD).send_keys("Иван")
        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(generate_random_email())
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys("12345")
        driver.find_element(*Locators.REG_BUTTON).click()  # Нажимаем кнопку регистрации
        error_element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.REG_ERROR_PASSWORD))  # Делаем задержку
        assert error_element.text == "Некорректный пароль"  # Проверяем текст ошибки
        