def filter_by_currency(transactions: list, code: str) -> iter:
    """Генератор фильтрации по валюте"""
    filtered_transactions = filter(lambda x: x["operationAmount"]["currency"]["code"] == code, transactions)
    return filtered_transactions


def transaction_descriptions(transactions: list) -> iter:
    """Генератор описаний транзакций"""
    for transaction in transactions:
        yield transaction["description"]


def format_number(number: int) -> str:
    """Функция форматирования числа в маску"""
    stroke_num = "0" * (16 - len(str(number))) + str(number)
    formated_number = " ".join([stroke_num[x * 4:(x + 1) * 4] for x in range(4)])
    return formated_number


def card_number_generator(start: int, stop: int) -> iter:
    """Генератор номера счета"""
    for number in range(start, stop + 1):
        yield format_number(number)
