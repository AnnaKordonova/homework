from typing import Iterable


def filter_by_currency(transactions: list[dict], currency: str) -> Iterable:
    """Функция принимающая на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочерёдно выдаёт транзакции,
    где валюта соответсвует заданной"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterable:
    """Функция принимающая список словарей с транзакциями.
    Возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        description = transaction.get("description")
        yield description


def card_number_generator(start: int, end: int) -> Iterable:
    """Функция, создающая генератор случайных номеров карт"""
    for number in range(start, end + 1):
        formatted_number = f"{number:016d}"
        yield f"{formatted_number[:4]} {formatted_number[4:8]} {formatted_number[8:12]} {formatted_number[12:16]}"


# for card_number in card_number_generator(35, 37):
#     print(card_number)
