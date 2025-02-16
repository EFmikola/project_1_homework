from datetime import datetime


def filter_by_state(dictionary_array: list, state: str = "EXECUTED") -> list:
    """Функция обработки списка словарей по статусу"""
    clear_dictionary_array = []
    for dictionary in dictionary_array:
        if dictionary["state"] == state:
            clear_dictionary_array.append(dictionary)
    return clear_dictionary_array


def sort_by_date(dictionary_array: list, sort_descending: bool = True) -> list:
    """Функция сортировки списка словарей по дате"""
    sorted_array = sorted(
        dictionary_array,
        key=lambda dict: datetime.strptime(dict["date"], "%Y-%m-%dT%H:%M:%S.%f"),
        reverse=sort_descending,
    )
    return sorted_array
