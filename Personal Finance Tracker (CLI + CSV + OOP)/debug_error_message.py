#!/usr/bin/env python3
"""
Debug script to see the exact error message being generated.
"""

import sys
import os
import tempfile
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.models.budget_manager import BudgetManager


def debug_error_messages():
    """Debug the exact error messages being generated."""
    print("Debugging Error Messages...")
    print("=" * 40)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        manager = BudgetManager(data_dir=tmpdir)
        
        # Test 1: Non-positive amount
        try:
            manager.add_transaction(0, "expense", "Food")
        except ValueError as e:
            print(f"1. Non-positive amount error: '{e}'")
            print(f"   Length: {len(str(e))}")
            print(f"   Bytes: {str(e).encode('utf-8')}")
        
        # Test 2: Empty category
        try:
            manager.add_transaction(100, "expense", "")
        except ValueError as e:
            print(f"2. Empty category error: '{e}'")
            print(f"   Length: {len(str(e))}")
            print(f"   Bytes: {str(e).encode('utf-8')}")
        
        # Test 3: Invalid transaction type (with existing category)
        manager.add_category("Food", 100)  # Add category first
        try:
            manager.add_transaction(100, "invalid", "Food")
        except ValueError as e:
            print(f"3. Invalid transaction type error: '{e}'")
            print(f"   Length: {len(str(e))}")
            print(f"   Bytes: {str(e).encode('utf-8')}")
        
        # Test 4: Non-existent category
        try:
            manager.add_transaction(100, "expense", "NonExistent")
        except ValueError as e:
            print(f"4. Non-existent category error: '{e}'")
            print(f"   Length: {len(str(e))}")
            print(f"   Bytes: {str(e).encode('utf-8')}")
            
            # Check against expected pattern
            expected = "Category 'NonExistent' does not exist. Please create it first."
            print(f"   Expected: '{expected}'")
            print(f"   Expected length: {len(expected)}")
            print(f"   Match: {str(e) == expected}")
            print(f"   Contains: {expected in str(e)}")


if __name__ == "__main__":
    debug_error_messages() 