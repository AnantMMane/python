import pytest
from src.models.category import Category

def test_category_creation():
    c = Category('Food', 5000)
    assert c.name == 'Food'
    assert c.budget_limit == 5000
    assert not c.is_predefined

def test_category_to_dict_and_from_dict():
    c = Category('Rent', 10000, is_predefined=True)
    d = c.to_dict()
    c2 = Category.from_dict(d)
    assert c2.name == c.name
    assert c2.budget_limit == c.budget_limit
    assert c2.is_predefined == c.is_predefined

def test_category_update_fields():
    c = Category('Misc')
    c.update_fields(name='Miscellaneous', budget_limit=2000)
    assert c.name == 'Miscellaneous'
    assert c.budget_limit == 2000 