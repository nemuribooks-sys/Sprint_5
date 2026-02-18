import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators

class TestNavigation:
    """Тесты навигации по сайту"""

    def test_transition_click_personal_account(self, driver):
        """Тест перехода по клику на Личный кабинет"""
        
        # Ждем загрузки главной страницы
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.MAIN_PAGE_TITLE)
        )
        
        # Клик по кнопке "Личный кабинет"
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()

        # Ожидание формы страницы "Вход"
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_PAGE_TITLE)
            )

    def test_constructor_navigation(self, driver):
        """Тест перехода по клику на «Конструктор»"""

        # Ждем загрузки главной страницы
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.MAIN_PAGE_TITLE)
        )
        
        # Клик по кнопке "Личный кабинет"
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()

        # Клик по кнопке "Конструктор"
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
    
    def test_logo_navigation(self, driver):
        """Тест перехода по клику на логотип Stellar Burgers"""
        
        # Ждем загрузки главной страницы
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.MAIN_PAGE_TITLE)
        )
        
        # Клик по кнопке "Личный кабинет"
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()

        # Клик на логотип Stellar Burgers
        driver.find_element(*Locators.LOGO).click()