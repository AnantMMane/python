"""
File Operations Examples
=======================

This file demonstrates comprehensive file handling concepts in Python,
covering all topics needed for PCAP certification.

Topics covered:
- File opening modes (text, binary, r, w, a, x, r+, w+, a+)
- with statement (context manager)
- Reading files (read, readline, readlines, iteration)
- Writing files (write, writelines, print)
- errno variable and error values
- Predefined streams (sys.stdin, sys.stdout, sys.stderr)
- Handles vs. streams
"""

import sys
import os
import errno
from typing import List, Dict, Any, Optional


def file_opening_modes():
    """Demonstrates different file opening modes."""
    print("\n=== File Opening Modes ===")
    
    # Create a test file for demonstrations
    test_content = "Hello, World!\nThis is a test file.\nPython file operations."
    
    # Example 1: Write mode ('w')
    print("1. Write mode ('w'):")
    with open('test_file.txt', 'w') as file:
        file.write(test_content)
    print("   File created and written successfully")
    
    # Example 2: Read mode ('r')
    print("\n2. Read mode ('r'):")
    with open('test_file.txt', 'r') as file:
        content = file.read()
        print(f"   Content: {repr(content)}")
    
    # Example 3: Append mode ('a')
    print("\n3. Append mode ('a'):")
    with open('test_file.txt', 'a') as file:
        file.write("\nThis line was appended.")
    
    # Read again to see the appended content
    with open('test_file.txt', 'r') as file:
        content = file.read()
        print(f"   Content after append: {repr(content)}")
    
    # Example 4: Exclusive creation mode ('x')
    print("\n4. Exclusive creation mode ('x'):")
    try:
        with open('new_file.txt', 'x') as file:
            file.write("This is a new file created with 'x' mode.")
        print("   New file created successfully")
    except FileExistsError:
        print("   File already exists (expected behavior)")
    
    # Example 5: Read and write mode ('r+')
    print("\n5. Read and write mode ('r+'):")
    with open('test_file.txt', 'r+') as file:
        # Read first
        content = file.read()
        print(f"   Original content: {repr(content)}")
        
        # Go to beginning and write
        file.seek(0)
        file.write("Modified: ")
        
        # Read again
        file.seek(0)
        new_content = file.read()
        print(f"   Modified content: {repr(new_content)}")
    
    # Example 6: Write and read mode ('w+')
    print("\n6. Write and read mode ('w+'):")
    with open('test_file.txt', 'w+') as file:
        # Write first (truncates the file)
        file.write("Fresh content with w+ mode")
        
        # Read what we wrote
        file.seek(0)
        content = file.read()
        print(f"   Content: {repr(content)}")
    
    # Example 7: Append and read mode ('a+')
    print("\n7. Append and read mode ('a+'):")
    with open('test_file.txt', 'a+') as file:
        # Append content
        file.write("\nAppended with a+ mode")
        
        # Read entire file
        file.seek(0)
        content = file.read()
        print(f"   Content: {repr(content)}")
    
    # Clean up test files
    for filename in ['test_file.txt', 'new_file.txt']:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"   Cleaned up {filename}")


def binary_file_operations():
    """Demonstrates binary file operations."""
    print("\n=== Binary File Operations ===")
    
    # Example 1: Writing binary data
    print("1. Writing binary data:")
    binary_data = bytes([65, 66, 67, 68, 69, 70])  # ABCDEF in ASCII
    
    with open('binary_file.bin', 'wb') as file:
        file.write(binary_data)
    print(f"   Wrote {len(binary_data)} bytes to binary file")
    
    # Example 2: Reading binary data
    print("\n2. Reading binary data:")
    with open('binary_file.bin', 'rb') as file:
        read_data = file.read()
        print(f"   Read data: {read_data}")
        print(f"   As integers: {list(read_data)}")
        print(f"   As ASCII: {read_data.decode('ascii')}")
    
    # Example 3: Binary file with mixed data
    print("\n3. Binary file with mixed data:")
    mixed_data = b'Hello\x00World\x00\x01\x02\x03'
    
    with open('mixed_file.bin', 'wb') as file:
        file.write(mixed_data)
    
    with open('mixed_file.bin', 'rb') as file:
        data = file.read()
        print(f"   Raw data: {data}")
        print(f"   Hex representation: {data.hex()}")
    
    # Clean up
    for filename in ['binary_file.bin', 'mixed_file.bin']:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"   Cleaned up {filename}")


