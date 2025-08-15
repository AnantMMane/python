import pytest
import tempfile
import os
import json
from pathlib import Path
from src.utils.encryption import DataEncryption, get_encryption


class TestDataEncryption:
    """Test cases for the DataEncryption class."""
    
    def test_encryption_initialization(self, tmp_path):
        """Test encryption utility initialization."""
        key_file = tmp_path / "test_key"
        encryption = DataEncryption(str(key_file))
        
        assert encryption.key_file == key_file
        assert len(encryption.key) == 44  # Fernet key length
        assert encryption.cipher_suite is not None
    
    def test_key_generation_and_loading(self, tmp_path):
        """Test key generation and loading."""
        key_file = tmp_path / "test_key"
        
        # First initialization should generate a key
        encryption1 = DataEncryption(str(key_file))
        key1 = encryption1.key
        
        # Second initialization should load the same key
        encryption2 = DataEncryption(str(key_file))
        key2 = encryption2.key
        
        assert key1 == key2
        assert key_file.exists()
    
    def test_encrypt_decrypt_string(self, tmp_path):
        """Test basic string encryption and decryption."""
        key_file = tmp_path / "test_key"
        encryption = DataEncryption(str(key_file))
        
        original_data = "This is sensitive financial data"
        encrypted_data = encryption.encrypt_data(original_data)
        decrypted_data = encryption.decrypt_data(encrypted_data)
        
        assert decrypted_data == original_data
        assert encrypted_data != original_data
    
    def test_encrypt_decrypt_json(self, tmp_path):
        """Test JSON encryption and decryption."""
        key_file = tmp_path / "test_key"
        encryption = DataEncryption(str(key_file))
        
        original_data = {
            "transactions": [
                {"id": "123", "amount": 100.0, "category": "Food"},
                {"id": "456", "amount": 200.0, "category": "Transport"}
            ],
            "metadata": {"version": "1.0", "encrypted": True}
        }
        
        encrypted_data = encryption.encrypt_json(original_data)
        decrypted_data = encryption.decrypt_json(encrypted_data)
        
        assert decrypted_data == original_data
        assert encrypted_data != json.dumps(original_data)
    
    def test_file_encryption_decryption(self, tmp_path):
        """Test file encryption and decryption."""
        key_file = tmp_path / "test_key"
        encryption = DataEncryption(str(key_file))
        
        # Create test file
        original_file = tmp_path / "original.txt"
        encrypted_file = tmp_path / "encrypted.enc"
        decrypted_file = tmp_path / "decrypted.txt"
        
        original_content = "Sensitive transaction data\nLine 2\nLine 3"
        original_file.write_text(original_content)
        
        # Encrypt file
        encryption.encrypt_file(str(original_file), str(encrypted_file))
        
        # Verify encrypted file is different
        encrypted_content = encrypted_file.read_text()
        assert encrypted_content != original_content
        
        # Decrypt file
        encryption.decrypt_file(str(encrypted_file), str(decrypted_file))
        
        # Verify decrypted content matches original
        decrypted_content = decrypted_file.read_text()
        assert decrypted_content == original_content
    
    def test_decrypt_invalid_data(self, tmp_path):
        """Test decryption with invalid data."""
        key_file = tmp_path / "test_key"
        encryption = DataEncryption(str(key_file))
        
        with pytest.raises(ValueError):
            encryption.decrypt_data("invalid_encrypted_data")
    
    def test_key_backup_restore(self, tmp_path):
        """Test key backup and restore functionality."""
        key_file = tmp_path / "test_key"
        backup_file = tmp_path / "backup_key"
        
        # Create encryption instance
        encryption1 = DataEncryption(str(key_file))
        original_key = encryption1.key
        
        # Backup key
        encryption1.backup_key(str(backup_file))
        assert backup_file.exists()
        
        # Create new encryption instance with different key
        key_file2 = tmp_path / "test_key2"
        encryption2 = DataEncryption(str(key_file2))
        different_key = encryption2.key
        
        assert original_key != different_key
        
        # Restore key
        encryption2.restore_key(str(backup_file))
        restored_key = encryption2.key
        
        assert restored_key == original_key
    
    def test_derive_key_from_password(self, tmp_path):
        """Test password-based key derivation."""
        key_file = tmp_path / "test_key"
        encryption = DataEncryption(str(key_file))
        
        password = "my_secure_password"
        key1, salt1 = encryption.derive_key_from_password(password)
        key2, salt2 = encryption.derive_key_from_password(password, salt1)
        
        assert key1 == key2
        assert salt1 == salt2
        
        # Different password should produce different key
        key3, salt3 = encryption.derive_key_from_password("different_password", salt1)
        assert key1 != key3


