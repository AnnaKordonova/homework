import os
from unittest.mock import patch

import pytest

from src.utils import load_transactions, transaction_amount


@pytest.fixture
def path():
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
    return PATH_TO_FILE


@pytest.fixture
def path_mistake_json():
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations_2.json")
    return PATH_TO_FILE


@pytest.fixture
def trans():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@pytest.fixture
def trans_1():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


def test_load_transactions_nofile():
    assert load_transactions("nofile") == []


def test_load_transactions(path):
    assert load_transactions(path)[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


def test_load_transactions_mistake_json(path_mistake_json):
    assert load_transactions(path_mistake_json) == []


def test_transaction_amount(trans):
    assert transaction_amount(trans) == "31957.58"


@patch("src.utils.convert_to_rub")
def test_transaction_amount_non_rub(mock_convert_to_rub, trans_1):
    mock_convert_to_rub.return_value = 1000.0
    assert transaction_amount(trans_1) == 1000.0
