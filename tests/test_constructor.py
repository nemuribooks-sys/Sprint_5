import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from pages.main_page import MainPage


class TestConstructor:
    """Тесты конструктора бургеров"""
    
    def test_buns_section_navigation(self, driver):
        """Переход к разделу 'Булки'"""
        main_page = MainPage(driver)

        # Клик по разделу "Соусы"
        main_page.click_sauces_section()
        
        # Клик по разделу "Булки"
        main_page.click_buns_section()
        
        # Проверка активности раздела "Булки"
        assert main_page.is_buns_section_active()
    
    def test_sauces_section_navigation(self, driver):
        """Переход к разделу 'Соусы'"""
        main_page = MainPage(driver)
        
        # Клик по разделу "Соусы"
        main_page.click_sauces_section()
        
        # Проверка активности раздела "Соусы"
        assert main_page.is_sauces_section_active()
    
    def test_fillings_section_navigation(self, driver):
        """Переход к разделу 'Начинки'"""
        main_page = MainPage(driver)
        
        # Клик по разделу "Начинки"
        main_page.click_fillings_section()
        
        # Проверка активности раздела "Начинки"
        assert main_page.is_fillings_section_active()
    
    def test_switch_between_sections(self, driver):
        """Переключение между разделами конструктора"""
        main_page = MainPage(driver)
        
        # Переход к разделу "Соусы"
        main_page.click_sauces_section()
        assert main_page.is_sauces_section_active()
        
        # Переход к разделу "Начинки"
        main_page.click_fillings_section()
        assert main_page.is_fillings_section_active()
        
        # Возврат к разделу "Булки"
        main_page.click_buns_section()
        assert main_page.is_buns_section_active()