# conftest.py в корне проекта Sprint_5-1/
import sys
import os

# Добавляем корневую директорию в путь поиска модулей
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = 'https://stellarburgers.education-services.ru'

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_experimental_option("prefs", {
        "profile.password_manager_leak_detection": False
    })
    # Раскомментируйте для headless режима
    # options.add_argument("--headless")
    
    browser = webdriver.Chrome(options=options)
    browser.get(BASE_URL)
    
    # Ждем загрузки главной страницы
    try:
        WebDriverWait(browser, 10).until(
            EC.title_contains("Соберите бургер")
        )
    except Exception as e:
        print(f"Ошибка при загрузке страницы: {e}")
        # Сохраняем скриншот для отладки
        browser.save_screenshot("error_screenshot.png")
    
    yield browser
    browser.quit()