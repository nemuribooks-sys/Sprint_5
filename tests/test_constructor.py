from locators import Locators
from data import Credentials
from curl import *


class TestConstructor:
    """Тесты конструктора бургеров"""
    
    def test_buns_section_navigation(self, driver):
        """Переход к разделу 'Булки'"""
        
        # Клик по разделу "Соусы"
        driver.find_element(*Locators.SAUCES_SECTION).click()
        
        # Клик по разделу "Булки"
        driver.find_element(*Locators.BUNS_SECTION ).click()
    
    def test_sauces_section_navigation(self, driver):
        """Переход к разделу 'Соусы'"""
        
        # Клик по разделу "Соусы"
        driver.find_element(*Locators.SAUCES_SECTION).click()
        
    
    def test_fillings_section_navigation(self, driver):
        """Переход к разделу 'Начинки'"""
        
        # Клик по разделу "Начинки"
        driver.find_element(*Locators.FILLINGS_SECTION).click()
        
    
    def test_switch_between_sections(self, driver):
        """Переключение между разделами конструктора"""
        
        # Переход к разделу "Соусы"
        driver.find_element(*Locators.SAUCES_SECTION).click()
        
        # Переход к разделу "Начинки"
        driver.find_element(*Locators.FILLINGS_SECTION).click()
        
        # Возврат к разделу "Булки"
        driver.find_element(*Locators.BUNS_SECTION ).click()