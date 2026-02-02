import random
import string


class TestData:
    """Генераторы тестовых данных"""
    
    @staticmethod
    def generate_email(cohort=38):
        """Генерация email в формате имя_фамилия_номер_когорты_3цифры@домен
        
        Args:
            cohort: номер когорты 38
        """
        name = "maria"
        surname = "egorenkova"
        random_digits = ''.join(random.choices(string.digits, k=3))
        return f"{name}_{surname}_{cohort}{random_digits}@yandex.ru"
    
    @staticmethod
    def generate_password(length=6):
        """Генерация пароля
        
        Args:
            length: длина пароля (минимум 6 символов)
        """
        if length < 6:
            length = 6
        # Используем буквы и цифры для пароля
        characters = string.ascii_letters + string.digits
        return ''.join(random.choices(characters, k=length))
    
    @staticmethod
    def generate_name():
        """Генерация имени"""
        names = ["Алексей", "Мария", "Иван", "Ольга", "Дмитрий", "Елена", "Сергей", "Анна"]
        return random.choice(names)
    
    @staticmethod
    def get_valid_user():
        """Получение валидных данных пользователя"""
        return {
            "name": TestData.generate_name(),
            "email": TestData.generate_email(),
            "password": TestData.generate_password(8)
        }
    
    @staticmethod
    def get_short_password_user():
        """Получение данных пользователя с коротким паролем"""
        return {
            "name": TestData.generate_name(),
            "email": TestData.generate_email(),
            "password": TestData.generate_password(5)  # Короткий пароль
        }