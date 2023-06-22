# Задача 17.
# Дан список чисел.
# Определите, сколько в нем встречается различных чисел.
# Вариант 1.
my_list = [1, 1, 2, 0, -1, 3, 4, 4]
print(len(set(my_list)))

# Вариант 2.
final_list = []
for i in my_list:
    if i not in final_list:
        final_list.append(i)
print(len(final_list))


# Задача 19.
# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо, K – положительное число.
my_list = [1, 2, 3, 4, 5]
k = int(input('Введите положительное число: '))

for i in range(k):
    my_list.insert(0, my_list.pop())
    print(my_list)

# Задача 21.
# Напишите программу для печати всех уникальных значений в словаре.
my_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
           {"VII": " S005 "}, {" V ": " S009 "}, {" VIII ": " S007 "}]
final_set = set()
for i in my_list:
    for j in i:
        final_set.add(i[j].strip())
print(final_set)

# Задача 23.
# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером).
my_list = [0, -1, 5, 2, 3, 5, 4, 6]
counter = 0
for i in range(len(my_list)-1):
    if my_list[i] < my_list[i + 1]:
        counter += 1
print(counter)


# Задача 3.
# Создайте список из случайных чисел. Найдите второй максимум.

a = [8, 1, 2, 13, 3, 4, 5, 6, 7, 14, 11]  # Первый максимум == 8, второй == 7
max_1 = 0
max_2 = 0
for num in a:
    if num > max_1:
        max_2 = max_1
        max_1 = num
        continue
    elif num > max_2:
        max_2 = num
print(max_1, max_2)
