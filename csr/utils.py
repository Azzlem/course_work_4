import json

import requests
from vacancies import Vacancies_hh

init_area = ["1.Платформа", "2.Город", "3.Ссылка", "4.Необходимые навыки", "5.Зарплата"]

name_of_vacansies = input("Введите интересующую вакансию: ")


def getpage(page=0):
    """
    Создаем метод для получения страницы со списком вакансий.
    Аргументы:
        page - Индекс страницы, начинается с 0. Значение по умолчанию 0, т.е. первая страница
    """

    # Справочник для параметров GET-запроса
    params = {
        'text': f'NAME:{name_of_vacansies}',  # Текст фильтра. В имени должно быть слово "Аналитик"
        'area': 2,  # Поиск ощуществляется по вакансиям города Москва
        'page': page,  # Индекс страницы поиска на HH
        'per_page': 100  # Кол-во вакансий на 1 странице
    }

    req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
    data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
    req.close()
    return data


a = json.loads(getpage())
vacansies_hh = []
for el in a["items"]:
    vacansies_hh.append(Vacancies_hh(
        el["alternate_url"],
        "Headhunter",
        el["area"]["name"],
        el["salary"],
        el["snippet"]["requirement"],
    )
    )

with open("text.json", "w") as f:
    f.write(getpage())


for _ in init_area:
    print(_)

list_user_input = input(
    f"Выберите критерии фильтра"
    f"(Наберите через пробел номера из предсталенного выше списка):"
).split(" ")

list_user_input = list(map(lambda x: int(x), list_user_input))

print(list_user_input)

for elem in vacansies_hh:
    for el in list_user_input:
        if 0 == el:
            print(elem.platform)
        elif 1 == el:
            print(elem.city)
        elif 2 == el:
            print(elem.url)
        elif 3 == el:
            print(elem.knowledge_stack)
        elif 4 == el:
            print(elem.pay)
