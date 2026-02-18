import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Credentials

from helper import generate_registration_data
from locators import Locators

class TestRegistration:
    """Тесты регистрации"""
    
    def test_successful_registration(self, driver):
        """"Успешная регистрация"""

        name, email, password = generate_registration_data()
        
        # Переход на страницу входа
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.LOGIN_PAGE_TITLE)
            )
        
        # Переход на регистрацию
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
            ).click()
        
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.REGISTRATION_PAGE_TITLE)
            )
        
        # Заполнение формы
        name_input = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.NAME_INPUT)
            )
        name_input.send_keys(name)
        
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.EMAIL_INPUT2)
        )
        email_input.send_keys(email)
        
        password_input = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.PASSWORD_INPUT)
            )
        password_input.send_keys(password)
        
        register = driver.find_element(*Locators.REGISTER_BUTTON)
        register.click()
        
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.LOGIN_PAGE_TITLE)
            )
        
    def test_registration_with_short_password(self, driver):
        """"Регистрация с коротким паролем"""

        name, email, _ = generate_registration_data()
        short_password = "12345"  # 5 символов
        
        # Переход на страницу входа
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.LOGIN_PAGE_TITLE)
            )
        
        # Переход на регистрацию
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
            ).click()
        
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.REGISTRATION_PAGE_TITLE)
            )
        
        # Заполнение формы
        name_input = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.NAME_INPUT)
            )
        name_input.send_keys(name)
        
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.EMAIL_INPUT)
            )
        email_input.send_keys(email)
        
        password_input = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.PASSWORD_INPUT)
            )
        password_input.send_keys(short_password)

        register = driver.find_element(*Locators.REGISTER_BUTTON)
        register.click()

        reg_text = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.PASSWORD_ERROR)).text
        assert reg_text == 'Некорректный пароль'

    def test_registration_with_empty_name(self, driver):
        """Регистрация с пустым именем"""
        _ , email, password = generate_registration_data()
        empty_name = ""  # Пустое имя
        
        # Переход на страницу входа
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.LOGIN_PAGE_TITLE)
            )
        
        # Переход на регистрацию
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
            ).click()
        
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.REGISTRATION_PAGE_TITLE)
            )
        
        # Заполнение формы
        name_input = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.NAME_INPUT)
            )
        name_input.clear()
        name_input.send_keys(empty_name)  # Вводим пустую строку
        
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.EMAIL_INPUT)
        )
        email_input.send_keys(email)
        
        password_input = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.PASSWORD_INPUT)
            )
        password_input.send_keys(password)
        
        register = driver.find_element(*Locators.REGISTER_BUTTON)
        register.click()

        current_url = driver.current_url.lower()
        assert "login" not in current_url, "Не должно быть перехода на страницу входа"

    def test_logout_personal_account(self, driver):
        """Выход из аккаунта"""
        
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_PAGE_TITLE)
            )
        
        email_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.EMAIL_INPUT)
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
        
        # Переход в личный кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        
        # Ожидание загрузки страницы профиля (появление поля имени)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.LOGOUT_BUTTON)
            )
        
        # Выход из аккаунта
        logout = driver.find_element(*Locators.LOGOUT_BUTTON)
        logout.click()
        
        # Проверка, что после выхода появилась страница входа
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_PAGE_TITLE)
            )