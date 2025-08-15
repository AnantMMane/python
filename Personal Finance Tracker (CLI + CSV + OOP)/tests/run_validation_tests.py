#!/usr/bin/env python3
"""
Run validation tests and show results.
This script tests the validation logic without requiring pytest.
"""

import sys
import os
import tempfile
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.models.budget_manager import BudgetManager
from src.models.transaction import Transaction
from src.models.category import Category


def test_all_validation():
    """Run all validation tests and report results."""
    print("Running Comprehensive Validation Tests...")
    print("=" * 60)
    
    passed = 0
    failed = 0
    
    # Test 1: Category validation
    print("\n1. Testing Category Validation:")
    
    # Empty category name
    try:
        Category("", 100)
        print("❌ FAIL: Empty category name should be rejected")
        failed += 1
    except ValueError as e:
        if "Category name must be non-empty" in str(e):
            print("✅ PASS: Empty category name rejected")
            passed += 1
        else:
            print(f"❌ FAIL: Wrong error message: {e}")
            failed += 1
    
    # Whitespace-only category name
    try:
        Category("   ", 100)
        print("❌ FAIL: Whitespace-only category name should be rejected")
        failed += 1
    except ValueError as e:
        if "Category name must be non-empty" in str(e):
            print("✅ PASS: Whitespace-only category name rejected")
            passed += 1
        else:
            print(f"❌ FAIL: Wrong error message: {e}")
            failed += 1
    
    # Negative budget limit
    try:
        Category("Food", -100)
        print("❌ FAIL: Negative budget limit should be rejected")
        failed += 1
    except ValueError as e:
        if "Budget limit cannot be negative" in str(e):
            print("✅ PASS: Negative budget limit rejected")
            passed += 1
        else:
            print(f"❌ FAIL: Wrong error message: {e}")
            failed += 1
    
    # Valid category
    try:
        category = Category("Food", 100)
        print("✅ PASS: Valid category accepted")
        passed += 1
    except Exception as e:
        print(f"❌ FAIL: Valid category should be accepted: {e}")
        failed += 1
    
    # Test 2: Transaction validation
    print("\n2. Testing Transaction Validation:")
    
    # Empty category
    try:
        Transaction(100, "expense", "")  # type: ignore
        print("❌ FAIL: Empty category should be rejected")
        failed += 1
    except ValueError as e:
        if "Category must be specified" in str(e):
            print("✅ PASS: Empty category rejected")
            passed += 1
        else:
            print(f"❌ FAIL: Wrong error message: {e}")
            failed += 1
    
    # Invalid transaction type
    try:
        Transaction(100, "invalid", "Food")  # type: ignore
        print("❌ FAIL: Invalid transaction type should be rejected")
        failed += 1
    except ValueError as e:
        if "Transaction type must be 'income', 'expense', or 'transfer'" in str(e):
            print("✅ PASS: Invalid transaction type rejected")
            passed += 1
        else:
            print(f"❌ FAIL: Wrong error message: {e}")
            failed += 1
    
    # Non-positive amount
    try:
        Transaction(0, "expense", "Food")
        print("❌ FAIL: Zero amount should be rejected")
        failed += 1
    except ValueError as e:
        if "Amount must be positive" in str(e):
            print("✅ PASS: Zero amount rejected")
            passed += 1
        else:
            print(f"❌ FAIL: Wrong error message: {e}")
            failed += 1
    
    # Valid transaction
    try:
        transaction = Transaction(100, "expense", "Food")
        print("✅ PASS: Valid transaction accepted")
        passed += 1
    except Exception as e:
        print(f"❌ FAIL: Valid transaction should be accepted: {e}")
        failed += 1
    
    # Test 3: Budget Manager validation
    print("\n3. Testing Budget Manager Validation:")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        manager = BudgetManager(data_dir=tmpdir)
        
        # Empty category name in add_category
        try:
            manager.add_category("", 100)
            print("❌ FAIL: Empty category name should be rejected")
            failed += 1
        except ValueError as e:
            if "Category name must be non-empty" in str(e):
                print("✅ PASS: Empty category name rejected in add_category")
                passed += 1
            else:
                print(f"❌ FAIL: Wrong error message: {e}")
                failed += 1
        
        # Negative budget limit in add_category
        try:
            manager.add_category("Food", -100)
            print("❌ FAIL: Negative budget limit should be rejected")
            failed += 1
        except ValueError as e:
            if "Budget limit cannot be negative" in str(e):
                print("✅ PASS: Negative budget limit rejected in add_category")
                passed += 1
            else:
                print(f"❌ FAIL: Wrong error message: {e}")
                failed += 1
        
        # Valid category addition
        try:
            category = manager.add_category("Food", 100)
            print("✅ PASS: Valid category added")
            passed += 1
        except Exception as e:
            print(f"❌ FAIL: Valid category should be added: {e}")
            failed += 1
        
        # Non-positive amount in add_transaction
        try:
            manager.add_transaction(0, "expense", "Food")
            print("❌ FAIL: Zero amount should be rejected")
            failed += 1
        except ValueError as e:
            if "Amount must be positive" in str(e):
                print("✅ PASS: Zero amount rejected in add_transaction")
                passed += 1
            else:
                print(f"❌ FAIL: Wrong error message: {e}")
                failed += 1
        
        # Empty category in add_transaction
        try:
            manager.add_transaction(100, "expense", "")
            print("❌ FAIL: Empty category should be rejected")
            failed += 1
        except ValueError as e:
            if "Category must be specified" in str(e):
                print("✅ PASS: Empty category rejected in add_transaction")
                passed += 1
            else:
                print(f"❌ FAIL: Wrong error message: {e}")
                failed += 1
        
        # Non-existent category
        try:
            manager.add_transaction(100, "expense", "NonExistent")
            print("❌ FAIL: Non-existent category should be rejected")
            failed += 1
        except ValueError as e:
            if "Category 'NonExistent' does not exist. Please create it first." in str(e):
                print("✅ PASS: Non-existent category rejected")
                passed += 1
            else:
                print(f"❌ FAIL: Wrong error message: {e}")
                failed += 1
        
        # Valid transaction addition
        try:
            transaction = manager.add_transaction(100, "expense", "Food")
            print("✅ PASS: Valid transaction added")
            passed += 1
        except Exception as e:
            print(f"❌ FAIL: Valid transaction should be added: {e}")
            failed += 1
    
    # Test 4: Input normalization
    print("\n4. Testing Input Normalization:")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        manager = BudgetManager(data_dir=tmpdir)
        
        # Category name normalization
        try:
            category = manager.add_category("  Food  ", 100)
            if category.name == "Food":
                print("✅ PASS: Category name normalized")
                passed += 1
            else:
                print(f"❌ FAIL: Category name not normalized: {category.name}")
                failed += 1
        except Exception as e:
            print(f"❌ FAIL: Category normalization failed: {e}")
            failed += 1
        
        # Transaction category normalization
        try:
            transaction = manager.add_transaction(100, "expense", "  Food  ")
            if transaction.category == "Food":
                print("✅ PASS: Transaction category normalized")
                passed += 1
            else:
                print(f"❌ FAIL: Transaction category not normalized: {transaction.category}")
                failed += 1
        except Exception as e:
            print(f"❌ FAIL: Transaction normalization failed: {e}")
            failed += 1
    
    # Summary
    print("\n" + "=" * 60)
    print(f"TEST SUMMARY:")
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    print(f"📊 Total: {passed + failed}")
    
    if failed == 0:
        print("🎉 All validation tests passed!")
        return True
    else:
        print("⚠️  Some validation tests failed.")
        return False


if __name__ == "__main__":
    success = test_all_validation()
    sys.exit(0 if success else 1) 