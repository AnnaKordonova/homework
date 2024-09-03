from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "USD",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
        ),
        (
            "RUB",
            [
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                }
            ],
        ),
        ("", []),
        ("TRDFEH", []),
    ],
)
def test_filter_by_currency(transactions: list[dict], state: str, expected: Any) -> Any:
    result = list(filter_by_currency(transactions, state))
    assert result == expected


def test_transactions_descriptions(transactions: list[dict]) -> Any:
    result = list(transaction_descriptions(transactions))
    assert result == ["Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет"]


def test_transactions_descriptions_empty(transactions: list[dict]) -> Any:
    result = list(transaction_descriptions(transactions))
    assert result


def test_card_number_generator() -> Any:
    expected = ["0000 0000 0000 0000", "0000 0000 0000 0001", "0000 0000 0000 0002"]
    result = list(card_number_generator(0, 2))
    assert result == expected


def test_card_number_generator_empty() -> Any:
    result = list(card_number_generator(5, 2))
    assert result == []

    result = list(card_number_generator(0, -1))
    assert result == []
