import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card_number, mask_card_number", [
    (1234567890123456, '1234 56** **** 3456'),
    (0000000000000000, '0000 00** **** 0000')])
def test_get_mask_card_number(card_number, mask_card_number):
    """Проверяем что маска генирируется верно"""
    assert get_mask_card_number(card_number) == mask_card_number


@pytest.mark.parametrize("account_number, mask_account_number", [
    (12345678901234567890, '**7890'),
    (00000000000000000000, '**0000')])
def test_get_mask_card_number(account_number, mask_account_number):
    """Проверяем что маска генирируется верно"""
    assert get_mask_account(account_number) == mask_account_number
