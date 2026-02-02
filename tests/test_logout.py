import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


class TestLogout:
    """Тесты выхода из аккаунта"""
    
    @pytest.fixture
    def logged_in_user(self, driver, test_data):
        """Фикстура для входа пользователя"""
        MainPage(driver)
        login_page = LoginPage(driver)
        
        # Регистрация и вход
        user_data = test_data.get_valid_user()
        
        # Переход на страницу регистрации и регистрация
        driver.get("https://stellarburgers.nomoreparties.site/register")
        from pages.registration_page import RegistrationPage
        registration_page = RegistrationPage(driver)
        registration_page.register(
            user_data["name"],
            user_data["email"],
            user_data["password"]
        )
        
        # Вход
        login_page.login(user_data["email"], user_data["password"])
        
        return user_data
    
    def test_logout(self, driver, logged_in_user):
        """Выход из аккаунта"""
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        login_page = LoginPage(driver)
        
        # Переход в личный кабинет
        main_page.click_personal_account_button()
        
        # Клик по кнопке "Выход"
        profile_page.click_logout_button()
        
        # Проверка выхода (редирект на страницу входа)
        assert login_page.is_login_page_loaded()