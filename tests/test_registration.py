import sys
import os

# Добавляем пути к проекту в PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Импорты
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
import pytest

class TestRegistration:
    """Тесты регистрации"""
    
    @pytest.mark.parametrize("user_data", [
        {"name": "Мария", "email": "maria_egorenkova_38_546@yandex.ru", "password": "123456"},
    ])
    def test_successful_registration(self, driver, user_data):
        """Успешная регистрация"""
        main_page = MainPage(driver)
        registration_page = RegistrationPage(driver)
        login_page = LoginPage(driver)
        
        # Переход на страницу регистрации
        main_page.click_login_button()
        login_page.click_register_link()
        
        # Проверка загрузки страницы регистрации
        assert registration_page.is_registration_page_loaded()
        
        # Регистрация
        registration_page.register(
            user_data["name"],
            user_data["email"],
            user_data["password"]
        )
        
        # Проверка успешной регистрации (редирект на страницу входа)
        assert login_page.is_login_page_loaded()
    
    def test_registration_with_short_password(self, driver, test_data):
        """Регистрация с некорректным паролем (меньше 6 символов)"""
        main_page = MainPage(driver)
        registration_page = RegistrationPage(driver)
        login_page = LoginPage(driver)
        
        # Переход на страницу регистрации
        main_page.click_login_button()
        login_page.click_register_link()
        
        # Регистрация с коротким паролем
        user_data = test_data.get_short_password_user()
        registration_page.register(
            user_data["name"],
            user_data["email"],
            user_data["password"]
        )
        
        # Проверка ошибки
        error_text = registration_page.get_password_error()
        assert "Некорректный пароль" in error_text
    
    def test_registration_with_empty_name(self, driver, test_data):
        """Регистрация с пустым именем"""
        main_page = MainPage(driver)
        registration_page = RegistrationPage(driver)
        login_page = LoginPage(driver)
        
        # Переход на страницу регистрации
        main_page.click_login_button()
        login_page.click_register_link()
        
        # Регистрация с пустым именем
        user_data = test_data.get_valid_user()
        registration_page.set_email(user_data["email"])
        registration_page.set_password(user_data["password"])
        # Имя не заполняем
        registration_page.click_register_button()
        
        # Проверка, что остались на странице регистрации
        assert registration_page.is_registration_page_loaded()
    
    def test_registration_with_invalid_email(self, driver, test_data):
        """Регистрация с некорректным email"""
        main_page = MainPage(driver)
        registration_page = RegistrationPage(driver)
        login_page = LoginPage(driver)
        
        # Переход на страницу регистрации
        main_page.click_login_button()
        login_page.click_register_link()
        
        # Регистрация с некорректным email
        user_data = test_data.get_valid_user()
        registration_page.set_name(user_data["name"])
        registration_page.set_password(user_data["password"])
        registration_page.set_email("invalid-email")
        registration_page.click_register_button()
        
        # Проверка, что остались на странице регистрации
        assert registration_page.is_registration_page_loaded()