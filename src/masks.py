import logging
import os

logs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs")

os.makedirs(logs_dir, exist_ok=True)

log_file_path = os.path.join(logs_dir, "masks.log")


logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int | None = None) -> str:
    """Функция для скрытия полного номера карты"""

    if card_number is None:
        logger.error("Ничего не введено")
        return "Ничего не введено"

    logger.info("Получен номер карты")

    hidden_card_list = [i for i in range(6, 12)]
    card_number_str = str(card_number)
    masks = ""

    if len(card_number_str) != 16:
        logger.error("Ошибка в номере карты")
        return "Ошибка в номере карты"

    for i in range(len(card_number_str)):
        if i != 0 and i % 4 == 0:
            masks += " "
        if i in hidden_card_list:
            masks += "*"
        else:
            masks += card_number_str[i]

    logger.info(f"Скрытый номер карты: {masks}")
    return masks


def get_mask_account(account_number: int | None = None) -> str:
    """Функция для скрытия полного номера счёта"""

    if account_number is None:
        logger.error("Ничего не введено")
        return "Ничего не введено"

    logger.info("Получен номер счёта")

    hidden_account_str = str(account_number)

    if len(hidden_account_str) != 20:
        logger.error("Ошибка в номере счёта")
        return "Ошибка в номере счёта"

    masked_account = "**" + hidden_account_str[-4:]
    logger.info(f"Скрытый номер счёта: {masked_account}")
    return masked_account


print(get_mask_card_number(1234567123456))
print(get_mask_account(1))
