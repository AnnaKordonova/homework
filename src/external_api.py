import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
values = os.getenv("API_KEY")


def convert_to_rub(transaction: Any) -> float:
    """Функция конвертации"""
    amount = transaction["operationAmount"]["amount"]
    code = transaction["operationAmount"]["currency"]["code"]
    if code == "RUB":
        return float(amount)
    to = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={code}&amount={amount}"
    payload = {}
    response = requests.get(url, headers={"apikey": values}, data=payload)
    result = response.json()
    return float(result["result"])
