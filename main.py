from src import masks as masks
import src.widget as w
import src.processing as proc

print(masks.get_mask_card_number(1234567890123456))
print(masks.get_mask_account(73654108430135874305))
print(w.get_date("2024-03-11T02:26:18.671407"))

sorting_array = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
print(proc.filter_by_state(sorting_array))
