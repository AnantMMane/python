import pytest
import os
import tempfile
from src.models.transaction import Transaction
from src.models.category import Category
from src.utils import csv_handler
from datetime import datetime

def test_write_and_read_transactions():
    t1 = Transaction(100, 'income', 'Salary', 'Pay', datetime(2023, 1, 1))
    t2 = Transaction(50, 'expense', 'Food', 'Lunch', datetime(2023, 1, 2))
    with tempfile.NamedTemporaryFile(suffix='.enc', delete=False) as tmp:
        csv_handler.write_transactions(tmp.name, [t1, t2])
        txns = csv_handler.read_transactions(tmp.name)
        assert len(txns) == 2
        assert txns[0].amount == 100
        assert txns[1].type == 'expense'
    os.remove(tmp.name)

def test_write_and_read_categories():
    c1 = Category('Food', 500)
    c2 = Category('Rent', 1000)
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        csv_handler.write_categories(tmp.name, [c1, c2])
        cats = csv_handler.read_categories(tmp.name)
        assert len(cats) == 2
        assert cats[0].name == 'Food'
        assert cats[1].budget_limit == 1000
    os.remove(tmp.name) 