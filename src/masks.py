def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты"""
    card_number_str = str(card_number)
    mask_card_number = card_number_str[:4] + " " + card_number_str[4:6] + "** **** " + card_number_str[-4:]
    return mask_card_number


def get_mask_account(account_number: int) -> str:
    """Функция маскировки номера банковского счета"""
    account_number_str = str(account_number)
    account_number_mask = "**" + account_number_str[-4:]
    return account_number_mask
