import os
import base64
import json
from pathlib import Path
from typing import Dict, Any, Optional
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend


class DataEncryption:
    """
    A secure encryption utility for protecting sensitive financial data.
    Uses Fernet symmetric encryption with PBKDF2 key derivation.
    """
    
    def __init__(self, key_file: str = "data/.encryption_key"):
        """
        Initialize the encryption utility.
        
        Args:
            key_file: Path to store the encryption key
        """
        self.key_file = Path(key_file)
        self.key = self._load_or_generate_key()
        self.cipher_suite = Fernet(self.key)
    
    def _load_or_generate_key(self) -> bytes:
        """
        Load existing key or generate a new one if it doesn't exist.
        
        Returns:
            Encryption key as bytes
        """
        if self.key_file.exists():
            with open(self.key_file, 'rb') as f:
                return f.read()
        else:
            # Generate a new key
            key = Fernet.generate_key()
            # Ensure the directory exists
            self.key_file.parent.mkdir(parents=True, exist_ok=True)
            # Save the key
            with open(self.key_file, 'wb') as f:
                f.write(key)
            return key
    
    def derive_key_from_password(self, password: str, salt: Optional[bytes] = None) -> bytes:
        """
        Derive a key from a password using PBKDF2.
        
        Args:
            password: User password
            salt: Salt for key derivation (generated if None)
            
        Returns:
            Derived key as bytes
        """
        if salt is None:
            salt = os.urandom(16)
        
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key, salt
    
    def encrypt_data(self, data: str) -> str:
        """
        Encrypt data string.
        
        Args:
            data: Data to encrypt
            
        Returns:
            Encrypted data as base64 string
        """
        encrypted_data = self.cipher_suite.encrypt(data.encode())
        return base64.urlsafe_b64encode(encrypted_data).decode()
    
    def decrypt_data(self, encrypted_data: str) -> str:
        """
        Decrypt data string.
        
        Args:
            encrypted_data: Encrypted data as base64 string
            
        Returns:
            Decrypted data as string
        """
        try:
            encrypted_bytes = base64.urlsafe_b64decode(encrypted_data.encode())
            decrypted_data = self.cipher_suite.decrypt(encrypted_bytes)
            return decrypted_data.decode()
        except Exception as e:
            raise ValueError(f"Failed to decrypt data: {e}")
    
    def encrypt_file(self, input_file: str, output_file: str) -> None:
        """
        Encrypt a file and save to output file.
        
        Args:
            input_file: Path to input file
            output_file: Path to output encrypted file
        """
        with open(input_file, 'r', encoding='utf-8') as f:
            data = f.read()
        
        encrypted_data = self.encrypt_data(data)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(encrypted_data)
    
    def decrypt_file(self, input_file: str, output_file: str) -> None:
        """
        Decrypt a file and save to output file.
        
        Args:
            input_file: Path to encrypted input file
            output_file: Path to output decrypted file
        """
        with open(input_file, 'r', encoding='utf-8') as f:
            encrypted_data = f.read()
        
        decrypted_data = self.decrypt_data(encrypted_data)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(decrypted_data)
    
    def encrypt_json(self, data: Dict[str, Any]) -> str:
        """
        Encrypt JSON data.
        
        Args:
            data: Dictionary to encrypt
            
        Returns:
            Encrypted JSON as base64 string
        """
        json_str = json.dumps(data, ensure_ascii=False)
        return self.encrypt_data(json_str)
    
    def decrypt_json(self, encrypted_data: str) -> Dict[str, Any]:
        """
        Decrypt JSON data.
        
        Args:
            encrypted_data: Encrypted JSON as base64 string
            
        Returns:
            Decrypted dictionary
        """
        decrypted_data = self.decrypt_data(encrypted_data)
        return json.loads(decrypted_data)
    
    def backup_key(self, backup_path: str) -> None:
        """
        Create a backup of the encryption key.
        
        Args:
            backup_path: Path to backup the key
        """
        backup_path = Path(backup_path)
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(self.key_file, 'rb') as src, open(backup_path, 'wb') as dst:
            dst.write(src.read())
    
    def restore_key(self, backup_path: str) -> None:
        """
        Restore encryption key from backup.
        
        Args:
            backup_path: Path to backup key file
        """
        backup_path = Path(backup_path)
        if not backup_path.exists():
            raise FileNotFoundError(f"Backup key file not found: {backup_path}")
        
        with open(backup_path, 'rb') as src, open(self.key_file, 'wb') as dst:
            dst.write(src.read())
        
        # Reload the key
        self.key = self._load_or_generate_key()
        self.cipher_suite = Fernet(self.key)


# Global encryption instance
_encryption_instance: Optional[DataEncryption] = None


def get_encryption() -> DataEncryption:
    """
    Get the global encryption instance.
    
    Returns:
        DataEncryption instance
    """
    global _encryption_instance
    if _encryption_instance is None:
        _encryption_instance = DataEncryption()
    return _encryption_instance


def encrypt_transactions_file(input_file: str, output_file: str) -> None:
    """
    Encrypt a transactions CSV file.
    
    Args:
        input_file: Path to input CSV file
        output_file: Path to output encrypted file
    """
    encryption = get_encryption()
    encryption.encrypt_file(input_file, output_file)


def decrypt_transactions_file(input_file: str, output_file: str) -> None:
    """
    Decrypt a transactions file.
    
    Args:
        input_file: Path to encrypted file
        output_file: Path to output CSV file
    """
    encryption = get_encryption()
    encryption.decrypt_file(input_file, output_file) 