class TestGlobalEncryption:
    """Test cases for global encryption functions."""
    
    def test_get_encryption_singleton(self):
        """Test that get_encryption returns the same instance."""
        encryption1 = get_encryption()
        encryption2 = get_encryption()
        
        assert encryption1 is encryption2
    
    def test_encrypt_transactions_file(self, tmp_path):
        """Test transaction file encryption."""
        # Create sample transaction data
        transaction_data = """id,date,amount,type,category,description,currency
123,2025-01-01,100.0,expense,Food,Grocery,USD
456,2025-01-02,200.0,income,Salary,Monthly salary,USD"""
        
        input_file = tmp_path / "transactions.csv"
        output_file = tmp_path / "transactions.csv.enc"
        
        input_file.write_text(transaction_data)
        
        # Import the function
        from src.utils.encryption import encrypt_transactions_file
        
        # Encrypt the file
        encrypt_transactions_file(str(input_file), str(output_file))
        
        # Verify encrypted file exists and is different
        assert output_file.exists()
        encrypted_content = output_file.read_text()
        assert encrypted_content != transaction_data
    
    def test_decrypt_transactions_file(self, tmp_path):
        """Test transaction file decryption."""
        # Create sample transaction data
        transaction_data = """id,date,amount,type,category,description,currency
123,2025-01-01,100.0,expense,Food,Grocery,USD
456,2025-01-02,200.0,income,Salary,Monthly salary,USD"""
        
        input_file = tmp_path / "transactions.csv"
        encrypted_file = tmp_path / "transactions.csv.enc"
        output_file = tmp_path / "decrypted.csv"
        
        input_file.write_text(transaction_data)
        
        # Import the functions
        from src.utils.encryption import encrypt_transactions_file, decrypt_transactions_file
        
        # Encrypt then decrypt
        encrypt_transactions_file(str(input_file), str(encrypted_file))
        decrypt_transactions_file(str(encrypted_file), str(output_file))
        
        # Verify decrypted content matches original
        decrypted_content = output_file.read_text()
        assert decrypted_content == transaction_data


class TestEncryptionIntegration:
    """Integration tests for encryption with CSV handler."""
    
    def test_csv_handler_with_encryption(self, tmp_path):
        """Test CSV handler integration with encryption."""
        from src.utils.csv_handler import read_transactions, write_transactions
        from src.models.transaction import Transaction
        from datetime import datetime
        
        # Create sample transactions
        transactions = [
            Transaction(
                id="123",
                date=datetime(2025, 1, 1),
                amount=100.0,
                type="expense",
                category="Food",
                description="Grocery shopping",
                currency="USD"
            ),
            Transaction(
                id="456",
                date=datetime(2025, 1, 2),
                amount=2000.0,
                type="income",
                category="Salary",
                description="Monthly salary",
                currency="USD"
            )
        ]
        
        encrypted_file = tmp_path / "transactions.csv.enc"
        
        # Write encrypted transactions
        write_transactions(str(encrypted_file), transactions)
        
        # Verify file is encrypted
        encrypted_content = encrypted_file.read_text()
        assert "id,date,amount,type,category,description,currency" not in encrypted_content
        
        # Read encrypted transactions
        read_transactions_list = read_transactions(str(encrypted_file))
        
        # Verify data integrity
        assert len(read_transactions_list) == len(transactions)
        assert read_transactions_list[0].id == transactions[0].id
        assert read_transactions_list[0].amount == transactions[0].amount
        assert read_transactions_list[1].id == transactions[1].id
        assert read_transactions_list[1].amount == transactions[1].amount


class TestEncryptionSecurity:
    """Security-focused test cases."""
    
    def test_encryption_key_isolation(self, tmp_path):
        """Test that different encryption instances have different keys."""
        key_file1 = tmp_path / "key1"
        key_file2 = tmp_path / "key2"
        
        encryption1 = DataEncryption(str(key_file1))
        encryption2 = DataEncryption(str(key_file2))
        
        assert encryption1.key != encryption2.key
    
    def test_encrypted_data_is_not_readable(self, tmp_path):
        """Test that encrypted data is not human-readable."""
        key_file = tmp_path / "test_key"
        encryption = DataEncryption(str(key_file))
        
        sensitive_data = "Bank account: 1234-5678-9012-3456\nBalance: $10,000"
        encrypted_data = encryption.encrypt_data(sensitive_data)
        
        # Encrypted data should not contain original text
        assert "Bank account" not in encrypted_data
        assert "1234-5678-9012-3456" not in encrypted_data
        assert "$10,000" not in encrypted_data
        
        # Encrypted data should be base64-like
        import re
        assert re.match(r'^[A-Za-z0-9+/=]+$', encrypted_data)
    
    def test_same_data_different_encryption(self, tmp_path):
        """Test that same data encrypted multiple times produces different results."""
        key_file = tmp_path / "test_key"
        encryption = DataEncryption(str(key_file))
        
        data = "Sensitive financial data"
        encrypted1 = encryption.encrypt_data(data)
        encrypted2 = encryption.encrypt_data(data)
        
        # Same data should produce different encrypted results (due to IV)
        assert encrypted1 != encrypted2
        
        # But both should decrypt to the same data
        decrypted1 = encryption.decrypt_data(encrypted1)
        decrypted2 = encryption.decrypt_data(encrypted2)
        
        assert decrypted1 == decrypted2 == data 