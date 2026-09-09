numbers = [0, 1, 0, 12, 3]

non_zero = []
zero_count = 0

for number in numbers:
    if number == 0:
        zero_count += 1
    else:
        non_zero.append(number)

numbers[:] = non_zero + [0] * zero_count

print(numbers)