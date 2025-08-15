#!/usr/bin/env python3
"""
CLI utility for managing encryption keys and performing encryption operations.
"""

import argparse
import sys
from pathlib import Path
from src.utils.encryption import get_encryption


def backup_key(args):
    """Backup the encryption key."""
    try:
        encryption = get_encryption()
        backup_path = args.backup_path or f"encryption_key_backup_{Path.cwd().name}.key"
        
        encryption.backup_key(backup_path)
        print(f"✓ Encryption key backed up to: {backup_path}")
        print("⚠️  Keep this backup safe - without it, you cannot access your encrypted data!")
        
    except Exception as e:
        print(f"✗ Failed to backup encryption key: {e}")
        sys.exit(1)


def restore_key(args):
    """Restore the encryption key from backup."""
    try:
        encryption = get_encryption()
        
        if not Path(args.backup_path).exists():
            print(f"✗ Backup file not found: {args.backup_path}")
            sys.exit(1)
        
        encryption.restore_key(args.backup_path)
        print(f"✓ Encryption key restored from: {args.backup_path}")
        
    except Exception as e:
        print(f"✗ Failed to restore encryption key: {e}")
        sys.exit(1)


def encrypt_file(args):
    """Encrypt a file."""
    try:
        encryption = get_encryption()
        
        if not Path(args.input_file).exists():
            print(f"✗ Input file not found: {args.input_file}")
            sys.exit(1)
        
        output_file = args.output_file or f"{args.input_file}.enc"
        encryption.encrypt_file(args.input_file, output_file)
        print(f"✓ File encrypted: {output_file}")
        
    except Exception as e:
        print(f"✗ Failed to encrypt file: {e}")
        sys.exit(1)


def decrypt_file(args):
    """Decrypt a file."""
    try:
        encryption = get_encryption()
        
        if not Path(args.input_file).exists():
            print(f"✗ Input file not found: {args.input_file}")
            sys.exit(1)
        
        output_file = args.output_file or args.input_file.replace('.enc', '')
        encryption.decrypt_file(args.input_file, output_file)
        print(f"✓ File decrypted: {output_file}")
        
    except Exception as e:
        print(f"✗ Failed to decrypt file: {e}")
        sys.exit(1)


def show_key_info(args):
    """Show information about the encryption key."""
    try:
        encryption = get_encryption()
        key_path = encryption.key_file
        
        print("Encryption Key Information:")
        print(f"  Key file: {key_path}")
        print(f"  Exists: {'Yes' if key_path.exists() else 'No'}")
        
        if key_path.exists():
            key_size = key_path.stat().st_size
            print(f"  Key size: {key_size} bytes")
            print(f"  Key type: Fernet (AES-128-CBC)")
        
        print("\nSecurity Notes:")
        print("  - Keep the encryption key file secure")
        print("  - Without this key, encrypted data cannot be accessed")
        print("  - Consider backing up the key to a secure location")
        
    except Exception as e:
        print(f"✗ Failed to get key information: {e}")
        sys.exit(1)


def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description="Personal Finance Tracker - Encryption Management CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Backup encryption key
  python src/utils/encryption_cli.py backup --backup-path /secure/location/key_backup.key
  
  # Restore encryption key
  python src/utils/encryption_cli.py restore --backup-path /secure/location/key_backup.key
  
  # Encrypt a file
  python src/utils/encryption_cli.py encrypt --input-file sensitive_data.txt
  
  # Decrypt a file
  python src/utils/encryption_cli.py decrypt --input-file sensitive_data.txt.enc
  
  # Show key information
  python src/utils/encryption_cli.py info
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Backup command
    backup_parser = subparsers.add_parser('backup', help='Backup encryption key')
    backup_parser.add_argument('--backup-path', help='Path to save the backup key')
    backup_parser.set_defaults(func=backup_key)
    
    # Restore command
    restore_parser = subparsers.add_parser('restore', help='Restore encryption key from backup')
    restore_parser.add_argument('backup_path', help='Path to the backup key file')
    restore_parser.set_defaults(func=restore_key)
    
    # Encrypt command
    encrypt_parser = subparsers.add_parser('encrypt', help='Encrypt a file')
    encrypt_parser.add_argument('input_file', help='File to encrypt')
    encrypt_parser.add_argument('--output-file', help='Output file path (default: input_file.enc)')
    encrypt_parser.set_defaults(func=encrypt_file)
    
    # Decrypt command
    decrypt_parser = subparsers.add_parser('decrypt', help='Decrypt a file')
    decrypt_parser.add_argument('input_file', help='File to decrypt')
    decrypt_parser.add_argument('--output-file', help='Output file path (default: input_file without .enc)')
    decrypt_parser.set_defaults(func=decrypt_file)
    
    # Info command
    info_parser = subparsers.add_parser('info', help='Show encryption key information')
    info_parser.set_defaults(func=show_key_info)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    args.func(args)


if __name__ == "__main__":
    main() 