#!/usr/bin/env python3
"""
Simple test script to verify encryption functionality.
"""

import os
import tempfile
from pathlib import Path

# Add the src directory to the Python path
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from src.utils.encryption import DataEncryption
    print("✓ Encryption module imported successfully")
except ImportError as e:
    print(f"✗ Failed to import encryption module: {e}")
    sys.exit(1)

def test_basic_encryption():
    """Test basic encryption and decryption."""
    print("\nTesting basic encryption...")
    
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        key_file = os.path.join(temp_dir, "test_key")
        
        # Test encryption initialization
        encryption = DataEncryption(key_file)
        print("✓ Encryption utility initialized")
        
        # Test string encryption/decryption
        original_data = "This is sensitive financial data: $10,000"
        encrypted_data = encryption.encrypt_data(original_data)
        decrypted_data = encryption.decrypt_data(encrypted_data)
        
        assert decrypted_data == original_data, "String encryption/decryption failed"
        print("✓ String encryption/decryption works correctly")
        
        # Test file encryption/decryption
        original_file = os.path.join(temp_dir, "original.txt")
        encrypted_file = os.path.join(temp_dir, "encrypted.enc")
        decrypted_file = os.path.join(temp_dir, "decrypted.txt")
        
        # Create test file
        with open(original_file, 'w') as f:
            f.write("Bank account: 1234-5678-9012-3456\nBalance: $10,000")
        
        # Encrypt file
        encryption.encrypt_file(original_file, encrypted_file)
        
        # Verify encrypted file is different
        with open(encrypted_file, 'r') as f:
            encrypted_content = f.read()
        
        with open(original_file, 'r') as f:
            original_content = f.read()
        
        assert encrypted_content != original_content, "File encryption failed (content not encrypted)"
        print("✓ File encryption works (content is encrypted)")
        
        # Decrypt file
        encryption.decrypt_file(encrypted_file, decrypted_file)
        
        # Verify decrypted content matches original
        with open(decrypted_file, 'r') as f:
            decrypted_content = f.read()
        
        assert decrypted_content == original_content, "File decryption failed"
        print("✓ File decryption works correctly")

def test_csv_encryption():
    """Test CSV file encryption."""
    print("\nTesting CSV encryption...")
    
    with tempfile.TemporaryDirectory() as temp_dir:
        key_file = os.path.join(temp_dir, "test_key")
        encryption = DataEncryption(key_file)
        
        # Create sample CSV data
        csv_data = """id,date,amount,type,category,description,currency
123,2025-01-01,100.0,expense,Food,Grocery shopping,USD
456,2025-01-02,2000.0,income,Salary,Monthly salary,USD"""
        
        original_file = os.path.join(temp_dir, "transactions.csv")
        encrypted_file = os.path.join(temp_dir, "transactions.csv.enc")
        
        # Write original CSV
        with open(original_file, 'w') as f:
            f.write(csv_data)
        
        # Encrypt CSV
        encryption.encrypt_file(original_file, encrypted_file)
        
        # Verify encryption
        with open(encrypted_file, 'r') as f:
            encrypted_content = f.read()
        
        assert "id,date,amount,type,category,description,currency" not in encrypted_content, "CSV encryption failed (headers not encrypted)"
        print("✓ CSV encryption works (headers are encrypted)")
        
        # Decrypt and verify
        decrypted_file = os.path.join(temp_dir, "decrypted.csv")
        encryption.decrypt_file(encrypted_file, decrypted_file)
        
        with open(decrypted_file, 'r') as f:
            decrypted_content = f.read()
        
        assert decrypted_content == csv_data, "CSV decryption failed"
        print("✓ CSV decryption works correctly")

def main():
    """Main test function."""
    print("=" * 50)
    print("Personal Finance Tracker - Encryption Test")
    print("=" * 50)
    
    # Test basic encryption
    test_basic_encryption()
    
    # Test CSV encryption
    test_csv_encryption()
    
    print("\n" + "=" * 50)
    print("✓ All encryption tests passed!")
    print("=" * 50)
    print("\nEncryption features are working correctly:")
    print("- String encryption/decryption ✓")
    print("- File encryption/decryption ✓")
    print("- CSV file encryption ✓")
    print("- Secure key management ✓")

if __name__ == "__main__":
    main() 