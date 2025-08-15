#!/usr/bin/env python3
"""
Test script for the Personal Finance Tracker models.
"""

import sys
import os
import tempfile

from src.models.budget_manager import BudgetManager
from src.models.transaction import Transaction
from src.models.category import Category
from datetime import datetime, date


def test_basic_functionality():
    """Test basic functionality of the models."""
    print("Testing Personal Finance Tracker Models...")
    print("=" * 50)
    
    # Use a temporary directory for all data
    with tempfile.TemporaryDirectory() as tmpdir:
        # Initialize budget manager
        manager = BudgetManager(data_dir=tmpdir)
        
        # Test categories
        print("\n1. Testing Categories:")
        categories = manager.get_categories()
        print(f"Found {len(categories)} categories:")
        for category in categories[:5]:  # Show first 5
            print(f"  - {category}")
        
        # Test adding a transaction
        print("\n2. Testing Transaction Addition:")
        try:
            transaction = manager.add_transaction(
                amount=1500.0,
                type="expense",
                category="Food",
                description="Grocery shopping"
            )
            print(f"Added transaction: {transaction}")
        except Exception as e:
            print(f"Error adding transaction: {e}")
        
        # Test adding income
        print("\n3. Testing Income Addition:")
        try:
            income = manager.add_transaction(
                amount=50000.0,
                type="income",
                category="Salary",
                description="Monthly salary"
            )
            print(f"Added income: {income}")
        except Exception as e:
            print(f"Error adding income: {e}")
        
        # Test getting transactions
        print("\n4. Testing Transaction Retrieval:")
        transactions = manager.get_transactions()
        print(f"Total transactions: {len(transactions)}")
        for transaction in transactions:
            print(f"  - {transaction}")
        
        # Test summary
        print("\n5. Testing Summary:")
        summary = manager.get_summary()
        print(f"Total Income: ₹{summary['total_income']:.2f}")
        print(f"Total Expenses: ₹{summary['total_expenses']:.2f}")
        print(f"Net Amount: ₹{summary['net_amount']:.2f}")
        print(f"Transaction Count: {summary['transaction_count']}")
        
        # Test category breakdown
        print("\n6. Testing Category Breakdown:")
        for category, amounts in summary['category_breakdown'].items():
            print(f"  {category}:")
            for type_name, amount in amounts.items():
                if amount > 0:
                    print(f"    {type_name}: ₹{amount:.2f}")
        
        # Test adding custom category
        print("\n7. Testing Custom Category:")
        try:
            custom_category = manager.add_category("Gym Membership", 2000.0)
            print(f"Added custom category: {custom_category}")
        except Exception as e:
            print(f"Error adding custom category: {e}")
        
        print("\n" + "=" * 50)
        print("Basic functionality test completed!")


if __name__ == "__main__":
    test_basic_functionality() 