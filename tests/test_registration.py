import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

from helper import generate_registration_data
from locators import Locators

class TestRegistration:
    """Тесты регистрации"""
    
    def test_successful_registration(self, driver):
        """Успешная регистрация"""
        name, email, password = generate_registration_data()
        print(f"\n=== Тестовые данные ===")
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


class TestNegativeRegistration:
    
    def test_registration_with_short_password(self, driver):
        """Негативный сценарий: регистрация с паролем меньше 6 символов"""
        
        # Генерируем данные, но пароль делаем коротким (< 6 символов)
        name, email, _ = generate_registration_data()
        short_password = "12345"  # 5 символов
        print(f"\n=== Тестовые данные ===")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Password: {short_password} (короткий пароль)")
        
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
        
        # Заполняем форму
        # Поле Имя
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input)[1]"))
        )
        name_input.send_keys(name)
        print("✓ Имя введено")
        
        # Поле Email
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input)[2]"))
        )
        email_input.send_keys(email)
        print("✓ Email введен")
        
        # Поле Пароль (вводим короткий пароль)
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input)[3]"))
        )
        password_input.send_keys(short_password)
        print(f"✓ Короткий пароль '{short_password}' введен")
        
        # Кнопка регистрации
        register_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Зарегистрироваться']"))
        )
        register_button.click()
        print("✓ Клик по кнопке 'Зарегистрироваться' выполнен")
        
        # НЕГАТИВНАЯ ПРОВЕРКА: ждем появления сообщения об ошибке
        error_found = False
        
        # Вариант 1: Проверяем сообщение об ошибке под полем пароля
        try:
            error_message = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//*[contains(text(), 'Пароль должен содержать не менее 6 символов')]")
                )
            )
            print(f"✓ Найдено сообщение об ошибке: '{error_message.text}'")
            error_found = True
        except TimeoutException:
            print("Сообщение 'Пароль должен содержать не менее 6 символов' не найдено")
        
        # Вариант 2: Альтернативный текст ошибки
        if not error_found:
            try:
                error_message = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//*[contains(text(), 'Некорректный парол')]")
                    )
                )
                print(f"✓ Найдено сообщение об ошибке: '{error_message.text}'")
                error_found = True
            except TimeoutException:
                print("Альтернативное сообщение об ошибке не найдено")
        
        # Вариант 3: Проверяем, что мы НЕ перешли на страницу входа
        if not error_found:
            try:
                # Проверяем, что URL не содержит login
                current_url = driver.current_url
                assert "login" not in current_url.lower(), \
                    f"Не должно быть перехода на страницу входа, но URL: {current_url}"
                assert "register" in current_url.lower() or "registration" in current_url.lower(), \
                    f"Ожидали остаться на странице регистрации, но URL: {current_url}"
                print("✓ Пользователь остался на странице регистрации (не произошло перенаправления)")
                
                # Дополнительная проверка: кнопка регистрации все еще доступна
                assert register_button.is_enabled(), "Кнопка регистрации должна быть активна"
                print("✓ Кнопка регистрации доступна для повторной попытки")
                error_found = True
            except AssertionError as e:
                print(f"Ошибка проверки: {e}")
        
        assert error_found, "Не найден ни один признак ошибки при коротком пароле"
        print("✓ Негативный тест успешно завершен: система заблокировала короткий пароль")

    def test_registration_with_empty_name(self, driver):
        """Негативный сценарий: регистрация с пустым именем"""
        # Генерируем данные, но имя оставляем пустым
        _, email, password = generate_registration_data()
        empty_name = ""  # Пустое имя
        print(f"\n=== Тестовые данные ===")
        print(f"Name: '{empty_name}' (пустое имя)")
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
        
        # Заполняем форму
        # Поле Имя (оставляем пустым)
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input)[1]"))
        )
        name_input.clear()
        name_input.send_keys(empty_name)  # Вводим пустую строку
        print("✓ Поле имени очищено (оставлено пустым)")
        
        # Поле Email
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input)[2]"))
        )
        email_input.send_keys(email)
        print("✓ Email введен")
        
        # Поле Пароль
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
        
        # НЕГАТИВНАЯ ПРОВЕРКА
        error_found = False
        
        # Вариант 1: Проверяем сообщение об ошибке под полем имени
        try:
            error_message = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Введите имя')]"))
            )
            print(f"✓ Найдено сообщение об ошибке: '{error_message.text}'")
            error_found = True
        except TimeoutException:
            print("Сообщение 'Введите имя' не найдено")
        
        # Вариант 2: Альтернативный текст ошибки
        if not error_found:
            try:
                error_message = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Имя обязательно')]"))
                )
                print(f"✓ Найдено сообщение об ошибке: '{error_message.text}'")
                error_found = True
            except TimeoutException:
                print("Сообщение 'Имя обязательно' не найдено")
        
        # Вариант 3: Проверяем HTML5 валидацию
        if not error_found:
            try:
                name_input = driver.find_element(By.XPATH, "(//input)[1]")
                # Проверяем через JavaScript, есть ли сообщение валидации
                validation_message = driver.execute_script(
                    "return arguments[0].validationMessage;", 
                    name_input
                )
                if validation_message:
                    print(f"✓ Найдено HTML5 сообщение валидации: '{validation_message}'")
                    error_found = True
            except Exception as e:
                print(f"Ошибка при проверке HTML5 валидации: {e}")
        
        # Вариант 4: Проверяем подсветку поля красным
        if not error_found:
            try:
                name_input = driver.find_element(By.XPATH, "(//input)[1]")
                input_class = name_input.get_attribute("class") or ""
                if "error" in input_class.lower() or "invalid" in input_class.lower():
                    print(f"✓ Поле имени подсвечено как ошибочное (class: {input_class})")
                    error_found = True
            except NoSuchElementException:
                print("Поле имени не найдено для проверки класса")
        
        # Вариант 5: Проверяем, что кнопка стала неактивной
        if not error_found:
            try:
                if not register_button.is_enabled():
                    print("✓ Кнопка регистрации стала неактивной (корректное поведение)")
                    error_found = True
            except Exception as e:
                print(f"Ошибка при проверке активности кнопки: {e}")
        
        # Вариант 6: Проверяем URL - мы должны остаться на странице регистрации
        if not error_found:
            try:
                current_url = driver.current_url.lower()
                assert "login" not in current_url, "Не должно быть перехода на страницу входа"
                assert "register" in current_url or "registration" in current_url or "signup" in current_url, \
                    f"Ожидали остаться на странице регистрации, но URL: {current_url}"
                print("✓ Пользователь остался на странице регистрации")
                error_found = True
            except AssertionError as e:
                print(f"Ошибка проверки URL: {e}")
        
        assert error_found, "Не найден ни один признак ошибки при пустом имени"
        print("✓ Негативный тест успешно завершен: система заблокировала регистрацию с пустым именем")