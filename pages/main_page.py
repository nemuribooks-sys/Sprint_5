from .base_page import BasePage
from locators import Locators


class MainPage(BasePage):
    """Главная страница Stellar Burgers"""
    
    def click_login_button(self):
        """Клик по кнопке 'Войти в аккаунт'"""
        self.click_element(Locators.LOGIN_BUTTON_MAIN)
    
    def click_personal_account_button(self):
        """Клик по кнопке 'Личный кабинет'"""
        self.click_element(Locators.PERSONAL_ACCOUNT_BUTTON)
    
    def click_constructor_button(self):
        """Клик по кнопке 'Конструктор'"""
        self.click_element(Locators.CONSTRUCTOR_BUTTON)
    
    def click_logo(self):
        """Клик по логотипу"""
        self.click_element(Locators.LOGO)
    
    def click_buns_section(self):
        """Клик по разделу 'Булки'"""
        self.click_element(Locators.BUNS_SECTION)
    
    def click_sauces_section(self):
        """Клик по разделу 'Соусы'"""
        self.click_element(Locators.SAUCES_SECTION)
    
    def click_fillings_section(self):
        """Клик по разделу 'Начинки'"""
        self.click_element(Locators.FILLINGS_SECTION)
    
    def get_active_section_text(self):
        """Получение текста активного раздела"""
        return self.get_text(Locators.ACTIVE_SECTION)
    
    def is_buns_section_active(self):
        """Проверка, что раздел 'Булки' активен"""
        return "Булки" in self.get_active_section_text()
    
    def is_sauces_section_active(self):
        """Проверка, что раздел 'Соусы' активен"""
        return "Соусы" in self.get_active_section_text()
    
    def is_fillings_section_active(self):
        """Проверка, что раздел 'Начинки' активен"""
        return "Начинки" in self.get_active_section_text()
    
    def is_main_page_loaded(self):
        """Проверка загрузки главной страницы"""
        return self.is_element_visible(Locators.MAIN_PAGE_TITLE)