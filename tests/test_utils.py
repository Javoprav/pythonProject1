import pytest
from utils import get_data, get_filtered_data


def test_get_data(test_url):
    assert len(get_data(test_url)[0]) > 0
    assert get_data('https://replit.com/@Javoprffjhfghgfav/Pythondfgd.py')[0] is None
    assert get_data('https://skyengpublic.notion.site/backend-7abf85179e2e4031ad03d04d051d938b')[0] is None
    assert get_data('https://skyengpublic.notion.site/backend-7abf1d938b')[0] is None


def test_get_filtered_data(test_data):
    assert len(get_filtered_data(test_data)) == 4
    assert len(get_filtered_data(test_data, filtred_empty_from=True)) == 2