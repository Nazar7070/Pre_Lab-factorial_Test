def process_user_data(users_data):
    # Оригінал: обробка даних користувачів як рядки без використання класів
    processed_users = []
    for user_data in users_data:
        parts = [part.strip() for part in user_data.split(',')]
        if len(parts) != 4:
            continue
        first_name, last_name, age_str, email = parts
        try:
            age = int(age_str)
        except ValueError:
            continue
        if age >= 18:
            # Додаємо користувача як словник
            processed_users.append({
                "first_name": first_name,
                "last_name": last_name,
                "age": age,
                "email": email
            })
    return processed_users