import requests
import json
# from My_Progect.hh_pars.main import varInput
url = "https://api.hh.ru/vacancies?text=Django&area=40"
response = requests.get(url)
json_data = response.content.decode('utf-8')
# print(json_data)


def write_file():
    with open("file_name.json", 'w') as file:
        json.dump(json_data, file)


def read_file():
    with open('file_name.json', 'r') as file:
        json_data1 = json.loads(file.read())
        json_data1 = json.loads(json_data1)
        print(json_data1['items'][1])
