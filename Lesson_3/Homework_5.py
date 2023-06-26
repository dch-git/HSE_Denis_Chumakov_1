import json
import csv
import re


def part_1():

    """
    Найдите информацию об организациях:
        Получите список ИНН из файла «traders.txt»;
        Найдите информацию об организациях с этими ИНН в файле «traders.json»;
        Сохраните информацию об ИНН, ОГРН и адресе организаций из файла «traders.txt» в файл «traders.csv»
    """

    """Получение списка ИНН из файла «traders.txt»"""
    with open("traders.txt", "r") as f:
        inn_list = [i.strip() for i in f]

    """Получение списка организаций-трейдеров из файла «traders.json»"""
    with open("traders.json", "r") as f:
        traders = json.load(f)

    """Создание списка пересекающихся ИНН и организаций-трейдеров"""
    cross = []
    for trader in traders:
        if trader['inn'] in inn_list:
            traders.append(trader)

    """Сохранение списка пересекающихся ИНН и организаций-трейдеров в файл «traders.csv»"""
    with open('traders.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['ИНН', 'ОГРН', 'Адрес'])
        for i in cross:
            writer.writerow((i['inn'], i['ogrn'], i['address']))



import json
def part_2():
    """
    Напишите регулярное выражение для поиска email-адресов в тексте.
    Для этого напишите функцию, которая принимает в качестве аргумента текст в виде строки и возвращает список найденных email-адресов или пустой список, если email-адреса не найдены.
    Используйте дата-сет на 1000 сообщений из Единого федерального реестра сведений о банкротстве (ЕФРСБ) для практики.

    Есть дата-сеты и побольше:
        дата-сет на 10 000 сообщений,
        дата-сет на 100 000 сообщений,
    но если компьютер слабый, ограничьтесь самым маленьким.

    Текст сообщений можно найти по ключу «msg_text».

    Найдите все email-адреса в дата-сете и соберите их в словарь, где ключом будет выступать ИНН опубликовавшего сообщение («publisher_inn»), а в значении будет хранится множество set() с email-адресами.
        Пример:
            {
            “77010127248512”: {“name_surname@yandex.ru”, “name_surname@mail.ru”}

            “77011235421242”: {“name_surname@yandex.ru”, “name_surname@gmail.com”}
            …
            }

    Сохраните собранные данные в файл «emails.json».
    """

def emails_search(string):
    pattern = re.compile(r"\b[0-9a-zA-Z.-_]+@[0-9a-zA-Z.-_]+\.[a-zA-Z]+\b")
    return re.findall(pattern, string)
def Part_2_Start():
    with open('1000_efrsb_messages.json', 'r') as json_register_file:
        dataset = json.load(json_register_file)
    results = {}
    for item in dataset:
        found = emails_search(item['msg_text'])
        if found:
            results[item['publisher_inn']] = set(found)
    emails = {}
    for key, value in results.items():
        emails[key] = list(value)
    with open('emails.json', 'w') as f:
        json.dump(emails, f, indent=4)
