import pytest
from collections import Counter
from src.banking_search import banking_search, number_operations

test_data = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    },
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    },
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }
]

@pytest.fixture
def sample_data():
    return test_data

def test_banking_search(sample_data):
    # Тестируем поиск по банку
    result = banking_search(sample_data, "Перевод")
    assert len(result) == 3
    assert all(transaction['description'] == "Перевод организации" for transaction in result)

    result_empty = banking_search(sample_data, "Неизвестный банк")
    assert len(result_empty) == 0

def test_number_operations(sample_data):
    # Тестируем подсчет операций по категориям
    categories = ["Перевод организации"]
    result = number_operations(sample_data, categories)
    assert result == {"Перевод организации": 3}

    categories_empty = ["Неизвестная категория"]
    result_empty = number_operations(sample_data, categories_empty)
    assert result_empty == {}

