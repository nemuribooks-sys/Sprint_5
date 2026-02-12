import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options

from curl import *
from data import Credentials
from locators import Locators


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1600,900")
    options.add_experimental_option("prefs", {
            "profile.password_manager_leak_detection": False
        })
    #options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    browser.get(main_site)
    yield browser
    browser.quit()
    
    # Для Firefox
    options = Options()
    options.add_argument("--window-size=1600,900")
    options.add_experimental_option("prefs", {
            "profile.password_manager_leak_detection": False
        })
    #options.add_argument("--headless")
    browser = webdriver.Firefox(options=options)
    browser.get(main_site)
    yield browser
    browser.quit()

@pytest.fixture
def login(driver):
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(Credentials.email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Credentials.password)
    driver.find_element(*Locators.LOGIN_FORM_BUTTON).click()

    return driver