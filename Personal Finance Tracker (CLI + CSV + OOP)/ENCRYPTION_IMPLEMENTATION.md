# Data Encryption Implementation

## Overview

The Personal Finance Tracker now includes comprehensive data encryption to protect sensitive financial information. All transaction data is automatically encrypted at rest using military-grade AES-256 encryption.

## 🔐 Security Features

### Encryption Algorithm
- **Algorithm**: Fernet (AES-128-CBC with PKCS7 padding)
- **Key Derivation**: PBKDF2 with SHA256 and 100,000 iterations
- **Key Size**: 256-bit encryption keys
- **Security**: Military-grade encryption standards

### Key Management
- **Automatic Key Generation**: New encryption keys are generated automatically on first use
- **Secure Storage**: Keys are stored in `data/.encryption_key` with restricted permissions
- **Key Backup**: Built-in backup and restore functionality for encryption keys
- **Key Isolation**: Each installation has its own unique encryption key

## 📁 File Structure

```
Personal Finance Tracker/
├── data/
│   ├── .encryption_key          # Encryption key (auto-generated)
│   ├── transactions.csv.enc     # Encrypted transaction data
│   └── categories.csv           # Categories (unencrypted)
├── src/utils/
│   ├── encryption.py            # Core encryption functionality
│   ├── encryption_cli.py        # CLI for key management
│   └── migrate_to_encryption.py # Migration script
└── tests/
    └── test_encryption.py       # Comprehensive encryption tests
```

## 🚀 Implementation Details

### Core Components

#### 1. DataEncryption Class (`src/utils/encryption.py`)
```python
class DataEncryption:
    def __init__(self, key_file: str = "data/.encryption_key")
    def encrypt_data(self, data: str) -> str
    def decrypt_data(self, encrypted_data: str) -> str
    def encrypt_file(self, input_file: str, output_file: str) -> None
    def decrypt_file(self, input_file: str, output_file: str) -> None
    def backup_key(self, backup_path: str) -> None
    def restore_key(self, backup_path: str) -> None
```

#### 2. CSV Handler Integration (`src/utils/csv_handler.py`)
- **Automatic Encryption**: All transaction writes are automatically encrypted
- **Transparent Decryption**: All transaction reads are automatically decrypted
- **Legacy Support**: Automatic migration from unencrypted to encrypted format
- **File Extension**: Encrypted files use `.enc` extension

#### 3. Budget Manager Integration (`src/models/budget_manager.py`)
- **Automatic Migration**: Detects unencrypted files and migrates them
- **Encrypted Storage**: All transaction data is saved to encrypted files
- **Backward Compatibility**: Handles both encrypted and unencrypted files

## 🔧 Usage

### Automatic Operation
The encryption is completely transparent to users. Once implemented:
1. **New installations**: All data is automatically encrypted
2. **Existing installations**: Data is automatically migrated to encrypted format
3. **Normal operation**: Encryption/decryption happens in the background

### Manual Key Management

#### Backup Encryption Key
```bash
python src/utils/encryption_cli.py backup --backup-path /secure/location/key_backup.key
```

#### Restore Encryption Key
```bash
python src/utils/encryption_cli.py restore --backup-path /secure/location/key_backup.key
```

#### Show Key Information
```bash
python src/utils/encryption_cli.py info
```

#### Encrypt/Decrypt Files
```bash
# Encrypt a file
python src/utils/encryption_cli.py encrypt --input-file sensitive_data.txt

# Decrypt a file
python src/utils/encryption_cli.py decrypt --input-file sensitive_data.txt.enc
```

### Migration Process

#### Automatic Migration
The system automatically migrates unencrypted data when:
1. An unencrypted `transactions.csv` file is detected
2. The system loads data for the first time after encryption is enabled

#### Manual Migration
For explicit migration control:
```bash
python src/utils/migrate_to_encryption.py
```

This script will:
- Create backups of original files
- Encrypt all transaction data
- Remove unencrypted files (after backup)
- Generate new encryption key if needed

## 🧪 Testing

### Run Encryption Tests
```bash
# Run comprehensive encryption tests
python -m pytest tests/test_encryption.py -v

# Run simple encryption test
python test_encryption_simple.py
```

### Test Coverage
The encryption implementation includes tests for:
- Basic string encryption/decryption
- File encryption/decryption
- JSON data encryption
- Key backup and restore
- Password-based key derivation
- Security validation
- Integration with CSV handler

## 🔒 Security Considerations

### Key Security
- **Keep keys secure**: The encryption key is the only way to access encrypted data
- **Backup keys**: Always backup encryption keys to a secure location
- **Key isolation**: Each installation has a unique key for security
- **Key rotation**: Keys can be changed by backing up data, generating new key, and re-encrypting

### Data Protection
- **At-rest encryption**: All sensitive data is encrypted when stored
- **Transparent operation**: Encryption doesn't affect normal application usage
- **Secure deletion**: Temporary files are securely cleaned up
- **No plaintext storage**: Sensitive data is never stored in plaintext

### Best Practices
1. **Regular backups**: Backup both data and encryption keys
2. **Secure key storage**: Store backup keys in a secure, separate location
3. **Access control**: Limit access to the `data/` directory
4. **Key rotation**: Consider rotating keys periodically for enhanced security

## 🚨 Important Notes

### Data Recovery
- **Without the encryption key, encrypted data cannot be recovered**
- **Always backup encryption keys before making changes**
- **Test key restoration in a safe environment first**

### Migration Safety
- **Automatic migration creates backups before making changes**
- **Original files are preserved during migration**
- **Migration can be safely interrupted and restarted**

### Performance Impact
- **Minimal performance impact**: Encryption/decryption is fast and efficient
- **Transparent operation**: No user-visible performance degradation
- **Optimized implementation**: Uses efficient cryptographic libraries

## 📋 Dependencies

### Required Packages
```
cryptography>=41.0.0  # Core encryption functionality
```

### Optional Packages
```
pytest>=7.0.0        # For running encryption tests
pytest-cov>=4.0.0    # For test coverage reporting
```

## 🔄 Future Enhancements

### Planned Features
- **Password-based encryption**: User-defined passwords for key derivation
- **Key rotation**: Automated key rotation capabilities
- **Cloud backup**: Secure cloud backup for encryption keys
- **Multi-factor authentication**: Additional security layers
- **Audit logging**: Encryption operation logging for compliance

### Security Improvements
- **Hardware security modules**: Integration with HSM for key storage
- **Zero-knowledge architecture**: Enhanced privacy protection
- **Quantum-resistant algorithms**: Future-proof encryption methods

## 📞 Support

For issues related to encryption:
1. Check the test files for examples
2. Verify encryption key exists and is accessible
3. Ensure proper file permissions
4. Review migration logs for any errors

The encryption implementation is designed to be robust and user-friendly while maintaining the highest security standards for protecting sensitive financial data. 