from selenium import webdriver  # Импортируем модуль для управления браузером
from selenium.webdriver.support.wait import WebDriverWait  # Импортируем класс для реализации ожиданий
from selenium.webdriver.support import expected_conditions as EC  # Импортируем набор стандартных условий для ожиданий
from locators import Locators  # Импортируем класс с локаторами элементов страницы

BASE_URL = "https://stellarburgers.education-services.ru"  # Задаем базовый URL тестируемого сайта

class TestAccount:  # Объявляем класс для тестирования функционала личного кабинета и навигации

    def login(self, driver):  # Вспомогательный метод для авторизации пользователя в системе
        driver.get(f"{BASE_URL}/login")  # Открываем страницу авторизации в браузере
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys("testtestov1984@yandex.ru")  # Вводим email 
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys("1234567")  # Вводим пароль 
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()  # Кликаем по кнопке отправки формы входа
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))  # Ждем появления кнопки "Оформить заказ"

    def test_transition_to_personal_account(self):  # Тест проверки перехода по клику на "Личный кабинет"
        driver = webdriver.Chrome()  # Запускаем браузер
        driver.get(BASE_URL)  # Открываем главную страницу сайта
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_ACCOUNT)).click()  # Кликаем по кнопке "Личный кабинет"
        WebDriverWait(driver, 5).until(EC.url_contains("/login"))  # Проверяем, что открылась страница авторизации
        driver.quit()  # Закрываем браузер

    def test_transition_from_account_to_constructor_by_button(self):  # Тест проверки перехода из личного кабинета в конструктор по кнопке
        driver = webdriver.Chrome()  # Запускаем браузер
        self.login(driver)  # Вызываем метод авторизации
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_ACCOUNT)).click()  # Нажимаем "Личный кабинет"
        WebDriverWait(driver, 5).until(EC.url_contains("/account"))  # Ожидаем переход в личный кабинет
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)).click()  # Кликаем по кнопке Конструктор
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BUNS)).is_displayed()  # Проверяем, что элемент конструктора Булки отображается
        driver.quit()  # Закрываем браузер

    def test_transition_from_account_to_constructor_by_logo(self):  # Тест проверки перехода из личного кабинета по клику на логотип
        driver = webdriver.Chrome()  # Запускаем браузер
        self.login(driver)  # Вызываем метод авторизации
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_ACCOUNT)).click()  # Нажимаем "Личный кабинет"
        WebDriverWait(driver, 5).until(EC.url_contains("/account"))  # Ожидаем переход в личный кабинет
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGO_STELLAR_BURGERS)).click()  # Кликаем по логотипу
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BUNS)).is_displayed()  # Проверяем, что элемент конструктора Булки отображается
        driver.quit()  # Закрываем браузер

    def test_logout_from_account(self):  # Тест проверки выхода из аккаунта
        driver = webdriver.Chrome()  # Запускаем браузер
        self.login(driver)  # Вызываем метод авторизации
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_PERSONAL_ACCOUNT)).click()  # Нажимаем "Личный кабинет"
        WebDriverWait(driver, 5).until(EC.url_contains("/account"))  # Ожидаем переход в личный кабинет
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)).click()  # Кликаем кнопку выхода
        WebDriverWait(driver, 5).until(EC.url_contains("/login"))  # Проверяем изменение URL на страницу логина
        driver.quit()  # Закрываем браузер