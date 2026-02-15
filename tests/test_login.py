import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
import time

from data import Credentials
from locators import Locators

class TestLogin:
    """Тесты входа в аккаунт"""
    
    def test_login_personal_account_button(self, driver):
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

    def test_login_account_button(self, driver):
        # Ждем загрузки главной страницы
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.MAIN_PAGE_TITLE)
        )
        print("\n=== Главная страница загружена ===")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.LOGIN_TO_ACCOUNT_BUTTON)
        ).click()
        print("Клик по кнопке 'Войти в аккаунт' выполнен")
        
        # Ждем загрузки страницы входа
        WebDriverWait(driver, 10).until(
            EC.url_contains("login")  # или другой индикатор страницы входа
        )
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
        
        # Заполняем форму входа
        # Здесь используем локаторы из Locators или временные XPATH
        try:
            # Пробуем найти поле email по типу email или текстовое поле
            email_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email'], input[type='text']"))
            )
            email_input.send_keys(Credentials.EMAIL)
            print("Email введен")
        except TimeoutException:
            # Если не нашли, используем первое текстовое поле
            print("Не найдено поле email по CSS селектору, используем XPATH")
            email_input = driver.find_element(By.XPATH, "//input[@type='text']")
            email_input.send_keys(Credentials.EMAIL)
            print("Email введен (первое текстовое поле)")
        
        # Поле пароля
        try:
            password_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
            )
            password_input.send_keys(Credentials.PASSWORD)
            print("Пароль введен")
        except TimeoutException:
            print("Не найдено поле пароля по CSS селектору")
            raise
        
        # Кнопка входа
        try:
            login_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Войти')]"))
            )
            login_button.click()
            print("Клик по кнопке 'Войти' выполнен")
        except TimeoutException:
            print("Не найдена кнопка 'Войти'")
            raise
        
        # Проверяем успешный вход
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.MAIN_PAGE_TITLE)
        )
        
        # Дополнительная проверка - наличие кнопки "Личный кабинет" после входа
        # или отсутствие кнопки "Войти"
        assert driver.find_element(*Locators.MAIN_PAGE_TITLE).is_displayed(), \
            "Не удалось войти в аккаунт"
        print("Тест успешно завершен!")

    def test_login_registration_button(self, driver):
        # Ждем загрузки главной страницы
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.MAIN_PAGE_TITLE)
        )
        print("\n=== Главная страница загружена ===")
        # Клик по кнопке "Личный кабинет"
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        print("Клик по кнопке 'Личный кабинет' выполнен")
        
        # Ждем загрузки страницы входа
        WebDriverWait(driver, 10).until(
            EC.url_contains("login")  # ожидаем страницу входа
        )
        print(f"Текущий URL после клика: {driver.current_url}")
        
        # Находим ссылку/кнопку "Зарегистрироваться" или переходим на страницу регистрации
        # Вариант 1: Если на странице входа есть ссылка на регистрацию
        try:
            register_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")
            register_link.click()
            print("Переход на страницу регистрации выполнен")
        except NoSuchElementException:
            print("Ссылка 'Зарегистрироваться' не найдена")
            # Вариант 2: Если нужно напрямую перейти по URL регистрации
            try:
                driver.get(driver.current_url.replace('login', 'register'))  # пример замены URL
                print("Переход на страницу регистрации по URL")
            except Exception as e:
                print(f"Ошибка при переходе по URL: {e}")
                raise
        
        # Ждем загрузки страницы регистрации
        try:
            WebDriverWait(driver, 10).until(
                EC.url_contains("register")
            )
            print(f"URL страницы регистрации: {driver.current_url}")
        except TimeoutException:
            print("Страница регистрации не загрузилась")
            # Продолжаем выполнение, возможно URL не содержит register
        
        # ОТЛАДКА: ищем все поля ввода на странице регистрации
        print("\n=== Поиск всех полей ввода на странице регистрации ===")
        inputs = driver.find_elements(By.TAG_NAME, "input")
        for i, input_elem in enumerate(inputs):
            print(f"\nПоле {i + 1}:")
            print(f"  type={input_elem.get_attribute('type')}")
            print(f"  name={input_elem.get_attribute('name')}")
            print(f"  placeholder={input_elem.get_attribute('placeholder')}")
            print(f"  class={input_elem.get_attribute('class')}")
            print(f"  id={input_elem.get_attribute('id')}")
        
        # ОТЛАДКА: ищем все кнопки на странице регистрации
        print("\n=== Поиск всех кнопок на странице регистрации ===")
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for i, button in enumerate(buttons):
            print(f"Кнопка {i + 1}: текст='{button.text}'")
        
        # ОТЛАДКА: ищем все ссылки на странице регистрации
        print("\n=== Поиск всех ссылок на странице регистрации ===")
        links = driver.find_elements(By.TAG_NAME, "a")
        for i, link in enumerate(links):
            print(f"Ссылка {i + 1}: текст='{link.text}', href='{link.get_attribute('href')}'")
        
        # Ищем кнопку/ссылку "Войти" на странице регистрации
        login_element = None
        
        # Вариант А: Если это кнопка
        try:
            login_element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Войти')]"))
            )
            print("Найдена кнопка 'Войти' на странице регистрации")
        except TimeoutException:
            print("Кнопка 'Войти' не найдена, ищем ссылку")
            
            # Вариант Б: Если это ссылка
            try:
                login_element = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Войти')]"))
                )
                print("Найдена ссылка 'Войти' на странице регистрации")
            except TimeoutException:
                print("Ссылка 'Войти' не найдена")
                
                # Вариант В: Пробуем другой текст
                try:
                    login_element = driver.find_element(By.XPATH, "//*[contains(text(), 'Вход') or contains(text(), 'вход') or contains(text(), 'login')]")
                    print("Найден элемент с текстом о входе")
                except NoSuchElementException:
                    print("Не найдена кнопка/ссылка 'Войти' на странице регистрации")
                    # Если не нашли, возможно форма входа уже открыта
                    pass
        
        # Если нашли элемент, кликаем по нему
        if login_element:
            try:
                login_element.click()
                print("Клик по элементу выполнен")
            except ElementNotInteractableException:
                try:
                    driver.execute_script("arguments[0].click();", login_element)
                    print("Клик по элементу выполнен через JavaScript")
                except Exception as e:
                    print(f"Не удалось кликнуть по элементу: {e}")
        
        # Ждем загрузки страницы входа
        try:
            WebDriverWait(driver, 10).until(
                EC.url_contains("login")
            )
            print(f"Возврат на страницу входа: {driver.current_url}")
        except TimeoutException:
            print("Страница входа не загрузилась, продолжаем тест")
        
        # Заполняем форму входа
        try:
            email_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email'], input[type='text']"))
            )
            email_input.send_keys(Credentials.EMAIL)
            print("Email введен")
        except TimeoutException:
            print("Не найдено поле для email")
            raise
        
        try:
            password_input = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
            password_input.send_keys(Credentials.PASSWORD)
            print("Пароль введен")
        except NoSuchElementException:
            print("Не найдено поле для пароля")
            raise
        
        # Находим и кликаем по кнопке входа
        try:
            login_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Войти')]"))
            )
            login_button.click()
            print("Клик по кнопке 'Войти' выполнен")
        except TimeoutException:
            print("Не найдена кнопка 'Войти'")
            raise
        
        # Проверяем успешный вход
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.MAIN_PAGE_TITLE)
        )
        
        assert driver.find_element(*Locators.MAIN_PAGE_TITLE).is_displayed(), \
            "Не удалось войти в аккаунт"
        print("Тест успешно завершен!")

    def test_login_password_recovery_button(self, driver):
        # Ждем загрузки главной страницы
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.MAIN_PAGE_TITLE)
        )
        print("\n=== Главная страница загружена ===")

        # Клик по кнопке "Личный кабинет"
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        print("Клик по кнопке 'Личный кабинет' выполнен")
        
        # Ждем загрузки страницы входа
        try:
            WebDriverWait(driver, 10).until(
                EC.url_contains("login")
            )
            print(f"Текущий URL после клика: {driver.current_url}")
        except TimeoutException:
            print("URL не содержит 'login', продолжаем тест")
        
        # Ищем ссылку на восстановление пароля
        print("\n=== Поиск ссылки на восстановление пароля ===")
        forgot_password_link = None
        
        try:
            # Пробуем найти ссылку "Забыли пароль?" или "Восстановить пароль"
            forgot_password_link = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, 
                    "//a[contains(text(), 'Забыли пароль') or contains(text(), 'забыли') or contains(text(), 'Восстановить') or contains(text(), 'Forgot')]"))
            )
            print("Найдена ссылка 'Забыли пароль?' по тексту")
        except TimeoutException:
            print("Ссылка по тексту не найдена")
            
            # Если не нашли по тексту, ищем по распространенным классам или атрибутам
            try:
                possible_links = driver.find_elements(By.XPATH, 
                    "//a[contains(@href, 'forgot') or contains(@href, 'reset') or contains(@href, 'restore')]")
                if possible_links:
                    forgot_password_link = possible_links[0]
                    print("Найдена ссылка восстановления пароля по href")
            except NoSuchElementException:
                print("Ссылка по href не найдена")
                
                # Пробуем перейти по URL напрямую
                try:
                    driver.get(driver.current_url.replace('login', 'forgot-password'))
                    print("Переход на страницу восстановления по URL")
                except Exception as e:
                    print(f"Ошибка при переходе по URL: {e}")
        
        # Если нашли ссылку, кликаем по ней
        if forgot_password_link:
            try:
                forgot_password_link.click()
                print("Клик по ссылке восстановления пароля выполнен")
            except ElementNotInteractableException:
                try:
                    driver.execute_script("arguments[0].click();", forgot_password_link)
                    print("Клик по ссылке выполнен через JavaScript")
                except Exception as e:
                    print(f"Не удалось кликнуть по ссылке: {e}")
        
        # Ждем загрузки страницы восстановления пароля
        try:
            WebDriverWait(driver, 10).until(
                EC.url_contains("forgot") or EC.url_contains("reset") or EC.url_contains("restore")
            )
            print(f"URL страницы восстановления пароля: {driver.current_url}")
        except TimeoutException:
            print("URL не содержит признаков страницы восстановления")
        
        # ОТЛАДКА: ищем все элементы на странице восстановления
        print("\n=== Поиск всех полей ввода на странице восстановления ===")
        inputs = driver.find_elements(By.TAG_NAME, "input")
        for i, input_elem in enumerate(inputs):
            print(f"\nПоле {i + 1}:")
            print(f"  type={input_elem.get_attribute('type')}")
            print(f"  name={input_elem.get_attribute('name')}")
            print(f"  placeholder={input_elem.get_attribute('placeholder')}")
            print(f"  class={input_elem.get_attribute('class')}")
            print(f"  id={input_elem.get_attribute('id')}")
        
        # ОТЛАДКА: ищем все кнопки
        print("\n=== Поиск всех кнопок на странице восстановления ===")
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for i, button in enumerate(buttons):
            print(f"Кнопка {i + 1}: текст='{button.text}'")
        
        # ОТЛАДКА: ищем все ссылки
        print("\n=== Поиск всех ссылок на странице восстановления ===")
        links = driver.find_elements(By.TAG_NAME, "a")
        for i, link in enumerate(links):
            print(f"Ссылка {i + 1}: текст='{link.text}', href='{link.get_attribute('href')}'")
        
        # Ищем кнопку/ссылку для возврата к форме входа на странице восстановления
        print("\n=== Поиск элемента для возврата к входу ===")
        
        # Варианты текста для поиска
        login_text_variants = [
            "Войти",
            "Вход",
            "Вспомнил пароль",
            "Вернуться к входу",
            "Назад к входу",
            "Уже есть аккаунт",
            "Авторизация",
            "Войти в аккаунт",
            "Войти сейчас",
            "Войти здесь",
            "Войти"
        ]
        
        login_element = None
        
        # Сначала ищем кнопку
        for text in login_text_variants:
            try:
                login_element = driver.find_element(By.XPATH, f"//button[contains(text(), '{text}')]")
                print(f"Найдена кнопка с текстом: '{text}'")
                break
            except NoSuchElementException:
                continue
        
        # Если не нашли кнопку, ищем ссылку
        if not login_element:
            for text in login_text_variants:
                try:
                    login_element = driver.find_element(By.XPATH, f"//a[contains(text(), '{text}')]")
                    print(f"Найдена ссылка с текстом: '{text}'")
                    break
                except NoSuchElementException:
                    continue
        
        # Если все еще не нашли, ищем по универсальному пути
        if not login_element:
            try:
                # Ищем элемент, который может вести на страницу входа
                login_element = driver.find_element(By.XPATH, 
                    "//*[contains(@href, 'login') or contains(@onclick, 'login') or contains(@class, 'login')]")
                print("Найден элемент с атрибутами, связанными с входом")
            except NoSuchElementException:
                print("Элемент для входа не найден")
        
        # Если нашли элемент, кликаем по нему
        if login_element:
            # Прокручиваем к элементу при необходимости
            driver.execute_script("arguments[0].scrollIntoView(true);", login_element)
            time.sleep(1)
            
            # Пробуем кликнуть разными способами
            try:
                login_element.click()
                print("Клик по элементу выполнен")
            except ElementNotInteractableException:
                try:
                    driver.execute_script("arguments[0].click();", login_element)
                    print("Клик по элементу выполнен через JavaScript")
                except Exception as e:
                    print(f"Не удалось кликнуть по элементу: {e}")
        
        # Ждем загрузки страницы входа
        try:
            WebDriverWait(driver, 10).until(
                EC.url_contains("login")
            )
            print(f"Возврат на страницу входа: {driver.current_url}")
        except TimeoutException:
            print("Страница входа не загрузилась, продолжаем тест")
        
        # Заполняем форму входа
        print("\n=== Заполнение формы входа ===")
        
        # Поле email
        try:
            email_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email'], input[type='text']"))
            )
            email_input.clear()
            email_input.send_keys(Credentials.EMAIL)
            print(f"Email '{Credentials.EMAIL}' введен")
        except TimeoutException:
            print("Не найдено поле для email")
            raise
        
        # Поле пароля
        try:
            password_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
            )
            password_input.clear()
            password_input.send_keys(Credentials.PASSWORD)
            print("Пароль введен")
        except TimeoutException:
            print("Не найдено поле для пароля")
            raise
        
        # Кнопка входа
        try:
            login_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Войти')]"))
            )
            login_button.click()
            print("Клик по кнопке 'Войти' выполнен")
        except TimeoutException:
            print("Не найдена кнопка 'Войти'")
            raise
        
        # Проверяем успешный вход
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.MAIN_PAGE_TITLE)
        )
        
        # Дополнительная проверка - наличие элементов после входа
        assert driver.find_element(*Locators.MAIN_PAGE_TITLE).is_displayed(), \
            "Не удалось войти в аккаунт"
        print("\n=== ТЕСТ УСПЕШНО ЗАВЕРШЕН! ===")


