"""
Задание

Необходимо собрать данные с сайта ЦБ РФ с помощью Python.

В ходе выполнения итогового задания вы самостоятельно:
    • выберите интересующие вас данные на сайте ЦБ РФ,
    • создадите парсер для их сбора,
    • подберёте структуру для хранения данных,
    • создадите модуль для работы с сохранёнными данными.

Шаг 1

Выбрать интересующие данные в следующих разделах на сайте ЦБ:
    • базы данных (https://www.cbr.ru/hd_base/),
    • реестры (https://www.cbr.ru/registries/),
    • статистика (https://www.cbr.ru/statistics/).

    Примеры: курс валют, цены на аффинированные драгоценные металлы, реестр микрофинансовых организаций и пр.

    ! Для выбора недоступна ключевая ставка, которая будет разбираться на одном из вебинаров и примеры для которой приведены в этом ТЗ.


Шаг 2

Определите структуру для хранения и работы. Для ключевой ставки ЦБ РФ это может быть словарь (dict), где ключом будет выступать дата, а значением — размер ключевой ставки на указанную дату:
    {
        …
        datetime.date(2022,4,7): Decimal("0.2000"),
        datetime.date(2022,4,8): Decimal("0.2000"),
        datetime.date(2022,4,11): Decimal("0.1700"),
        datetime.date(2022,4,12): Decimal("0.1700"),
        datetime.date(2022,4,13): Decimal("0.1700"),
        …
    }


Шаг 3

Напишите скрипт, который будет производить сбор данных с выбранной страницы на сайте ЦБ РФ либо осуществлять загрузку xsl/xslx/pdf/csv или иного файла с данными в рабочую директорию с последующим его парсингом.


Шаг 4

Сделайте метод сериализации и десериализации данных для сохранения их в JSON-файл и подготовки данных для работы модулем из Шага 7. При написании метода используйте dict/list comprehensions.

Пример сериализованных данных для ключевой ставки:
    {
        …
        '2022-04-07': '0.2000',
        '2022-04-08': '0.2000',
        '2022-04-11': '0.1700',
        '2022-04-12': '0.1700',
        '2022-04-13': '0.1700'
    …
    }

    ! Формат JSON не позволяет хранить данные в виде объектов datetime и decimal.

    Сохранение файла должно производиться в директорию parsed_data внутри папки проекта.
    Путь к директории parsed_data должен быть прописан так, чтобы он был кроссплатформенным. Написанный скрипт должен запуститься на любой операционной системе и при запуске скрипта из любой директории.


Шаг 5

Необходимо привести данные к рабочим типам. Например:
    Даты привести к строковому формату ISO8601 или к типу datetime.
    Числа с плавающей точкой привести к типу decimal или хранить в строковом виде.
    И т. д.

    Продумайте и реализуйте методологию заполнения пробелов в данных, если это необходимо для работы. Пример для ключевой ставки, которая не публикуется для нерабочих дней, однако используется в расчётах:
    {
        …
        '2022-04-07': '0.2000',
        '2022-04-08': '0.2000',
        '2022-04-09': '0.2000',
        '2022-04-10': '0.2000',
        '2022-04-11': '0.1700',
        '2022-04-12': '0.1700',
        '2022-04-13': '0.1700'
        …
    }


Шаг 6

Оберните весь написанный код парсера в класс ParserCBRF.

Запуск парсера должен осуществляться через вызов метода start().


Шаг 7

Создайте отдельный класс для работы с собранными данными.

Для работы с ключевой ставкой можно описать класс KeyRateCBRF, экземпляр которого при работе будет обращаться к файлу с сохранёнными данными и через свои методы позволит быстро и удобно получать необходимые данные.

В рассматриваемом случае класс KeyRateCBRF может содержащий следующие публичные методы:

    • keyrate_by_date(date) — возвращает размер ставки на определённую дату

        Input:
        KeyRateCBRF.keyrate_by_date(“2022-04-07”)
        Output:
        "0.2000"

    • keyrate_last() — возвращает размер ключевой ставки на последнюю доступную дату

        Input:
        KeyRateCBRF.keyrate_last()
        Output:
        "0.7500"

    • keyrate_range_dates(from_date, to_date) — возвращает отсортированный список кортеж пар (дата, ключевая ставка) за определённый период

        Input:
        KeyRateCBRF.keyrate_range_dates('2022-04-07', '2022-04-13')
        Output:
        [
            ('2022-04-07', '0.2000'),
            ('2022-04-08', '0.2000'),
            ('2022-04-09', '0.2000'),
            ('2022-04-10', '0.2000'),
            ('2022-04-11', '0.1700'),
            ('2022-04-12', '0.1700'),
            ('2022-04-13', '0.1700')
        ]


Методы, указанные выше, являются примером для ключевой ставки. Список методов класса для работы с данными должен быть составлен в зависимости от вида данных, которые вы выбрали.
"""

from datetime import date
from bs4 import BeautifulSoup
import json
import os
import requests

print("Эта программа собирает данные о курсе валют")
chosen_date = input("Введите дату для просмотра курса валют в формате 'дд.мм.гггг': ")

class ParserCBRF:
    def __init__(self):
        self.url = ""
    def today_human_date(self):
        today = date.today().strftime("%d.%m.%Y")
        return today
    def get_page(self):
        url = f"https://cbr.ru/currency_base/daily/?" \
              f"UniDbQuery.Posted=True&" \
              f"UniDbQuery.To={chosen_date}"
        r = requests.get(url)
        return r.text

    def get_currency_base(self):
        html = self.get_page()
        soup = BeautifulSoup(html, "html.parser")
        table = [i.text for i in soup.find("table", class_="data").find_all("td")]
        self.table = table

    def currency_base_table(self):
        data_dict = {}
        self.data_dict = data_dict
        for i in range(1, len(self.table), 5):
            currency_code_iso = self.table[i]
            currency_amount = self.table[i+1]
            currency_name = self.table[i+2]
            currency_rate = self.table[i+3]
            currency_code_number = self.table[i-1]
            data_dict[currency_name] = {
                "Код валюты ISO 4217": currency_code_iso,
                "Код валюты цифровой": currency_code_number,
                "Единиц валюты":  currency_amount,
                "Курс к рублю РФ": currency_rate
            }
\
        currency_base_dict = dict(sorted(data_dict.items()))
        return currency_base_dict

    def save_file(self, parsed_data):
        currency = self.data_dict
        if not os.path.exists("parsed_data"):
            os.makedirs("parsed_data")
        with open(os.path.join("parsed_data", "currency_base.json"), "w", encoding="utf-8") as file:
            json.dump(currency, file, ensure_ascii=False, indent=4)


    def start(self):
        self.get_currency_base()
        self.currency_base_table()
        self.save_file("parsed_data.json")


def main():
    parser = ParserCBRF()
    parser.start()
    print("stop")


if __name__ == "__main__":
    main()
    print("stop")