import csv
from csv import writer
import log
import requests
import json

table = ['last_name', 'name', 'phone_number', 'post', 'salary']


def add_data(data):
    """Write"""
    with open('data.csv', 'a', newline='') as f:
        writer(f).writerow(data)

    log_message = f'Добавлены данные: {data}'
    log.write_log(log_message)
    return log_message


def find_data(find_request):
    """Find"""
    with open('data.csv', encoding='utf=8') as file:
        reader = csv.reader(file, delimiter=',')
        for line in reader:
            if find_request in line:
                description = dict(zip(table, line))
                result =""
                for key, value in description.items():
                    result = result + " " + key + ":" + value + "\n"
                    print(result)
            else:
                result = 'данные не найдены'

    log_message = f'Поиск данных по запросу: {find_request}'
    log.write_log(log_message)
    
    return result


def delete_data(delete_request):
    """Delete"""
    with open('data.csv', 'r+') as in_f:
        data = list(csv.reader(in_f))
        in_f.truncate(0)

    data = list(filter(None, data))

    with open('data.csv', 'w', newline='') as out_f:
        for row in data:
            if delete_request not in row:
                writer(out_f).writerow(row)

    log_message = f'Удалены данные по запросу: {delete_request}'
    log.write_log(log_message)
    return log_message

def get_weather (city):
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=4321a3d417b53045aa1b6617c529c910&units=metric&lang=ru")
    a=response.json()
    tipe_weather = json.dumps(a['weather'][0]['main'])
    temperature = json.dumps(a['main']['temp'])
    wind = json.dumps(a['wind']['speed'])
    result = f"В {city} сегодня : " + tipe_weather + '\n' + "Температура :" + temperature + '\n' + 'Ветер : ' + wind + ' метров в секунду'
    return result