import random
import string
import time

class TestData:
    def __init__(self):
        self.base_email = "maria_egorenkova_38_546@yandex.ru"
        self.base_password = "123456"
        self.base_name = "Мария"
    
    def generate_random_email(self):
        """Генерация уникального email"""
        timestamp = str(int(time.time()))
        random_str = ''.join(random.choices(string.ascii_lowercase, k=5))
        return f"{self.base_email}_{timestamp}_{random_str}@example.com"
    
    def generate_random_name(self):
        """Генерация уникального имени"""
        timestamp = str(int(time.time()))
        random_str = ''.join(random.choices(string.ascii_lowercase, k=3))
        return f"{self.base_name}_{timestamp}_{random_str}"
    
    def get_unregistered_user(self):
        """Возвращает данные незарегистрированного пользователя"""
        return {
            "email": self.generate_random_email(),
            "password": self.base_password + str(random.randint(100, 999)),
            "name": self.generate_random_name()
        }
    
    def get_valid_user(self):
        """Возвращает данные для тестов (можно использовать для регистрации)"""
        return {
            "email": self.generate_random_email(),
            "password": self.base_password,
            "name": self.generate_random_name()
        }