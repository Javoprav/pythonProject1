import pytest
from utils import get_data, get_filtered_data, get_last_values, get_formatted_date


def test_get_data(test_url):
    assert len(get_data(test_url)[0]) > 0
    assert get_data('https://replit.com/@Javoprffjhfghgfav/Pythondfgd.py')[0] is None
    assert get_data('https://skyengpublic.notion.site/backend-7abf85179e2e4031ad03d04d051d938b')[0] is None
    assert get_data('https://skyengpublic.notion.site/backend-7abf1d938b')[0] is None


def test_get_filtered_data(test_data):
    assert len(get_filtered_data(test_data)) == 4
    assert len(get_filtered_data(test_data, filtred_empty_from=True)) == 2


def test_get_last_values(test_data):
    data = get_last_values(test_data, 4)
    assert data[0]['date'] == '2019-08-26T10:50:58.294041'
    assert len(data) == 4


def test_get_formatted_date(test_data):
    data = get_formatted_date(test_data)
    assert data == ['        26.08.2019 Перевод организации\n'
                    '        Maestro 1596 83** **** 5199 -> Счет **9589\n'
                    '        31957.58 руб.\n'
                    '        ',
                    '        03.07.2019 Перевод организации\n'
                    '        Maestro 1596 83** **** 5199 -> Счет **5560\n'
                    '        8221.37 USD\n'
                    '        ',
                    '        30.06.2018 Перевод организации\n'
                    '        Счет 7510 68** **** 6952 -> Счет **6702\n'
                    '        9824.07 USD\n'
                    '        ',
                    '        23.03.2018 Открытие вклада\n'
                    '        Счет 7510 68** **** 6952 -> Счет **2431\n'
                    '        48223.05 руб.\n'
                    '        ',
                    '        04.04.2019 Перевод со счета на счет\n'
                    '        Счет 1970 86** **** 8542 -> Счет **4188\n'
                    '        79114.93 USD\n'
                    '        ']
