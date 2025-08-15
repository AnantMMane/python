import pytest
from datetime import datetime
from src.models.transaction import Transaction

def test_transaction_creation():
    t = Transaction(1000, 'income', 'Salary', 'Test income', datetime(2023, 1, 1), 'INR')
    assert t.amount == 1000
    assert t.type == 'income'
    assert t.category == 'Salary'
    assert t.description == 'Test income'
    assert t.currency == 'INR'
    assert isinstance(t.id, str)
    assert isinstance(t.date, datetime)

def test_transaction_to_dict_and_from_dict():
    t = Transaction(500, 'expense', 'Food', 'Lunch', datetime(2023, 2, 2), 'INR')
    d = t.to_dict()
    t2 = Transaction.from_dict(d)
    assert t2.amount == t.amount
    assert t2.type == t.type
    assert t2.category == t.category
    assert t2.description == t.description
    assert t2.currency == t.currency
    assert t2.date == t.date

def test_transaction_update_fields():
    t = Transaction(100, 'expense', 'Food')
    t.update_fields(amount=200, type='income', category='Salary', description='Updated', currency='USD')
    assert t.amount == 200
    assert t.type == 'income'
    assert t.category == 'Salary'
    assert t.description == 'Updated'
    assert t.currency == 'USD' 