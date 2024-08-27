from typing import Any

import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "user_card, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("", "Ничего не введено"),
        ("784427496", "Неверные данные"),
        ("Проба 3456789009087654323456789098079", "Неверные данные"),
    ],
)
def test_mask_account_card(user_card: str, expected: Any) -> Any:
    assert mask_account_card(user_card) == expected


@pytest.mark.parametrize(
    "user_data, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-01-15T08:45:30.123456", "15.01.2024"),
        ("2023-11-11T11:11:11.111111", "11.11.2023"),
        ("", "Неверно задана дата"),
        ("25-2-28T23:59:59.99", "Неверно задана дата"),
    ],
)
def test_get_date(user_data: str, expected: Any) -> Any:
    assert get_date(user_data) == expected
