from logger import *

def interface():
    choice = ''
    while choice != '5':
        print(
            'Варианты действия:\n'
            '1 - ввод данных контакта \n'
            '2 - вывести данные на экран \n'
            '3 - изменить данные контакта \n'
            '4 - удалить контакт\n'
            '5 - выход'
            
        )
        print()
        choice = input('Выберите номер действия: ')
        print()
        
        while choice not in ('1', '2', '3', '4', '5'):
            print('Некорректный ввод данных!')
            choice = input('Выберите номер действия: ')
            print()
        match choice:
            case '1':
                data_input()
            case '2':
                show_data()
            case '3':            
                change_data()
            case '4':
                delete_contact()
            case '5':
                print('Всего доброго!')
            