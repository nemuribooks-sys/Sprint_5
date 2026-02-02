from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Базовый класс для страниц"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator):
        """Поиск элемента с ожиданием"""
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def click_element(self, locator):
        """Клик по элементу"""
        element = self.find_element(locator)
        element.click()
    
    def input_text(self, locator, text):
        """Ввод текста в поле"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Получение текста элемента"""
        return self.find_element(locator).text
    
    def wait_for_url(self, url):
        """Ожидание URL"""
        return self.wait.until(EC.url_to_be(url))
    
    def is_element_visible(self, locator):
        """Проверка видимости элемента"""
        return self.find_element(locator).is_displayed()