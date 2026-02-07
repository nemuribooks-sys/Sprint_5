import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.profile_page import ProfilePage


class TestLogin:
    """Тесты входа в аккаунт"""
    
    @pytest.fixture
    def unregistered_user_data(self, test_data):
        """Фикстура для данных НЕзарегистрированного пользователя"""
        return test_data.get_unregistered_user()
    
    @pytest.fixture
    def fresh_user_data(self, test_data):
        """Фикстура для данных нового пользователя (для регистрации)"""
        return test_data.get_valid_user()
    
    @pytest.fixture
    def registered_user(self, driver, fresh_user_data):
        """Фикстура для уже зарегистрированного пользователя"""
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        registration_page = RegistrationPage(driver)
        
        # Регистрация пользователя
        driver.get("https://stellarburgers.education-services.ru/register")
        registration_page.register(
            fresh_user_data["name"],
            fresh_user_data["email"],
            fresh_user_data["password"]
        )
        
        # Ждем перехода на страницу входа
        login_page.wait_for_login_page()
        
        # Входим с зарегистрированными данными
        login_page.login(
            fresh_user_data["email"],
            fresh_user_data["password"]
        )
        
        # Ждем загрузки главной страницы
        main_page.wait_for_main_page()
        
        # Возвращаем данные пользователя
        return fresh_user_data
    
    def test_login_with_unregistered_user(self, driver, unregistered_user_data):
        """Тест: Вход с данными незарегистрированного пользователя"""
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        
        # 1. Переходим на главную страницу
        driver.get("https://stellarburgers.education-services.ru/")
        
        # 2. Нажимаем кнопку "Войти в аккаунт"
        main_page.click_login_button()
        
        # 3. Вводим данные незарегистрированного пользователя
        login_page.login(
            unregistered_user_data["email"],
            unregistered_user_data["password"]
        )
        
        # 4. Проверяем, что появилась ошибка (пользователь не найден)
        assert login_page.is_error_message_displayed(), "Ожидалась ошибка при входе незарегистрированного пользователя"
        
        # 5. Проверяем текст ошибки (опционально)
        error_text = login_page.get_error_message_text()
        assert "Неверный логин или пароль" in error_text or "пользователь не найден" in error_text.lower()
    
    def test_successful_login_with_registration(self, driver, fresh_user_data):
        """Тест: Регистрация нового пользователя и успешный вход"""
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        registration_page = RegistrationPage(driver)
        
        # Шаг 1: Регистрация нового пользователя
        driver.get("https://stellarburgers.education-services.ru/register")
        registration_page.register(
            fresh_user_data["name"],
            fresh_user_data["email"],
            fresh_user_data["password"]
        )
        
        # Ждем перехода на страницу входа после регистрации
        login_page.wait_for_login_page()
        
        # Шаг 2: Вход с только что зарегистрированными данными
        login_page.login(
            fresh_user_data["email"],
            fresh_user_data["password"]
        )
        
        # Проверяем успешный вход
        main_page.wait_for_main_page()
        assert main_page.is_main_page_loaded(), "Не удалось войти после регистрации"
        assert main_page.is_order_button_visible(), "Кнопка 'Оформить заказ' не видна"
    
    def test_login_with_wrong_password(self, driver, fresh_user_data):
        """Тест: Вход с правильным email, но неправильным паролем"""
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        registration_page = RegistrationPage(driver)
        
        # 1. Сначала регистрируем пользователя
        driver.get("https://stellarburgers.education-services.ru/register")
        registration_page.register(
            fresh_user_data["name"],
            fresh_user_data["email"],
            fresh_user_data["password"]
        )
        login_page.wait_for_login_page()
        
        # 2. Пытаемся войти с неправильным паролем
        login_page.login(
            fresh_user_data["email"],
            "WrongPassword123"  # Неправильный пароль
        )
        
        # 3. Проверяем, что появилась ошибка
        assert login_page.is_error_message_displayed(), "Ожидалась ошибка при вводе неправильного пароля"
    
    def test_login_via_personal_account_button_after_logout(self, driver, fresh_user_data):
        """Тест: Вход через кнопку 'Личный кабинет' после выхода"""
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        registration_page = RegistrationPage(driver)
        profile_page = ProfilePage(driver)
        
        # 1. Регистрация пользователя
        driver.get("https://stellarburgers.education-services.ru/register")
        registration_page.register(
            fresh_user_data["name"],
            fresh_user_data["email"],
            fresh_user_data["password"]
        )
        login_page.wait_for_login_page()
        
        # 2. Входим
        login_page.login(
            fresh_user_data["email"],
            fresh_user_data["password"]
        )
        main_page.wait_for_main_page()
        
        # 3. Выходим из аккаунта
        main_page.click_personal_account_button()
        profile_page.wait_for_profile_page()
        profile_page.click_logout_button()
        login_page.wait_for_login_page()
        
        # 4. Теперь входим через кнопку "Личный кабинет" на главной
        driver.get("https://stellarburgers.education-services.ru/")
        main_page.click_personal_account_button()
        
        # 5. Вводим данные
        login_page.login(
            fresh_user_data["email"],
            fresh_user_data["password"]
        )
        
        # 6. Проверяем успешный вход
        main_page.wait_for_main_page()
        assert main_page.is_main_page_loaded()
    
    def test_login_via_main_page_button_with_registered_user(self, driver, registered_user):
        """Вход по кнопке 'Войти в аккаунт' на главной странице с зарегистрированным пользователем"""
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        
        # Переход на главную страницу
        driver.get("https://stellarburgers.education-services.ru/")
        
        # Клик по кнопке "Войти в аккаунт"
        main_page.click_login_button()
        
        # Вход
        login_page.login(registered_user["email"], registered_user["password"])
        
        # Проверка успешного входа
        assert main_page.is_main_page_loaded()
    
    def test_login_via_personal_account_button_with_registered_user(self, driver, registered_user):
        """Вход через кнопку 'Личный кабинет' с зарегистрированным пользователем"""
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        
        # Переход на главную страницу
        driver.get("https://stellarburgers.education-services.ru/")
        
        # Клик по кнопке "Личный кабинет" (для неавторизованного пользователя)
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
        driver.get("https://stellarburgers.education-services.ru/register")
        
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
        driver.get("https://stellarburgers.education-services.ru/login")
        
        # Клик по ссылке "Восстановить пароль"
        login_page.click_forgot_password_link()
        
        # Клик по ссылке "Войти" на странице восстановления пароля
        forgot_password_page.click_login_link()
        
        # Вход
        login_page.login(registered_user["email"], registered_user["password"])
        
        # Проверка успешного входа
        assert main_page.is_main_page_loaded()