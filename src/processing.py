from typing import Any


def filter_by_state(data: list[dict[str, Any]], state = "EXECUTED") -> list[dict[str, Any]]:
    new_list = []
    for operation in data:
        if operation.get("state") == state:
            new_list.append(operation)
    return new_list
