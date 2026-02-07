from .base_page import BasePage
from locators import Locators


class RegistrationPage(BasePage):
    """Страница регистрации"""
    
    def set_name(self, name):
        """Ввод имени"""
        self.input_text(Locators.NAME_INPUT, name)
    
    def set_email(self, email):
        """Ввод email"""
        self.input_text(Locators.EMAIL_INPUT, email)
    
    def set_password(self, password):
        """Ввод пароля"""
        self.input_text(Locators.PASSWORD_INPUT, password)
    
    def click_register_button(self):
        """Клик по кнопке 'Зарегистрироваться'"""
        self.click_element(Locators.REGISTER_BUTTON)
    
    def click_login_link(self):
        """Клик по ссылке 'Войти'"""
        self.click_element(Locators.LOGIN_LINK)
    
    def register(self, name, email, password):
        """Полный процесс регистрации"""
        self.set_name(name)
        self.set_email(email)
        self.set_password(password)
        self.click_register_button()
    
    def get_password_error(self):
        """Получение текста ошибки пароля"""
        return self.get_text(Locators.PASSWORD_ERROR)
    
    def is_registration_page_loaded(self):
        """Проверка загрузки страницы регистрации"""
        return self.is_element_visible(Locators.REGISTRATION_PAGE_TITLE)
    
    def is_successful_registration(self):
        """Проверка успешной регистрации (редирект на страницу входа)"""
        return self.is_element_visible(Locators.SUCCESSFUL_REGISTRATION)