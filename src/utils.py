import json
import logging
import os
from json import JSONDecodeError
from typing import Any

from src.external_api import convert_to_rub

logs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs")

os.makedirs(logs_dir, exist_ok=True)

log_file_path = os.path.join(logs_dir, "utils.log")


logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_transactions(file_path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        with open(file_path, encoding="utf-8") as fin_file:
            try:
                transactions = json.load(fin_file)
                logger.info(f"Успешно загружены транзакции из файла: {file_path}")
            except JSONDecodeError:
                logger.error(f"Ошибка декодирования JSON файле: {file_path}")
                return []
        if not isinstance(transactions, list):
            logger.error(f"Данные в файле {file_path} не являются списком.")
            return []
        return transactions
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []


def transaction_amount(trans: dict, currency: str = "RUB") -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if trans["operationAmount"]["currency"]["code"] == currency:
        amount = trans["operationAmount"]["amount"]
        logger.info(f"Сумма транзакции в рублях: {amount}")
    else:
        amount = convert_to_rub(trans)
        logger.info(f"Конвертированная сумма транзакции в рублях: {amount}")
    return amount


print(load_transactions("operations.json"))
