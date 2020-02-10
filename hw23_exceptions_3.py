documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "id", "number": "123456"}
]
# Перечень полок с документами:
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}


def names():
    """
    Выводит имена всех владельцев документов
    """
    for doc in documents:
        try:
            print(doc["name"])
        except KeyError:
            print(f'{doc["type"]},{doc["number"]} занесен в базу без ФИО владельца!')



def people():
    """
    Выводит фамилию и имя по заданному номеру документа
    """
    doc_number = input('Введите номер документа: ')
    counter = 0
    for doc in documents:
        if doc_number in doc.values():
            counter += 1
    if counter == 0:
        print('Такого документа не существует')
    elif counter == 1:
        for doc in documents:
            if doc["number"] == doc_number:
                print(doc["name"])


def doc_list():
    """
    выводит список документов (тип, номер, фамилия, имя)
    """
    for doc in documents:
        try:
            print(doc["type"], doc["number"], doc["name"])
        except KeyError:
            print(f'{doc["type"]},{doc["number"]} занесен в базу без ФИО владельца!')


def shelf():
    """
    выводит номер полки по номеру документа
    """
    doc_number = input('Введите номер документа: ')
    counter = 0
    for doc_shelf in directories:
        if doc_number in directories[doc_shelf]:
            counter += 1
            print('Документ хранится на полке ', doc_shelf)
    if counter == 0:
        print('Такого документа не существует')


def add():
    """
    добавляет новый документ в базу
    """
    new_number = input('Введите номер нового документа ')
    new_type = input('Введите тип нового документа ')
    new_person = input('Введите имя и фамилию ')
    new_shelf = input('Введите номер полки, на которую нужно добавить новый документ ')
    if new_shelf not in directories:
        print('Такой полки не существует, будет создана новая полка')
        directories[new_shelf] = []
    new_doc = {"type": new_type, "number": new_number, "name": new_person}
    documents.append(new_doc)
    directories[new_shelf].append(new_number)


def delete():
    """
    удаляет документ из базы
    """
    counter1 = 0
    counter2 = 0
    del_doc = input('введите номер удаляемого документа ')
    for doc in documents:
        if del_doc in doc.values():
            documents.remove(doc)
            counter1 += 1
    for key, value in directories.items():
        if del_doc in value:
            value.remove(del_doc)
            counter2 += 1
    if counter1 == 0 and counter2 == 0:
        print('Такого документа нет в базе')


def move():
    """
    перемещает документ на другую полку
    """
    counter = 0
    move_doc = input('Введите номер перемещаемого документа ')
    move_shelf = input('Введите номер полки, на которую нужно переместить документ ')
    if move_shelf not in directories:
        print('Такой полки не существует')
    else:
        for value in directories.values():
            if move_doc in value:
                value.remove(move_doc)
                counter += 1
        if counter == 0:
            print('Такого документа не существует')
        else:
            directories[move_shelf].append(move_doc)


def add_shelf():
    """
    добавляет новую полку
    """
    new_shelf_number = input('Введите номер новой полки ')
    if new_shelf_number in directories:
        print('Полка с таким номером уже есть')
    else:
        directories[new_shelf_number] = []


def main():
    while True:
        user_input = input('Введите команду (p,l,s,a,d,m,as,n): ')
        if user_input == 'p':
            people()
        elif user_input == 'l':
            doc_list()
        elif user_input == 'a':
            add()
        elif user_input == 's':
            shelf()
        elif user_input == 'd':
            delete()
        elif user_input == 'm':
            move()
        elif user_input == 'as':
            add_shelf()
        elif user_input == 'n':
            names()
        elif user_input == 'q':
            break


main()
