from random import randrange
# 3адача 30:
# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


def my_func(a, b, c):
    list_1 = []
    for i in range(c):
        list_1.append(a)
        a += b
    return list_1


print(*my_func(7, 2, 5))


# Задача 32:
# Определить индексы элементов массива(списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума).

n = int(input('Введите минимум диапазона: '))
m = int(input('Введите максимум диапазона: '))
list_1 = [randrange(-10, 11) for i in range(20)]
print(list_1)


def my_func_2(min, max, lst):
    result = []
    for i in range(len(lst)):
        if min <= lst[i] <= max:
            result.append(i)
    return result


print(my_func_2(n, m, list_1))
