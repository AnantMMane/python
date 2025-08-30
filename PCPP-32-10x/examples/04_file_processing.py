#!/usr/bin/env python3
"""
File Processing & I/O Examples
PCPP Certification Study Material

This module demonstrates file processing and I/O concepts including:
- Advanced file operations
- Context managers
- JSON and XML processing
- Binary file handling
- CSV data processing
- Configuration file management
- Database integration
"""

import os
import json
import xml.etree.ElementTree as ET
import csv
import pickle
import sqlite3
import configparser
import tempfile
import shutil
import zipfile
import hashlib
from datetime import datetime
from pathlib import Path
import struct


# 1. Advanced File Operations
class FileManager:
    """Advanced file manager with context manager support"""
    
    def __init__(self, filename, mode='r', encoding='utf-8', backup=False):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.backup = backup
        self.file = None
        self.backup_path = None
    
    def __enter__(self):
        """Enter context manager"""
        # Create backup if requested
        if self.backup and os.path.exists(self.filename) and 'w' in self.mode:
            self.backup_path = f"{self.filename}.backup"
            shutil.copy2(self.filename, self.backup_path)
            print(f"Backup created: {self.backup_path}")
        
        # Open file
        self.file = open(self.filename, self.mode, encoding=self.encoding)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit context manager"""
        if self.file:
            self.file.close()
        
        # Handle exceptions
        if exc_type is not None:
            print(f"Error occurred: {exc_val}")
            # Restore backup if error occurred during write
            if self.backup_path and os.path.exists(self.backup_path):
                shutil.copy2(self.backup_path, self.filename)
                print("File restored from backup")
        
        # Clean up backup if everything went well
        elif self.backup_path and os.path.exists(self.backup_path):
            os.remove(self.backup_path)
        
        # Return False to propagate exceptions
        return False


class SecureFileHandler:
    """Secure file handler with encryption and integrity checks"""
    
    @staticmethod
    def calculate_checksum(filename, algorithm='sha256'):
        """Calculate file checksum"""
        hash_obj = hashlib.new(algorithm)
        
        with open(filename, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_obj.update(chunk)
        
        return hash_obj.hexdigest()
    
    @staticmethod
    def verify_file_integrity(filename, expected_checksum, algorithm='sha256'):
        """Verify file integrity using checksum"""
        actual_checksum = SecureFileHandler.calculate_checksum(filename, algorithm)
        return actual_checksum == expected_checksum
    
    @staticmethod
    def create_secure_temp_file(prefix='temp_', suffix='.tmp'):
        """Create secure temporary file"""
        with tempfile.NamedTemporaryFile(prefix=prefix, suffix=suffix, delete=False) as temp_file:
            temp_path = temp_file.name
        
        # Set restrictive permissions (owner read/write only)
        os.chmod(temp_path, 0o600)
        return temp_path
    
    @staticmethod
    def safe_file_move(source, destination):
        """Safely move file with atomic operation"""
        # Create temporary file in destination directory
        dest_dir = os.path.dirname(destination)
        temp_dest = tempfile.mktemp(dir=dest_dir)
        
        try:
            # Copy to temporary location
            shutil.copy2(source, temp_dest)
            
            # Atomic move
            os.rename(temp_dest, destination)
            
            # Remove source
            os.remove(source)
            
            return True
        except Exception as e:
            # Clean up temp file if it exists
            if os.path.exists(temp_dest):
                os.remove(temp_dest)
            raise e


# 2. JSON Processing
class JSONProcessor:
    """Advanced JSON processing with custom encoders and validation"""
    
    class DateTimeEncoder(json.JSONEncoder):
        """Custom JSON encoder for datetime objects"""
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            return super().default(obj)
    
    @staticmethod
    def save_json(data, filename, indent=2, sort_keys=True):
        """Save data to JSON file with pretty formatting"""
        with FileManager(filename, 'w', backup=True) as f:
            json.dump(data, f, cls=JSONProcessor.DateTimeEncoder, 
                     indent=indent, sort_keys=sort_keys, ensure_ascii=False)
    
    @staticmethod
    def load_json(filename, default=None):
        """Load JSON data with error handling"""
        try:
            with FileManager(filename, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading JSON: {e}")
            return default
    
    @staticmethod
    def merge_json_files(input_files, output_file):
        """Merge multiple JSON files into one"""
        merged_data = {}
        
        for input_file in input_files:
            data = JSONProcessor.load_json(input_file, {})
            if isinstance(data, dict):
                merged_data.update(data)
            else:
                # Handle non-dict data by using filename as key
                key = os.path.splitext(os.path.basename(input_file))[0]
                merged_data[key] = data
        
        JSONProcessor.save_json(merged_data, output_file)
        return merged_data
    
    @staticmethod
    def process_large_json(filename, processor_func):
        """Process large JSON files line by line"""
        results = []
        
        with FileManager(filename, 'r') as f:
            for line_num, line in enumerate(f, 1):
                try:
                    data = json.loads(line.strip())
                    result = processor_func(data)
                    if result is not None:
                        results.append(result)
                except json.JSONDecodeError:
                    print(f"Invalid JSON on line {line_num}: {line[:50]}...")
                    continue
        
        return results
    
    @staticmethod
    def validate_json_schema(data, schema):
        """Basic JSON schema validation"""
        def validate_field(field_name, field_value, field_schema):
            if 'type' in field_schema:
                expected_type = field_schema['type']
                type_map = {
                    'string': str,
                    'number': (int, float),
                    'integer': int,
                    'boolean': bool,
                    'array': list,
                    'object': dict
                }
                
                if expected_type in type_map:
                    if not isinstance(field_value, type_map[expected_type]):
                        return False, f"Field '{field_name}' should be {expected_type}"
            
            if 'required' in field_schema and field_schema['required']:
                if field_value is None:
                    return False, f"Field '{field_name}' is required"
            
            return True, None
        
        # Simple validation (this could be extended with a proper JSON schema library)
        for field_name, field_schema in schema.items():
            field_value = data.get(field_name)
            is_valid, error_msg = validate_field(field_name, field_value, field_schema)
            if not is_valid:
                return False, error_msg
        
        return True, None


# 3. XML Processing
class XMLProcessor:
    """XML processing and manipulation"""
    
    @staticmethod
    def dict_to_xml(data, root_name='root'):
        """Convert dictionary to XML"""
        def build_element(parent, data):
            if isinstance(data, dict):
                for key, value in data.items():
                    if isinstance(value, list):
                        for item in value:
                            elem = ET.SubElement(parent, key)
                            build_element(elem, item)
                    else:
                        elem = ET.SubElement(parent, key)
                        build_element(elem, value)
            else:
                parent.text = str(data)
        
        root = ET.Element(root_name)
        build_element(root, data)
        return ET.ElementTree(root)
    
    @staticmethod
    def xml_to_dict(element):
        """Convert XML element to dictionary"""
        result = {}
        
        # Handle attributes
        if element.attrib:
            result['@attributes'] = element.attrib
        
        # Handle text content
        if element.text and element.text.strip():
            if len(element) == 0:  # No children
                return element.text.strip()
            result['text'] = element.text.strip()
        
        # Handle children
        children = {}
        for child in element:
            child_data = XMLProcessor.xml_to_dict(child)
            
            if child.tag in children:
                if not isinstance(children[child.tag], list):
                    children[child.tag] = [children[child.tag]]
                children[child.tag].append(child_data)
            else:
                children[child.tag] = child_data
        
        result.update(children)
        return result
    
    @staticmethod
    def save_xml(element_tree, filename, encoding='utf-8'):
        """Save XML tree to file with proper formatting"""
        # Add pretty printing
        XMLProcessor._indent(element_tree.getroot())
        
        element_tree.write(filename, encoding=encoding, xml_declaration=True)
    
    @staticmethod
    def _indent(elem, level=0):
        """Add whitespace for pretty printing"""
        i = "\n" + level * "  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                XMLProcessor._indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i
    
    @staticmethod
    def transform_xml(input_file, output_file, transform_func):
        """Transform XML file using custom function"""
        tree = ET.parse(input_file)
        root = tree.getroot()
        
        # Apply transformation
        transformed_root = transform_func(root)
        
        # Create new tree and save
        new_tree = ET.ElementTree(transformed_root)
        XMLProcessor.save_xml(new_tree, output_file)


# 4. Binary File Handling
class BinaryFileHandler:
    """Binary file processing utilities"""
    
    @staticmethod
    def pack_data(filename, *data):
        """Pack data into binary file using struct"""
        with open(filename, 'wb') as f:
            for item in data:
                if isinstance(item, int):
                    f.write(struct.pack('i', item))
                elif isinstance(item, float):
                    f.write(struct.pack('f', item))
                elif isinstance(item, str):
                    encoded = item.encode('utf-8')
                    f.write(struct.pack('I', len(encoded)))  # Length prefix
                    f.write(encoded)
                elif isinstance(item, bytes):
                    f.write(struct.pack('I', len(item)))
                    f.write(item)
    
    @staticmethod
    def unpack_data(filename, format_string):
        """Unpack data from binary file"""
        results = []
        
        with open(filename, 'rb') as f:
            while True:
                try:
                    # Read based on format
                    if 's' in format_string:  # String with length prefix
                        length = struct.unpack('I', f.read(4))[0]
                        data = f.read(length).decode('utf-8')
                    else:
                        size = struct.calcsize(format_string)
                        data = struct.unpack(format_string, f.read(size))[0]
                    
                    results.append(data)
                except struct.error:
                    break
        
        return results
    
    @staticmethod
    def serialize_object(obj, filename):
        """Serialize object to binary file using pickle"""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
            return True
        except Exception as e:
            print(f"Serialization error: {e}")
            return False
    
    @staticmethod
    def deserialize_object(filename):
        """Deserialize object from binary file"""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            print(f"Deserialization error: {e}")
            return None
    
    @staticmethod
    def compare_binary_files(file1, file2, chunk_size=4096):
        """Compare two binary files for equality"""
        try:
            with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
                while True:
                    chunk1 = f1.read(chunk_size)
                    chunk2 = f2.read(chunk_size)
                    
                    if chunk1 != chunk2:
                        return False
                    
                    if not chunk1:  # End of both files
                        return True
        except Exception:
            return False


# 5. CSV Data Processing
class CSVProcessor:
    """Advanced CSV processing with various options"""
    
    @staticmethod
    def read_csv_with_types(filename, type_converters=None, skip_errors=True):
        """Read CSV with automatic type conversion"""
        data = []
        
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row_num, row in enumerate(reader, 2):  # Start from 2 (header is 1)
                converted_row = {}
                
                for field, value in row.items():
                    try:
                        if type_converters and field in type_converters:
                            converted_value = type_converters[field](value)
                        else:
                            # Auto-detect type
                            converted_value = CSVProcessor._auto_convert_type(value)
                        
                        converted_row[field] = converted_value
                        
                    except (ValueError, TypeError) as e:
                        if skip_errors:
                            print(f"Type conversion error at row {row_num}, field '{field}': {e}")
                            converted_row[field] = value  # Keep original value
                        else:
                            raise
                
                data.append(converted_row)
        
        return data
    
    @staticmethod
    def _auto_convert_type(value):
        """Automatically convert string to appropriate type"""
        if value == '':
            return None
        
        # Try integer
        try:
            return int(value)
        except ValueError:
            pass
        
        # Try float
        try:
            return float(value)
        except ValueError:
            pass
        
        # Try boolean
        lower_value = value.lower()
        if lower_value in ('true', 'false', 'yes', 'no', '1', '0'):
            return lower_value in ('true', 'yes', '1')
        
        # Return as string
        return value
    
    @staticmethod
    def write_csv_from_objects(filename, objects, fieldnames=None):
        """Write objects to CSV file"""
        if not objects:
            return
        
        # Auto-detect fieldnames if not provided
        if fieldnames is None:
            if hasattr(objects[0], '__dict__'):
                fieldnames = list(objects[0].__dict__.keys())
            elif isinstance(objects[0], dict):
                fieldnames = list(objects[0].keys())
            else:
                raise ValueError("Cannot determine fieldnames for objects")
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for obj in objects:
                if hasattr(obj, '__dict__'):
                    row = obj.__dict__
                elif isinstance(obj, dict):
                    row = obj
                else:
                    row = dict(zip(fieldnames, obj))
                
                writer.writerow(row)
    
    @staticmethod
    def filter_csv(input_file, output_file, filter_func):
        """Filter CSV file based on custom function"""
        with open(input_file, 'r', newline='') as infile, \
             open(output_file, 'w', newline='') as outfile:
            
            reader = csv.DictReader(infile)
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
            writer.writeheader()
            
            for row in reader:
                if filter_func(row):
                    writer.writerow(row)
    
    @staticmethod
    def aggregate_csv(filename, group_by_field, aggregations):
        """Aggregate CSV data by field with custom aggregation functions"""
        # First, read all data
        data = CSVProcessor.read_csv_with_types(filename)
        
        # Group by field
        groups = {}
        for row in data:
            key = row[group_by_field]
            if key not in groups:
                groups[key] = []
            groups[key].append(row)
        
        # Apply aggregations
        results = []
        for group_key, group_data in groups.items():
            result = {group_by_field: group_key}
            
            for field, agg_func in aggregations.items():
                values = [row[field] for row in group_data if row[field] is not None]
                if values:
                    result[f"{field}_{agg_func.__name__}"] = agg_func(values)
                else:
                    result[f"{field}_{agg_func.__name__}"] = None
            
            results.append(result)
        
        return results


# 6. Configuration Management
class ConfigManager:
    """Configuration file manager supporting multiple formats"""
    
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.config_data = {}
        self.load_config()
    
    def load_config(self):
        """Load configuration from file"""
        if os.path.exists(self.config_file):
            file_ext = os.path.splitext(self.config_file)[1].lower()
            
            if file_ext == '.json':
                self.config_data = JSONProcessor.load_json(self.config_file, {})
            elif file_ext in ['.ini', '.cfg']:
                self.config.read(self.config_file)
                # Convert to dict for easier access
                self.config_data = {
                    section: dict(self.config[section]) 
                    for section in self.config.sections()
                }
            else:
                print(f"Unsupported config file format: {file_ext}")
    
    def get(self, key, section=None, default=None):
        """Get configuration value"""
        if section:
            return self.config_data.get(section, {}).get(key, default)
        else:
            # Search all sections
            for section_data in self.config_data.values():
                if isinstance(section_data, dict) and key in section_data:
                    return section_data[key]
            return default
    
    def set(self, key, value, section='DEFAULT'):
        """Set configuration value"""
        if section not in self.config_data:
            self.config_data[section] = {}
        self.config_data[section][key] = value
    
    def save_config(self):
        """Save configuration to file"""
        file_ext = os.path.splitext(self.config_file)[1].lower()
        
        if file_ext == '.json':
            JSONProcessor.save_json(self.config_data, self.config_file)
        elif file_ext in ['.ini', '.cfg']:
            # Convert back to ConfigParser format
            for section, values in self.config_data.items():
                if not self.config.has_section(section) and section != 'DEFAULT':
                    self.config.add_section(section)
                for key, value in values.items():
                    self.config.set(section, key, str(value))
            
            with open(self.config_file, 'w') as f:
                self.config.write(f)
    
    def get_database_config(self):
        """Get database configuration"""
        return {
            'host': self.get('host', 'database', 'localhost'),
            'port': int(self.get('port', 'database', 5432)),
            'database': self.get('database', 'database', 'mydb'),
            'username': self.get('username', 'database', 'user'),
            'password': self.get('password', 'database', '')
        }


# 7. Database Integration
class DatabaseManager:
    """SQLite database manager with ORM-like features"""
    
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = None
    
    def __enter__(self):
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row  # Enable dict-like access
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            if exc_type is None:
                self.connection.commit()
            else:
                self.connection.rollback()
            self.connection.close()
    
    def create_table(self, table_name, columns):
        """Create table with specified columns"""
        column_defs = []
        for col_name, col_type in columns.items():
            column_defs.append(f"{col_name} {col_type}")
        
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(column_defs)})"
        self.connection.execute(query)
    
    def insert(self, table_name, data):
        """Insert data into table"""
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?' for _ in data])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        
        cursor = self.connection.execute(query, list(data.values()))
        return cursor.lastrowid
    
    def select(self, table_name, where=None, order_by=None, limit=None):
        """Select data from table"""
        query = f"SELECT * FROM {table_name}"
        params = []
        
        if where:
            conditions = []
            for key, value in where.items():
                conditions.append(f"{key} = ?")
                params.append(value)
            query += f" WHERE {' AND '.join(conditions)}"
        
        if order_by:
            query += f" ORDER BY {order_by}"
        
        if limit:
            query += f" LIMIT {limit}"
        
        cursor = self.connection.execute(query, params)
        return [dict(row) for row in cursor.fetchall()]
    
    def update(self, table_name, data, where):
        """Update data in table"""
        set_clauses = []
        params = []
        
        for key, value in data.items():
            set_clauses.append(f"{key} = ?")
            params.append(value)
        
        where_clauses = []
        for key, value in where.items():
            where_clauses.append(f"{key} = ?")
            params.append(value)
        
        query = f"UPDATE {table_name} SET {', '.join(set_clauses)} WHERE {' AND '.join(where_clauses)}"
        cursor = self.connection.execute(query, params)
        return cursor.rowcount
    
    def delete(self, table_name, where):
        """Delete data from table"""
        where_clauses = []
        params = []
        
        for key, value in where.items():
            where_clauses.append(f"{key} = ?")
            params.append(value)
        
        query = f"DELETE FROM {table_name} WHERE {' AND '.join(where_clauses)}"
        cursor = self.connection.execute(query, params)
        return cursor.rowcount
    
    def import_csv(self, table_name, csv_file, create_table=True):
        """Import CSV data into database table"""
        # Read CSV data
        data = CSVProcessor.read_csv_with_types(csv_file)
        
        if not data:
            return 0
        
        # Create table if requested
        if create_table:
            # Infer column types from first row
            columns = {}
            for key, value in data[0].items():
                if isinstance(value, int):
                    columns[key] = 'INTEGER'
                elif isinstance(value, float):
                    columns[key] = 'REAL'
                elif isinstance(value, bool):
                    columns[key] = 'INTEGER'
                else:
                    columns[key] = 'TEXT'
            
            self.create_table(table_name, columns)
        
        # Insert data
        inserted_count = 0
        for row in data:
            try:
                self.insert(table_name, row)
                inserted_count += 1
            except sqlite3.Error as e:
                print(f"Error inserting row: {e}")
        
        return inserted_count


# 8. Archive and Compression
class ArchiveManager:
    """Archive and compression utilities"""
    
    @staticmethod
    def create_zip(source_path, archive_path, exclude_patterns=None):
        """Create ZIP archive from directory or file"""
        exclude_patterns = exclude_patterns or []
        
        with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            if os.path.isfile(source_path):
                zipf.write(source_path, os.path.basename(source_path))
            else:
                for root, dirs, files in os.walk(source_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        
                        # Check exclude patterns
                        should_exclude = False
                        for pattern in exclude_patterns:
                            if pattern in file_path:
                                should_exclude = True
                                break
                        
                        if not should_exclude:
                            arc_path = os.path.relpath(file_path, source_path)
                            zipf.write(file_path, arc_path)
    
    @staticmethod
    def extract_zip(archive_path, extract_to, password=None):
        """Extract ZIP archive"""
        with zipfile.ZipFile(archive_path, 'r') as zipf:
            if password:
                zipf.setpassword(password.encode())
            zipf.extractall(extract_to)
    
    @staticmethod
    def list_zip_contents(archive_path):
        """List contents of ZIP archive"""
        with zipfile.ZipFile(archive_path, 'r') as zipf:
            return [info.filename for info in zipf.filelist]


# Demo functions
def demo_file_operations():
    """Demonstrate file operations"""
    print("=== File Operations Demo ===")
    
    # Create test file with backup
    test_file = "test_file.txt"
    
    try:
        with FileManager(test_file, 'w', backup=True) as f:
            f.write("Hello, World!\n")
            f.write("This is a test file.\n")
        
        # Read file
        with FileManager(test_file, 'r') as f:
            content = f.read()
            print(f"File content:\n{content}")
        
        # Calculate checksum
        checksum = SecureFileHandler.calculate_checksum(test_file)
        print(f"File checksum: {checksum}")
        
    finally:
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)


def demo_json_processing():
    """Demonstrate JSON processing"""
    print("\n=== JSON Processing Demo ===")
    
    # Sample data with datetime
    data = {
        "name": "John Doe",
        "age": 30,
        "created_at": datetime.now(),
        "scores": [85, 92, 78, 96],
        "active": True
    }
    
    json_file = "sample.json"
    
    try:
        # Save JSON
        JSONProcessor.save_json(data, json_file)
        print(f"Saved data to {json_file}")
        
        # Load JSON
        loaded_data = JSONProcessor.load_json(json_file)
        print(f"Loaded data: {loaded_data}")
        
        # Validate schema
        schema = {
            "name": {"type": "string", "required": True},
            "age": {"type": "integer", "required": True},
            "active": {"type": "boolean", "required": False}
        }
        
        is_valid, error = JSONProcessor.validate_json_schema(loaded_data, schema)
        print(f"Schema validation: {is_valid}, Error: {error}")
        
    finally:
        if os.path.exists(json_file):
            os.remove(json_file)


def demo_csv_processing():
    """Demonstrate CSV processing"""
    print("\n=== CSV Processing Demo ===")
    
    csv_file = "sample.csv"
    
    try:
        # Create sample CSV
        sample_data = [
            {"name": "Alice", "age": "25", "score": "85.5", "active": "true"},
            {"name": "Bob", "age": "30", "score": "92.0", "active": "false"},
            {"name": "Charlie", "age": "35", "score": "78.5", "active": "true"}
        ]
        
        # Write CSV
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["name", "age", "score", "active"])
            writer.writeheader()
            writer.writerows(sample_data)
        
        # Read with type conversion
        type_converters = {
            "age": int,
            "score": float,
            "active": lambda x: x.lower() == 'true'
        }
        
        data = CSVProcessor.read_csv_with_types(csv_file, type_converters)
        print("CSV data with type conversion:")
        for row in data:
            print(f"  {row}")
        
        # Aggregate data
        aggregations = {
            "age": lambda values: sum(values) / len(values),  # Average
            "score": max  # Maximum
        }
        
        # Group by active status
        agg_results = CSVProcessor.aggregate_csv(csv_file, "active", aggregations)
        print("\nAggregated results:")
        for result in agg_results:
            print(f"  {result}")
        
    finally:
        if os.path.exists(csv_file):
            os.remove(csv_file)


def demo_database_operations():
    """Demonstrate database operations"""
    print("\n=== Database Operations Demo ===")
    
    db_file = "sample.db"
    
    try:
        with DatabaseManager(db_file) as db:
            # Create table
            columns = {
                "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
                "name": "TEXT NOT NULL",
                "age": "INTEGER",
                "email": "TEXT UNIQUE"
            }
            db.create_table("users", columns)
            
            # Insert data
            users = [
                {"name": "Alice", "age": 25, "email": "alice@example.com"},
                {"name": "Bob", "age": 30, "email": "bob@example.com"},
                {"name": "Charlie", "age": 35, "email": "charlie@example.com"}
            ]
            
            for user in users:
                user_id = db.insert("users", user)
                print(f"Inserted user with ID: {user_id}")
            
            # Select data
            all_users = db.select("users")
            print(f"\nAll users: {all_users}")
            
            # Select with condition
            young_users = db.select("users", where={"age": 25})
            print(f"Users aged 25: {young_users}")
            
            # Update data
            updated_count = db.update("users", {"age": 26}, {"name": "Alice"})
            print(f"Updated {updated_count} users")
            
            # Delete data
            deleted_count = db.delete("users", {"name": "Bob"})
            print(f"Deleted {deleted_count} users")
            
            # Final state
            final_users = db.select("users")
            print(f"Final users: {final_users}")
    
    finally:
        if os.path.exists(db_file):
            os.remove(db_file)


def run_file_processing_demos():
    """Run all file processing demonstrations"""
    print("File Processing & I/O Examples")
    print("=" * 40)
    
    demo_file_operations()
    demo_json_processing()
    demo_csv_processing()
    demo_database_operations()
    
    print("\nAll file processing demos completed!")


if __name__ == "__main__":
    run_file_processing_demos()
