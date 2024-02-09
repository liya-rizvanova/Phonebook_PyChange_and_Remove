from data_create import *


def data_input():
    name = input_name()
    surname = input_surname()
    phone = input_phone()
    address = input_address()

    var = int(input(f'Select format to save data: \n\n'
    f'Version 1: \n'
    f'{name}\n{surname}\n{phone}\n{address}\n\n'
    f'Version 2: \n'
    f'{name};{surname};{phone};{address}\n\n'
    f'Select format: '))
    
    while var !=1 and var !=2:
        print('Wrong entrance!')
        var = int(input('Select format: '))

    if var == 1:
        with open('C:/Users/Администратор/Desktop/Phonebook_PyChange_and_Remove/phonebook/data_first_variant.csv', 'a', encoding='utf-8') as f:   # где a - append
            f.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    elif var == 2:
        with open('C:/Users/Администратор/Desktop/Phonebook_PyChange_and_Remove/phonebook/data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f'{name};{surname};{phone};{address}\n\n')


def read_file():
    var = ''    
    while var != '1' and var != '2':
        print(
            'Select file to show:\n'
            '1 - data_first_variant.csv\n'
            '2 - data_second_variant.csv'
        )
        var = input('Enter the number of the file to show: ')

    if var == '1':   
        with open('C:/Users/Администратор/Desktop/Phonebook_PyChange_and_Remove/phonebook/data_first_variant.csv', 'r', encoding='utf-8') as f:
            return f.read()
    elif var == '2':
        with open('C:/Users/Администратор/Desktop/Phonebook_PyChange_and_Remove/phonebook/data_second_variant.csv', 'r', encoding='utf-8') as f:
            return f.read()


def show_data():
    contacts = read_file()

    if contacts is not None:
        contacts_list = contacts.strip().split('\n\n')
        print()
        
        for idx, contact in enumerate(contacts_list, 1):
            print(f"{idx}. {contact}")
            print()


def read_file_to_change(var):
    if var == '1':
        file_path = 'C:/Users/Администратор/Desktop/Phonebook_PyChange_and_Remove/phonebook/data_first_variant.csv'
        format_string = '{new_name}\n{new_surname}\n{new_phone}\n{new_address}\n\n'
    elif var == '2':
        file_path = 'C:/Users/Администратор/Desktop/Phonebook_PyChange_and_Remove/phonebook/data_second_variant.csv'
        format_string = '{new_name};{new_surname};{new_phone};{new_address}\n\n'
    else:
        print("Invalid file selected.")
        return None

    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read(), file_path, format_string

def change_data():
    var = ''
    while var != '1' and var != '2':
        print(
            'Select file to change data:\n'
            '1 - data_first_variant.csv\n'
            '2 - data_second_variant.csv'
        )
        var = input('Enter the number of the file to show: ')

    contacts, file_path, format_string = read_file_to_change(var)
    if contacts is not None:
        contacts_list = contacts.strip().split('\n\n')
        print()

        for idx, contact in enumerate(contacts_list, 1):
            print(f"{idx}. {contact}")
            
        try:
            contact_index = int(input("Enter the number of the contact to change: ")) - 1
            if 0 <= contact_index < len(contacts_list):
                new_name = input("Enter the new name: ").title()
                new_surname = input("Enter the new surname: ").title()
                new_phone = input("Enter the new phone: ")
                new_address = input("Enter the new address: ").title()

                contacts_list[contact_index] = format_string.format(new_name=new_name, new_surname=new_surname,
                                                                    new_phone=new_phone, new_address=new_address)

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(contacts_list))
                print("Contact updated successfully.")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif contacts is None:
        return


def read_file_to_delete(var):
    if var == '1':
        file_path = 'C:/Users/Администратор/Desktop/Phonebook_PyChange_and_Remove/phonebook/data_first_variant.csv'
        format_string = '{new_name}\n{new_surname}\n{new_phone}\n{new_address}\n\n'
    elif var == '2':
        file_path = 'C:/Users/Администратор/Desktop/Phonebook_PyChange_and_Remove/phonebook/data_second_variant.csv'
        format_string = '{new_name};{new_surname};{new_phone};{new_address}\n\n'
    else:
        print("Invalid file selected.")
        return None

    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read(), file_path, format_string
    
def delete_contact():
    var = ''
    while var != '1' and var != '2':
        print(
            'Select file to delete contact:\n'
            '1 - data_first_variant.csv\n'
            '2 - data_second_variant.csv'
        )
        var = input('Enter the number of the file to delete contact: ')

    contacts, file_path, format_string = read_file_to_delete(var)
    if contacts is not None:
        contacts_list = contacts.strip().split('\n\n')
        print()

        for idx, contact in enumerate(contacts_list, 1):
            print(f"{idx}. {contact}")

        try:
            contact_index = int(input("Enter the number of the contact to delete: ")) - 1
            if 0 <= contact_index < len(contacts_list):
                del contacts_list[contact_index]

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write('\n\n'.join(contacts_list) + '\n\n')
                print("Contact deleted successfully.")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("Invalid file selected.")
