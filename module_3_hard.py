def calculate_structure_sum(data_structure):
    total_sum = 0

    if isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            total_sum += calculate_structure_sum(item)  # Рекурсивный вызов
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            total_sum += calculate_structure_sum(key)   # Суммируем ключи
            total_sum += calculate_structure_sum(value) # Суммируем значения
    elif isinstance(data_structure, str):
        total_sum += len(data_structure)  # Суммируем длину строки
    elif isinstance(data_structure, (int, float)):
        total_sum += data_structure  # Суммируем число
    return total_sum

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)