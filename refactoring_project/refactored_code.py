from typing import List, Optional

class User:
    # Відрефакторено: створено клас User для структурованого зберігання даних
    def __init__(self, first_name: str, last_name: str, age: int, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

def parse_user_data(user_data: str) -> Optional[User]:
    # Відрефакторено: виділено парсинг рядка в окрему функцію з обробкою помилок
    try:
        parts = [part.strip() for part in user_data.split(',')]
        if len(parts) != 4:
            return None
        first_name, last_name, age_str, email = parts
        age = int(age_str)
        return User(first_name, last_name, age, email)
    except Exception:
        return None

def process_user_data(users_data: List[str]) -> List[User]:
    # Відрефакторено: замість обробки рядків напряму, тепер використовуємо клас User
    # Застосована функція парсингу для кожного рядка
    # Фільтруємо користувачів за віком >= 18 років
    processed_users = []
    for user_data in users_data:
        user = parse_user_data(user_data)
        if user and user.age >= 18:
            processed_users.append(user)
    return processed_users