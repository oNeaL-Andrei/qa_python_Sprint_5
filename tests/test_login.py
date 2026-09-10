from selenium import webdriver  
from selenium.webdriver.support.wait import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from locators import Locators  

BASE_URL = "https://stellarburgers.education-services.ru"  # Задаем базовый адрес сайта
# Тест 1: Вход по кнопке «Войти в аккаунт» на главной странице
class TestLogin:  # Создаем класс для тестов авторизации

    def test_login_from_main_page_button(self):
        driver = webdriver.Chrome()  # Запускаем браузер Google Chrome
        driver.get(f"{BASE_URL}/")  # Переходим на главную страницу сайта
        driver.find_element(*Locators.LOGIN_BUTTON).click()  # Нажимаем кнопку "Войти в аккаунт"
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys("testtestov1984@yandex.ru")  # Вводим email 
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys("1234567")  # Вводим пароль 
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()  # Нажимаем кнопку "Войти"
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON)) # делаем задержку 5 секунд
        assert driver.find_element(*Locators.ORDER_BUTTON).is_displayed() # Проверяем, что кнопка "Оформить заказ" отображается на странице
        driver.quit()  # Закрываем браузер

    # Тест 2: Вход через кнопку "Личный кабинет" в шапке
    def test_login_via_personal_cabinet_button(self):
        driver = webdriver.Chrome()  # Запускаем браузер
        driver.get(f"{BASE_URL}/")  # Переходим на главную страницу
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()  # Нажимаем "Личный Кабинет" в шапке
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys("testtestov1984@yandex.ru")  # Вводим email
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys("1234567")  # Вводим пароль
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()  # Нажимаем кнопку "Войти"
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON)) # делаем задержку в 5 секунд
        assert driver.find_element(*Locators.ORDER_BUTTON).is_displayed()  # Проверяем успешный вход
        driver.quit()  # Закрываем браузер

    # Тест 3: Вход через ссылку "Войти" в форме регистрации
    def test_login_from_registration_form(self):
        driver = webdriver.Chrome()  # Запускаем браузер
        driver.get(f"{BASE_URL}/register")  # Переходим сразу на страницу регистрации
        driver.find_element(*Locators.REG_LOGIN_LINK).click()  # Нажимаем ссылку "Войти" 
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys("testtestov1984@yandex.ru")  # Вводим email
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys("1234567")  # Вводим пароль
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()  # Нажимаем "Войти"
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON)) #делаем задержку в 5 секунд
        assert driver.find_element(*Locators.ORDER_BUTTON).is_displayed() # проверяем
        driver.quit()  # Закрываем браузер

    # Тест 4: Вход через ссылку "Войти" в форме восстановления пароля
    def test_login_from_forgot_password_form(self):
        driver = webdriver.Chrome()  # Запускаем браузер
        driver.get(f"{BASE_URL}/forgot-password")  # Переходим на страницу восстановления пароля
        driver.find_element(*Locators.PASSWORD_RECOVERY_LOGIN_BUTTON).click()  # Нажимаем ссылку "Войти"
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys("testtestov1984@yandex.ru")  # Вводим email
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys("1234567")  # Вводим пароль
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()  # Нажимаем "Войти"
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON)) #делаем задержку в 5 секунд
        assert driver.find_element(*Locators.ORDER_BUTTON).is_displayed()
        driver.quit()  # Закрываем браузер