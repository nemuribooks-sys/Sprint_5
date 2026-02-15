import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

from data import Credentials
from locators import Locators

class TestLogin:
    """Тесты входа в аккаунт"""
    
    def test_login_account(self, driver):
        # Ждем загрузки главной страницы
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.MAIN_PAGE_TITLE)
        )
        print("\n=== Главная страница загружена ===")
        
        # Клик по кнопке "Личный кабинет"
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        print("Клик по кнопке 'Личный кабинет' выполнен")
        
        # Ждем загрузки страницы входа
        time.sleep(2)  # Даем время для загрузки
        
        # ОТЛАДКА: выводим текущий URL
        print(f"Текущий URL после клика: {driver.current_url}")
        
        # ОТЛАДКА: ищем все поля ввода
        print("\n=== Поиск всех полей ввода на странице ===")
        inputs = driver.find_elements(By.TAG_NAME, "input")
        for i, input_elem in enumerate(inputs):
            print(f"\nПоле {i + 1}:")
            print(f"  type={input_elem.get_attribute('type')}")
            print(f"  name={input_elem.get_attribute('name')}")
            print(f"  placeholder={input_elem.get_attribute('placeholder')}")
            print(f"  class={input_elem.get_attribute('class')}")
            print(f"  id={input_elem.get_attribute('id')}")
        
        # ОТЛАДКА: ищем все кнопки
        print("\n=== Поиск всех кнопок на странице ===")
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for i, button in enumerate(buttons):
            print(f"Кнопка {i + 1}: текст='{button.text}'")
        
        # Теперь заполняем форму (исправим локаторы после отладки)
        # Временно используем найденные локаторы
        email_input = driver.find_element(By.XPATH, "//input[@type='text']")  # Первое текстовое поле
        email_input.send_keys(Credentials.EMAIL)
        print("Email введен")
        
        password_input = driver.find_element(By.XPATH, "//input[@type='password']")
        password_input.send_keys(Credentials.PASSWORD)
        print("Пароль введен")
        
        login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
        login_button.click()
        print("Клик по кнопке 'Войти' выполнен")
        
        # Проверяем успешный вход
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.MAIN_PAGE_TITLE)
        )
        
        assert driver.find_element(*Locators.MAIN_PAGE_TITLE).is_displayed(), \
            "Не удалось войти в аккаунт"
        print("Тест успешно завершен!")