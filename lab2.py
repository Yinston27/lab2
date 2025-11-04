import csv
import random



def element_length_greater(count, list_dict_reader):
    return_list = []
    for string in list_dict_reader:
        if len(string['Название']) > count:
            return_list.append(string)
    for string in return_list:
        print(string)


def search_book(authors_name, list_dict_reader):
    return_list = []
    for string in list_dict_reader:
        if string['Автор'] == authors_name and int(string['Цена поступления']) >= 200:
            return_list.append(string)
    for string in return_list:
        print(string)


def link_generator(count_book, list):
    return_list = []
    random_book = random.sample(list, len(list))
    for i in range(count_book):
        #Делим "дата поступления" на две части: дату и время - берём только дату; делим дату по точкам и берём последний элемент - год
        year = random_book[i]['Дата поступления'].split(' ')[0].split('.')[2]
        return_list.append(f'{i+1}. {random_book[i]['Автор']}. {random_book[i]['Название']} - {year}')
    with open("results.txt", 'w') as results:
        for i in range(count_book):
            results.write(return_list[i]+'\n')


with open("books.csv") as books_file:
    books_reader = csv.DictReader(books_file, delimiter=";")
    books_list = [i for i in books_reader]  #список словарей, каждый словарь - строка исходной таблицы

    # element_length_greater(30, books_list)
    # search_book('Б. А. Воскресенский', books_list)
    # link_generator(20, books_list)


