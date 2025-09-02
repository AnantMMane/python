# Module 8: File Handling and I/O Operations
## Working with Files and Data Persistence

Welcome to Module 8! This module covers file handling, input/output operations, and data persistence in Python. You'll learn how to read from and write to files, handle different file formats, and manage file operations safely.

## 🎯 Module Objectives

By the end of this module, you will be able to:
- Understand file handling concepts and file types
- Read from and write to text and binary files
- Handle file operations safely with context managers
- Work with different file formats (CSV, JSON, etc.)
- Implement proper error handling for file operations
- Use file system operations and path handling

## 📋 What You'll Learn

### 1. File Handling Fundamentals
- File types and modes
- Opening and closing files
- File paths and directories
- File encoding considerations

### 2. Reading Files
- Reading entire files
- Reading line by line
- Reading specific portions
- Handling different encodings

### 3. Writing Files
- Writing text and data
- Appending to files
- Creating new files
- Safe file operations

### 4. Advanced File Operations
- Context managers (with statements)
- File system operations
- Working with directories
- File metadata and properties

## 🚀 Getting Started

### Prerequisites
- Complete Modules 1-7
- Basic understanding of Python syntax
- Familiarity with data types and control flow

### Setup
1. Ensure you have Python 3.8+ installed
2. Create a working directory for file operations
3. Have some sample text files ready for practice

## 📚 Core Concepts

### File Types and Modes

Python supports different file types and access modes:

```python
# Text files (default)
file = open("example.txt", "r")  # Read mode
file = open("example.txt", "w")  # Write mode
file = open("example.txt", "a")  # Append mode

# Binary files
file = open("image.jpg", "rb")   # Read binary
file = open("data.bin", "wb")    # Write binary

# Text mode with encoding
file = open("file.txt", "r", encoding="utf-8")
```

### File Modes
- `r`: Read (default)
- `w`: Write (overwrites existing content)
- `a`: Append (adds to existing content)
- `x`: Exclusive creation (fails if file exists)
- `b`: Binary mode
- `t`: Text mode (default)
- `+`: Read and write

## 💻 Hands-On Practice

### Exercise 1: Basic File Operations

Create a simple text file and perform basic operations:

```python
# Creating and writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n")
    file.write("Python file handling is awesome!")

# Reading the entire file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)

# Reading line by line
with open("sample.txt", "r") as file:
    print("\nLine by line:")
    for line_num, line in enumerate(file, 1):
        print(f"Line {line_num}: {line.rstrip()}")
```

### Exercise 2: File Information and Properties

Get information about files:

```python
import os
import time

def file_info(filename):
    """Display comprehensive file information."""
    if os.path.exists(filename):
        stat = os.stat(filename)
        
        print(f"File: {filename}")
        print(f"Size: {stat.st_size} bytes")
        print(f"Created: {time.ctime(stat.st_ctime)}")
        print(f"Modified: {time.ctime(stat.st_mtime)}")
        print(f"Accessed: {time.ctime(stat.st_atime)}")
        print(f"Permissions: {oct(stat.st_mode)}")
        
        # Check if it's a file or directory
        if os.path.isfile(filename):
            print("Type: File")
        elif os.path.isdir(filename):
            print("Type: Directory")
    else:
        print(f"File {filename} does not exist")

# Test the function
file_info("sample.txt")
```

### Exercise 3: Working with CSV Files

Handle CSV data:

```python
import csv

# Writing CSV data
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

with open("people.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Reading CSV data
with open("people.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"Name: {row[0]}, Age: {row[1]}, City: {row[2]}")
```

### Exercise 4: JSON File Operations

Work with JSON data:

```python
import json

# Sample data
person = {
    "name": "John Doe",
    "age": 30,
    "city": "Boston",
    "skills": ["Python", "JavaScript", "SQL"],
    "active": True
}

# Write JSON to file
with open("person.json", "w") as file:
    json.dump(person, file, indent=2)

# Read JSON from file
with open("person.json", "r") as file:
    loaded_person = json.load(file)
    print("Loaded person data:")
    print(json.dumps(loaded_person, indent=2))
```

### Exercise 5: File Copying and Moving

File system operations:

