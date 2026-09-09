def even_index_sum(numbers):
    if not numbers:
        return 0
    return sum(numbers[::2]) * numbers[-1]


# Проверка
print(even_index_sum([0, 1, 7, 2, 4, 8]))  # 88
print(even_index_sum([1, 3, 5]))          # 30
print(even_index_sum([6]))                # 36
print(even_index_sum([]))                 # 0