def write_name(name):
    with open('/Users/nikita/Desktop/Документы_Никита/Курс_разработчик_программист/Знакомство_с_языком_Python/lesson_8/phonebook/phonebook.txt', 'a') as f:
        f.write(f'{name}\n')
    print(f'\nЗапись добавлена\n')

def read_phonebook():
    with open('/Users/nikita/Desktop/Документы_Никита/Курс_разработчик_программист/Знакомство_с_языком_Python/lesson_8/phonebook/phonebook.txt', 'r') as f:
        print(f.read())


def search_name(word):
    with open('/Users/nikita/Desktop/Документы_Никита/Курс_разработчик_программист/Знакомство_с_языком_Python/lesson_8/phonebook/phonebook.txt', 'r') as f:
        for line in f:
            line = line.rstrip('\n')
            if word.lower() in line.lower():
                print(f'{line}\n')


def edit_name():
    with open('/Users/nikita/Desktop/Документы_Никита/Курс_разработчик_программист/Знакомство_с_языком_Python/lesson_8/phonebook/phonebook.txt', 'r') as f:
        old_data = f.read()

    old_line = input('Введите строку, которую хотите изменить: ')
    new_line = input('Введите строку, на которую хотите изменить старую: ')
    new_data = old_data.replace(old_line, new_line)

    with open('/Users/nikita/Desktop/Документы_Никита/Курс_разработчик_программист/Знакомство_с_языком_Python/lesson_8/phonebook/phonebook.txt', 'w') as f:
        f.write(new_data)

    print(f'\nИзменения внесены\n')


def delete_name():
    with open('/Users/nikita/Desktop/Документы_Никита/Курс_разработчик_программист/Знакомство_с_языком_Python/lesson_8/phonebook/phonebook.txt', 'r') as f:
        data = f.readlines()
    delet_line = input('Введите строку, которую хотите удалить: ')
    for line in data:
        if line.rstrip() == delet_line:
            data.remove(line)
    with open('/Users/nikita/Desktop/Документы_Никита/Курс_разработчик_программист/Знакомство_с_языком_Python/lesson_8/phonebook/phonebook.txt', 'w') as f:
        f.writelines(data)

    print(f'\nИмя удалено\n')