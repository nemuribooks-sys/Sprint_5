from selenium.webdriver.common.by import By


class Locators:
    """Локаторы для элементов Stellar Burgers"""
    
    # Заголовки
    MAIN_PAGE_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")  # Заголовок главной страницы
    LOGIN_PAGE_TITLE = (By.XPATH, "//h2[text()='Вход']")  # Заголовок страницы входа
    REGISTRATION_PAGE_TITLE = (By.XPATH, "//h2[text()='Регистрация']")  # Заголовок регистрации
    
    # Кнопки навигации
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт" на главной
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка "Личный кабинет"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка "Конструктор"
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # Логотип Stellar Burgers
    
    # Формы
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # Поле ввода имени
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле ввода email
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")  # Поле ввода пароля
    
    # Кнопки форм
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка регистрации
    LOGIN_FORM_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка входа в форме
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")  # Кнопка сохранения
    
    # Ссылки
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # Ссылка "Войти" на странице регистрации
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")  # Ссылка "Зарегистрироваться" на странице входа
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")  # Ссылка восстановления пароля
    LOGIN_LINK_FORGOT_PASSWORD = (By.XPATH, "//a[text()='Войти']")  # Ссылка "Войти" на странице восстановления пароля
    
    # Личный кабинет
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")  # Вкладка "Профиль" в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка выхода из аккаунта
    
    # Конструктор
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div")  # Раздел "Булки"
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::div")  # Раздел "Соусы"
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::div")  # Раздел "Начинки"
    
    # Активные разделы конструктора
    ACTIVE_SECTION = (By.XPATH, "//div[contains(@class, 'current')]")  # Активный раздел
    BUNS_SECTION_TITLE = (By.XPATH, "//h2[text()='Булки']")  # Заголовок раздела булок
    SAUCES_SECTION_TITLE = (By.XPATH, "//h2[text()='Соусы']")  # Заголовок раздела соусов
    FILLINGS_SECTION_TITLE = (By.XPATH, "//h2[text()='Начинки']")  # Заголовок раздела начинок
    
    # Ошибки
    PASSWORD_ERROR = (By.XPATH, "//p[contains(@class, 'input__error')]")  # Ошибка пароля
    
    # Успешная регистрация
    SUCCESSFUL_REGISTRATION = (By.XPATH, "//h2[text()='Вход']")  # После регистрации переходим на страницу входа