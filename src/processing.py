from operator import itemgetter
from typing import Any


def filter_by_state(data: list[dict[str, Any]], state="EXECUTED") -> list[dict[str, Any]]:
    """Функция, возвращающая список словарей по определённому ключу 'state'"""
    new_list = []
    for operation in data:
        if operation["state"] == state:
            new_list.append(operation)
    return new_list


def sort_by_date(data: list[dict[str, Any]], ascending=True) -> list[dict[str, Any]]:
    """Функция, возвращающая список словарей отсортированных по дате"""
    result = sorted(data, key=itemgetter("date"))
    return result
