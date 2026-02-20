from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestConstructor:
    """Тесты конструктора бургеров"""
    
    def test_buns_section_navigation(self, driver):
        """Переход к разделу 'Булки'"""
        driver.find_element(*Locators.MAIN_PAGE_TITLE).click()
        
        # Клик по разделу "Соусы"
        driver.find_element(*Locators.SAUCES_SECTION).click()
        
        # Клик по разделу "Булки"
        driver.find_element(*Locators.BUNS_SECTION).click()
        
        assert driver.find_element(*Locators.ACTIVE_BUNS_SECTION).is_displayed()

    def test_sauces_section_navigation(self, driver):
        """Переход к разделу 'Соусы'"""
        driver.find_element(*Locators.MAIN_PAGE_TITLE).click()
        
        # Клик по разделу "Соусы"
        driver.find_element(*Locators.SAUCES_SECTION).click()
        
        assert driver.find_element(*Locators.ACTIVE_SAUCES_SECTION).is_displayed()
    
    def test_fillings_section_navigation(self, driver):
        """Переход к разделу 'Начинки'"""
        driver.find_element(*Locators.MAIN_PAGE_TITLE).click()
        
        # Клик по разделу "Начинки"
        driver.find_element(*Locators.FILLINGS_SECTION).click()
        
        assert driver.find_element(*Locators.ACTIVE_FILLINGS_SECTION).is_displayed()

    def test_switch_between_sections(self, driver):
        """Переключение между разделами конструктора"""
        driver.find_element(*Locators.MAIN_PAGE_TITLE).click()
        
        # Переход к разделу "Соусы"
        driver.find_element(*Locators.SAUCES_SECTION).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ACTIVE_SAUCES_SECTION)
        )
        
        # Переход к разделу "Начинки"
        driver.find_element(*Locators.FILLINGS_SECTION).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ACTIVE_FILLINGS_SECTION)
        )
    
        # Возврат к разделу "Булки"
        driver.find_element(*Locators.BUNS_SECTION).click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ACTIVE_BUNS_SECTION)
        )
