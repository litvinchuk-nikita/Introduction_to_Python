import random


# Задача 33.
# Хакер Василий получил доступ к классному журналу
# и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.
n = int(input('Введите количество оценок: '))
my_list = [random.randrange(2, 6) for i in range(n)]
print(my_list)
max = max(my_list)
min = min(my_list)
for i in range(len(my_list)):
    if my_list[i] == max:
        my_list[i] = min
print(my_list)


# Задача 35.
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)

def is_prime(a):
    if a < 2:
        return False
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            return False
    else:
        return True


print(is_prime(int(input())))
