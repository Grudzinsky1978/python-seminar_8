# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи (например, имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# 1. Добавление контакта +
#     ввод данных контакта
#     открыть файл (a)
#     записать данные в файл

# 2. Вывод контактов
#     открыть файл на считывание (r)
#     получить данные из файла
#     распечатать их

# 3. Поиск контактов
#     ввод данных (строки) для поиска
#     открытие файла для чтения (r)
#     считывание данных
#     поиск контакта по данным
#     вывод на экран

# 4. User Interface (UI, меню пользователя) +
#     создание файла
#     вывести на экран меню пользователя
#     запросить действие у пользователя
#     выполнить действие

# pass # Заглушка

def input_name():
    return input("Введите имя: ").title()

def input_surname():
    return input("Введите фамилию: ").title()

def input_patronumic():
    return input("Введите Отчество: ").title()

def input_phone():
    return input("Введите телефон: ")

def input_address():
    return input("Введите адрес: ").title()

def create_contact():
    surname = input_surname()
    name = input_name()
    patronumic = input_patronumic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronumic} {phone}\n{address}\n\n'

def add_contact():
    contact = create_contact()
    with open('phonebook.txt', 'a', encoding="utf-8") as file_a:
        file_a.write(contact)

# def print_contacts():
#     with open('phonebook.txt', 'r', encoding="utf-8") as file_r:
#         print(file_r.read())
#         print("---" * 20)
#         print("Вывод контактов завершён.")

def print_contacts():
    # with open('phonebook.txt', 'r', encoding="utf-8") as file_r:
    #     print(file_r.read())
    #     print("---" * 20)
    #     print("Вывод контактов завершён.")
    
    with open('phonebook.txt', 'r', encoding="utf-8") as file_r:
        list_contacts = file_r.read().rstrip().split("\n\n")
    # print(enumerate(list_contacts))
    # print(list(enumerate(list_contacts, 1)))
    for i, contact in enumerate(list_contacts, 1):
        print(i, contact + "\n")
    print("----------------------------\n")


def search_contact():
    print("Варианты поиска:\n"
        "1 По фамилии\n"
        "2 По имени\n"
        "3 По отчеству\n"
        "4 По телефону\n"
        "5 По адресу\n")
    var = input("Выберете вариант поиска: ")
    while var not in ('1', '2', '3', '4', '5'):
            print("Введите число от 1 до 5")
            var = input("Выберете вариант для поиска: ")
    index_var = int(var) - 1
    search = input("Введите данные для поиска: ")
    with open('phonebook.txt', 'r', encoding="utf-8") as file_r:
        list_contacts = file_r.read().rstrip().split("\n\n")
    for contact_str in list_contacts:
        # print(contact_str)
        contact_lst = contact_str.split()
        # print(contact_lst)
        if search in contact_lst[index_var]:
            print(contact_str + "\n")

def copy_to_file_contact():
    print_contacts()
    result = ''
    command = int(input("Введите номер контакта, который желаете скопировать в новый файл: "))
    with open('phonebook.txt', 'r', encoding="utf-8") as file_r:
        list_contacts = file_r.read().rstrip().split("\n\n")
    if 0 < command <= len(list_contacts):
        with open('phonebook_select.txt', 'a', encoding="utf-8") as file_a:
            for i, contact in enumerate(list_contacts, 1):
                if i == command:
                    result = str(contact)
            file_a.write(result + '\n\n')
            print("--------------------\n"
                  "Контакт " + str(command) + " скопирован в файл phonebook_select.txt\n"
                  "--------------------\n")
    else:
        print("--------------------\n"
              "Нет такого номера!\n"
              "--------------------\n")
    

def interface():
    with open('phonebook.txt', 'a', encoding="utf-8"):
        pass
    command = ''
    while command != '5':
        print("Меню:\n"
            "1 Добавление контакта\n"
            "2 Вывод контактов\n"
            "3 Поиск контакта\n"
            "4 Копирование контакта в другой файл\n"
            "5 Выход\n")
        command = input("Выберете вариант меню: ")
        while command not in ('1', '2', '3', '4', '5'):
            print("Введите число от 1 до 5")
            command = input("Выберете вариант меню: ")
        match command:
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                copy_to_file_contact()
            case '5':
                print("Всего доброго!")


interface()

# Домашнее задание:
# Дополнить справочник возможностью копирования данных из одного файла в другой. Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.