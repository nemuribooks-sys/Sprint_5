from selenium.webdriver.common.by import By


class Locators:
    """Локаторы для элементов Stellar Burgers"""
    
    # Заголовки
    MAIN_PAGE_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")  # Заголовок главной страницы
    LOGIN_PAGE_TITLE = (By.XPATH, "//h2[text()='Вход']")  # Заголовок страницы входа
    REGISTRATION_PAGE_TITLE = (By.XPATH, "//h2[text()='Регистрация']")  # Заголовок регистрации
    
    # Кнопки навигации
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт" на главной
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка "Личный кабинет"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка "Конструктор"
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # Логотип Stellar Burgers
    
    # Формы
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']")  # Поле ввода имени
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']")  # Поле ввода email
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']")  # Поле ввода пароля
    
    # Кнопки форм
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка регистрации
    LOGIN_FORM_BUTTON = (By.XPATH, "//a[text()='Войти']")  # Кнопка входа в форме
    
    # Ссылки
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # Ссылка "Войти" на странице регистрации
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")  # Ссылка "Зарегистрироваться" на странице входа
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")  # Ссылка восстановления пароля
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")  # Ссылка "Восстановить" на странице восстановления пароля
    
    # Личный кабинет
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")  # Вкладка "Профиль" в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка выхода из аккаунта
    
    # Конструктор
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']")  # Раздел "Булки"
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']")  # Раздел "Соусы"
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']")  # Раздел "Начинки"
    
    # Активные разделы конструктора
    ACTIVE_SECTION = (By.XPATH, "//div[contains(@class, 'current')]")  # Активный раздел
    BUNS_SECTION_TITLE = (By.XPATH, "//h2[text()='Булки']")  # Заголовок раздела булок
    SAUCES_SECTION_TITLE = (By.XPATH, "//h2[text()='Соусы']")  # Заголовок раздела соусов
    FILLINGS_SECTION_TITLE = (By.XPATH, "//h2[text()='Начинки']")  # Заголовок раздела начинок
    
    # Ошибки
    INCORRECT_PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")  # Ошибка пароля
    
    # Успешная регистрация
    SUCCESSFUL_REGISTRATION = (By.XPATH, "//h2[text()='Вход']")  # После регистрации переходим на страницу входа