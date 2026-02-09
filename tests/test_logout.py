from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from data import TestData 
from locators import Locators

cdef test_success_logout(self, driver):
    try:
        email = "maria_egorenkova_38_546@yandex.ru"
        password = "123456"
        
        print("1. Начинаем процесс входа...")
        
        # 1. Клик по кнопке входа в аккаунт
        login_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.LOGIN_TO_ACCOUNT_BUTTON)
        )
        print("2. Кнопка входа найдена, кликаем...")
        login_btn.click()
        
        # 2. Ждем появления формы
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.NAME_INPUT)
        )
        print("3. Форма логина найдена")
        
        # 3. Вводим email
        email_field = driver.find_element(*Locators.NAME_INPUT)
        print(f"4. Ввод email: {email}")
        email_field.send_keys(email)
        
        # 4. Вводим пароль
        password_field = driver.find_element(*Locators.PASSWORD_INPUT)
        print(f"5. Ввод пароля: {'*' * len(password)}")
        password_field.send_keys(password)
        
        # 5. Делаем скриншот перед кликом
        driver.save_screenshot("before_login.png")
        
        # 6. Кликаем кнопку входа
        login_submit_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.LOGIN_FORM_BUTTON)
        )
        print("6. Кликаем кнопку 'Войти'")
        login_submit_btn.click()
        
        # 7. Проверяем успешность входа
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(Locators.MAIN_PAGE_TITLE)
            )
            print("7. Вход успешен!")
        except TimeoutException:
            print("7. Ошибка: не удалось войти")
            # Проверяем, есть ли сообщение об ошибке
            driver.save_screenshot("login_failed.png")
            raise
            
    except Exception as e:
        print(f"Критическая ошибка: {e}")
        driver.save_screenshot("critical_error.png")
        raise