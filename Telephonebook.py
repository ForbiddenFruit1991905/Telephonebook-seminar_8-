import json
    
# Функция для чтения и загрузки контактов из телефонного справочника
def read_contacts():
    try:
        with open('TelePhoneBook.json', 'r') as file:
            contacts = json.load(file)
        return contacts
    except:
        contacts = {1: {'lastname': 'Lastname_1', 
                    'firstname': 'Firstname_1', 
                    'middlename': 'Middlename_1',
                    'phonenumber': 111111111, 
                    'birthday': '01.01.1900', 
                    'email': 'id_1@yandex.ru' },
                    2: {'lastname': 'Lastname_2', 
                    'firstname': 'Firstname_2', 
                    'middlename': 'Middlename_3',
                    'phonenumber': 333333333,
                    'birthday': '01.01.2000',
                    'email': None},
                    3: {'lastname': None,
                    'firstname': 'Firstname_3',
                    'middlename': None,
                    'phonenumber': 444444444,
                    'birthday': None,
                    'email': 'id_3@yandex.ru'} 
                    }
        return contacts
print("Контакы подгружены")

# Функция для сохранения контактов в файл
def save_contacts(contacts):
    with open('TelePhoneBook.json', 'w', encoding = 'utf-8') as file:
        json.dump(contacts, file)

def save():
    with open ('TelePhoneBook.json','a', encoding='utf-8') as contacts:
        json.dumps(contacts, ensure_ascii = False)
    print("Контак добавлен")
    
# Функция для показа всех контактов телефонного справочника
def show_contacts():
    contacts = read_contacts()
    if len(contacts) == 0:
        print("У вас нет записей контактов в телефонном справочнике.")
    else:
        for contact in contacts:
            print('{}: {}'.format(contact, contacts[contact]))

# Функция поиска контакта в телефонном справочнике
def find_contact():
    contacts = read_contacts()
    id = input("Введите порядковый номер контакта: ")
    try:
        print(contacts[id])
    except:
        print("Такого id не существует")

# Функция для добавления контакта
def add_contact():
    contacts = read_contacts()
    id = input("Введите порядковый номер контакта: ")   # это основной ключ
    if id not in contacts:
        lastname = input("Введите фамилию: ")
        firstname = input("Введите имя: ")
        middlename = input("Введите отчество: ")
        phonenumber = input("Введите номер телефона: ")
        birthday = input("Введите день рождения в формате дд/мм/гггг: ")
        email = input(" Введите email: ")
        contact = {'lastname': lastname, 'firstname': firstname, 'middlename': middlename, 'phonenumber': phonenumber, 'birthday': birthday, 'email': email}
        contacts[id] = contact
        print("Запись о контакте успешно добавлена.")
        print(contacts)
        return
    print("Такое id уже существует")

# Функция для редактирования записи контакта
def edit_contact():
    contacts = read_contacts()
    id = input("Enter id: ")
    if id in contacts:
        new_lastname = input("Введите фамилию: ")
        contacts['lastname'] = new_lastname
        new_firstname = input("Введите имя: ")
        contacts['firstname'] = new_firstname
        new_middlename = input("Введите отчество: ")
        contacts['middlename'] = new_middlename
        new_birthday = input("Введите день рождения в формате дд/мм/гггг: ")
        new_phonenumber = input("Введите номер телефона: ")
        contacts["phonenumber"] = new_phonenumber 
        contacts['birthday'] = new_birthday
        new_email = input(" Введите email: ")
        contacts['email'] = new_email
        contact = {'lastname': new_lastname, 'firstname': new_firstname, 'middlename': new_middlename, 'phonenumber': new_phonenumber, 'birthday': new_birthday, 'email': new_email}
        contacts[id] = contact
        save_contacts(contacts)
        print("Запись контакта скорректирована.")
        return
    print("Такого id контакта нет")

# Функция для удаления записи контакта из телефонного справочника
def delete_contact():
    contacts = read_contacts()
    id = input("Введите ID контакта, которое хотите удалить: ")
    try:
        del contacts[id]
        save_contacts(contacts)
        print("Запись о контакте успешно удалена.")
        return
    except:
        print("Контакт с указанным ID не найден.")

# Интерфейс командного интерпретатора
while True:
    print("Выберите действие:")
    print("1 - Посмотреть контакты")
    print("2 - Найти контакт")
    print("3 - Добавить контакт")
    print("4 - Изменить контакт")
    print("5 - Удалить контакт")
    print("0 - Выйти из приложения")
    
    choice = input("Введите номер действия: ")

    if choice == '1':
        show_contacts()
    elif choice == '2':
        find_contact()
    elif choice == '3':
        add_contact()
    elif choice == '4':
        edit_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '0':
        print("Вы вышли из приложения")
        break
    else:
        print("Неправильный выбор. Попробуйте снова.")