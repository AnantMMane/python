# Module 6: Modules and Packages
## Organizing and Structuring Code

Welcome to Module 6! This module teaches you how to organize your Python code into modules and packages. You'll learn how to create reusable code libraries, manage imports, and structure large projects effectively.

## 🎯 Module Objectives

By the end of this module, you will be able to:
- Create and use modules effectively
- Organize code into packages
- Understand import mechanisms and search paths
- Work with standard library modules
- Use `__name__` and `__main__` patterns
- Create and distribute packages

## 📋 What You'll Learn

### 1. Module Fundamentals
- Creating and importing modules
- Module namespaces and attributes
- Import statements and aliasing
- Module reloading and caching

### 2. Package Organization
- Package structure and `__init__.py` files
- Relative vs absolute imports
- Package initialization and configuration
- Subpackage organization

### 3. Import System
- Module search paths
- Import hooks and customization
- Circular import handling
- Dynamic imports

### 4. Standard Library
- Common standard library modules
- Module documentation and help
- Best practices for module usage
- Third-party package management

## 🚀 Getting Started

### Prerequisites
- Completed Module 5 (Object-Oriented Programming)
- Understanding of Python classes and functions
- Basic knowledge of file systems

### Estimated Time
- **Reading**: 2-3 hours
- **Practice**: 3-4 hours
- **Exercises**: 2-3 hours
- **Total**: 7-10 hours

## 📚 Module Content

### Section 1: Module Fundamentals

#### Creating and Using Modules
A module is a Python file containing functions, classes, and variables that can be imported and used in other programs.

```python
# math_utils.py - A simple module
"""Mathematical utility functions."""

PI = 3.14159
E = 2.71828

def add(a, b):
    """Add two numbers."""
    return a + b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def power(base, exponent):
    """Raise base to the power of exponent."""
    return base ** exponent

def factorial(n):
    """Calculate factorial of n."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

class Calculator:
    """Simple calculator class."""
    
    def __init__(self):
        self.history = []
    
    def calculate(self, operation, a, b):
        """Perform calculation and store in history."""
        if operation == 'add':
            result = add(a, b)
        elif operation == 'multiply':
            result = multiply(a, b)
        elif operation == 'power':
            result = power(a, b)
        else:
            raise ValueError(f"Unknown operation: {operation}")
        
        self.history.append(f"{operation}({a}, {b}) = {result}")
        return result
    
    def get_history(self):
        """Get calculation history."""
        return self.history.copy()
```

#### Importing Modules
```python
# main.py - Using the math_utils module
import math_utils

# Access module attributes
print(f"PI: {math_utils.PI}")
print(f"E: {math_utils.E}")

# Use module functions
result = math_utils.add(5, 3)
print(f"5 + 3 = {result}")

# Use module classes
calc = math_utils.Calculator()
calc.calculate('add', 10, 20)
calc.calculate('multiply', 4, 5)
print("History:", calc.get_history())

# Import specific items
from math_utils import add, multiply, PI
print(f"Imported PI: {PI}")
print(f"10 * 5 = {multiply(10, 5)}")

# Import with aliasing
import math_utils as math_utils
from math_utils import Calculator as Calc

calc = Calc()
result = calc.calculate('power', 2, 8)
print(f"2^8 = {result}")

# Import all (not recommended)
from math_utils import *
print(f"PI from * import: {PI}")
```

### Section 2: Package Organization

#### Creating Packages
A package is a directory containing multiple modules and an `__init__.py` file.

