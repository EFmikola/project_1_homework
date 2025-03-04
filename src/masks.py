def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты"""
    card_number_str = str(card_number)
    if len(card_number_str) < 16:
        card_number_str = '0' * (16 - len(card_number_str)) + card_number_str
    mask_card_number = card_number_str[:4] + " " + card_number_str[4:6] + "** **** " + card_number_str[-4:]
    return mask_card_number


def get_mask_account(account_number: int) -> str:
    """Функция маскировки номера банковского счета"""
    account_number_str = str(account_number)
    if len(account_number_str) < 20:
        account_number_str = '0' * (20 - len(account_number_str)) + account_number_str
    account_number_mask = "**" + account_number_str[-4:]
    return account_number_mask
