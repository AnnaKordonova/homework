import os
from typing import Any

import pytest

from src.decorators import log


@log()
def success_func(x: int | float, y: int | float) -> int | float:
    return x + y


@log("mylog.txt")
def fail_func(x: int | float, y: int | float) -> int | float:
    return x / y


def test_success_func(capsys: Any) -> Any:
    success_func(2, 3)
    captured = capsys.readouterr()
    assert captured.out == f"Начало работы функции 'success_func'\n5Конец работы функции 'success_func'\n"


def test_fail_func() -> None:
    with pytest.raises(ZeroDivisionError):
        fail_func(1, 0)

    assert os.path.exists("mylog.txt")
    with open("mylog.txt", "r", encoding="utf-8") as file:
        test_log_text = file.read()
        assert (
            test_log_text
            == "Начало работы функции 'fail_func'\n'fail_func' error: ZeroDivisionError. Inputs: (1, 0), {}\n"
        )
