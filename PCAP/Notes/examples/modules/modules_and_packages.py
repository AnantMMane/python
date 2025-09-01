"""
Modules and Packages Examples
============================

This file demonstrates comprehensive module and package concepts in Python,
covering all topics needed for PCAP certification.

Topics covered:
- Module search path (sys.path)
- dir() for introspection
- Package structure (__init__.py)
- Relative/absolute imports
- __all__ variable
- Public/private variables
- __pycache__ directory
- __name__ variable
- Standard Library Modules (math, random, platform)
"""

import sys
import os
import math
import random
import platform
from typing import List, Dict, Any


def module_search_path():
    """Demonstrates module search path (sys.path)."""
    print("\n=== Module Search Path (sys.path) ===")
    
    print("Current module search path:")
    for i, path in enumerate(sys.path[:5], 1):  # Show first 5
        print(f"   {i}. {path}")
    
    # Add a directory to the search path
    new_path = os.path.join(os.getcwd(), 'custom_modules')
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    
    if new_path not in sys.path:
        sys.path.append(new_path)
        print(f"Added to search path: {new_path}")
    
    # Clean up
    if os.path.exists(new_path):
        os.rmdir(new_path)


def dir_introspection():
    """Demonstrates using dir() for module introspection."""
    print("\n=== Dir() for Introspection ===")
    
    # Introspecting math module
    math_attributes = dir(math)
    public_math_attrs = [attr for attr in dir(math) if not attr.startswith('_')]
    print(f"Math module public attributes (first 10): {public_math_attrs[:10]}")
    
    # Introspecting current module
    current_attrs = [attr for attr in dir() if not attr.startswith('_')]
    print(f"Current module public attributes: {current_attrs}")


def package_structure():
    """Demonstrates package structure and __init__.py files."""
    print("\n=== Package Structure ===")
    
    # Create a simple package structure
    package_dirs = ['my_package', 'my_package/submodule1']
    
    for dir_path in package_dirs:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
    
    # Create __init__.py files
    main_init_content = '''"""
My Package - A demonstration package
"""

__version__ = "1.0.0"
__author__ = "Python Developer"

from .submodule1 import calculator

__all__ = ['calculator', '__version__', '__author__']
'''
    
    with open('my_package/__init__.py', 'w') as f:
        f.write(main_init_content)
    
    # Create a simple module
    calculator_content = '''"""
Calculator functions
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b
'''
    
    with open('my_package/submodule1/calculator.py', 'w') as f:
        f.write(calculator_content)
    
    # Test the package
    try:
        import my_package
        print(f"Package imported: {my_package.__version__}")
        print(f"Calculator add(5, 3): {my_package.calculator.add(5, 3)}")
    except ImportError as e:
        print(f"Import error: {e}")
    
    # Clean up
    import shutil
    if os.path.exists('my_package'):
        shutil.rmtree('my_package')


def import_examples():
    """Demonstrates different import styles."""
    print("\n=== Import Examples ===")
    
    # Absolute imports
    import math
    print(f"math.pi: {math.pi}")
    
    # Import specific items
    from math import sqrt, pi
    print(f"sqrt(16): {sqrt(16)}")
    print(f"pi: {pi}")
    
    # Import with aliases
    import random as rand
    print(f"rand.random(): {rand.random()}")
    
    # Conditional imports
    try:
        import json
        print(f"json.dumps({{'key': 'value'}}): {json.dumps({'key': 'value'})}")
    except ImportError:
        print("json module not available")


def all_variable():
    """Demonstrates the __all__ variable."""
    print("\n=== __all__ Variable ===")
    
    # Create a module with __all__
    all_module_content = '''"""
Module demonstrating __all__ variable
"""

def public_function():
    """This function is public."""
    return "Public function"

def _private_function():
    """This function is private."""
    return "Private function"

PUBLIC_CONSTANT = 42
_PRIVATE_CONSTANT = 100

__all__ = ['public_function', 'PUBLIC_CONSTANT']
'''
    
    with open('all_demo.py', 'w') as f:
        f.write(all_module_content)
    
    try:
        import all_demo
        print(f"Module __all__: {all_demo.__all__}")
        print(f"Public function: {all_demo.public_function()}")
        print(f"Public constant: {all_demo.PUBLIC_CONSTANT}")
    except ImportError as e:
        print(f"Import error: {e}")
    
    # Clean up
    if os.path.exists('all_demo.py'):
        os.remove('all_demo.py')


