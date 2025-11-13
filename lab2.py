import csv
import random
import xml.etree.ElementTree as ET


def element_length_greater(count, list_dict_reader):
    return_list = []
    for entry in list_dict_reader:
        if len(entry['Название']) > count:
            return_list.append(entry)
    for entry_return in return_list:
        print(entry_return)


def search_book(authors_name, list_dict_reader):
    return_list = []
    for entry in list_dict_reader:
        if entry['Автор'] == authors_name and int(entry['Цена поступления']) >= 200:
            return_list.append(entry)
    for entry_return in return_list:
        print(entry_return)


def link_generator(count_book, incoming_list):
    return_list = []
    random_book = random.sample(incoming_list, len(incoming_list))
    for i in range(count_book):
        #Делим "дата поступления" на две части: дату и время; делим дату по точкам и берём последний элемент - год
        date_enrty, time_entry = random_book[i]['Дата поступления'].split(' ')
        year = date_enrty.split('.')[-1]
        return_list.append(f'{i+1}. {random_book[i]['Автор']}. {random_book[i]['Название']} - {year}')
    with open("results.txt", 'w') as results:
        for i in range(count_book):
            results.write(return_list[i]+'\n')


def parser():
    tree = ET.parse('currency.xml')
    root = tree.getroot()
    list_dicts = []
    f = 0
    for elem in root.iter():
        if elem.tag == 'Valute' or elem.tag == 'ValCurs':
            f = 0
            continue
        if f == 0:
            list_dicts.append({})
            f = 1
        list_dicts[-1][elem.tag] = elem.text
    return_dict = {}
    for dict in list_dicts:
        return_dict[dict['Name']] = dict['CharCode']

    # если понадобится вывод словаря
    for i in return_dict:
        print(i, return_dict[i])


with open("books.csv") as books_file:
    books_reader = csv.DictReader(books_file, delimiter=";")
    books_list = [i for i in books_reader]  #список словарей, каждый словарь - строка исходной таблицы

    # element_length_greater(200, books_list)
    # search_book('Б. А. Воскресенский', books_list)
    # link_generator(20, books_list)
    # parser()


