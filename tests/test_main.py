from unittest.mock import patch

import pytest

from main import main

mock_json_data = [
    {
        "date": "2023-01-01T12:00:00",
        "description": "Тестовая транзакция",
        "from": "Счет 1234567890",
        "to": "Счет 0987654321",
        "operationAmount": {"amount": 1000, "currency": {"code": "RUB"}},
    }
]

mock_csv_data = mock_json_data
mock_excel_data = mock_json_data


@pytest.fixture
def mock_load_transactions(mocker):
    return mocker.patch("src.utils.load_transactions", return_value=mock_json_data)


@pytest.fixture
def mock_read_csv_file(mocker):
    return mocker.patch("src.read_file.read_csv_file", return_value=mock_csv_data)


@pytest.fixture
def mock_read_xlsx_file(mocker):
    return mocker.patch("src.read_file.read_xlsx_file", return_value=mock_excel_data)


def test_main_json(mock_load_transactions, mock_read_csv_file, mock_read_xlsx_file):
    with patch("builtins.input", side_effect=["1", "EXECUTED", "да", "в порядке убывания", "да", "тест", "да"]):
        with patch("src.processing.filter_by_state", return_value=mock_json_data), patch(
            "src.processing.sort_by_date", return_value=mock_json_data
        ), patch("src.generators.filter_by_currency", return_value=mock_json_data), patch(
            "src.banking_search.banking_search", return_value=mock_json_data
        ), patch(
            "src.widget.mask_account_card", side_effect=lambda x: "****" + x[-4:]
        ):
            main()


def test_main_csv(mock_load_transactions, mock_read_csv_file, mock_read_xlsx_file):
    with patch("builtins.input", side_effect=["2", "EXECUTED", "нет", "нет", "нет", "нет", "нет"]):
        with patch("src.processing.filter_by_state", return_value=mock_csv_data), patch(
            "src.processing.sort_by_date", return_value=mock_csv_data
        ), patch("src.generators.filter_by_currency", return_value=mock_csv_data), patch(
            "src.banking_search.banking_search", return_value=mock_csv_data
        ), patch(
            "src.widget.mask_account_card", side_effect=lambda x: "****" + x[-4:]
        ):
            main()


def test_main_xlsx(mock_load_transactions, mock_read_csv_file, mock_read_xlsx_file):
    with patch("builtins.input", side_effect=["3", "EXECUTED", "да", "в порядке возрастания", "нет", "да", "тест"]):
        with patch("src.processing.filter_by_state", return_value=mock_excel_data), patch(
            "src.processing.sort_by_date", return_value=mock_excel_data
        ), patch("src.generators.filter_by_currency", return_value=mock_excel_data), patch(
            "src.banking_search.banking_search", return_value=mock_excel_data
        ), patch(
            "src.widget.mask_account_card", side_effect=lambda x: "****" + x[-4:]
        ):
            main()


def test_invalid_selection(mock_load_transactions, mock_read_csv_file, mock_read_xlsx_file):
    with patch("builtins.input", side_effect=["4"]):
        with patch("src.processing.filter_by_state", return_value=mock_json_data):
            main()
