#!/usr/bin/env python3
"""
Migration script to convert unencrypted transaction data to encrypted format.
This script helps users migrate their existing data to the new encrypted format.
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
from src.utils.encryption import get_encryption
from src.utils.csv_handler import read_transactions, write_transactions


def backup_original_file(file_path: str) -> str:
    """
    Create a backup of the original file.
    
    Args:
        file_path: Path to the original file
        
    Returns:
        Path to the backup file
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = path.parent / f"{path.stem}_backup_{timestamp}{path.suffix}"
    
    shutil.copy2(file_path, backup_path)
    print(f"Created backup: {backup_path}")
    return str(backup_path)


def migrate_transactions_file(file_path: str, create_backup: bool = True) -> bool:
    """
    Migrate a transactions CSV file to encrypted format.
    
    Args:
        file_path: Path to the transactions CSV file
        create_backup: Whether to create a backup of the original file
        
    Returns:
        True if migration was successful, False otherwise
    """
    path = Path(file_path)
    if not path.exists():
        print(f"File not found: {file_path}")
        return False
    
    try:
        # Create backup if requested
        if create_backup:
            backup_path = backup_original_file(file_path)
        
        # Read the unencrypted transactions
        print(f"Reading transactions from: {file_path}")
        transactions = read_transactions(file_path)
        print(f"Found {len(transactions)} transactions")
        
        # Create encrypted file path
        encrypted_path = str(path.with_suffix('.csv.enc'))
        
        # Write transactions to encrypted file
        print(f"Writing encrypted transactions to: {encrypted_path}")
        write_transactions(encrypted_path, transactions)
        
        # Verify the encrypted file can be read
        print("Verifying encrypted file...")
        encrypted_transactions = read_transactions(encrypted_path)
        
        if len(encrypted_transactions) == len(transactions):
            print("✓ Migration successful! Encrypted file verified.")
            
            # Remove original unencrypted file
            if create_backup:
                os.remove(file_path)
                print(f"Removed original file: {file_path}")
            else:
                print(f"Original file preserved: {file_path}")
            
            return True
        else:
            print(f"✗ Verification failed! Expected {len(transactions)} transactions, got {len(encrypted_transactions)}")
            return False
            
    except Exception as e:
        print(f"✗ Migration failed: {e}")
        return False


def migrate_data_directory(data_dir: str = "data", create_backups: bool = True) -> bool:
    """
    Migrate all transaction files in a data directory.
    
    Args:
        data_dir: Path to the data directory
        create_backups: Whether to create backups of original files
        
    Returns:
        True if all migrations were successful, False otherwise
    """
    data_path = Path(data_dir)
    if not data_path.exists():
        print(f"Data directory not found: {data_dir}")
        return False
    
    success_count = 0
    total_count = 0
    
    # Find all transaction CSV files
    transaction_files = list(data_path.glob("transactions.csv"))
    
    if not transaction_files:
        print("No transaction files found to migrate.")
        return True
    
    print(f"Found {len(transaction_files)} transaction file(s) to migrate:")
    for file_path in transaction_files:
        print(f"  - {file_path}")
    
    print("\nStarting migration...")
    
    for file_path in transaction_files:
        total_count += 1
        print(f"\nMigrating: {file_path}")
        
        if migrate_transactions_file(str(file_path), create_backups):
            success_count += 1
        else:
            print(f"Failed to migrate: {file_path}")
    
    print(f"\nMigration complete: {success_count}/{total_count} files migrated successfully")
    return success_count == total_count


def main():
    """Main migration function."""
    print("=" * 60)
    print("Personal Finance Tracker - Data Encryption Migration")
    print("=" * 60)
    print()
    print("This script will migrate your unencrypted transaction data to encrypted format.")
    print("Your sensitive financial data will be protected from unauthorized access.")
    print()
    
    # Check if encryption key already exists
    encryption = get_encryption()
    key_path = Path("data/.encryption_key")
    
    if key_path.exists():
        print(f"✓ Encryption key found: {key_path}")
    else:
        print(f"✓ New encryption key will be generated: {key_path}")
    
    print()
    
    # Ask for confirmation
    response = input("Do you want to proceed with the migration? (y/N): ").strip().lower()
    if response not in ['y', 'yes']:
        print("Migration cancelled.")
        return
    
    print()
    
    # Perform migration
    success = migrate_data_directory("data", create_backups=True)
    
    if success:
        print("\n" + "=" * 60)
        print("✓ Migration completed successfully!")
        print("=" * 60)
        print()
        print("Important notes:")
        print("- Your transaction data is now encrypted and secure")
        print("- The encryption key is stored in: data/.encryption_key")
        print("- Keep this key safe - without it, you cannot access your data")
        print("- Consider backing up the encryption key to a secure location")
        print()
        print("Your Personal Finance Tracker will now use encrypted files by default.")
    else:
        print("\n" + "=" * 60)
        print("✗ Migration completed with errors!")
        print("=" * 60)
        print()
        print("Please check the error messages above and try again.")
        print("Your original data files have been backed up and are still available.")


if __name__ == "__main__":
    main() 