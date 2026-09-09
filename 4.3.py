import random

# 1. Генерируем случайное количество элементов от 3 до 10
length = random.randint(3, 10)

# Заполняем список случайными числами (например, от 1 до 10)
original_list = [random.randint(1, 10) for _ in range(length)]

# 2. Создаем новый список: 1-й (индекс 0), 3-й (индекс 2) и 2-й с конца (индекс -2)
result_list = [original_list[0], original_list[2], original_list[-2]]

# Вывод результатов для проверки
print(f"{original_list} == {result_list}")