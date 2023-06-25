"""
Напишите скрипт, который будет производить сбор данных с выбранной страницы на сайте ЦБ РФ,
    либо осуществлять загрузку xsl, xslx, pdf, csv или иного файла с данными в рабочую директорию с последующим его парсингом.

У класса должен быть только один публичный метод start(). Все остальные методы, содержащие логику по выгрузке и сохранению данных, должны быть приватными.

Определите структуру для хранения.
    Например, для ключевой ставки ЦБ РФ это может быть словарь (dict), где ключом будет выступать дата, а значением — размер ключевой ставки на указанную дату.

Оберните весь написанный код парсера в класс ParserCBRF
"""

from datetime import date
from bs4 import BeautifulSoup
import json
import os
import requests


class ParserCBRF:
    def __init__(self):
        self.url = ""
    def today_human_date(self):
        today = date.today().strftime("%d.%m.%Y")
        return today
    def get_page(self):
        url = f"https://www.cbr.ru/hd_base/KeyRate/?" \
              f"UniDbQuery.Posted=True&" \
              f"UniDbQuery.To={self.today_human_date()}"
        r = requests.get(url)
        return r.text

    def get_key_rate_base(self):
        html = self.get_page()
        soup = BeautifulSoup(html, "html.parser")
        table = [i.text for i in soup.find("table", class_="data").find_all("td")]
        self.table = table

    def key_rate_table(self):
        data_dict = {}
        self.data_dict = data_dict
        for i in range(0, len(self.table), 2):
            key_rate = self.table[i]
            key_rate_date = self.table[i+1]
            data_dict[key_rate] = {
                "Ставка": key_rate_date,
            }

        key_rate_dict = dict(sorted(data_dict.items()))
        return key_rate_dict

    def save_file(self, parsed_data):
        currency = self.data_dict
        if not os.path.exists("parsed_data"):
            os.makedirs("parsed_data")
        with open(os.path.join("parsed_data", "key_rate_base.json"), "w", encoding="utf-8") as file:
            json.dump(currency, file, ensure_ascii=False, indent=4)


    def start(self):
        self.get_key_rate_base()
        self.key_rate_table()
        self.save_file("parsed_data.json")


def main():
    parser = ParserCBRF()
    parser.start()
    print("stop")


if __name__ == "__main__":
    main()
    print("stop")