```python
# my_package/__init__.py
"""My package for mathematical operations."""

from .math_utils import add, multiply, power, factorial
from .geometry import Circle, Rectangle
from .statistics import mean, median, mode

__version__ = "1.0.0"
__author__ = "Your Name"

# Package-level variables
PACKAGE_NAME = "my_package"
DESCRIPTION = "A collection of mathematical utilities"

def get_info():
    """Get package information."""
    return {
        'name': PACKAGE_NAME,
        'version': __version__,
        'description': DESCRIPTION,
        'author': __author__
    }

# my_package/geometry.py
"""Geometry-related classes and functions."""

import math

class Circle:
    """Circle class."""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        """Calculate circle area."""
        return math.pi * self.radius ** 2
    
    def circumference(self):
        """Calculate circle circumference."""
        return 2 * math.pi * self.radius

class Rectangle:
    """Rectangle class."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate rectangle area."""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate rectangle perimeter."""
        return 2 * (self.width + self.height)

# my_package/statistics.py
"""Statistical functions."""

def mean(numbers):
    """Calculate arithmetic mean."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    """Calculate median."""
    if not numbers:
        return 0
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    if n % 2 == 0:
        return (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        return sorted_numbers[n//2]

def mode(numbers):
    """Calculate mode (most frequent value)."""
    if not numbers:
        return None
    
    from collections import Counter
    counter = Counter(numbers)
    return counter.most_common(1)[0][0]
```

#### Using Packages
```python
# main.py - Using the package
import my_package

# Get package info
info = my_package.get_info()
print(f"Package: {info['name']} v{info['version']}")

# Use package modules
from my_package import add, Circle, mean

# Math functions
result = add(15, 25)
print(f"15 + 25 = {result}")

# Geometry classes
circle = Circle(5)
print(f"Circle area: {circle.area():.2f}")

# Statistics functions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Mean: {mean(numbers)}")

# Import specific modules
from my_package import geometry, statistics

rect = geometry.Rectangle(4, 6)
print(f"Rectangle area: {rect.area()}")

data = [1, 2, 2, 3, 4, 4, 4, 5]
print(f"Mode: {statistics.mode(data)}")
```

### Section 3: Import System

#### Module Search Paths
Python searches for modules in specific locations defined by `sys.path`.

```python
# explore_paths.py
import sys
import os

def explore_module_paths():
    """Explore Python module search paths."""
    print("Python Module Search Paths:")
    print("=" * 50)
    
    for i, path in enumerate(sys.path, 1):
        print(f"{i:2d}. {path}")
        if os.path.exists(path):
            print(f"    Exists: Yes")
            if os.path.isdir(path):
                print(f"    Type: Directory")
            else:
                print(f"    Type: File")
        else:
            print(f"    Exists: No")
        print()

def add_custom_path(path):
    """Add a custom path to module search."""
    if path not in sys.path:
        sys.path.append(path)
        print(f"Added path: {path}")
    else:
        print(f"Path already exists: {path}")

def find_module_location(module_name):
    """Find where a module is located."""
    try:
        module = __import__(module_name)
        if hasattr(module, '__file__'):
            return module.__file__
        else:
            return "Built-in module (no file location)"
    except ImportError:
        return "Module not found"

# Explore paths
explore_module_paths()

# Add custom path
custom_path = "/path/to/your/modules"
add_custom_path(custom_path)

# Find module locations
modules_to_find = ['os', 'sys', 'math', 'requests']
print("\nModule Locations:")
print("=" * 30)
for module in modules_to_find:
    location = find_module_location(module)
    print(f"{module}: {location}")
```

#### Import Mechanisms
```python
# import_examples.py
"""Examples of different import mechanisms."""

# Standard import
import os
import sys

# Import with alias
import datetime as dt
import json as js

# Import specific items
from math import pi, sqrt, cos
from random import choice, randint

# Import with alias for specific items
from collections import defaultdict as dd, Counter as cnt

# Conditional imports
try:
    import numpy as np
    NUMPY_AVAILABLE = True
except ImportError:
    NUMPY_AVAILABLE = False
    print("NumPy not available")

# Dynamic imports
def import_module_dynamically(module_name):
    """Import a module dynamically."""
    try:
        module = __import__(module_name)
        return module
    except ImportError as e:
        print(f"Failed to import {module_name}: {e}")
        return None

# Test dynamic import
math_module = import_module_dynamically('math')
if math_module:
    print(f"Math module imported: {math_module.pi}")

# Import from package
from my_package.geometry import Circle
from my_package.statistics import mean

# Relative imports (when inside a package)
# from .math_utils import add
# from ..other_package import some_function
```

### Section 4: Standard Library Modules