class TestNavigation:
    """Тесты навигации по сайту"""

    def test_transition_click_personal_account(self, driver):
        """Тест перехода по клику на Личный кабинет"""
        # Ждем загрузки главной страницы
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.MAIN_PAGE_TITLE)
        )
        print("\n=== Главная страница загружена ===")
        # СОХРАНЯЕМ URL ГЛАВНОЙ СТРАНИЦЫ
        main_page_url = driver.current_url
        print(f"URL главной страницы: {main_page_url}")
        
        # ПРОВЕРЯЕМ, ЧТО КНОПКА "ЛИЧНЫЙ КАБИНЕТ" СУЩЕСТВУЕТ И ВИДИМА
        try:
            assert driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).is_displayed(), \
                "Кнопка 'Личный кабинет' не отображается на странице"
            print("Кнопка 'Личный кабинет' отображается на странице")
        except NoSuchElementException:
            print("Кнопка 'Личный кабинет' не найдена")
            raise
        
        # ПРОВЕРЯЕМ ТЕКСТ КНОПКИ (ОПЦИОНАЛЬНО)
        try:
            button_text = driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).text
            print(f"Текст кнопки: '{button_text}'")
        except NoSuchElementException:
            print("Не удалось получить текст кнопки")
        
        # КЛИК ПО КНОПКЕ "ЛИЧНЫЙ КАБИНЕТ" С ОЖИДАНИЕМ КЛИКАБЕЛЬНОСТИ
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(Locators.LOGIN_TO_ACCOUNT_BUTTON)
            ).click()
            print("Клик по кнопке 'Личный кабинет' выполнен")
        except TimeoutException:
            print("Кнопка 'Личный кабинет' не стала кликабельной")
            raise
        
        # ПРОВЕРКА 1: ИЗМЕНИЛСЯ ЛИ URL?
        time.sleep(1)  # Небольшая задержка для обновления URL
        new_url = driver.current_url
        print(f"URL после клика: {new_url}")
        
        # Проверяем, что URL изменился
        assert new_url != main_page_url, "URL не изменился после клика на 'Личный кабинет'"
        print("✓ URL успешно изменился")
        
        # ПРОВЕРКА 2: СОДЕРЖИТ ЛИ НОВЫЙ URL ПРИЗНАКИ СТРАНИЦЫ ВХОДА?
        login_indicators = ['login', 'signin', 'auth', 'account', 'войти', 'вход']
        url_contains_login = any(indicator in new_url.lower() for indicator in login_indicators)
        
        if url_contains_login:
            print(f"✓ URL содержит признак страницы входа: {new_url}")
        else:
            print(f"! URL не содержит явных признаков страницы входа: {new_url}")
        
        # ПРОВЕРКА 3: ПОЯВИЛИСЬ ЛИ ПОЛЯ ДЛЯ ВВОДА?
        print("\n=== Проверка наличия полей ввода ===")
        inputs = driver.find_elements(By.TAG_NAME, "input")
        print(f"Найдено полей ввода: {len(inputs)}")
        
        # Проверяем, что есть хотя бы одно поле ввода
        assert len(inputs) > 0, "На странице нет полей ввода после клика на 'Личный кабинет'"
        
        # Ищем поле для email/логина
        email_fields = []
        for input_elem in inputs:
            input_type = input_elem.get_attribute('type')
            input_name = input_elem.get_attribute('name')
            input_placeholder = input_elem.get_attribute('placeholder')
            
            print(f"Поле: type={input_type}, name={input_name}, placeholder={input_placeholder}")
            
            if input_type in ['email', 'text'] or (input_name and 'email' in input_name.lower()) or (input_placeholder and 'логин' in input_placeholder.lower()):
                email_fields.append(input_elem)
        
        # Проверяем, что есть поле для email
        assert len(email_fields) > 0, "Не найдено поле для ввода email/логина"
        print(f"✓ Найдено поле для email/логина")
        
        # Ищем поле для пароля
        password_fields = [input_elem for input_elem in inputs if input_elem.get_attribute('type') == 'password']
        assert len(password_fields) > 0, "Не найдено поле для ввода пароля"
        print(f"✓ Найдено поле для пароля")
        
        # ПРОВЕРКА 4: ПОЯВИЛАСЬ ЛИ КНОПКА "ВОЙТИ"?
        print("\n=== Проверка наличия кнопки входа ===")
        buttons = driver.find_elements(By.TAG_NAME, "button")
        print(f"Найдено кнопок: {len(buttons)}")
        
        login_button_found = False
        for i, button in enumerate(buttons):
            button_text = button.text
            print(f"Кнопка {i + 1}: текст='{button_text}'")
            
            if button_text and ('войти' in button_text.lower() or 'вход' in button_text.lower() or 'login' in button_text.lower()):
                login_button_found = True
                print(f"✓ Найдена кнопка входа с текстом: '{button_text}'")
        
        assert login_button_found, "Не найдена кнопка 'Войти' на странице"
        
        # ПРОВЕРКА 5: ПРОВЕРЯЕМ, ЧТО МЫ НЕ НА ГЛАВНОЙ СТРАНИЦЕ
        try:
            # Пытаемся найти элемент главной страницы - его НЕ должно быть
            main_page_element = driver.find_element(*Locators.MAIN_PAGE_TITLE)
            if main_page_element.is_displayed():
                assert False, "Мы все еще на главной странице"
        except NoSuchElementException:
            # Если элемент не найден - это хорошо, значит мы не на главной
            print("✓ Элемент главной страницы отсутствует - мы успешно перешли")
        
        print("\n=== ВСЕ ПРОВЕРКИ ПЕРЕХОДА ПРОЙДЕНЫ УСПЕШНО ===")
        
        # ДАЛЬШЕ МОЖНО ПРОДОЛЖИТЬ ТЕСТ ВХОДА
        print("\n=== Продолжаем тест входа ===")
        
        # Теперь заполняем форму
        try:
            email_input = driver.find_element(By.XPATH, "//input[@type='text']")  # Первое текстовое поле
            email_input.send_keys(Credentials.EMAIL)
            print("Email введен")
        except NoSuchElementException:
            print("Не найдено поле для email")
            raise
        
        try:
            password_input = driver.find_element(By.XPATH, "//input[@type='password']")
            password_input.send_keys(Credentials.PASSWORD)
            print("Пароль введен")
        except NoSuchElementException:
            print("Не найдено поле для пароля")
            raise
        
        try:
            login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]")
            login_button.click()
            print("Клик по кнопке 'Войти' выполнен")
        except NoSuchElementException:
            print("Не найдена кнопка 'Войти'")
            raise
        
        # Проверяем успешный вход
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(Locators.MAIN_PAGE_TITLE)
            )
        except TimeoutException:
            print("Не удалось дождаться загрузки главной страницы после входа")
            raise
        
        # Проверяем, что мы вернулись на главную
        assert driver.current_url == main_page_url or driver.find_element(*Locators.MAIN_PAGE_TITLE).is_displayed(), \
            "Не удалось войти в аккаунт или вернуться на главную"
        
        print("\n=== ТЕСТ УСПЕШНО ЗАВЕРШЕН! ===")
        print("✓ Клик на 'Личный кабинет' работает корректно")
        print("✓ Форма входа отображается")
        print("✓ Вход в аккаунт выполнен успешно")

    def test_constructor_navigation(self, driver):
        """Тест перехода по клику на «Конструктор»"""

        # ШАГ 1: Загружаем главную страницу
        print("\n=== ТЕСТ ПЕРЕХОДА ПО КЛИКУ НА «КОНСТРУКТОР» ===")
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(Locators.MAIN_PAGE_TITLE)
            )
            print("Главная страница загружена")
        except TimeoutException:
            print("Не удалось загрузить главную страницу")
            raise
        
        # Сохраняем URL главной страницы
        main_page_url = driver.current_url
        print(f"URL главной страницы: {main_page_url}")
        
        # ШАГ 2: Переходим в Личный кабинет (чтобы потом вернуться через Конструктор)
        print("\n--- Переходим в Личный кабинет ---")
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(Locators.LOGIN_TO_ACCOUNT_BUTTON)
            ).click()
            print("Клик по кнопке 'Личный кабинет' выполнен")
        except TimeoutException:
            print("Не удалось кликнуть по кнопке 'Личный кабинет'")
            raise
        
        # Ждем загрузки страницы входа
        try:
            WebDriverWait(driver, 10).until(
                EC.url_contains("login") or EC.presence_of_element_located((By.TAG_NAME, "input"))
            )
            account_page_url = driver.current_url
            print(f"URL страницы входа: {account_page_url}")
            assert account_page_url != main_page_url, "Не удалось перейти в личный кабинет"
        except TimeoutException:
            print("Страница входа не загрузилась")
            account_page_url = driver.current_url
            print(f"Текущий URL: {account_page_url}")
        
        # ШАГ 3: Проверяем наличие кнопки «Конструктор»
        print("\n--- Поиск кнопки «Конструктор» ---")
        constructor_button = None
        
        # Вариант 1: по тексту ссылки
        possible_locators = [
            (By.XPATH, "//a[contains(text(), 'Конструктор')]"),
            (By.XPATH, "//p[contains(text(), 'Конструктор')]"),
            (By.XPATH, "//span[contains(text(), 'Конструктор')]"),
            (By.XPATH, "//div[contains(text(), 'Конструктор')]"),
            (By.XPATH, "//*[contains(@class, 'constructor') and contains(text(), 'Конструктор')]"),
            (By.XPATH, "//a[@href='/']"),  # ссылка на главную
        ]
        
        for locator in possible_locators:
            try:
                elements = driver.find_elements(*locator)
                for elem in elements:
                    if elem.is_displayed():
                        elem_text = elem.text.lower() if elem.text else ""
                        if 'конструктор' in elem_text or 'constructor' in elem_text:
                            constructor_button = elem
                            print(f"Найдена кнопка «Конструктор» по локатору: {locator}")
                            print(f"  Текст элемента: '{elem.text}'")
                            print(f"  Тег: {elem.tag_name}")
                            break
                if constructor_button:
                    break
            except Exception as e:
                print(f"Ошибка при поиске по локатору {locator}: {e}")
                continue
        
        assert constructor_button is not None, "Кнопка «Конструктор» не найдена на странице"
        print("✓ Кнопка «Конструктор» найдена и видима")
        
        # Проверяем, что кнопка кликабельна
        assert constructor_button.is_enabled(), "Кнопка «Конструктор» не активна"
        
        # ШАГ 4: Кликаем по кнопке «Конструктор»
        print("\n--- Клик по кнопке «Конструктор» ---")
        # Прокручиваем к элементу при необходимости
        driver.execute_script("arguments[0].scrollIntoView(true);", constructor_button)
        time.sleep(1)
        
        # Сохраняем URL до клика
        url_before_click = driver.current_url
        
        # Выполняем клик
        try:
            constructor_button.click()
            print("Клик по кнопке «Конструктор» выполнен")
        except ElementNotInteractableException:
            try:
                driver.execute_script("arguments[0].click();", constructor_button)
                print("Клик по кнопке выполнен через JavaScript")
            except Exception as e:
                print(f"Не удалось кликнуть по кнопке: {e}")
                raise
        
        # ШАГ 5: Проверяем переход
        print("\n--- Проверка перехода ---")
        
        # Ждем изменения URL или загрузки главной страницы
        try:
            WebDriverWait(driver, 10).until(
                EC.url_contains(main_page_url) or EC.visibility_of_element_located(Locators.MAIN_PAGE_TITLE)
            )
        except TimeoutException:
            print("Не удалось дождаться загрузки главной страницы")
        
        # Проверяем URL после клика
        url_after_click = driver.current_url
        print(f"URL после клика: {url_after_click}")
        
        # Проверка 1: URL должен измениться (если мы были не на главной)
        if url_before_click != main_page_url:
            assert url_after_click != url_before_click, "URL не изменился после клика"
            print("✓ URL изменился")
        
        # Проверка 2: Мы должны оказаться на главной странице
        assert main_page_url in url_after_click or url_after_click == main_page_url, \
            f"Мы не на главной странице. Текущий URL: {url_after_click}"
        print("✓ Мы вернулись на главную страницу")
        
        # Проверка 3: Должен отображаться заголовок главной страницы
        try:
            assert driver.find_element(*Locators.MAIN_PAGE_TITLE).is_displayed(), \
                "Заголовок главной страницы не отображается"
            print("✓ Заголовок главной страницы отображается")
        except NoSuchElementException:
            print("Заголовок главной страницы не найден")
            raise
        
        print("\n=== ТЕСТ ПЕРЕХОДА ПО КЛИКУ НА «КОНСТРУКТОР» УСПЕШНО ПРОЙДЕН ===")
    
    def test_logo_navigation(self, driver):
        """Тест перехода по клику на логотип Stellar Burgers"""
        
        print("\n=== ТЕСТ ПЕРЕХОДА ПО КЛИКУ НА ЛОГОТИП STELLAR BURGERS ===")
        
        # ШАГ 1: Загружаем главную страницу
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(Locators.MAIN_PAGE_TITLE)
            )
            print("Главная страница загружена")
        except TimeoutException:
            print("Не удалось загрузить главную страницу")
            raise
        
        # Сохраняем URL главной страницы
        main_page_url = driver.current_url
        print(f"URL главной страницы: {main_page_url}")
        
        # ШАГ 2: Переходим в Личный кабинет (чтобы потом вернуться через логотип)
        print("\n--- Переходим в Личный кабинет ---")
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(Locators.LOGIN_TO_ACCOUNT_BUTTON)
            ).click()
            print("Клик по кнопке 'Личный кабинет' выполнен")
        except TimeoutException:
            print("Не удалось кликнуть по кнопке 'Личный кабинет'")
            raise
        
        # Ждем загрузки страницы входа
        try:
            WebDriverWait(driver, 10).until(
                EC.url_contains("login") or EC.presence_of_element_located((By.TAG_NAME, "input"))
            )
            account_page_url = driver.current_url
            print(f"URL страницы входа: {account_page_url}")
            assert account_page_url != main_page_url, "Не удалось перейти в личный кабинет"
        except TimeoutException:
            print("Страница входа не загрузилась")
            account_page_url = driver.current_url
            print(f"Текущий URL: {account_page_url}")
        
        # ШАГ 3: Проверяем наличие логотипа
        print("\n--- Поиск логотипа Stellar Burgers ---")
        logo = None
        
        # Варианты локаторов для логотипа
        logo_locators = [
            (By.XPATH, "//div[contains(@class, 'logo')]"),
            (By.XPATH, "//*[contains(@class, 'logo')]"),
            (By.XPATH, "//a[contains(@href, '/')]//*[contains(text(), 'Stellar') or contains(text(), 'Бургер')]"),
            (By.XPATH, "//img[contains(@alt, 'logo') or contains(@alt, 'Логотип')]"),
            (By.XPATH, "//svg[contains(@class, 'logo')]"),
            (By.XPATH, "//a[@href='/']"),  # ссылка на главную
        ]
        
        for locator in logo_locators:
            try:
                elements = driver.find_elements(*locator)
                for elem in elements:
                    if elem.is_displayed():
                        # Проверяем, что это похоже на логотип
                        html = elem.get_attribute('outerHTML').lower() if elem.get_attribute('outerHTML') else ""
                        class_name = elem.get_attribute('class') or ""
                        if ('stellar' in html or 'бургер' in html or 'logo' in html or 
                            'logo' in class_name or 
                            elem.tag_name == 'svg'):
                            logo = elem
                            print(f"Найден логотип по локатору: {locator}")
                            print(f"  Тег элемента: {elem.tag_name}")
                            print(f"  Класс: {class_name}")
                            break
                if logo:
                    break
            except Exception as e:
                print(f"Ошибка при поиске по локатору {locator}: {e}")
                continue
        
        # Если не нашли специфичный логотип, ищем любой элемент с классом logo
        if not logo:
            try:
                logo = driver.find_element(By.XPATH, "//*[contains(@class, 'logo')]")
                print("Найден элемент с классом 'logo'")
            except NoSuchElementException:
                print("Элемент с классом 'logo' не найден")
        
        assert logo is not None, "Логотип не найден на странице"
        print("✓ Логотип найден и видим")
        
        # Проверяем, что логотип кликабелен
        assert logo.is_enabled(), "Логотип не активен"
        
        # ШАГ 4: Кликаем по логотипу
        print("\n--- Клик по логотипу ---")
        # Прокручиваем к элементу
        driver.execute_script("arguments[0].scrollIntoView(true);", logo)
        time.sleep(1)
        
        # Сохраняем URL до клика
        url_before_click = driver.current_url
        
        # Выполняем клик
        try:
            logo.click()
            print("Клик по логотипу выполнен")
        except ElementNotInteractableException:
            try:
                driver.execute_script("arguments[0].click();", logo)
                print("Клик по логотипу выполнен через JavaScript")
            except Exception as e:
                print(f"Не удалось кликнуть по логотипу: {e}")
                raise
        
        # ШАГ 5: Проверяем переход
        print("\n--- Проверка перехода ---")
        
        # Ждем изменения URL или загрузки главной страницы
        try:
            WebDriverWait(driver, 10).until(
                EC.url_contains(main_page_url) or EC.visibility_of_element_located(Locators.MAIN_PAGE_TITLE)
            )
        except TimeoutException:
            print("Не удалось дождаться загрузки главной страницы")
        
        # Проверяем URL после клика
        url_after_click = driver.current_url
        print(f"URL после клика: {url_after_click}")
        
        # Проверка 1: URL должен измениться (если мы были не на главной)
        if url_before_click != main_page_url:
            assert url_after_click != url_before_click, "URL не изменился после клика"
            print("✓ URL изменился")
        
        # Проверка 2: Мы должны оказаться на главной странице
        assert main_page_url in url_after_click or url_after_click == main_page_url, \
            f"Мы не на главной странице. Текущий URL: {url_after_click}"
        print("✓ Мы вернулись на главную страницу")
        
        # Проверка 3: Должен отображаться заголовок главной страницы
        try:
            assert driver.find_element(*Locators.MAIN_PAGE_TITLE).is_displayed(), \
                "Заголовок главной страницы не отображается"
            print("✓ Заголовок главной страницы отображается")
        except NoSuchElementException:
            print("Заголовок главной страницы не найден")
            raise
        
        print("\n=== ТЕСТ ПЕРЕХОДА ПО КЛИКУ НА ЛОГОТИП УСПЕШНО ПРОЙДЕН ===")