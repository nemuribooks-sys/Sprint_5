from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestConstructor:
    """Тесты конструктора бургеров"""
    
    def test_buns_section_navigation(self, driver):
        """Переход к разделу 'Булки'"""
        driver.get("https://stellarburgers.education-services.ru/")
        
        # Клик по разделу "Соусы"
        driver.find_element(*Locators.SAUCES_SECTION).click()
        
        # Клик по разделу "Булки"
        driver.find_element(*Locators.BUNS_SECTION).click()
        
        # Проверяем, что раздел "Булки" стал активным
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ACTIVE_BUNS_SECTION)
        )
    
    def test_sauces_section_navigation(self, driver):
        """Переход к разделу 'Соусы'"""
        driver.get("https://stellarburgers.education-services.ru/")
        
        # Клик по разделу "Соусы"
        driver.find_element(*Locators.SAUCES_SECTION).click()
        
        # Проверяем, что раздел "Соусы" стал активным
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ACTIVE_SAUCES_SECTION)
        )
    
    def test_fillings_section_navigation(self, driver):
        """Переход к разделу 'Начинки'"""
        driver.get("https://stellarburgers.education-services.ru/")
        
        # Клик по разделу "Начинки"
        driver.find_element(*Locators.FILLINGS_SECTION).click()
        
        # Проверяем, что раздел "Начинки" стал активным
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ACTIVE_FILLINGS_SECTION)
        )
    
    def test_switch_between_sections(self, driver):
        """Переключение между разделами конструктора"""
        driver.get("https://stellarburgers.education-services.ru/")
        
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