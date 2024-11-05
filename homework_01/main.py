import json


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
        print_contact = "Contact doesn't exist"

    return print_contact


def delete_contact(**kwargs):
    '''Delete existing contacts'''
    test = find_contact()
    if test == "Contact doesn't exist":
        print(test)
    else:
        if len(test) == 1:
#   kwargs = str(input('Enter data - '))
            with open("phonebook.json", "r", encoding="utf-8") as file:
                contact = json.load(file)
                for i in test:
                    id_delete_contact = int(i["id"]) - 1
                contact.pop(id_delete_contact)
        else:
            for i in test: parse_phonebook(i)
            id_delete_contact = int(input("Find several contacts, choose ID contact for delete - ")) - 1
            with open("phonebook.json", "r", encoding="utf-8") as file:
                contact = json.load(file)
            contact.pop(id_delete_contact)
        for a in contact:
            a["id"] = str(contact.index(a) +1 )
        with open('phonebook.json', "w", encoding="utf-8") as file:
            json.dump(contact, file, indent=4)


def update_contact(**kwargs):
    '''Edit existing contacts'''
    test = find_contact()
    if test == "Contact doesn't exist":
        print(test)
    else:
        if len(test) == 1:
            id_update_contact = int(test["id"]) - 1
            parse_phonebook(test)
            with open("phonebook.json", "r", encoding="utf-8") as file:
                edit_contact = json.load(file)
                edit_contact[id_update_contact].update({
                    "name": input("Enter name - "),
                    "phone_number": input("Enter phone number - ")
                })
            with open('phonebook.json', "w", encoding="utf-8") as file:
                json.dump(edit_contact, file, indent=4)
        if len(test) > 1:
            for i in test: parse_phonebook(i)
            id_update_contact = int(input("Find several contacts, choose ID contact for edit - ")) - 1
            with open("phonebook.json", "r", encoding="utf-8") as file:
                edit_contact = json.load(file)
                edit_contact[id_update_contact].update({
                    "name": input("Enter name - "),
                    "phone_number": input("Enter phone number - ")
                })
            with open('phonebook.json', "w", encoding="utf-8") as file:
                json.dump(edit_contact, file, indent=4)

def start(command):

    if command == "1":
        load_phonebook()

    if command == "2":
        add_contact()

    if command == "3":
        test = find_contact()
        if test == "Contact doesn't exist":
            print(test + "\n")
        else:
            for i in test:
                parse_phonebook(i)

    if command == "4":
        update_contact()
        print("Edited successfully")

    if command == "5":
        delete_contact()
        print("Deleted successfully")



if __name__ == "__main__":
    while True:
        start(
            input(
                "Contacts: \n "
                "Show all contacts - 1 \n "
                "Create contact - 2 \n "
                "Find contact - 3 \n "
                "Edit contact - 4 \n"
                "Delete contact - 5 \n"
                "EEnter option number - "
            )
        )
