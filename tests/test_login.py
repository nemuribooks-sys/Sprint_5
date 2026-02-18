import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from locators import Locators

class TestLogin:
    """Тесты входа в аккаунт"""
    
    def test_login_account_button(self, driver):
        """Вход через кнопку Войти в аккаунт на главной"""

        # Ждем загрузки главной страницы
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.MAIN_PAGE_TITLE)
        )
        
        # Клик по кнопке "Личный кабинет"
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        
        # Теперь заполняем форму
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.EMAIL_INPUT)
        )
        email_input.send_keys(Credentials.EMAIL)
        
        password_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.PASSWORD_INPUT)
            )
        password_input.send_keys(Credentials.PASSWORD)
        
        driver.find_element(*Locators.LOGIN_FORM_BUTTON).click()
        
        # Ожидание главной страницы после входа
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.MAIN_PAGE)
            )

    def test_login_personal_account_button(self, driver):
        """Вход через кнопку Личный кабинет"""

        # Ждем загрузки главной страницы
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.MAIN_PAGE_TITLE)
            )
        
        # Клик по кнопке "Личный кабинет"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        # Теперь заполняем форму
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.EMAIL_INPUT)
            )
        email_input.send_keys(Credentials.EMAIL)
        
        password_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.PASSWORD_INPUT)
            )
        password_input.send_keys(Credentials.PASSWORD)
        
        driver.find_element(*Locators.LOGIN_FORM_BUTTON).click()
        
        # Ожидание главной страницы после входа
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.MAIN_PAGE)
            )

    def test_login_registration_button(self, driver):
        """Вход через кнопку в форме регистрации"""

        # Ждем загрузки главной страницы
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.MAIN_PAGE_TITLE)
        )
        
        # Клик по кнопке "Личный кабинет"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        # Переход на регистрацию
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
            ).click()
        
        # Клик по кнопке "Войти"
        driver.find_element(*Locators.LOGIN_LINK).click()

        # Теперь заполняем форму
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.EMAIL_INPUT)
        )
        email_input.send_keys(Credentials.EMAIL)
        
        password_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.PASSWORD_INPUT)
            )
        password_input.send_keys(Credentials.PASSWORD)
        
        driver.find_element(*Locators.LOGIN_FORM_BUTTON).click()
        
        # Ожидание главной страницы после входа
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.MAIN_PAGE)
            )

    def test_login_password_recovery_button(self, driver):
        """Вход через кнопку в форме восстановления пароля"""

        # Ждем загрузки главной страницы
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.MAIN_PAGE_TITLE)
            )
        
        # Клик по кнопке "Личный кабинет"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        # Клик по кнопке "Восстановить пароль"
        driver.find_element(*Locators.FORGOT_PASSWORD_LINK).click()

        # Клик по кнопке "Войти"
        driver.find_element(*Locators.LOGIN_LINK).click()

        # Теперь заполняем форму
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.EMAIL_INPUT)
        )
        email_input.send_keys(Credentials.EMAIL)
        
        password_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.PASSWORD_INPUT)
            )
        password_input.send_keys(Credentials.PASSWORD)
        
        driver.find_element(*Locators.LOGIN_FORM_BUTTON).click()
        
        # Ожидание главной страницы после входа
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.MAIN_PAGE)
            )