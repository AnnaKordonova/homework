from masks import get_mask_account, get_mask_card_number


def mask_account_card(user_card: str) -> str:
    """Функция для вывода скрытых банковских реквизитов"""
    account_numbers = []
    bank_details = []
    str_number = ""
    for symbol in user_card:
        if symbol.isdigit():
            account_numbers.append(symbol)
        else:
            bank_details.append(symbol)

    int_list_number = int("".join(account_numbers))
    str_bank_details = "".join(bank_details)

    if len(account_numbers) == 16:
        str_number = get_mask_card_number(int_list_number)
    else:
        str_number = get_mask_account(int_list_number)

    all_info = str_bank_details + str_number

    return all_info
