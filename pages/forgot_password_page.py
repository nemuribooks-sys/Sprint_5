from .base_page import BasePage
from locators import Locators


class ForgotPasswordPage(BasePage):
    """Страница восстановления пароля"""
    
    def click_login_link(self):
        """Клик по ссылке 'Войти'"""
        self.click_element(Locators.LOGIN_LINK_FORGOT_PASSWORD)