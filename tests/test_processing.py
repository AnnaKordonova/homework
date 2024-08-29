from typing import Any

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ("UNKNOWN", []),
        ("", []),
    ],
)
def test_filter_by_state(bank_operation: list[dict], state: str, expected: Any) -> Any:
    assert filter_by_state(bank_operation, state) == expected


def test_sort_by_date():
    operations = [
        {"id": 30303030, "state": "EXECUTED", "date": "2024-03-13T02:26:18.671407"},
        {"id": 10101010, "state": "EXECUTED", "date": "2024-03-11T10:20:30.123456"},
        {"id": 20202020, "state": "EXECUTED", "date": "2024-03-12T14:45:00.987654"},
    ]
    sorted_operations = sort_by_date(operations, ascending=True)
    assert sorted_operations == [
        {"id": 30303030, "state": "EXECUTED", "date": "2024-03-13T02:26:18.671407"},
        {"id": 20202020, "state": "EXECUTED", "date": "2024-03-12T14:45:00.987654"},
        {"id": 10101010, "state": "EXECUTED", "date": "2024-03-11T10:20:30.123456"},
    ]


def test_sort_by_date_empty_list():
    assert sort_by_date([]) == []
