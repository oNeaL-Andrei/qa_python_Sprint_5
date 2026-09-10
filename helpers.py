import random 
import string
def generate_random_email(): # Создаём 3 случайные цифры 
    random_digits = ''.join(random.choices(string.digits, k=3)) # содаём уникальный email
    return f"qa_student_19_{random_digits}@yandex.ru"

def generate_random_password(): # создаём пароль из 6 символов
    return "abcd123"