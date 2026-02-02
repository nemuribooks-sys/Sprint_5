import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


class TestProfileNavigation:
    """Тесты навигации в личном кабинете"""
    
    @pytest.fixture
    def logged_in_user(self, driver, test_data):
        """Фикстура для входа пользователя"""
        main_page = MainPage(driver)
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
    
    def test_navigate_to_personal_account(self, driver, logged_in_user):
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