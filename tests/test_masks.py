from unittest.mock import patch

from src.masks import get_mask_account, get_mask_card_number


@patch("logging.Logger.info")
@patch("logging.Logger.error")
def test_get_mask_card_number_success(mock_error, mock_info):
    result = get_mask_card_number(1234567812345678)
    assert result == "1234 56** **** 5678"
    mock_info.assert_called_with("Скрытый номер карты: 1234 56** **** 5678")


@patch("logging.Logger.error")
def test_get_mask_card_number_none(mock_error):
    result = get_mask_card_number(None)
    assert result == "Ничего не введено"
    mock_error.assert_called_with("Ничего не введено")


@patch("logging.Logger.error")
def test_get_mask_card_number_invalid_length(mock_error):
    result = get_mask_card_number(123456)
    assert result == "Ошибка в номере карты"
    mock_error.assert_called_with("Ошибка в номере карты")


@patch("logging.Logger.info")
@patch("logging.Logger.error")
def test_get_mask_account_success(mock_error, mock_info):
    result = get_mask_account(12345678901234567890)
    assert result == "**7890"
    mock_info.assert_called_with("Скрытый номер счёта: **7890")


@patch("logging.Logger.error")
def test_get_mask_account_none(mock_error):
    result = get_mask_account(None)
    assert result == "Ничего не введено"
    mock_error.assert_called_with("Ничего не введено")


@patch("logging.Logger.error")
def test_get_mask_account_invalid_length(mock_error):
    result = get_mask_account(123456)
    assert result == "Ошибка в номере счёта"
    mock_error.assert_called_with("Ошибка в номере счёта")
