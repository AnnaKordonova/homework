import logging
import os

import pandas as pd

logs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs")

log_file_path = os.path.join(logs_dir, "read_file.log")

logger = logging.getLogger("read_file")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_csv_file(file_path: str) -> list:
    """Считывает данные из CSV-файла и возвращает список словарей с транзакциями."""
    logger.info(f"Считывание данных из CSV-файла: {file_path}")
    try:
        data = pd.read_csv(file_path)
        logger.info("Данные успешно считаны из CSV-файла.")

        transactions = data.to_dict(orient="records")
        return transactions
    except Exception as e:
        logger.error(f"Ошибка при считывании CSV-файла: {e}")
        raise


def read_xlsx_file(file_path: str) -> list:
    """Считывает данные из XLSX-файла и возвращает список словарей с транзакциями."""
    logger.info(f"Считывание данных из XLSX-файла: {file_path}")
    try:
        data = pd.read_excel(file_path)
        logger.info("Данные успешно считаны из XLSX-файла.")

        transactions = data.to_dict(orient="records")
        return transactions
    except Exception as e:
        logger.error(f"Ошибка при считывании XLSX-файла: {e}")
        raise


def main() -> None:
    try:
        csv_data = read_csv_file("transactions.csv")
        print("Данные из CSV-файла:")
        print(csv_data)
    except FileNotFoundError:
        print("Файл 'transactions.csv' не найден.")

    try:
        xlsx_data = read_xlsx_file("transactions_excel.xlsx")
        print("\nДанные из XLSX-файла:")
        print(xlsx_data)
    except FileNotFoundError:
        print("Файл 'transactions_excel.xlsx' не найден.")


if __name__ == "__main__":
    main()