def reading_files():
    """Demonstrates different ways to read files."""
    print("\n=== Reading Files ===")
    
    # Create a test file with multiple lines
    test_lines = [
        "First line of the file",
        "Second line with some content",
        "Third line for demonstration",
        "Fourth line to show different reading methods",
        "Fifth and final line"
    ]
    
    with open('reading_test.txt', 'w') as file:
        file.write('\n'.join(test_lines))
    
    # Example 1: read() method
    print("1. read() method:")
    with open('reading_test.txt', 'r') as file:
        content = file.read()
        print(f"   Full content: {repr(content)}")
    
    # Example 2: readline() method
    print("\n2. readline() method:")
    with open('reading_test.txt', 'r') as file:
        line1 = file.readline()
        line2 = file.readline()
        print(f"   First line: {repr(line1)}")
        print(f"   Second line: {repr(line2)}")
    
    # Example 3: readlines() method
    print("\n3. readlines() method:")
    with open('reading_test.txt', 'r') as file:
        lines = file.readlines()
        print(f"   All lines: {lines}")
        print(f"   Number of lines: {len(lines)}")
    
    # Example 4: File iteration
    print("\n4. File iteration:")
    with open('reading_test.txt', 'r') as file:
        for i, line in enumerate(file, 1):
            print(f"   Line {i}: {repr(line.rstrip())}")
    
    # Example 5: Reading with encoding
    print("\n5. Reading with encoding:")
    with open('reading_test.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(f"   UTF-8 content: {repr(content)}")
    
    # Example 6: Reading specific number of characters
    print("\n6. Reading specific number of characters:")
    with open('reading_test.txt', 'r') as file:
        first_10 = file.read(10)
        next_10 = file.read(10)
        print(f"   First 10 chars: {repr(first_10)}")
        print(f"   Next 10 chars: {repr(next_10)}")
    
    # Clean up
    if os.path.exists('reading_test.txt'):
        os.remove('reading_test.txt')
        print("   Cleaned up reading_test.txt")


def writing_files():
    """Demonstrates different ways to write files."""
    print("\n=== Writing Files ===")
    
    # Example 1: write() method
    print("1. write() method:")
    with open('write_test.txt', 'w') as file:
        file.write("This is written using write() method.\n")
        file.write("Multiple write() calls create multiple lines.\n")
        file.write("No automatic newline is added.")
    print("   File written using write() method")
    
    # Example 2: writelines() method
    print("\n2. writelines() method:")
    lines_to_write = [
        "First line from writelines\n",
        "Second line from writelines\n",
        "Third line from writelines\n"
    ]
    
    with open('writelines_test.txt', 'w') as file:
        file.writelines(lines_to_write)
    print("   File written using writelines() method")
    
    # Example 3: print() function with file
    print("\n3. print() function with file:")
    with open('print_test.txt', 'w') as file:
        print("This is written using print()", file=file)
        print("Multiple print() calls", file=file)
        print("Each print() adds a newline automatically", file=file)
        print("You can also specify separator and end", file=file, sep=' | ', end='\n---\n')
    print("   File written using print() function")
    
    # Example 4: Writing different data types
    print("\n4. Writing different data types:")
    with open('data_types.txt', 'w') as file:
        file.write(f"String: Hello World\n")
        file.write(f"Integer: {42}\n")
        file.write(f"Float: {3.14159}\n")
        file.write(f"Boolean: {True}\n")
        file.write(f"List: {[1, 2, 3, 4, 5]}\n")
        file.write(f"Dictionary: {{'key': 'value'}}\n")
    print("   File written with different data types")
    
    # Example 5: Appending to files
    print("\n5. Appending to files:")
    with open('data_types.txt', 'a') as file:
        file.write("\n--- Appended content ---\n")
        file.write("This content was appended to the existing file.\n")
        file.write("The original content is preserved.\n")
    print("   Content appended to existing file")
    
    # Clean up
    for filename in ['write_test.txt', 'writelines_test.txt', 'print_test.txt', 'data_types.txt']:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"   Cleaned up {filename}")


