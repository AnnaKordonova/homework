import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("7000792289606361", "7000 79** **** 6361"),
        ("7000792289606361", "7000 79** **** 6361"),
        ("", "Ничего не введено"),
        ("457846387643754375475", "Ошибка в номере карты"),
        ("686235", "Ошибка в номере карты"),
    ]
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("73654439856893673489", "**3489"),
        ("05667143248967509325", "**9325"),
        ("", "Ничего не введено"),
        ("4578463876437543754345675", "Ошибка в номере счёта"),
        ("686235", "Ошибка в номере счёта"),
    ]
)
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected
