import random
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pages.main_page import MainPage
from pages.login_page import LoginPage

def pytest_addoption(parser):
    """Добавление опций командной строки"""
    parser.addoption("--browser", action="store", default="chrome", 
                     help="Браузер для тестов: chrome или firefox")
    parser.addoption("--url", action="store", 
                     default="https://stellarburgers.education-services.ru/", 
                     help="Базовый URL приложения")

@pytest.fixture(scope="function")
def driver(request):
    """Фикстура для создания драйвера"""
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    
    if browser == "chrome":
        # Для Chrome
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
    elif browser == "firefox":
        # Для Firefox
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )
    else:
        raise ValueError(f"Браузер {browser} не поддерживается")
    
    driver.get(url)
    driver.implicitly_wait(10)
    
    yield driver
    
    driver.quit()

@pytest.fixture
def test_data():
    """Фикстура с тестовыми данными"""
    class TestData:
        @staticmethod
        def get_unregistered_user():
            return {
                "name": "НовыйПользователь",
                "email": f"test_{random.randint(1000, 9999)}@example.com",  # noqa: F821
                "password": "Qwerty123"
            }
        
        @staticmethod
        def get_valid_user():
            return {
                "name": "Мария",
                "email": "maria_egorenkova_38_546@yandex.ru",
                "password": "123456"
            }
    
    return TestData()

@pytest.fixture
def authenticated_user(driver):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    
    test_email = "maria_egorenkova_38_546@yandex.ru"
    test_password = "123456"
    
    # 1. Переходим на страницу входа
    driver.get("https://stellarburgers.education-services.ru/login")
    login_page.wait_for_login_page_loaded()
    
    # 2. Выполняем вход
    login_page.login(test_email, test_password)
    
    # 3. Ждем загрузки главной страницы
    main_page.wait_for_main_page()
    
    # Проверяем, что вход выполнен успешно
    assert main_page.is_profile_button_visible(), "Пользователь не авторизовался"
    
    # Возвращаем объект главной страницы
    # Можете возвращать словарь с несколькими объектами, если нужно
    return {
        "main_page": main_page,
        "login_page": login_page
    }