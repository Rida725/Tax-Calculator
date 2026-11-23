import pytest

from tax_calculator import (
    taxable_income,
    tax,
    net_income
)


def test_taxable_income():
    assert taxable_income(200000) == 200000


def test_taxable_income_zero():
    assert taxable_income(0) == 0


def test_negative_income():
    with pytest.raises(ValueError):
        taxable_income(-100)


def test_tax_no_tax_below_limit():
    assert tax(200000) == 0


def test_tax_middle_slab():
    assert tax(600000) == 22500


def test_net_income():
    assert net_income(600000) == 577500