def with_statement_context_manager():
    """Demonstrates the with statement as a context manager."""
    print("\n=== With Statement (Context Manager) ===")
    
    # Example 1: Basic with statement
    print("1. Basic with statement:")
    try:
        with open('context_test.txt', 'w') as file:
            file.write("This file is managed by the with statement.\n")
            file.write("The file will be automatically closed.\n")
        print("   File written and automatically closed")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Example 2: Multiple files in one with statement
    print("\n2. Multiple files in one with statement:")
    try:
        with open('source.txt', 'w') as source, open('destination.txt', 'w') as dest:
            source.write("Source file content")
            dest.write("Destination file content")
        print("   Multiple files handled simultaneously")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Example 3: Reading and writing in the same with block
    print("\n3. Reading and writing in the same with block:")
    try:
        with open('source.txt', 'r') as source, open('copy.txt', 'w') as copy:
            content = source.read()
            copy.write(f"Copied: {content}")
        print("   File copied successfully")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Example 4: Exception handling with with statement
    print("\n4. Exception handling with with statement:")
    try:
        with open('nonexistent_file.txt', 'r') as file:
            content = file.read()
    except FileNotFoundError as e:
        print(f"   File not found: {e}")
    except Exception as e:
        print(f"   Other error: {e}")
    else:
        print("   File read successfully")
    finally:
        print("   With block completed (file automatically closed)")
    
    # Clean up
    for filename in ['context_test.txt', 'source.txt', 'destination.txt', 'copy.txt']:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"   Cleaned up {filename}")


def errno_and_error_handling():
    """Demonstrates errno variable and error handling in file operations."""
    print("\n=== Errno and Error Handling ===")
    
    # Example 1: Common file operation errors
    print("1. Common file operation errors:")
    
    # File not found
    try:
        with open('nonexistent.txt', 'r') as file:
            pass
    except FileNotFoundError as e:
        print(f"   FileNotFoundError: {e}")
        print(f"   Errno: {e.errno}")
        print(f"   Errno name: {errno.errorcode.get(e.errno, 'Unknown')}")
    
    # Permission denied
    try:
        # Try to write to a directory (which should fail)
        with open('/', 'w') as file:
            pass
    except PermissionError as e:
        print(f"   PermissionError: {e}")
        print(f"   Errno: {e.errno}")
    
    # Example 2: Using errno for specific error handling
    print("\n2. Using errno for specific error handling:")
    
    def safe_file_operation(filename, mode='r'):
        try:
            with open(filename, mode) as file:
                if mode == 'r':
                    return file.read()
                else:
                    file.write("Test content")
                    return "File written successfully"
        except FileNotFoundError as e:
            if e.errno == errno.ENOENT:
                return f"File '{filename}' does not exist"
            else:
                return f"File error: {e}"
        except PermissionError as e:
            if e.errno == errno.EACCES:
                return f"Permission denied accessing '{filename}'"
            else:
                return f"Permission error: {e}"
        except Exception as e:
            return f"Unexpected error: {e}"
    
    # Test the function
    print(f"   Result 1: {safe_file_operation('nonexistent.txt')}")
    print(f"   Result 2: {safe_file_operation('test_write.txt', 'w')}")
    
    # Clean up
    if os.path.exists('test_write.txt'):
        os.remove('test_write.txt')


def predefined_streams():
    """Demonstrates predefined streams (sys.stdin, sys.stdout, sys.stderr)."""
    print("\n=== Predefined Streams ===")
    
    # Example 1: sys.stdout
    print("1. sys.stdout:")
    sys.stdout.write("This is written to stdout using sys.stdout.write()\n")
    print("This is written using print() (goes to stdout)")
    
    # Example 2: sys.stderr
    print("\n2. sys.stderr:")
    sys.stderr.write("This is an error message written to stderr\n")
    print("Error message", file=sys.stderr)
    
    # Example 3: sys.stdin (simulated)
    print("\n3. sys.stdin (simulated):")
    print("   Note: In interactive mode, sys.stdin.read() would wait for input")
    print("   Here we simulate reading from stdin")
    
    # Example 4: Redirecting streams
    print("\n4. Redirecting streams:")
    
    # Save original streams
    original_stdout = sys.stdout
    original_stderr = sys.stderr
    
    try:
        # Redirect stdout to a file
        with open('stdout_redirect.txt', 'w') as stdout_file:
            sys.stdout = stdout_file
            print("This goes to the file instead of console")
            print("Multiple lines can be redirected")
        
        # Restore stdout
        sys.stdout = original_stdout
        print("   Stdout redirected to file and restored")
        
        # Read the redirected output
        with open('stdout_redirect.txt', 'r') as file:
            content = file.read()
            print(f"   Redirected content: {repr(content)}")
    
    finally:
        # Ensure streams are restored
        sys.stdout = original_stdout
        sys.stderr = original_stderr
    
    # Clean up
    if os.path.exists('stdout_redirect.txt'):
        os.remove('stdout_redirect.txt')
        print("   Cleaned up stdout_redirect.txt")


