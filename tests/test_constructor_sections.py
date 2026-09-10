from selenium import webdriver  
from selenium.webdriver.support.wait import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from locators import Locators  

BASE_URL = "https://stellarburgers.education-services.ru"  # Задаем базовый URL тестируемого сайта

class TestConstructorSections:  # эту часть кода советовался с ИИ

    def test_transition_to_buns_section(self):  # Тест проверки перехода к разделу «Булки»
        driver = webdriver.Chrome()  # Запускаем браузер
        driver.get(BASE_URL)  # Открываем главную страницу сайта
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.SAUCES)).click() # Сначала кликаем на другую вкладку («Соусы»)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUNS)).click() # Кликаем по вкладке «Булки»
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BUNS)).is_displayed() # Проверяем, что вкладка «Булки» отображается
        driver.quit()  # Закрываем браузер

    def test_transition_to_sauces_section(self):  # Тест проверки перехода к разделу «Соусы»
        driver = webdriver.Chrome()  # Запускаем браузер
        driver.get(BASE_URL)  # Открываем главную страницу сайта
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.SAUCES)).click() # Кликаем по вкладке «Соусы»
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.SAUCES)).is_displayed() # Проверяем, что вкладка «Соусы» отображается
        driver.quit()  # Закрываем браузер

    def test_transition_to_fillings_section(self):  # Тест проверки перехода к разделу «Начинки»
        driver = webdriver.Chrome()  # Запускаем браузер
        driver.get(BASE_URL)  # Открываем главную страницу сайта
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.FILLINGS)).click() # Кликаем по вкладке «Начинки»
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.FILLINGS)).is_displayed() # Проверяем, что вкладка «Начинки» отображается
        driver.quit()  # Закрываем браузер