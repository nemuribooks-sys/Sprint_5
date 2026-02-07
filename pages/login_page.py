from .base_page import BasePage
from locators import Locators


class LoginPage(BasePage):
    """Страница входа"""
    
    def set_email(self, email):
        """Ввод email"""
        self.input_text(Locators.EMAIL_INPUT, email)
    
    def set_password(self, password):
        """Ввод пароля"""
        self.input_text(Locators.PASSWORD_INPUT, password)
    
    def click_login_button(self):
        """Клик по кнопке 'Войти'"""
        self.click_element(Locators.LOGIN_FORM_BUTTON)
    
    def click_register_link(self):
        """Клик по ссылке 'Зарегистрироваться'"""
        self.click_element(Locators.REGISTER_LINK)
    
    def click_forgot_password_link(self):
        """Клик по ссылке 'Восстановить пароль'"""
        self.click_element(Locators.FORGOT_PASSWORD_LINK)
    
    def login(self, email, password):
        """Полный процесс входа"""
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()
    
    def is_login_page_loaded(self):
        """Проверка загрузки страницы входа"""
        return self.is_element_visible(Locators.LOGIN_PAGE_TITLE)