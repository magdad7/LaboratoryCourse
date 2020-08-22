import csv
import random
import datetime

if __name__ == '__main__':
    print("Example of data parsing and saving")

    # path_to_csv = 'probki.csv'

    # with open('hrdata.csv') as csvfile:
    #     csv_reader = csv.DictReader(csvfile, delimiter=',')
    #     csv_file_rows = []
    #     for row in csv_reader:
    #         csv_file_rows.append(row)
    #
    #     lista_imon = []
    #     for dict_row in csv_file_rows:
    #         print(dict_row['Name'])
    #         lista_imon.append(dict_row['Name'])

    # lista = []
    # for i in range(10):
    #     lista.append(i)
    # print(lista)
    #
    # def kwadrat(i):
    #     return i*i
    #
    # # list comprehension
    # lista_2 = [kwadrat(i) for i in [0.2, 0.5]]
    # print(lista_2)

    # with open(path_to_csv, 'w', newline='') as csvfile:
    #     spamwriter = csv.writer(csvfile, delimiter=',')
    #     spamwriter.writerow(['Nr zlecenia', 'Nazwa firmy', 'Adres', 'Data przyjęcia', 'Numer próbki'])
    #     nry_zlecenia = []
    #     nazwy_firm = []
    #     adresy = []
    #     data = []
    #     nr_probek = [random.randrange(100) for i in range(5)]
    #
    #     current_time = datetime.datetime.now()
    #     string_time = str(current_time.hour) + '_' + str(current_time.minute) + '_' + str(current_time.day) + '_' + \
    #                     str(current_time.month) + '_' + str(current_time.year)
    #     for i in range(5):
    #         nry_zlecenia.append(random.randrange(10))
    #         nazwy_firm.append('firma_' + str(i))
    #         adresy.append('lipowa ' + str(i))
    #         data.append(string_time)
    #     for i in range(5):
    #         spamwriter.writerow([nry_zlecenia[i],
    #                              nazwy_firm[i],
    #                              adresy[i],
    #                              data[i],
    #                              nr_probek[i]])

    #
    #     print(lista_imon)
    # a = {'imie': 'Andrzej'}
    # print(a['imie'])
    # b = ['imie', 'Andrzej']
    # print(b[1])

    import json

    my_json_string = """{
       "article": [

          {
             "id":"01",
             "language": "JSON",
             "edition": "first",
             "author": "Derrick Mwiti"
          },

          {
             "id":"02",
             "language": "Python",
             "edition": "second",
             "author": "Derrick Mwiti SZUKANY"
          }
       ],

       "blog":[
       {
           "name": "Datacamp",
           "URL":"datacamp.com"
       }
       ]
    }
    """
    to_python = json.loads(my_json_string)
    print(to_python['blog'][0]['name'])
    print(to_python['article'][1]['author'])
