import pytest
import tempfile
import os
from src.models.budget_manager import BudgetManager
from src.models.category import Category
from src.models.transaction import Transaction
from datetime import datetime


class TestCategoryValidation:
    """Test category validation logic."""
    
    def test_empty_category_name(self):
        """Test that empty category names are rejected."""
        with pytest.raises(ValueError, match="Category name must be non-empty"):
            Category("", 100)
        
        with pytest.raises(ValueError, match="Category name must be non-empty"):
            Category("   ", 100)
        
        with pytest.raises(ValueError, match="Category name must be non-empty"):
            Category("\t\n", 100)
    
    def test_valid_category_name(self):
        """Test that valid category names are accepted."""
        category = Category("Food", 100)
        assert category.name == "Food"
        assert category.budget_limit == 100
    
    def test_category_name_normalization(self):
        """Test that category names are normalized (trimmed)."""
        category = Category("  Food  ", 100)
        assert category.name == "Food"
    
    def test_negative_budget_limit(self):
        """Test that negative budget limits are rejected."""
        with pytest.raises(ValueError, match="Budget limit cannot be negative"):
            Category("Food", -100)
    
    def test_update_fields_validation(self):
        """Test validation in update_fields method."""
        category = Category("Food", 100)
        
        # Test empty name update
        with pytest.raises(ValueError, match="Category name must be non-empty"):
            category.update_fields(name="")
        
        # Test whitespace-only name update
        with pytest.raises(ValueError, match="Category name must be non-empty"):
            category.update_fields(name="   ")
        
        # Test valid name update
        category.update_fields(name="Groceries")
        assert category.name == "Groceries"


class TestTransactionValidation:
    """Test transaction validation logic."""
    
    def test_empty_category(self):
        """Test that empty categories are rejected."""
        with pytest.raises(ValueError, match="Category must be specified"):
            Transaction(100, "expense", "")
        
        with pytest.raises(ValueError, match="Category must be specified"):
            Transaction(100, "expense", "   ")
    
    def test_invalid_transaction_type(self):
        """Test that invalid transaction types are rejected."""
        with pytest.raises(ValueError, match="Transaction type must be 'income', 'expense', or 'transfer'"):
            Transaction(100, "invalid", "Food")  # type: ignore
    
    def test_non_positive_amount(self):
        """Test that non-positive amounts are rejected."""
        with pytest.raises(ValueError, match="Amount must be positive"):
            Transaction(0, "expense", "Food")
        
        with pytest.raises(ValueError, match="Amount must be positive"):
            Transaction(-100, "expense", "Food")
    
    def test_valid_transaction(self):
        """Test that valid transactions are accepted."""
        transaction = Transaction(100, "expense", "Food")
        assert transaction.amount == 100
        assert transaction.type == "expense"
        assert transaction.category == "Food"
    
    def test_category_normalization(self):
        """Test that category names are normalized."""
        transaction = Transaction(100, "expense", "  Food  ")
        assert transaction.category == "Food"
    
    def test_update_fields_validation(self):
        """Test validation in update_fields method."""
        transaction = Transaction(100, "expense", "Food")
        
        # Test empty category update
        with pytest.raises(ValueError, match="Category must be specified"):
            transaction.update_fields(category="")
        
        # Test non-positive amount update
        with pytest.raises(ValueError, match="Amount must be positive"):
            transaction.update_fields(amount=0)
        
        # Test invalid type update
        with pytest.raises(ValueError, match="Transaction type must be 'income', 'expense', or 'transfer'"):
            transaction.update_fields(type="invalid")


