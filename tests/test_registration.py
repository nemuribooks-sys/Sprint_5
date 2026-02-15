import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

from helper import generate_registration_data
from locators import Locators

class TestRegistration:
    """Тесты регистрации"""
    
    def test_successful_registration(self, driver):
        """Успешная регистрация"""
        name, email, password = generate_registration_data()
        print(f"\n=== Тестовые данные ===")  # noqa: F541
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Password: {password}")
        
        # Ждем загрузки главной страницы
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.MAIN_PAGE_TITLE)
        )
        print("✓ Главная страница загружена")
        
        # Клик по кнопке "Личный кабинет"
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        print("✓ Клик по 'Личный кабинет' выполнен")
        
        # Ждем загрузки страницы входа
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_PAGE_TITLE)
        )
        print("✓ Страница входа загружена")
        
        # Клик по ссылке "Зарегистрироваться"
        register_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.REGISTER_LINK)
        )
        register_link.click()
        print("✓ Клик по 'Зарегистрироваться' выполнен")
        
        # Даем время для загрузки страницы регистрации
        time.sleep(2)
        
        # ОТЛАДКА: выводим текущий URL
        print(f"Текущий URL: {driver.current_url}")
        
        # ОТЛАДКА: ищем все поля на странице регистрации
        print("\n=== Поиск всех полей на странице регистрации ===")
        all_inputs = driver.find_elements(By.TAG_NAME, "input")
        print(f"Найдено полей ввода: {len(all_inputs)}")
        
        for i, input_elem in enumerate(all_inputs):
            print(f"\nПоле {i + 1}:")
            print(f"  type: {input_elem.get_attribute('type')}")
            print(f"  name: {input_elem.get_attribute('name')}")
            print(f"  placeholder: {input_elem.get_attribute('placeholder')}")
            print(f"  class: {input_elem.get_attribute('class')}")
            print(f"  id: {input_elem.get_attribute('id')}")
        
        # ОТЛАДКА: ищем заголовок страницы регистрации
        print("\n=== Поиск заголовка страницы регистрации ===")
        headers = driver.find_elements(By.TAG_NAME, "h2")
        for h in headers:
            print(f"Заголовок h2: '{h.text}'")
        
        # Теперь заполняем форму с правильными локаторами
        # Поле Имя (обычно первое поле)
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input)[1]"))
        )
        name_input.send_keys(name)
        print("✓ Имя введено")
        
        # Поле Email (второе поле)
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input)[2]"))
        )
        email_input.send_keys(email)
        print("✓ Email введен")
        
        # Поле Пароль (третье поле)
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input)[3]"))
        )
        password_input.send_keys(password)
        print("✓ Пароль введен")
        
        # Кнопка регистрации
        register_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Зарегистрироваться']"))
        )
        register_button.click()
        print("✓ Клик по кнопке 'Зарегистрироваться' выполнен")
        
        # Проверяем, что появилась страница входа
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.LOGIN_PAGE_TITLE)
        )
        print("✓ Перенаправление на страницу входа")
        

        print("✓ Тест успешно завершен!")