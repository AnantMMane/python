#!/usr/bin/env python3
"""
Simple validation test script for the Personal Finance Tracker.
Tests all the validation logic without requiring pytest.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.models.budget_manager import BudgetManager
from src.models.transaction import Transaction
from src.models.category import Category
from datetime import datetime


def test_category_validation():
    """Test category validation logic."""
    print("Testing Category Validation...")
    
    # Test empty category name
    try:
        Category("", 100)
        print("❌ FAIL: Empty category name should be rejected")
    except ValueError as e:
        if "Category name must be non-empty" in str(e):
            print("✅ PASS: Empty category name rejected")
        else:
            print(f"❌ FAIL: Wrong error message: {e}")
    
    # Test whitespace-only category name
    try:
        Category("   ", 100)
        print("❌ FAIL: Whitespace-only category name should be rejected")
    except ValueError as e:
        if "Category name must be non-empty" in str(e):
            print("✅ PASS: Whitespace-only category name rejected")
        else:
            print(f"❌ FAIL: Wrong error message: {e}")
    
    # Test valid category name
    try:
        category = Category("Food", 100)
        print("✅ PASS: Valid category name accepted")
        assert category.name == "Food"
        assert category.budget_limit == 100
    except Exception as e:
        print(f"❌ FAIL: Valid category should be accepted: {e}")
    
    # Test category name normalization
    try:
        category = Category("  Food  ", 100)
        print("✅ PASS: Category name normalized (trimmed)")
        assert category.name == "Food"
    except Exception as e:
        print(f"❌ FAIL: Category name should be normalized: {e}")
    
    # Test negative budget limit
    try:
        Category("Food", -100)
        print("❌ FAIL: Negative budget limit should be rejected")
    except ValueError as e:
        if "Budget limit cannot be negative" in str(e):
            print("✅ PASS: Negative budget limit rejected")
        else:
            print(f"❌ FAIL: Wrong error message: {e}")


def test_transaction_validation():
    """Test transaction validation logic."""
    print("\nTesting Transaction Validation...")
    
    # Test empty category
    try:
        Transaction(100, "expense", "")
        print("❌ FAIL: Empty category should be rejected")
    except ValueError as e:
        if "Category must be specified" in str(e):
            print("✅ PASS: Empty category rejected")
        else:
            print(f"❌ FAIL: Wrong error message: {e}")
    
    # Test invalid transaction type
    try:
        Transaction(100, "invalid", "Food")  # type: ignore
        print("❌ FAIL: Invalid transaction type should be rejected")
    except ValueError as e:
        if "Transaction type must be 'income', 'expense', or 'transfer'" in str(e):
            print("✅ PASS: Invalid transaction type rejected")
        else:
            print(f"❌ FAIL: Wrong error message: {e}")
    
    # Test non-positive amount
    try:
        Transaction(0, "expense", "Food")
        print("❌ FAIL: Zero amount should be rejected")
    except ValueError as e:
        if "Amount must be positive" in str(e):
            print("✅ PASS: Zero amount rejected")
        else:
            print(f"❌ FAIL: Wrong error message: {e}")
    
    try:
        Transaction(-100, "expense", "Food")
        print("❌ FAIL: Negative amount should be rejected")
    except ValueError as e:
        if "Amount must be positive" in str(e):
            print("✅ PASS: Negative amount rejected")
        else:
            print(f"❌ FAIL: Wrong error message: {e}")
    
    # Test valid transaction
    try:
        transaction = Transaction(100, "expense", "Food")
        print("✅ PASS: Valid transaction accepted")
        assert transaction.amount == 100
        assert transaction.type == "expense"
        assert transaction.category == "Food"
    except Exception as e:
        print(f"❌ FAIL: Valid transaction should be accepted: {e}")
    
    # Test category normalization
    try:
        transaction = Transaction(100, "expense", "  Food  ")
        print("✅ PASS: Transaction category normalized")
        assert transaction.category == "Food"
    except Exception as e:
        print(f"❌ FAIL: Transaction category should be normalized: {e}")


def test_budget_manager_validation():
    """Test budget manager validation logic."""
    print("\nTesting Budget Manager Validation...")
    
    import tempfile
    
    with tempfile.TemporaryDirectory() as tmpdir:
        manager = BudgetManager(data_dir=tmpdir)
        
        # Test empty category name in add_category
        try:
            manager.add_category("", 100)
            print("❌ FAIL: Empty category name should be rejected")
        except ValueError as e:
            if "Category name must be non-empty" in str(e):
                print("✅ PASS: Empty category name rejected in add_category")
            else:
                print(f"❌ FAIL: Wrong error message: {e}")
        
        # Test negative budget limit in add_category
        try:
            manager.add_category("Food", -100)
            print("❌ FAIL: Negative budget limit should be rejected")
        except ValueError as e:
            if "Budget limit cannot be negative" in str(e):
                print("✅ PASS: Negative budget limit rejected in add_category")
            else:
                print(f"❌ FAIL: Wrong error message: {e}")
        
        # Test valid category addition
        try:
            category = manager.add_category("Food", 100)
            print("✅ PASS: Valid category added")
            assert category.name == "Food"
            assert category.budget_limit == 100
        except Exception as e:
            print(f"❌ FAIL: Valid category should be added: {e}")
        
        # Test non-positive amount in add_transaction
        try:
            manager.add_transaction(0, "expense", "Food")
            print("❌ FAIL: Zero amount should be rejected")
        except ValueError as e:
            if "Amount must be positive" in str(e):
                print("✅ PASS: Zero amount rejected in add_transaction")
            else:
                print(f"❌ FAIL: Wrong error message: {e}")
        
        # Test empty category in add_transaction
        try:
            manager.add_transaction(100, "expense", "")
            print("❌ FAIL: Empty category should be rejected")
        except ValueError as e:
            if "Category must be specified" in str(e):
                print("✅ PASS: Empty category rejected in add_transaction")
            else:
                print(f"❌ FAIL: Wrong error message: {e}")
        
        # Test valid transaction addition
        try:
            transaction = manager.add_transaction(100, "expense", "Food")
            print("✅ PASS: Valid transaction added")
            assert transaction.amount == 100
            assert transaction.type == "expense"
            assert transaction.category == "Food"
        except Exception as e:
            print(f"❌ FAIL: Valid transaction should be added: {e}")


def test_input_normalization():
    """Test that input is properly normalized."""
    print("\nTesting Input Normalization...")
    
    import tempfile
    
    with tempfile.TemporaryDirectory() as tmpdir:
        manager = BudgetManager(data_dir=tmpdir)
        
        # Test category name normalization
        try:
            category = manager.add_category("  Food  ", 100)
            print("✅ PASS: Category name normalized in add_category")
            assert category.name == "Food"
            assert "Food" in manager.categories
            assert "  Food  " not in manager.categories
        except Exception as e:
            print(f"❌ FAIL: Category name should be normalized: {e}")
        
        # Test transaction category normalization
        try:
            transaction = manager.add_transaction(100, "expense", "  Food  ")
            print("✅ PASS: Transaction category normalized")
            assert transaction.category == "Food"
            
            # Test that normalized category is used in filtering
            transactions = manager.get_transactions(category_filter="Food")
            assert len(transactions) == 1
            assert transactions[0].category == "Food"
            print("✅ PASS: Normalized category used in filtering")
        except Exception as e:
            print(f"❌ FAIL: Transaction category should be normalized: {e}")


def main():
    """Run all validation tests."""
    print("Personal Finance Tracker - Validation Tests")
    print("=" * 50)
    
    test_category_validation()
    test_transaction_validation()
    test_budget_manager_validation()
    test_input_normalization()
    
    print("\n" + "=" * 50)
    print("Validation tests completed!")


if __name__ == "__main__":
    main() 