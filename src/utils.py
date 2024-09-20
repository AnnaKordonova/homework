import json
import os
from typing import Any


def json_file_reader(file_path: str) -> list:
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, encoding='utf-8') as trans_file:
            data = json.load(trans_file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (json.JSONDecodeError, OSError):
        return []


def get_amount_transaction(trans: dict, currency: str="RUB") -> Any:
    if trans["operationAmount"]["currency"]["code"] == currency:
        amount = trans["operationAmount"]["amount"]
    else:
        amount = currency_conversion(trans)
    return amount