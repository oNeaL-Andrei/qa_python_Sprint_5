from selenium import webdriver  
from selenium.webdriver.support.wait import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from locators import Locators  
from urls import Urls  # Импортируем класс с константами URL. Изменнено согластно комментариям.

# Тест 1: Вход по кнопке «Войти в аккаунт» на главной странице
class TestLogin:  # Создаем класс для тестов авторизации

    def test_login_from_main_page_button(self, driver): # Изменино добавлен аргумент фикстуры
        driver.get(Urls.BASE_URL)  # Переходим на главную страницу сайта. Изменнено согластно комментариям.
        driver.find_element(*Locators.LOGIN_BUTTON).click()  # Нажимаем кнопку "Войти в аккаунт"
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys("testtestov1984@yandex.ru")  # Вводим email 
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys("1234567")  # Вводим пароль 
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()  # Нажимаем кнопку "Войти"
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON)).is_displayed() # Изменино объединили ожидание и проверку

    # Тест 2: Вход через кнопку "Личный кабинет" в шапке
    def test_login_via_personal_cabinet_button(self, driver): # Изменино добавлен аргумент фикстуры
        driver.get(Urls.BASE_URL)  # Переходим на главную страницу. Изменнено согластно комментариям.
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()  # Нажимаем "Личный Кабинет" в шапке
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys("testtestov1984@yandex.ru")  # Вводим email
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys("1234567")  # Вводим пароль
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()  # Нажимаем кнопку "Войти"
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON)).is_displayed() # Изменино объединили ожидание и проверку

    # Тест 3: Вход через ссылку "Войти" в форме регистрации
    def test_login_from_registration_form(self, driver):  # Изменино добавлен аргумент фикстуры
        driver.get(Urls.REGISTER_URL)  # Переходим сразу на страницу регистрации. Изменнено согластно комментариям.
        driver.find_element(*Locators.REG_LOGIN_LINK).click()  # Нажимаем ссылку "Войти" 
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys("testtestov1984@yandex.ru")  # Вводим email
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys("1234567")  # Вводим пароль
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()  # Нажимаем "Войти"
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON)).is_displayed() # Изменино объединили ожидание и проверку

    # Тест 4: Вход через ссылку "Войти" в форме восстановления пароля
    def test_login_from_forgot_password_form(self, driver): # Изменино добавлен аргумент фикстуры
        driver.get(Urls.FORGOT_PASSWORD_URL)  # Переходим на страницу восстановления пароля. Изменнено согластно комментариям.
        driver.find_element(*Locators.PASSWORD_RECOVERY_LOGIN_BUTTON).click()  # Нажимаем ссылку "Войти"
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys("testtestov1984@yandex.ru")  # Вводим email
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys("1234567")  # Вводим пароль
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()  # Нажимаем "Войти"
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON)).is_displayed() # Изменино объединили ожидание и проверку