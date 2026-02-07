from .base_page import BasePage
from locators import Locators


class ProfilePage(BasePage):
    """Страница профиля в личном кабинете"""
    
    def click_logout_button(self):
        """Клик по кнопке 'Выход'"""
        self.click_element(Locators.LOGOUT_BUTTON)
    
    def click_constructor_button(self):
        """Клик по кнопке 'Конструктор'"""
        self.click_element(Locators.CONSTRUCTOR_BUTTON)
    
    def click_logo(self):
        """Клик по логотипу"""
        self.click_element(Locators.LOGO)
    
    def is_profile_loaded(self):
        """Проверка загрузки страницы профиля"""
        return self.is_element_visible(Locators.PROFILE_LINK)