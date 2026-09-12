from selenium import webdriver  
from selenium.webdriver.support.wait import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from locators import Locators  
from urls import Urls  # Импортируем класс с константами URL. Изменено согластно комментариям.


class TestConstructorSections:  # эту часть кода советовался с ИИ

    def test_transition_to_buns_section(self, driver):  # Тест проверки перехода к разделу «Булки» Изменино добавлен аргумент фикстуры
        driver.get(Urls.BASE_URL)  # Открываем главную страницу сайта. Изменено согластно комментариям.
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.SAUCES)).click() # Сначала кликаем на другую вкладку («Соусы»)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUNS)).click() # Кликаем по вкладке «Булки»
        tab_buns = driver.find_element(*Locators.BUNS) # находим элемент вкладки "булки"
        assert "tab_type_current" in tab_buns.get_attribute("class")  # проверяем что родительский элемент вкладки булки имеет класс

    def test_transition_to_sauces_section(self, driver):  # Тест проверки перехода к разделу «Соусы» Изменино добавлен аргумент фикстуры
        driver.get(Urls.BASE_URL)  # Открываем главную страницу сайта. Изменено согластно комментариям.
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.SAUCES)).click() # Кликаем по вкладке «Соусы»
        tab_sauces = driver.find_element(*Locators.SAUCES) # находим элемент вкладки "соусы"
        assert "tab_type_current" in tab_sauces.get_attribute("class")  # проверяем что родительский элемент вкладки соусы имеет класс

    def test_transition_to_fillings_section(self, driver):  # Тест проверки перехода к разделу «Начинки» Изменино добавлен аргумент фикстуры
        driver.get(Urls.BASE_URL)  # Открываем главную страницу сайта. Изменено согластно комментариям.
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.FILLINGS)).click() # Кликаем по вкладке «Начинки»
        tab_fillings = driver.find_element(*Locators.FILLINGS) # находим элемент вкладки "начинки"
        assert "tab_type_current" in tab_fillings.get_attribute("class")  # проверяем что родительский элемент вкладки начинки имеет класс