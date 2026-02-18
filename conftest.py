import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data import Credentials
from locators import Locators
from urls import BASE_URL

# session, module, class, function
@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1600,900")
    options.add_experimental_option("prefs", {
            "profile.password_manager_leak_detection": False
        })
    #options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    browser.get(BASE_URL)
    yield browser
    browser.quit()


@pytest.fixture
def login(driver):
    """
    Фикстура для авторизации пользователя.
    """
    driver.find_element(*Locators.NAME_INPUT).send_keys(Credentials.NAME)
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(Credentials.EMAIL)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Credentials.PASSWORD)
    driver.find_element(*Locators.REGISTER_BUTTON).click()

    return driver