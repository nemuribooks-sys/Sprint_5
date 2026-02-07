import sys
import os
import pytest

# Добавляем пути к проекту в PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Импорты - только ОДИН раз каждый класс
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestProfileNavigation:
    """Тесты навигации в личном кабинете"""
    
    @pytest.mark.parametrize("user_data", [
        {"email": "maria_egorenkova_38_546@yandex.ru", "password": "123456"},
    ])
    
    def test_navigate_to_personal_account(self, driver, logged_in_user, user_data):
        """Переход в личный кабинет"""
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        
        # Клик по кнопке "Личный кабинет"
        main_page.click_personal_account_button()
        
        # Проверка перехода в личный кабинет
        assert profile_page.is_profile_loaded()
    
    def test_navigate_from_profile_to_constructor_via_button(self, driver, logged_in_user):
        """Переход из личного кабинета в конструктор через кнопку 'Конструктор'"""
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        
        # Переход в личный кабинет
        main_page.click_personal_account_button()
        
        # Клик по кнопке "Конструктор"
        profile_page.click_constructor_button()
        
        # Проверка перехода на главную страницу
        assert main_page.is_main_page_loaded()
    
    def test_navigate_from_profile_to_constructor_via_logo(self, driver, logged_in_user):
        """Переход из личного кабинета в конструктор через логотип"""
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        
        # Переход в личный кабинет
        main_page.click_personal_account_button()
        
        # Клик по логотипу
        profile_page.click_logo()
        
        # Проверка перехода на главную страницу
        assert main_page.is_main_page_loaded()