def handles_vs_streams():
    """Demonstrates the difference between handles and streams."""
    print("\n=== Handles vs Streams ===")
    
    # Example 1: File handle
    print("1. File handle:")
    file_handle = open('handle_test.txt', 'w')
    print(f"   File handle type: {type(file_handle)}")
    print(f"   File handle name: {file_handle.name}")
    print(f"   File handle mode: {file_handle.mode}")
    print(f"   File handle closed: {file_handle.closed}")
    
    # Write using handle
    file_handle.write("Content written using file handle\n")
    file_handle.close()
    print(f"   File handle closed: {file_handle.closed}")
    
    # Example 2: Stream (using with statement)
    print("\n2. Stream (using with statement):")
    with open('stream_test.txt', 'w') as stream:
        print(f"   Stream type: {type(stream)}")
        print(f"   Stream name: {stream.name}")
        print(f"   Stream mode: {stream.mode}")
        print(f"   Stream closed: {stream.closed}")
        stream.write("Content written using stream\n")
    
    print("   Stream automatically closed after with block")
    
    # Example 3: Reading with both approaches
    print("\n3. Reading with both approaches:")
    
    # Using handle
    handle = open('handle_test.txt', 'r')
    content1 = handle.read()
    handle.close()
    print(f"   Handle read: {repr(content1)}")
    
    # Using stream
    with open('stream_test.txt', 'r') as stream:
        content2 = stream.read()
    print(f"   Stream read: {repr(content2)}")
    
    # Clean up
    for filename in ['handle_test.txt', 'stream_test.txt']:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"   Cleaned up {filename}")


def practical_file_operations():
    """Demonstrates practical file operation scenarios."""
    print("\n=== Practical File Operations ===")
    
    # Example 1: Configuration file handling
    print("1. Configuration file handling:")
    
    config_data = {
        'database': {
            'host': 'localhost',
            'port': 5432,
            'name': 'myapp'
        },
        'logging': {
            'level': 'INFO',
            'file': 'app.log'
        }
    }
    
    # Write configuration
    with open('config.txt', 'w') as file:
        for section, settings in config_data.items():
            file.write(f"[{section}]\n")
            for key, value in settings.items():
                file.write(f"{key} = {value}\n")
            file.write("\n")
    
    print("   Configuration file written")
    
    # Read configuration
    config = {}
    current_section = None
    
    with open('config.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('[') and line.endswith(']'):
                current_section = line[1:-1]
                config[current_section] = {}
            elif '=' in line and current_section:
                key, value = line.split('=', 1)
                config[current_section][key.strip()] = value.strip()
    
    print(f"   Configuration read: {config}")
    
    # Example 2: Log file rotation
    print("\n2. Log file rotation:")
    
    def write_log_entry(message, log_file='app.log'):
        with open(log_file, 'a') as file:
            import datetime
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(f"[{timestamp}] {message}\n")
    
    # Write some log entries
    write_log_entry("Application started")
    write_log_entry("User login successful")
    write_log_entry("Database connection established")
    
    print("   Log entries written")
    
    # Read log file
    with open('app.log', 'r') as file:
        log_content = file.read()
        print(f"   Log content:\n{log_content}")
    
    # Example 3: CSV-like file processing
    print("\n3. CSV-like file processing:")
    
    # Create CSV-like data
    csv_data = [
        "Name,Age,City",
        "John,25,New York",
        "Jane,30,Los Angeles",
        "Bob,35,Chicago"
    ]
    
    with open('users.csv', 'w') as file:
        for line in csv_data:
            file.write(line + '\n')
    
    # Process CSV-like file
    users = []
    with open('users.csv', 'r') as file:
        header = file.readline().strip().split(',')
        for line in file:
            values = line.strip().split(',')
            user = dict(zip(header, values))
            users.append(user)
    
    print(f"   Processed users: {users}")
    
    # Clean up
    for filename in ['config.txt', 'app.log', 'users.csv']:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"   Cleaned up {filename}")


if __name__ == "__main__":
    print("File Operations Examples")
    print("=" * 50)
    
    # Run all demonstrations
    file_opening_modes()
    binary_file_operations()
    reading_files()
    writing_files()
    with_statement_context_manager()
    errno_and_error_handling()
    predefined_streams()
    handles_vs_streams()
    practical_file_operations()
    
    print("\n" + "=" * 50)
    print("File operations examples completed!")
