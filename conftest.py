import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    """Добавление опций командной строки"""
    parser.addoption("--browser", action="store", default="chrome", help="Браузер для тестов: chrome или firefox")
    parser.addoption("--url", action="store", default="https://stellarburgers.nomoreparties.site", 
                     help="Базовый URL приложения")


@pytest.fixture(scope="function")
def driver(request):
    """Фикстура для инициализации драйвера"""
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
    elif browser == "firefox":
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
    """Фикстура для тестовых данных"""
    from data import TestData
    return TestData