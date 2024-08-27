from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_card: str) -> str:
    """Функция для вывода скрытых банковских реквизитов"""
    account_numbers = []
    bank_details = []
    str_number = ""
    if len(user_card) == 0:
        return "Ничего не введено"
    for symbol in user_card:
        if symbol.isdigit():
            account_numbers.append(symbol)
        else:
            bank_details.append(symbol)

    int_list_number = int("".join(account_numbers))
    str_bank_details = "".join(bank_details)

    if len(account_numbers) > 20 or len(account_numbers) < 16:
        return  "Неверные данные"

    if len(account_numbers) == 16:
        str_number = get_mask_card_number(int_list_number)
    else:
        str_number = get_mask_account(int_list_number)

    all_info = str_bank_details + str_number

    return all_info


def get_date(implicated_date: str) -> str:
    """Функция для извлечения даты из строки в формат ДД.ММ.ГГГГ"""
    if len(implicated_date) > 26 or len(implicated_date) < 26 or len(implicated_date) == 0:
        return "Неверно задана дата"

    formatted_date = implicated_date.split("T")[0]
    extracted_date = f"{formatted_date[-2:]}.{formatted_date[5:7]}.{formatted_date[:4]}"
    return extracted_date
