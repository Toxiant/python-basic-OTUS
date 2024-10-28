import json
from base64 import encode
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
                # print('Name: ' + i['name'])
                # print('phone number: ' + i['phone_number'])
                # print('id: ' + i['id'])
                # print('/n')


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
        for i in print_contact:
            parse_phonebook(i)

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
    with open('phonebook.json', "w", encoding="utf-8") as file:
         json.dump(contact, file, indent=4)

