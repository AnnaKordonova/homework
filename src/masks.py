def get_mask_card_number(card_number: int) -> str:
    """Функция для скрытия полного номера карты"""

    hidden_card_list = [i for i in range(6, 12)]
    card_number_str = str(card_number)
    masks = ""
    if len(card_number_str) == 0:
        return "Ничего не введено"
    if len(card_number_str) > 16 or len(card_number_str) < 16:
        return "Ошибка в номере карты"
    for i in range(len(card_number_str)):
        if i != 0 and i % 4 == 0:
            masks += " "
        if i in hidden_card_list:
            masks += "*"
        else:
            masks += card_number_str[i]
    return masks


def get_mask_account(account_number: int) -> str:
    """Функция для скрытия полного номера счёта"""

    hidden_account_str = str(account_number)
    if len(hidden_account_str) == 0:
        return "Ничего не введено"
    if len(hidden_account_str) > 20 or len(hidden_account_str) < 20:
        return "Ошибка в номере счёта"
    return "**" + hidden_account_str[-4:]
