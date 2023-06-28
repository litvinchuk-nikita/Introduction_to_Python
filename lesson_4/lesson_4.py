# Задача 25.
# Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
my_str = 'a a a b c a a d c d d'
final_str = ''
count = {}

for i in my_str.split(' '):
    if i in final_str:
        final_str += f'{i}_{count[i]} '
        count[i] += 1
    else:
        count[i] = 1
        final_str += f'{i} '
print(final_str)

# Решения с семинара:
result = {}
for i in my_str.split():
    if i in result:
        result[i] += 1
        print(f"{i}_{result[i]}", end=" ")
    else:
        result[i] = 0
        print(i, end=" ")


# Задача 27.
# Пользователь вводит текст(строка).
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов.
# Определите, сколько различных слов содержится в этом тексте.
my_str = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"

# Вариант 1.
result = []
for i in my_str.lower().split():
    if i not in result:
        result.append(i.strip())
print(len(result))

# Вариант 2.
result_2 = {i.strip().lower() for i in my_str.split()}
print(len(result_2))


# Решение с семинара:
print(len(set(my_str.lower().split())))


# Задача 29.
# Ваня и Петя поспорили, кто быстрее решит следующую задачу:
# “Задана последовательность неотрицательных целых чисел.
# Требуется определить значение наибольшего элемента последовательности,
# которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”.
# Однако 2 друга оказались не такими смышлеными.
# Никто из ребят не смог до конца сделать это задание.
# Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор.
# За помощью товарищи обратились к Вам, студентам.

# Ваня: 2 ошибки                  # Петя: 3 ошибки
# n = int(input())                # n = int(input())
# max_number = 1000               # max_number = -1
# while n != 0:                   # while n < 0:
#     n = int(input())                # n = int(input())
#     if max_number > n:              # if max_number < n:
#         max_number = n                    # n = max_number
# print(max_number)               # print(n)

# Решение.
n = int(input())
max_number = -1
while n != 0:
    n = int(input())
    if max_number < n:
        max_number = n
print(max_number)
