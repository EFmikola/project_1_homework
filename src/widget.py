from src import masks as m


def mask_account_card(payment_number_and_text: str) -> str:
    """Функция для обработки информации о картах и счетах"""
    space_index = payment_number_and_text.rfind(" ")
    payment_text, payment_number = (
        payment_number_and_text[: space_index + 1],
        payment_number_and_text[space_index + 1 :],
    )
    if len(payment_number) == 16:
        number_mask = m.get_mask_card_number(int(payment_number))
    else:
        number_mask = m.get_mask_account(int(payment_number))
    mask = payment_text + number_mask
    return mask


def get_date(date_str: str) -> str:
    date_new_form = f"{date_str[8:10]}.{date_str[5:7]}.{date_str[:4]}"
    return date_new_form
