import csv
import tempfile
import os
from typing import List
from pathlib import Path
from src.models.transaction import Transaction
from src.models.category import Category
from src.utils.encryption import get_encryption

def read_transactions(csv_path: str) -> List[Transaction]:
    """
    Read transactions from an encrypted CSV file and return a list of Transaction objects.
    """
    transactions = []
    path = Path(csv_path)
    if not path.exists():
        return transactions
    
    encryption = get_encryption()
    
    # Check if the file is encrypted (has .enc extension)
    if csv_path.endswith('.enc'):
        # Decrypt the file to a temporary location
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as temp_file:
            temp_path = temp_file.name
        
        try:
            encryption.decrypt_file(csv_path, temp_path)
            
            # Read from the decrypted temporary file
            with open(temp_path, mode='r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    transactions.append(Transaction.from_dict(row))
        finally:
            # Clean up temporary file
            if os.path.exists(temp_path):
                os.unlink(temp_path)
    else:
        # Handle legacy unencrypted files
        with open(csv_path, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                transactions.append(Transaction.from_dict(row))
    
    return transactions

def write_transactions(csv_path: str, transactions: List[Transaction]) -> None:
    """
    Write a list of Transaction objects to an encrypted CSV file.
    """
    encryption = get_encryption()
    
    # Create a temporary CSV file
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as temp_file:
        temp_path = temp_file.name
    
    try:
        # Write to the temporary CSV file
        with open(temp_path, mode='w', newline='', encoding='utf-8') as f:
            fieldnames = ['id', 'date', 'amount', 'type', 'category', 'description', 'currency']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for transaction in transactions:
                writer.writerow(transaction.to_dict())
        
        # Encrypt the temporary file to the final destination
        encryption.encrypt_file(temp_path, csv_path)
    finally:
        # Clean up temporary file
        if os.path.exists(temp_path):
            os.unlink(temp_path)

def read_categories(csv_path: str) -> List[Category]:
    """
    Read categories from a CSV file and return a list of Category objects.
    """
    categories = []
    path = Path(csv_path)
    if not path.exists():
        return categories
    with open(csv_path, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            categories.append(Category.from_dict(row))
    return categories

def write_categories(csv_path: str, categories: List[Category]) -> None:
    """
    Write a list of Category objects to a CSV file.
    """
    with open(csv_path, mode='w', newline='', encoding='utf-8') as f:
        fieldnames = ['name', 'budget_limit', 'is_predefined']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for category in categories:
            writer.writerow(category.to_dict()) 