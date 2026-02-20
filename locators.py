from selenium.webdriver.common.by import By
class Locators:
    """Локаторы для элементов Stellar Burgers"""
    
    # Заголовки
    MAIN_PAGE = (By.XPATH, "//h2[text()='Вход']")
    MAIN_PAGE_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    LOGIN_PAGE_TITLE= (By.XPATH, "//h2[text()='Вход']")
    REGISTRATION_PAGE_TITLE = (By.XPATH, "//h2[text()='Регистрация']")
    
    # Кнопки навигации
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") 
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    LOGO = (By.XPATH, "//a[@href='/']")

    # Формы
    NAME_INPUT = (By.XPATH, "//input[@name='name' and not(@disabled) and not(@hidden)]")
    EMAIL_INPUT = (By.XPATH, "html/body/div/div/main/div/form/fieldset[1]/div/div/input")
    EMAIL_INPUT2 = (By.XPATH, "html/body/div/div/main/div/form/fieldset[2]/div/div/input")  # для поля регистрация
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    
    # Кнопки форм
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    LOGIN_FORM_BUTTON = (By.XPATH, "//button[text()='Войти']")
    
    # Ссылки
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    LOGIN_LINK_FORGOT_PASSWORD = (By.XPATH, "//button[text()='Войти']")
    
    # Личный кабинет
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    
    # Конструктор
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']")
    
    # Активные разделы конструктора
    ACTIVE_BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/parent::*[contains(@class, 'current')]")
    ACTIVE_SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::*[contains(@class, 'current')]") 
    ACTIVE_FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::*[contains(@class, 'current')]") 
    
    BUNS_SECTION_TITLE = (By.XPATH, "//h2[text()='Булки']")
    SAUCES_SECTION_TITLE = (By.XPATH, "//h2[text()='Соусы']")
    FILLINGS_SECTION_TITLE = (By.XPATH, "//h2[text()='Начинки']")
    
    # Ошибки
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")
    
    # Успешная регистрация
    SUCCESSFUL_REGISTRATION = (By.XPATH, "//h2[text()='Вход']")