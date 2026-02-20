import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
