def generate_password(n):
    if n < 3 or n > 20:
        raise ValueError("Число должно быть от 3 до 20.")

    result = ""
    pairs = []

    # Генерация уникальных пар
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if i != j:  # Уникальные пары
                pairs.append((i, j))

    # Проверка кратности
    for pair in pairs:
        pair_sum = sum(pair)
        if n % pair_sum == 0:
            result += f"{pair[0]}{pair[1]}"

    return result

# Ввод числа пользователем
try:
    n = int(input("Введите число от 3 до 20: "))
    password = generate_password(n)
    print(f"Сгенерированный пароль: {password}")
except ValueError as e:
    print(e)
