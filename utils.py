import requests
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
    pprint(data[:5])
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