#### Common Standard Library Modules
```python
# standard_library_demo.py
"""Demonstration of common standard library modules."""

import os
import sys
import datetime
import json
import csv
import random
import math
import statistics
import collections
import itertools

def demonstrate_os_module():
    """Demonstrate OS module functionality."""
    print("OS Module Examples:")
    print("-" * 30)
    
    # Current working directory
    print(f"Current directory: {os.getcwd()}")
    
    # List directory contents
    print(f"Directory contents: {os.listdir('.')[:5]}")  # First 5 items
    
    # Environment variables
    print(f"Python version: {sys.version}")
    print(f"Platform: {sys.platform}")
    
    # File operations
    if os.path.exists('test_file.txt'):
        print("test_file.txt exists")
    else:
        print("test_file.txt does not exist")

def demonstrate_datetime_module():
    """Demonstrate datetime module functionality."""
    print("\nDatetime Module Examples:")
    print("-" * 30)
    
    # Current time
    now = datetime.datetime.now()
    print(f"Current time: {now}")
    print(f"Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Date arithmetic
    tomorrow = now + datetime.timedelta(days=1)
    print(f"Tomorrow: {tomorrow.date()}")
    
    # Parsing dates
    date_string = "2024-01-15"
    parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    print(f"Parsed date: {parsed_date}")

def demonstrate_collections_module():
    """Demonstrate collections module functionality."""
    print("\nCollections Module Examples:")
    print("-" * 30)
    
    # DefaultDict
    word_count = collections.defaultdict(int)
    text = "hello world hello python world"
    for word in text.split():
        word_count[word] += 1
    
    print(f"Word count: {dict(word_count)}")
    
    # Counter
    counter = collections.Counter([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    print(f"Most common: {counter.most_common(2)}")
    
    # NamedTuple
    Point = collections.namedtuple('Point', ['x', 'y'])
    p = Point(3, 4)
    print(f"Point: {p}, x={p.x}, y={p.y}")

def demonstrate_itertools_module():
    """Demonstrate itertools module functionality."""
    print("\nItertools Module Examples:")
    print("-" * 30)
    
    # Infinite iterators
    counter = itertools.count(1, 2)  # Start at 1, step by 2
    first_five = list(itertools.islice(counter, 5))
    print(f"First 5 odd numbers: {first_five}")
    
    # Combinations
    letters = ['A', 'B', 'C']
    combinations = list(itertools.combinations(letters, 2))
    print(f"Combinations of 2: {combinations}")
    
    # Permutations
    permutations = list(itertools.permutations(letters, 2))
    print(f"Permutations of 2: {permutations}")

# Run demonstrations
if __name__ == "__main__":
    demonstrate_os_module()
    demonstrate_datetime_module()
    demonstrate_collections_module()
    demonstrate_itertools_module()
```

### Section 5: Advanced Module Features

#### `__name__` and `__main__` Pattern
```python
# module_with_main.py
"""Module demonstrating __name__ and __main__ pattern."""

def utility_function():
    """A utility function."""
    return "Utility function called"

def another_function():
    """Another function."""
    return "Another function called"

# This code runs when the module is imported
print(f"This module's name: {__name__}")

# This code only runs when the module is run directly
if __name__ == "__main__":
    print("This module is being run directly")
    print(utility_function())
    print(another_function())
else:
    print("This module is being imported")

# main.py - Importing the module
import module_with_main

print("In main.py")
print(module_with_main.utility_function())
```

#### Module Reloading
```python
# reload_demo.py
"""Demonstrate module reloading."""

import importlib
import time

def demonstrate_reloading():
    """Demonstrate module reloading."""
    print("Module Reloading Demo:")
    print("=" * 30)
    
    # Import a module
    import my_module
    
    # Use the module
    print(f"Initial value: {my_module.VALUE}")
    print(f"Initial function: {my_module.get_value()}")
    
    # Simulate module modification
    print("\nModifying module file...")
    time.sleep(2)  # Simulate file modification
    
    # Reload the module
    print("Reloading module...")
    importlib.reload(my_module)
    
    # Use the reloaded module
    print(f"New value: {my_module.VALUE}")
    print(f"New function: {my_module.get_value()}")

# Note: This requires a separate my_module.py file that can be modified
```

