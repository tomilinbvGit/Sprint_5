import random


# Создаем генератор эл. почты для теста регистрации
def email_generator():
    unique_email = f'test{random.randint(10000, 100000)}tomilinBV@ya.ru'
    return unique_email


# Создаем генератор пароля для теста регистрации
def password_generator():
    unique_password = f'gerternord{random.randint(10, 9999)}'
    return unique_password
