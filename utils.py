import requests
from datetime import datetime
from pprint import pprint


def get_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json(), "INFO: Данные получены успешно"
        return None, f"Error: status_code {response.status_code}"
    except requests.exceptions.ConnectionError:
        return None, 'Error: requests.exceptions.ConnectionError'
    except requests.exceptions.JSONDecodeError:

        return None, 'Error: requests.exceptions.JSONDecodeError'


def get_filtered_data(data, filtred_empty_from=False):
    #pprint(data[:5])
    # print(len(data))
    data = [x for x in data if "state" in x and x['state'] == "EXECUTED"]
    if filtred_empty_from:
        data = [x for x in data if "from" in x]
    # print(len(data))
    return data


def get_last_values(data, count_last_values):
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    data = data[:count_last_values]
    return data


def get_formatted_date(data):
    pprint(data[0])
    for row in data:
        data = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = row['description']
        sender = row['from'].split()
        from_bill = sender.pop(-1)
        from_bill = f'{from_bill[:4]} {from_bill[4:6]}** **** {from_bill[-4:]}'
        from_info = ' '.join(sender)
        to = f"{row['to'].split()[0]} **{row['to'][-4:]}"
        operation_amount = f"{row['operationAmount']['amount']} {row['operationAmount']['currency']}"
