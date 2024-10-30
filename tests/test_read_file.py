from unittest.mock import patch

import pandas as pd
import pytest

from src.read_file import read_csv_file, read_xlsx_file


@patch("pandas.read_csv")
def test_read_csv_file_success(mock_read_csv):
    mock_data = pd.DataFrame({"column1": [1, 2], "column2": [3, 4]})
    mock_read_csv.return_value = mock_data

    result = read_csv_file("dummy_path.csv")

    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0] == {"column1": 1, "column2": 3}
    assert result[1] == {"column1": 2, "column2": 4}

    mock_read_csv.assert_called_once_with("dummy_path.csv")


@patch("pandas.read_csv")
def test_read_csv_file_failure(mock_read_csv):
    mock_read_csv.side_effect = FileNotFoundError("File not found")

    with pytest.raises(FileNotFoundError):
        read_csv_file("dummy_path.csv")


@patch("pandas.read_excel")
def test_read_xlsx_file_success(mock_read_excel):
    mock_data = pd.DataFrame({"column1": [1, 2], "column2": [3, 4]})
    mock_read_excel.return_value = mock_data

    result = read_xlsx_file("dummy_path.xlsx")

    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0] == {"column1": 1, "column2": 3}
    mock_read_excel.assert_called_once_with("dummy_path.xlsx")


@patch("pandas.read_excel")
def test_read_xlsx_file_failure(mock_read_excel):
    mock_read_excel.side_effect = FileNotFoundError("File not found")

    with pytest.raises(FileNotFoundError):
        read_xlsx_file("dummy_path.xlsx")