## 💻 Hands-On Practice

### Exercise 1: Create a Utility Package
Create a package with various utility modules:

```python
# utilities/__init__.py
"""Utilities package for common operations."""

from .string_utils import reverse_string, count_words, is_palindrome
from .number_utils import is_prime, factorial, fibonacci
from .file_utils import read_file, write_file, append_file

__version__ = "1.0.0"

def get_package_info():
    """Get package information."""
    return {
        'name': 'utilities',
        'version': __version__,
        'modules': ['string_utils', 'number_utils', 'file_utils']
    }

# utilities/string_utils.py
"""String utility functions."""

def reverse_string(text):
    """Reverse a string."""
    return text[::-1]

def count_words(text):
    """Count words in a string."""
    return len(text.split())

def is_palindrome(text):
    """Check if string is palindrome."""
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

# utilities/number_utils.py
"""Number utility functions."""

def is_prime(n):
    """Check if number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    """Calculate factorial."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Calculate nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# utilities/file_utils.py
"""File utility functions."""

def read_file(filename):
    """Read file content."""
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f"File {filename} not found"
    except Exception as e:
        return f"Error reading file: {e}"

def write_file(filename, content):
    """Write content to file."""
    try:
        with open(filename, 'w') as f:
            f.write(content)
        return f"Successfully wrote to {filename}"
    except Exception as e:
        return f"Error writing file: {e}"

def append_file(filename, content):
    """Append content to file."""
    try:
        with open(filename, 'a') as f:
            f.write(content)
        return f"Successfully appended to {filename}"
    except Exception as e:
        return f"Error appending to file: {e}"

# main.py - Using the utilities package
import utilities

# Get package info
info = utilities.get_package_info()
print(f"Package: {info['name']} v{info['version']}")

# Use string utilities
from utilities import reverse_string, count_words, is_palindrome

text = "Hello World Python"
print(f"Original: {text}")
print(f"Reversed: {reverse_string(text)}")
print(f"Word count: {count_words(text)}")
print(f"Is palindrome: {is_palindrome(text)}")

# Use number utilities
from utilities import is_prime, factorial, fibonacci

print(f"Is 17 prime? {is_prime(17)}")
print(f"Factorial of 5: {factorial(5)}")
print(f"Fibonacci(10): {fibonacci(10)}")

# Use file utilities
from utilities import write_file, read_file, append_file

# Write to file
write_file("test.txt", "Hello, this is a test file!")
print("File written successfully")

# Read from file
content = read_file("test.txt")
print(f"File content: {content}")

# Append to file
append_file("test.txt", "\nThis is appended content!")
print("Content appended successfully")

# Read updated file
updated_content = read_file("test.txt")
print(f"Updated content: {updated_content}")
```

### Exercise 2: Module Import Manager
Create a system to manage module imports:

