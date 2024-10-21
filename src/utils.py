import json
from json import JSONDecodeError
from typing import Any

from src.external_api import convert_to_rub


def load_transactions(file_path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        with open(file_path, encoding="utf-8") as fin_file:
            try:
                transactions = json.load(fin_file)
            except JSONDecodeError:
                return []
        if not isinstance(transactions, list):
            return []
        return transactions
    except FileNotFoundError:
        return []


def transaction_amount(trans: dict, currency: str = "RUB") -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if trans["operationAmount"]["currency"]["code"] == currency:
        amount = trans["operationAmount"]["amount"]
    else:
        amount = convert_to_rub(trans)
    return amount


print(load_transactions("operations.json"))