class TestBudgetManagerValidation:
    """Test budget manager validation logic."""
    
    def test_add_category_validation(self):
        """Test validation in add_category method."""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = BudgetManager(data_dir=tmpdir)

            # Test empty category name
            with pytest.raises(ValueError, match="Category name must be non-empty"):
                manager.add_category("", 100)

            # Test whitespace-only category name
            with pytest.raises(ValueError, match="Category name must be non-empty"):
                manager.add_category("   ", 100)

            # Test negative budget limit
            with pytest.raises(ValueError, match="Budget limit cannot be negative"):
                manager.add_category("TestFood", -100)  # Use unique name instead of 'Food'
            
            # Test valid category
            category = manager.add_category("TestCategory", 100)  # Use unique name instead of 'Food'
            assert category.name == "TestCategory"
            assert category.budget_limit == 100
    
    def test_edit_category_validation(self):
        """Test validation in edit_category method."""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = BudgetManager(data_dir=tmpdir)
            manager.add_category("TestFood", 100)  # Use unique name instead of 'Food'
            
            # Test empty new name
            with pytest.raises(ValueError, match="Category name must be non-empty"):
                manager.edit_category("Food", new_name="")
            
            # Test negative budget limit
            with pytest.raises(ValueError, match="Budget limit cannot be negative"):
                manager.edit_category("Food", budget_limit=-200)
            
            # Test valid edit
            result = manager.edit_category("Food", new_name="Groceries", budget_limit=200)
            assert result is True
            assert "Groceries" in manager.categories
            assert manager.categories["Groceries"].budget_limit == 200
    
    def test_add_transaction_validation(self):
        """Test validation in add_transaction method."""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = BudgetManager(data_dir=tmpdir)
            
            # Test non-positive amount
            with pytest.raises(ValueError, match="Amount must be positive"):
                manager.add_transaction(0, "expense", "Food")
            
            # Test empty category
            with pytest.raises(ValueError, match="Category must be specified"):
                manager.add_transaction(100, "expense", "")
            
            # Test non-existent category
            with pytest.raises(ValueError, match="Category 'NonExistentCategory' does not exist. Please create it first."):
                manager.add_transaction(100, "expense", "NonExistentCategory")  # Use unique name
            
            # Test invalid transaction type (after adding category)
            manager.add_category("TestCategory", 100)  # Use unique name instead of 'Food'
            with pytest.raises(ValueError, match="Transaction type must be 'income', 'expense', or 'transfer'"):
                manager.add_transaction(100, "invalid", "TestCategory")  # Use the category we just added
            
            # Test valid transaction
            transaction = manager.add_transaction(100, "expense", "TestCategory")  # Use the category we just added
            assert transaction.amount == 100
            assert transaction.type == "expense"
            assert transaction.category == "TestCategory"
    
    def test_edit_transaction_validation(self):
        """Test validation in edit_transaction method."""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = BudgetManager(data_dir=tmpdir)
            manager.add_category("TestFood", 100)  # Use unique name instead of 'Food'
            transaction = manager.add_transaction(100, "expense", "Food")
            
            # Test non-positive amount
            with pytest.raises(ValueError, match="Amount must be positive"):
                manager.edit_transaction(transaction.id, amount=0)
            
            # Test empty category
            with pytest.raises(ValueError, match="Category must be specified"):
                manager.edit_transaction(transaction.id, category="")
            
            # Test invalid transaction type
            with pytest.raises(ValueError, match="Transaction type must be 'income', 'expense', or 'transfer'"):
                manager.edit_transaction(transaction.id, type="invalid")
            
            # Test valid edit
            result = manager.edit_transaction(transaction.id, amount=200, category="Food")
            assert result is True
            updated_transaction = manager.get_transaction_by_id(transaction.id)
            assert updated_transaction is not None
            assert updated_transaction.amount == 200


class TestInputNormalization:
    """Test that input is properly normalized."""
    
    def test_category_name_normalization(self):
        """Test that category names are properly normalized."""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = BudgetManager(data_dir=tmpdir)

            # Test whitespace normalization
            category = manager.add_category("  TestFood  ", 100)  # Use unique name instead of 'Food'
            assert category.name == "TestFood"
            
            # Test that normalized name is used in lookup
            assert "TestFood" in manager.categories
            assert "  TestFood  " not in manager.categories
    
    def test_transaction_category_normalization(self):
        """Test that transaction categories are properly normalized."""
        with tempfile.TemporaryDirectory() as tmpdir:
            manager = BudgetManager(data_dir=tmpdir)
            manager.add_category("TestFood", 100)  # Use unique name instead of 'Food'
            
            # Test whitespace normalization
            transaction = manager.add_transaction(100, "expense", "  Food  ")
            assert transaction.category == "Food"
            
            # Test that normalized category is used in filtering
            transactions = manager.get_transactions(category_filter="Food")
            assert len(transactions) == 1
            assert transactions[0].category == "Food"


if __name__ == "__main__":
    pytest.main([__file__]) 