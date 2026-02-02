import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.forgot_password_page import ForgotPasswordPage


class TestLogin:
    """Тесты входа в аккаунт"""
    
    @pytest.fixture
    def registered_user(self, driver, test_data):
        """Фикстура для регистрации пользователя перед тестами входа"""
        main_page = MainPage(driver)
        registration_page = RegistrationPage(driver)
        login_page = LoginPage(driver)
        
        # Регистрация пользователя
        main_page.click_login_button()
        login_page.click_register_link()
        
        user_data = test_data.get_valid_user()
        registration_page.register(
            user_data["name"],
            user_data["email"],
            user_data["password"]
        )
        
        return user_data
    
    def test_login_via_main_page_button(self, driver, registered_user):
        """Вход по кнопке 'Войти в аккаунт' на главной странице"""
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        
        # Переход на главную страницу
        driver.get("https://stellarburgers.nomoreparties.site/")
        
        # Клик по кнопке "Войти в аккаунт"
        main_page.click_login_button()
        
        # Вход
        login_page.login(registered_user["email"], registered_user["password"])
        
        # Проверка успешного входа (появление кнопки "Оформить заказ")
        assert main_page.is_main_page_loaded()
    
    def test_login_via_personal_account_button(self, driver, registered_user):
        """Вход через кнопку 'Личный кабинет'"""
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        
        # Клик по кнопке "Личный кабинет"
        main_page.click_personal_account_button()
        
        # Вход
        login_page.login(registered_user["email"], registered_user["password"])
        
        # Проверка успешного входа
        assert main_page.is_main_page_loaded()
    
    def test_login_via_registration_form_link(self, driver, registered_user):
        """Вход через кнопку в форме регистрации"""
        main_page = MainPage(driver)
        registration_page = RegistrationPage(driver)
        login_page = LoginPage(driver)
        
        # Переход на страницу регистрации
        main_page.click_login_button()
        login_page.click_register_link()
        
        # Клик по ссылке "Войти" на странице регистрации
        registration_page.click_login_link()
        
        # Вход
        login_page.login(registered_user["email"], registered_user["password"])
        
        # Проверка успешного входа
        assert main_page.is_main_page_loaded()
    
    def test_login_via_forgot_password_form_link(self, driver, registered_user):
        """Вход через кнопку в форме восстановления пароля"""
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        
        # Переход на страницу входа
        main_page.click_login_button()
        
        # Клик по ссылке "Восстановить пароль"
        login_page.click_forgot_password_link()
        
        # Клик по ссылке "Войти" на странице восстановления пароля
        forgot_password_page.click_login_link()
        
        # Вход
        login_page.login(registered_user["email"], registered_user["password"])
        
        # Проверка успешного входа
        assert main_page.is_main_page_loaded()