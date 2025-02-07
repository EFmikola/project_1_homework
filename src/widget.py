import masks as m


def mask_account_card(payment_number_and_text: str) -> str:
    """Функция для обработки информации о картах и счетах"""
    space_index = payment_number_and_text.rfind(" ")
    payment_text, payment_number = (
        payment_number_and_text[: space_index + 1],
        payment_number_and_text[space_index + 1 :],
    )
    if len(payment_number) == 16:
        number_mask = m.get_mask_card_number(payment_number)
    else:
        number_mask = m.get_mask_account(payment_number)
    return payment_text + number_mask
