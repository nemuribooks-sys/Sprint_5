import pytest
import time
import random
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.registration_page import RegistrationPage


class TestLogout:
    """Тесты выхода из аккаунта"""
    
    @pytest.fixture
    def registered_user(self, driver, test_data):
        """Фикстура для регистрации пользователя"""
        # Создаем уникальные данные для пользователя
        timestamp = int(time.time())
        random_num = random.randint(1000, 9999)
        
        user_data = test_data.get_valid_user().copy()  # Копируем базовые данные
        # Делаем email уникальным
        user_data["email"] = user_data["email"].split('@')[0] + f"_{timestamp}_{random_num}@" + user_data["email"].split('@')[1]
        # Делаем имя уникальным
        user_data["name"] = f"{user_data['name']}_{timestamp}"
        
        registration_page = RegistrationPage(driver)
        login_page = LoginPage(driver)
        
        # Регистрация пользователя
        driver.get("https://stellarburgers.nomoreparties.site/register")
        registration_page.register(
            user_data["name"],
            user_data["email"],
            user_data["password"]
        )
        
        # Ждем перехода на страницу входа после регистрации
        login_page.wait_for_login_page()
        
        return user_data
    
    @pytest.fixture
    def logged_in_user(self, driver, registered_user):
        """Фикстура для входа пользователя"""
        login_page = LoginPage(driver)
        
        # Вход с зарегистрированными данными
        driver.get("https://stellarburgers.nomoreparties.site/login")
        login_page.login(registered_user["email"], registered_user["password"])
        
        # Подтверждаем, что вход успешен
        main_page = MainPage(driver)
        main_page.wait_for_main_page()
        
        return registered_user
    
    def test_logout(self, driver, logged_in_user):
        """Выход из аккаунта"""
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        login_page = LoginPage(driver)
        
        # Переход в личный кабинет
        main_page.click_personal_account_button()
        
        # Ждем загрузки страницы профиля
        profile_page.wait_for_profile_page()
        
        # Клик по кнопке "Выход"
        profile_page.click_logout_button()
        
        # Проверка выхода (редирект на страницу входа)
        login_page.wait_for_login_page()
        assert login_page.is_login_page_loaded()