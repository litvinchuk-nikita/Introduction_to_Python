from view import input_num, input_name, input_word
from database import write_name, read_phonebook, search_name, edit_name, delete_name
# Задача 49.
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной


# Задача 38:
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных.


def main():
    while True:
        num = input_num()
        if num == 1:
            name = input_name()
            write_name(name)
        elif num == 2:
            read_phonebook()
        elif num == 3:
            word = input_word()
            search_name(word)
        elif num == 4:
            read_phonebook()
            edit_name()
        elif num == 5:
            read_phonebook()
            delete_name()
        elif num == 6:
            break


main()