def public_private_variables():
    """Demonstrates public and private variables in modules."""
    print("\n=== Public/Private Variables ===")
    
    # Create module with public/private variables
    privacy_module_content = '''"""
Module demonstrating public and private variables
"""

PUBLIC_CONSTANT = "This is public"
_private_variable = "This is private"
__mangled_variable = "This is name-mangled"

def public_function():
    """This function is public."""
    return "Public function"

def _private_function():
    """This function is private."""
    return "Private function"

def __mangled_function():
    """This function is name-mangled."""
    return "Name-mangled function"
'''
    
    with open('privacy_demo.py', 'w') as f:
        f.write(privacy_module_content)
    
    try:
        import privacy_demo
        
        # Public variables
        print(f"PUBLIC_CONSTANT: {privacy_demo.PUBLIC_CONSTANT}")
        print(f"public_function(): {privacy_demo.public_function()}")
        
        # Private variables (still accessible)
        print(f"_private_variable: {privacy_demo._private_variable}")
        print(f"_private_function(): {privacy_demo._private_function()}")
        
        # Name-mangled variables
        print(f"__mangled_variable: {privacy_demo._privacy_demo__mangled_variable}")
        print(f"__mangled_function(): {privacy_demo._privacy_demo__mangled_function()}")
        
    except ImportError as e:
        print(f"Import error: {e}")
    
    # Clean up
    if os.path.exists('privacy_demo.py'):
        os.remove('privacy_demo.py')


def pycache_demo():
    """Demonstrates __pycache__ directory behavior."""
    print("\n=== __pycache__ Directory ===")
    
    # Create a module to trigger __pycache__
    cache_module_content = '''"""
Module to demonstrate __pycache__ behavior
"""

def cache_function():
    """Function that will be cached."""
    return "This function is cached"

CACHE_CONSTANT = "This constant is cached"
'''
    
    with open('cache_demo.py', 'w') as f:
        f.write(cache_module_content)
    
    try:
        import cache_demo
        print(f"Module imported: {cache_demo}")
        
        # Check for __pycache__ directory
        cache_dir = '__pycache__'
        if os.path.exists(cache_dir):
            print(f"__pycache__ directory exists")
            cache_files = os.listdir(cache_dir)
            print(f"Cache files: {cache_files}")
        else:
            print("__pycache__ directory not found")
        
    except ImportError as e:
        print(f"Import error: {e}")
    
    # Clean up
    if os.path.exists('__pycache__'):
        import shutil
        shutil.rmtree('__pycache__')
    if os.path.exists('cache_demo.py'):
        os.remove('cache_demo.py')


def name_variable():
    """Demonstrates the __name__ variable."""
    print("\n=== __name__ Variable ===")
    
    print(f"Current module __name__: {__name__}")
    
    # Create a module to demonstrate __name__
    name_module_content = '''"""
Module demonstrating __name__ variable
"""

print(f"Module __name__: {__name__}")

if __name__ == "__main__":
    print("Module is being run directly")
else:
    print("Module is being imported")

def demo_function():
    """Demo function."""
    return "Demo function called"
'''
    
    with open('name_demo.py', 'w') as f:
        f.write(name_module_content)
    
    try:
        import name_demo
        print(f"Imported module name: {name_demo.__name__}")
    except ImportError as e:
        print(f"Import error: {e}")
    
    # Clean up
    if os.path.exists('name_demo.py'):
        os.remove('name_demo.py')


def standard_library_modules():
    """Demonstrates standard library modules."""
    print("\n=== Standard Library Modules ===")
    
    # Math module
    print("Math module:")
    print(f"   pi: {math.pi}")
    print(f"   sqrt(16): {math.sqrt(16)}")
    print(f"   ceil(3.7): {math.ceil(3.7)}")
    
    # Random module
    print("\nRandom module:")
    print(f"   random(): {random.random()}")
    print(f"   randint(1, 10): {random.randint(1, 10)}")
    print(f"   choice(['a', 'b', 'c']): {random.choice(['a', 'b', 'c'])}")
    
    # Platform module
    print("\nPlatform module:")
    print(f"   system(): {platform.system()}")
    print(f"   machine(): {platform.machine()}")
    print(f"   python_version(): {platform.python_version()}")
    
    # OS module
    print("\nOS module:")
    print(f"   getcwd(): {os.getcwd()}")
    print(f"   name: {os.name}")
    
    # Sys module
    print("\nSys module:")
    print(f"   platform: {sys.platform}")
    print(f"   executable: {sys.executable}")


if __name__ == "__main__":
    print("Modules and Packages Examples")
    print("=" * 50)
    
    # Run all demonstrations
    module_search_path()
    dir_introspection()
    package_structure()
    import_examples()
    all_variable()
    public_private_variables()
    pycache_demo()
    name_variable()
    standard_library_modules()
    
    print("\n" + "=" * 50)
    print("Modules and packages examples completed!")
