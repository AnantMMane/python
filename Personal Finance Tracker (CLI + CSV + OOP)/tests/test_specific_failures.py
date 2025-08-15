#!/usr/bin/env python3
"""
Test the specific failing test cases to verify they work correctly.
"""

import sys
import os
import tempfile
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.models.budget_manager import BudgetManager


def test_edit_category_validation():
    """Test the specific edit_category validation that was failing."""
    print("Testing edit_category validation...")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        manager = BudgetManager(data_dir=tmpdir)
        manager.add_category("TestFood", 100)  # Use unique name instead of 'Food'
        
        # Test empty new name
        try:
            manager.edit_category("Food", new_name="")
            assert False, "Empty new name should be rejected"
        except ValueError as e:
            assert "Category name must be non-empty" in str(e), f"Wrong error message: {e}"
            print("✅ PASS: Empty new name rejected")
        
        # Test negative budget limit
        try:
            manager.edit_category("Food", budget_limit=-200)
            assert False, "Negative budget limit should be rejected"
        except ValueError as e:
            assert "Budget limit cannot be negative" in str(e), f"Wrong error message: {e}"
            print("✅ PASS: Negative budget limit rejected")
        
        # Test valid edit
        result = manager.edit_category("Food", new_name="Groceries", budget_limit=200)
        assert result is True, "Valid edit should return True"
        assert "Groceries" in manager.categories, "Valid edit should update categories"
        print("✅ PASS: Valid edit successful")


def test_add_transaction_validation():
    """Test the specific add_transaction validation that was failing."""
    print("\nTesting add_transaction validation...")
    
    with tempfile.TemporaryDirectory() as tmpdir:
        manager = BudgetManager(data_dir=tmpdir)
        
        # Test non-positive amount
        try:
            manager.add_transaction(0, "expense", "Food")
            assert False, "Zero amount should be rejected"
        except ValueError as e:
            assert "Amount must be positive" in str(e), f"Wrong error message: {e}"
            print("✅ PASS: Zero amount rejected")
        
        # Test empty category
        try:
            manager.add_transaction(100, "expense", "")
            assert False, "Empty category should be rejected"
        except ValueError as e:
            expected_message = "Category must be specified"
            actual_message = str(e)
            print(f"DEBUG: Expected: '{expected_message}'")
            print(f"DEBUG: Actual: '{actual_message}'")
            assert expected_message in actual_message, f"Wrong error message. Expected: '{expected_message}', Got: '{actual_message}'"
            print("✅ PASS: Empty category rejected")
        
        # Test non-existent category
        try:
            manager.add_transaction(100, "expense", "NonExistentCategory")  # Use unique name
            assert False, "Non-existent category should be rejected"
        except ValueError as e:
            assert "does not exist" in str(e), f"Wrong error message: {e}"
            print("✅ PASS: Non-existent category rejected")
        
        # Test invalid transaction type (after adding category)
        manager.add_category("TestCategory", 100)  # Use unique name instead of 'Food'
        try:
            manager.add_transaction(100, "invalid", "TestCategory")  # Use the category we just added
            assert False, "Invalid transaction type should be rejected"
        except ValueError as e:
            assert "Transaction type must be" in str(e), f"Wrong error message: {e}"
            print("✅ PASS: Invalid transaction type rejected")
        
        # Test valid transaction
        transaction = manager.add_transaction(100, "expense", "Food")
        assert transaction.amount == 100, "Valid transaction should have correct amount"
        assert transaction.type == "expense", "Valid transaction should have correct type"
        assert transaction.category == "Food", "Valid transaction should have correct category"
        print("✅ PASS: Valid transaction added")


def main():
    """Run the specific failing tests."""
    print("Testing Specific Failing Test Cases")
    print("=" * 50)
    
    try:
        test_edit_category_validation()
        test_add_transaction_validation()
        print("\n" + "=" * 50)
        print("🎉 All specific tests passed!")
        return True
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return False
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 