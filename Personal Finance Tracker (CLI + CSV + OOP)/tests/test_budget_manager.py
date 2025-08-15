import pytest
import os
import tempfile
from datetime import datetime
from src.models.budget_manager import BudgetManager

def test_add_and_get_transaction():
    with tempfile.TemporaryDirectory() as tmpdir:
        manager = BudgetManager(data_dir=tmpdir)
        manager.add_category('TestCat')
        t = manager.add_transaction(100, 'income', 'TestCat', 'Test', datetime(2023, 1, 1))
        assert t in manager.get_transactions()
        assert manager.get_transaction_by_id(t.id) == t

def test_edit_and_delete_transaction():
    with tempfile.TemporaryDirectory() as tmpdir:
        manager = BudgetManager(data_dir=tmpdir)
        manager.add_category('TestCat')
        t = manager.add_transaction(200, 'expense', 'TestCat')
        manager.edit_transaction(t.id, amount=300, type='income', category='TestCat', description='Updated')
        t2 = manager.get_transaction_by_id(t.id)
        assert t2 is not None
        assert t2.amount == 300
        assert t2.type == 'income'
        assert t2.description == 'Updated'
        assert manager.delete_transaction(t.id)
        assert manager.get_transaction_by_id(t.id) is None

def test_add_edit_delete_category():
    with tempfile.TemporaryDirectory() as tmpdir:
        manager = BudgetManager(data_dir=tmpdir)
        c = manager.add_category('TestCat', 1000)
        assert c.name == 'TestCat'
        assert c.budget_limit == 1000
        manager.edit_category('TestCat', new_name='TestCat2', budget_limit=2000)
        assert 'TestCat2' in manager.categories
        assert manager.categories['TestCat2'].budget_limit == 2000
        assert manager.delete_category('TestCat2')
        assert 'TestCat2' not in manager.categories

def test_summary_and_alerts():
    with tempfile.TemporaryDirectory() as tmpdir:
        manager = BudgetManager(data_dir=tmpdir)
        manager.add_category('TestFood', 100)  # Use unique name instead of 'Food'
        manager.add_transaction(50, 'expense', 'TestFood', date=datetime(2023, 1, 1))  # Use the category we added
        manager.add_transaction(60, 'expense', 'TestFood', date=datetime(2023, 1, 2))  # Use the category we added
        summary = manager.get_monthly_summary(2023, 1)
        assert summary['total_expenses'] == 110
        alerts = manager.check_budget_alerts(2023, 1)
        assert any('exceeded' in a for a in alerts) 