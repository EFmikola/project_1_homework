def filter_by_state(dictionary_array: list, state: str = "EXECUTED") -> list:
    """Функция обработки списка словарей по статусу"""
    clear_dictionary_array = []
    for dictionary in dictionary_array:
        if dictionary["state"] == state:
            clear_dictionary_array.append(dictionary)
    return clear_dictionary_array
