import sys
import os
import pytest
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from pages.forgot_password_page import ForgotPasswordPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


class TestLogin:
    """Тесты входа в аккаунт"""
    
    @pytest.fixture
    def unregistered_user_data(self):
        """Фикстура для данных НЕзарегистрированного пользователя"""
        return {
            "name": "НовыйПользователь",
            "email": f"test_{int(time.time())}@example.com",  # Уникальный email
            "password": "Qwerty123"
        }
    
    @pytest.fixture
    def fresh_user_data(self):
        """Фикстура для данных нового пользователя"""
        return {
            "name": "Мария",
            "email": "maria_egorenkova_38_546@yandex.ru",
            "password": "123456"
        }
    
    @pytest.fixture
    def registered_user(self, driver, fresh_user_data):
        """Фикстура для уже зарегистрированного пользователя"""
        MainPage(driver)
        login_page = LoginPage(driver)
        registration_page = RegistrationPage(driver)
        
        try:
            # Регистрация пользователя
            driver.get("https://stellarburgers.education-services.ru/register")
            
            # Проверяем, что мы на странице регистрации
            if not registration_page.is_registration_page_loaded():
                # Если пользователь уже зарегистрирован, пытаемся войти
                driver.get("https://stellarburgers.education-services.ru/login")
                login_page.login(
                    fresh_user_data["email"],
                    fresh_user_data["password"]
                )
            else:
                # Регистрируем нового пользователя
                registration_page.register(
                    fresh_user_data["name"],
                    fresh_user_data["email"],
                    fresh_user_data["password"]
                )
                
                # Ждем перехода на страницу входа
                if login_page.is_login_page_loaded():
                    # Входим с зарегистрированными данными
                    login_page.login(
                        fresh_user_data["email"],
                        fresh_user_data["password"]
                    )
        
        except Exception as e:
            print(f"Ошибка при подготовке пользователя: {e}")
        
        # Возвращаем данные пользователя
        return fresh_user_data
    
    def test_example(self, driver, registered_user):
        """Пример теста с зарегистрированным пользователем"""
        print(f"Тестируем пользователя: {registered_user['email']}")

class TestLoginNavigation:
    """Тесты навигации со страницы входа"""
    
    def test_navigate_back_to_login_from_registration(self, driver):
        """Переход со страницы регистрации обратно на вход"""
        registration_page = RegistrationPage(driver)
        login_page = LoginPage(driver)
        
        driver.get("https://stellarburgers.education-services.ru/register")
        
        # Кликаем на ссылку "Войти"
        registration_page.click_login_link()
        
        # Проверяем, что вернулись на страницу входа
        assert login_page.is_login_page_loaded()
    
    def test_navigate_back_to_login_from_forgot_password(self, driver):
        """Переход со страницы восстановления обратно на вход"""
        forgot_password_page = ForgotPasswordPage(driver)  # noqa: F821
        login_page = LoginPage(driver)
        
        driver.get("https://stellarburgers.education-services.ru/forgot-password")
        
        # Кликаем на ссылку "Войти"
        forgot_password_page.click_login_link()
        
        # Проверяем, что вернулись на страницу входа
        assert login_page.is_login_page_loaded()