```python
# import_manager.py
"""Module import manager with caching and error handling."""

import sys
import importlib
import importlib.util
from typing import Dict, Any, Optional

class ImportManager:
    """Manages module imports with caching and error handling."""
    
    def __init__(self):
        self.cache: Dict[str, Any] = {}
        self.failed_imports: Dict[str, str] = {}
    
    def import_module(self, module_name: str, alias: Optional[str] = None) -> Optional[Any]:
        """Import a module with caching."""
        cache_key = alias or module_name
        
        # Check cache first
        if cache_key in self.cache:
            print(f"Using cached import: {cache_key}")
            return self.cache[cache_key]
        
        # Check if import previously failed
        if module_name in self.failed_imports:
            print(f"Import previously failed: {module_name}")
            return None
        
        try:
            # Attempt import
            module = importlib.import_module(module_name)
            self.cache[cache_key] = module
            print(f"Successfully imported: {module_name}")
            return module
            
        except ImportError as e:
            error_msg = f"Failed to import {module_name}: {e}"
            self.failed_imports[module_name] = str(e)
            print(error_msg)
            return None
    
    def import_from_module(self, module_name: str, item_name: str) -> Optional[Any]:
        """Import specific item from a module."""
        module = self.import_module(module_name)
        if module is None:
            return None
        
        try:
            item = getattr(module, item_name)
            print(f"Imported {item_name} from {module_name}")
            return item
        except AttributeError:
            error_msg = f"Item {item_name} not found in {module_name}"
            print(error_msg)
            return None
    
    def reload_module(self, module_name: str) -> bool:
        """Reload a previously imported module."""
        if module_name not in self.cache:
            print(f"Module {module_name} not in cache")
            return False
        
        try:
            importlib.reload(self.cache[module_name])
            print(f"Reloaded module: {module_name}")
            return True
        except Exception as e:
            print(f"Failed to reload {module_name}: {e}")
            return False
    
    def get_cache_info(self) -> Dict[str, Any]:
        """Get information about cached modules."""
        return {
            'cached_modules': list(self.cache.keys()),
            'failed_imports': self.failed_imports.copy(),
            'cache_size': len(self.cache)
        }
    
    def clear_cache(self):
        """Clear the import cache."""
        self.cache.clear()
        print("Import cache cleared")

# Test the import manager
if __name__ == "__main__":
    manager = ImportManager()
    
    # Import some modules
    os_module = manager.import_module('os')
    math_module = manager.import_module('math')
    
    # Import specific items
    pi_value = manager.import_from_module('math', 'pi')
    sqrt_func = manager.import_from_module('math', 'sqrt')
    
    # Try to import non-existent module
    fake_module = manager.import_module('non_existent_module')
    
    # Get cache info
    cache_info = manager.get_cache_info()
    print(f"\nCache info: {cache_info}")
    
    # Test reloading
    if 'math' in manager.cache:
        manager.reload_module('math')
    
    # Clear cache
    manager.clear_cache()
    print(f"Cache after clearing: {manager.get_cache_info()}")
```

## 📝 Module Quiz

### Quiz Questions
1. What is the purpose of the `__init__.py` file in a package?
2. What is the difference between `import module` and `from module import item`?
3. How do you reload a module in Python?
4. What does `if __name__ == "__main__":` do?
5. How can you add a custom path to Python's module search path?

### Quiz Answers
1. It marks a directory as a Python package and can contain package initialization code
2. `import module` imports the entire module, `from module import item` imports specific items
3. Use `importlib.reload(module)` or `reload(module)` in Python 2
4. It runs code only when the module is executed directly, not when imported
5. Add the path to `sys.path` list

## 🔍 Key Concepts Review

### Module Best Practices
- Keep modules focused on a single responsibility
- Use descriptive module names
- Document your modules with docstrings
- Handle import errors gracefully
- Use `__all__` to control what gets imported with `*`

### Package Organization
- Use `__init__.py` for package initialization
- Organize related modules logically
- Use relative imports within packages
- Provide clear package-level APIs
- Version your packages

### Import Guidelines
- Prefer explicit imports over wildcard imports
- Use aliases to avoid naming conflicts
- Import at the top of files
- Handle import errors appropriately
- Use virtual environments for dependency management

## 🎯 Module Checklist

- [ ] Understand module creation and usage
- [ ] Create and organize packages
- [ ] Master import statements and mechanisms
- [ ] Work with standard library modules
- [ ] Use `__name__` and `__main__` patterns
- [ ] Handle module reloading
- [ ] Complete hands-on exercises
- [ ] Take module quiz
- [ ] Review key concepts

## 🚀 Next Steps

1. **Complete Exercises**: Work through all hands-on exercises
2. **Practice Organization**: Create your own packages and modules
3. **Explore Standard Library**: Learn more standard library modules
4. **Move to Module 7**: String Processing

## 💡 Pro Tips

- **Start with simple modules** and build complexity gradually
- **Use virtual environments** to manage package dependencies
- **Follow PEP 8** for import organization
- **Document your modules** thoroughly
- **Test imports** in different contexts
- **Use `__init__.py`** to create clean package APIs

---

**Congratulations on completing Module 6! You now have a solid understanding of modules and packages in Python. In the next module, you'll learn about string processing and manipulation. Keep practicing and happy coding! 🐍✨**
