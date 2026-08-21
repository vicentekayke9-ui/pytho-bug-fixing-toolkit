import pytest

from main import calculate_total, process_order


def test_calculate_total():
    assert calculate_total(10, 3) == 30


def test_calculate_total_with_decimal():
    assert calculate_total(19.99, 3) == 59.97


def test_negative_price():
    with pytest.raises(ValueError):
        calculate_total(-10, 2)


def test_negative_quantity():
    with pytest.raises(ValueError):
        calculate_total(10, -2)


def test_process_order():
    order = {
        "price": 20,
        "quantity": 4
    }

    assert process_order(order) == 80


def test_missing_fields():
    with pytest.raises(ValueError):
        process_order({"price": 20})