```python
import shutil
import os

def safe_copy_file(source, destination):
    """Safely copy a file with error handling."""
    try:
        # Create destination directory if it doesn't exist
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        
        # Copy the file
        shutil.copy2(source, destination)
        print(f"Successfully copied {source} to {destination}")
        
    except FileNotFoundError:
        print(f"Source file {source} not found")
    except PermissionError:
        print(f"Permission denied for {destination}")
    except Exception as e:
        print(f"Error copying file: {e}")

def safe_move_file(source, destination):
    """Safely move a file with error handling."""
    try:
        # Create destination directory if it doesn't exist
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        
        # Move the file
        shutil.move(source, destination)
        print(f"Successfully moved {source} to {destination}")
        
    except FileNotFoundError:
        print(f"Source file {source} not found")
    except PermissionError:
        print(f"Permission denied for {destination}")
    except Exception as e:
        print(f"Error moving file: {e}")

# Test the functions
safe_copy_file("sample.txt", "backup/sample_backup.txt")
safe_move_file("people.csv", "data/people.csv")
```

## 🧪 Module Quiz

Test your understanding with these questions:

### Question 1
What happens when you open a file in "w" mode if the file already exists?
- A) The file is opened for reading
- B) The existing content is preserved
- C) The existing content is overwritten
- D) An error occurs

**Answer: C** - Write mode overwrites existing content.

### Question 2
Which of the following is the recommended way to handle files in Python?
- A) `file = open("file.txt"); file.close()`
- B) `with open("file.txt") as file:`
- C) `try: file = open("file.txt"); finally: file.close()`
- D) All of the above

**Answer: B** - Context managers (with statements) automatically handle file closing.

### Question 3
What does the `encoding` parameter do when opening a file?
- A) Determines file compression
- B) Specifies how to interpret the file's bytes as text
- C) Sets file permissions
- D) Defines file format

**Answer: B** - Encoding specifies how bytes are interpreted as text characters.

### Question 4
Which method reads a file line by line?
- A) `file.read()`
- B) `file.readline()`
- C) `file.readlines()`
- D) Iterating over the file object

**Answer: D** - Iterating over the file object reads line by line efficiently.

### Question 5
What is the purpose of the `newline=""` parameter when working with CSV files?
- A) To create new lines in the CSV
- B) To handle line ending differences between operating systems
- C) To add empty rows
- D) To specify the delimiter

**Answer: B** - It handles line ending differences between operating systems.

## 🔑 Key Concepts Review

### File Handling Best Practices
1. **Always use context managers** (`with` statements) for automatic resource cleanup
2. **Handle exceptions** when working with files
3. **Specify encoding** for text files to avoid encoding issues
4. **Close files explicitly** if not using context managers
5. **Use appropriate file modes** for your operations

### Common File Operations
- **Reading**: `read()`, `readline()`, `readlines()`, iteration
- **Writing**: `write()`, `writelines()`
- **Seeking**: `seek()` for positioning within files
- **Flushing**: `flush()` for immediate writing

### File System Operations
- **Path handling**: `os.path` module
- **Directory operations**: `os.mkdir()`, `os.rmdir()`, `shutil.rmtree()`
- **File operations**: `os.rename()`, `shutil.copy()`, `shutil.move()`
- **File information**: `os.stat()`, `os.path.getsize()`

## ✅ Module Checklist

Before moving to the next module, ensure you can:

- [ ] Open and close files using context managers
- [ ] Read from text and binary files
- [ ] Write data to files safely
- [ ] Handle file encoding issues
- [ ] Work with CSV and JSON files
- [ ] Perform basic file system operations
- [ ] Implement proper error handling for file operations
- [ ] Use file paths and directories correctly

## 🚀 Next Steps

After completing this module:

1. **Practice file operations** with different file types
2. **Experiment with encoding** to understand text handling
3. **Build a file management tool** as a project
4. **Move to Module 9** to learn about modules and packages
5. **Review file handling** in your previous code examples

## 💡 Pro Tips

### Performance Optimization
- Use `readline()` or iteration for large files instead of `read()`
- Buffer writes for better performance with many small writes
- Use `shutil.copyfile()` for faster file copying

### Error Handling
- Always check if files exist before operations
- Handle permission errors gracefully
- Use try-except blocks for file operations

### File Organization
- Organize files in logical directory structures
- Use descriptive file names
- Implement backup strategies for important data

### Cross-Platform Compatibility
- Use `os.path.join()` for path construction
- Handle line endings with `newline=""`
- Consider different file system limitations

## 🔗 Related Topics

- **Module 3**: Control Flow (for conditional file operations)
- **Module 4**: Functions and Data Structures (for organizing file operations)
- **Module 6**: Modules and Packages (for file organization)
- **Module 7**: String Processing (for text file manipulation)

---

**Ready to master file handling?** Start with the exercises above and practice with your own files. Remember, file operations are fundamental to most real-world Python applications!
