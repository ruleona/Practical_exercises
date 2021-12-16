"""Приложение для работы с клиентской базой в  sqlite3.
Если файл с базой данных client_database.sqlite3 отсутствует, то программа создает его.
В приложении поддерживается создание новых записей, поиск, чтение  и удаление.
Ссылки на социальные сети в клиентской базе являются уникальными. """

import sqlite3
import re


RED = '\033[1;31m'
WHITE = '\033[00m'
GREEN = '\033[0;92m'


def get_connection():
    connection = sqlite3.connect('client_database.sqlite3')
    connection.execute('''
        CREATE TABLE IF NOT EXISTS clients
        (name TEXT, link TEXT UNIQUE)
    ''')
    return connection


def add():
    try:
        user_input = input('Введите данные через пробел: имя фамилия ссылка_на_соцсети: ')
        client_name = (re.search(r'\w*\s\w* ', user_input)).group().strip()
        client_url = (re.search(r'https?://[\S]+', user_input)).group().strip()
    except (ValueError, AttributeError):
        print(f'{RED}Неверно введены данные. Данные должны содержать имя, фамилию и ссылку на социальную сеть, разделенные знаком пробела{WHITE}')
    else:
        insert_data(connection, client_name, client_url)


def delete():
    user_choice = input(f'Удалить контакт по имени {GREEN}(1){WHITE} / по ссылке? {GREEN}(2){WHITE} ')
    if user_choice == '1':
        name_to_delete = input('Введите имя и/или фамилию контакта для удаления: \n').strip()
        delete_by_name(connection, name_to_delete)
    elif user_choice == '2':
        url_to_delete = input('Введите ссылку на социальную сеть контакта для удаления: \n ').strip()
        delete_by_url(connection, url_to_delete)
    else:
        print(f'{RED}Неверная команда.{WHITE}')


def search():
    param = input('Введите параметр для поиска(имя и/или фамилия): ').strip().capitalize()
    search_data(connection, param)


def read():
    show_data(connection)


def insert_data(connection, name, url):
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO clients VALUES(?, ?)", (name, url))   # Обратить внимание на синтаксис! Профилактика SQL-инъекций
        connection.commit()
        print(f'{GREEN}Данные успешно добавлены.{WHITE}')
    except sqlite3.IntegrityError:
        print(f'{RED}Пользователь с таким url уже есть в базе{WHITE}')


def show_data(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM clients")
    for el in cursor.fetchall():
        print(*el)


def delete_by_name(connection, name):
    cursor = connection.cursor()
    name = '%' + name + '%'
    cursor.execute("SELECT * FROM clients WHERE name LIKE ?", (name, ))
    result = cursor.fetchall()
    if result:
        for count, (user_name, user_link) in enumerate(result, start=1):
            print(f'{count}) {user_name} {user_link}')
        if len(result) == 1:
            link = result[0][1]
            delete_by_url(connection, link)
        else:
            try:
                link = result[int(input('Введите порядковый номер элемента для удаления: ')) - 1][1]
            except ValueError:
                print(f'{RED}Необходимо ввести число{WHITE}')
            except (IndexError, UnboundLocalError):
                print(f'{RED}Нет элемента с таким номером{WHITE}')
            else:
                delete_by_url(connection, link)
    else:
        print(f'{RED}По запросу ничего не найдено.{WHITE}')
        user_choice = input(f'Желаете изменить параметры поиска? Да {GREEN}(1){WHITE} / отмена {GREEN}(2){WHITE}')
        if user_choice == '1':
            delete()
        elif user_choice == '2':
            print(f'{RED}Операция отменена{WHITE}')
        else:
            print(f'{RED}Неизвестная команда.{WHITE}')


def delete_by_url(connection, url):
    user_choice = input(f'Подтвердите действие: подтвердить{GREEN}(1){WHITE} / отмена{GREEN}(2){WHITE} ')
    if user_choice == '1':
        cursor = connection.cursor()
        cursor.execute("DELETE FROM clients WHERE link = ?", (url,))
        connection.commit()
        print(f'{GREEN}Данные успешно удалены.{WHITE}')
    else:
        print(f'{RED}Операция отменена{WHITE}')


def search_data(connection, request):
    request = '%' + request + '%'
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM clients WHERE name LIKE ?", (request, ))
    result = cursor.fetchall()
    if result:
        print('По запросу найдено: ')
        for el in result:
            print(*el)
    else:
        print(f'{RED}По запросу ничего не найдено{WHITE}')


if __name__ == '__main__':
    print('Добро пожаловать в обработчик клиентской базы.')
    actions = {
        '1': add,
        '2': read,
        '3': delete,
        '4': search
    }
    while True:
        connection = get_connection()
        action = input(f'Выберите действие: добавление {GREEN}(1){WHITE} / чтение {GREEN}(2){WHITE} / удаление {GREEN}(3){WHITE} / поиск {GREEN}(4){WHITE} / выход {GREEN}(5){WHITE}: \n').lower().strip()
        if action == '5':
            connection.close()
            print('Спасибо за работу с базой данных. До свидания.')
            break
        elif action in actions:
            actions[action]()
        else:
            print(f'{RED}Неизвестная команда.{WHITE}')
