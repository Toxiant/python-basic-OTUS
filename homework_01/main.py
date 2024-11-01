import json
from base64 import encode
from logging import NullHandler
from operator import iconcat, index
from re import search

def parse_phonebook(phonebook):
        print('Name: ' + phonebook['name'])
        print('phone number: ' + phonebook['phone_number'])
        print('id: ' + phonebook['id'])
        print(' ')


def load_phonebook():
    '''Get all contacts'''
    with open('phonebook.json', 'r') as file:
            phonebook = json.load(file)
            for i in phonebook:
                parse_phonebook(i)


def add_contact(**kwargs):
    '''Add new contact'''
    with open('phonebook.json') as file:
            contact = json.load(file)
            new_contact = {
                "name": input("Enter name - "),
                "phone_number": input("Enter phone number - "),
                "id": str(len(contact) + 1)
            }
            contact.append(new_contact)
    with open('phonebook.json', "w", encoding="utf-8") as file:
         json.dump(contact, file, indent=4)

# def find_contact(**kwargs):
#     '''Find existing contacts'''
#     print_contact = []
#     null = []
#     kwargs = str(input('Enter data - '))
#     with open("phonebook.json", "r", encoding="utf-8") as file:
#         contact = json.load(file)
#         for i in contact:
#             if i["name"].title() == kwargs.title():
#                 print_contact.append(i)
#             elif i["phone_number"] == kwargs:
#                 print_contact.append(i)
#             elif i["id"] == kwargs:
#                 print_contact.append(i)
#     if print_contact == null:
#         print("The contact isn't exist")
#     else:
#         for i in print_contact:
#             parse_phonebook(i)

def find_contact(**kwargs):
    '''Find existing contacts'''
    print_contact = []
    null = []
    kwargs = str(input('Enter data - '))
    with open("phonebook.json", "r", encoding="utf-8") as file:
        contact = json.load(file)
        for i in contact:
            if i["name"].title() == kwargs.title():
                print_contact.append(i)
            elif i["phone_number"] == kwargs:
                print_contact.append(i)
            elif i["id"] == kwargs:
                print_contact.append(i)
    if print_contact == null:
        print("The contact isn't exist")
    else:
        return print_contact

def delete_contact(**kwargs):
    '''Delete existing contacts'''
    kwargs = str(input('Enter data - '))
    with open("phonebook.json", "r", encoding="utf-8") as file:
        contact = json.load(file)
        print(contact)
        for i in contact:
            if i["name"].title() == kwargs.title():
                rm = contact.index(i)
                contact.pop(rm)
            elif i["phone_number"] == kwargs:
                rm = contact.index(i)
                contact.pop(rm)
            elif i["id"] == kwargs:
                rm = contact.index(i)
                contact.pop(rm)
        else:
            print("The contact isn't exist")
    for a in contact:
        a["id"] = str(contact.index(a) +1 )
    with open('phonebook.json', "w", encoding="utf-8") as file:
        json.dump(contact, file, indent=4)

def update_contact(**kwargs):
    test = find_contact() # -переменной присваиваем найденный контакт (функия возвращает словарь)
    id_update_contact = int(test["id"]) - 1
    parse_phonebook(test)
    with open("phonebook.json", "r", encoding="utf-8") as file:
        edit_contact = json.load(file)
        edit_contact[id_update_contact].update({
            "name": input("Enter name - "),
            "phone_number": input("Enter phone number - ")
        })# -обращаемся к элементу в листе по id
    # -изменяем найденный элемен
    # -данные записываем в файл
    with open('phonebook.json', "w", encoding="utf-8") as file:
        json.dump(edit_contact, file, indent=4)

def menu(option):

    if option == "1":
        load_phonebook()

    if option == "2":
        add_contact()

    if option== "3":
        find_contact()


    if option == "4":
        update_contact()
        print("Данные изменены")

    if option == "5":
        delete_contact()
        print("Контакт удалён")



if __name__ == "__main__":
    while True:
        menu(
            input(
                "Команды: \n "
                "Показать все контакты - 1 \n "
                "Создать контакт - 2 \n "
                "Найти контакт - 3 \n "
                "Изменить контакт - 4 \n"
                "Удалить контакт - 5 \n"
                " Введите команду -"
            )
        )
