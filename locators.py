from selenium.webdriver.common.by import By

class Locators:
    # Главная страница
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']") # Кнопка Войти в аккаунт на главной
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, ".//p[text()='Личный Кабинет']") # Кнопка "Личный Кабинет" в шапке
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']") # Кнопка "Конструктор" в шапке
    LOGO_STELLAR_BURGERS = (By.XPATH, ".//div[contains(@class,'header__logo')]/a") # Логотип сайта в шапке

    # Раздел «Конструктор»
    BUNS = (By.XPATH, ".//span[text()='Булки']/parent::div") # Вкладка "Булки"
    SAUCES = (By.XPATH, ".//span[text()='Соусы']/parent::div") # Вкладка "Соусы"
    FILLINGS = (By.XPATH, ".//span[text()='Начинки']/parent::div") # Вкладка "Начинки"
    ACTIVE = (By.XPATH, ".//div[contains(@class,'tab_tab_type_current')]") # Активная выбранная вкладка

    # Страница регистрации
    NAME_INPUT_FIELD = (By.XPATH, ".//label[text()='Имя']/following-sibling::input") # Поле ввода имени
    EMAIL_INPUT_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input") # Поле ввода email
    PASSWORD_INPUT_FIELD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input") # Поле ввода пароля
    REG_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться"
    REG_ERROR_PASSWORD = (By.XPATH, ".//p[text()='Некорректный пароль']") # Текст ошибки короткого пароля
    REG_LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']") # Ссылка «Войти» на странице регистрации
    # Страница входа
    LOGIN_EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input") # Поле ввода email на стронице входа
    LOGIN_PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input") # Поле ввода пароля на странице входа
    LOGIN_SUBMIT_BUTTON = (By.XPATH, ".//button[text()='Войти']") # Кнопка "Войти"
    LOGIN_HEADER = (By.XPATH, ".//h2[text()='Вход']") # Заголовок "Вход"

    # Восстановление пароля
    PASSWORD_RECOVERY_LOGIN_BUTTON = (By.XPATH, ".//a[text()='Войти']") # Кнопка "Войти" под формой восстановления пароля

    # Личный кабинет
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']") # Кнопка "Оформить заказ"
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']") # Кнопка "Выйти" из аккаунта