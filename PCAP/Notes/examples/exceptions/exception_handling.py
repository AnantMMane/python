"""
Exception Handling Examples
===========================

This file demonstrates comprehensive exception handling concepts in Python,
covering all topics needed for PCAP certification.

Topics covered:
- Exception hierarchy and types
- try-except-else-finally blocks
- Multiple exception handling
- Raising exceptions
- assert statement
- Custom exceptions
- Exception chaining
- Exception objects and properties
"""

import sys
import traceback
from typing import Union, List, Dict, Any


def basic_exception_handling():
    """Basic try-except block demonstration."""
    print("\n=== Basic Exception Handling ===")
    
    # Example 1: Division by zero
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    
    # Example 2: Index out of range
    try:
        numbers = [1, 2, 3]
        print(numbers[10])
    except IndexError as e:
        print(f"Caught IndexError: {e}")
    
    # Example 3: Key error
    try:
        person = {"name": "John", "age": 30}
        print(person["city"])
    except KeyError as e:
        print(f"Caught KeyError: {e}")


def try_except_else_finally():
    """Demonstrates try-except-else-finally blocks."""
    print("\n=== Try-Except-Else-Finally ===")
    
    # Example 1: Successful operation
    try:
        number = int("42")
        print(f"Successfully converted: {number}")
    except ValueError as e:
        print(f"ValueError: {e}")
    else:
        print("No exception occurred - else block executed")
    finally:
        print("Finally block always executes")
    
    print()
    
    # Example 2: Failed operation
    try:
        number = int("abc")
        print(f"Successfully converted: {number}")
    except ValueError as e:
        print(f"ValueError: {e}")
    else:
        print("No exception occurred - else block executed")
    finally:
        print("Finally block always executes")


def multiple_exception_handling():
    """Demonstrates handling multiple exception types."""
    print("\n=== Multiple Exception Handling ===")
    
    # Example 1: Multiple except clauses
    def process_data(data):
        try:
            if isinstance(data, str):
                return int(data)
            elif isinstance(data, list):
                return data[0]
            else:
                return data / 0
        except ValueError as e:
            print(f"ValueError: {e}")
        except IndexError as e:
            print(f"IndexError: {e}")
        except ZeroDivisionError as e:
            print(f"ZeroDivisionError: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
    
    # Test different scenarios
    process_data("abc")      # ValueError
    process_data([])         # IndexError
    process_data(10)         # ZeroDivisionError
    
    # Example 2: Single except with tuple
    def safe_operation(value):
        try:
            result = 100 / value
            return result
        except (ValueError, TypeError, ZeroDivisionError) as e:
            print(f"Caught error: {type(e).__name__}: {e}")
            return None
    
    print(f"Result: {safe_operation(0)}")
    print(f"Result: {safe_operation('abc')}")


def raising_exceptions():
    """Demonstrates raising exceptions."""
    print("\n=== Raising Exceptions ===")
    
    # Example 1: Raising built-in exceptions
    def validate_age(age):
        if not isinstance(age, int):
            raise TypeError("Age must be an integer")
        if age < 0:
            raise ValueError("Age cannot be negative")
        if age > 150:
            raise ValueError("Age seems unrealistic")
        return age
    
    # Test the function
    try:
        validate_age("twenty")
    except TypeError as e:
        print(f"TypeError: {e}")
    
    try:
        validate_age(-5)
    except ValueError as e:
        print(f"ValueError: {e}")
    
    # Example 2: Re-raising exceptions
    def process_user_input(user_input):
        try:
            number = int(user_input)
            return number * 2
        except ValueError:
            print("Invalid input, re-raising exception")
            raise  # Re-raise the current exception
    
    try:
        result = process_user_input("abc")
    except ValueError as e:
        print(f"Caught re-raised ValueError: {e}")


def assert_statement():
    """Demonstrates the assert statement."""
    print("\n=== Assert Statement ===")
    
    # Example 1: Basic assertions
    def calculate_square_root(number):
        assert number >= 0, "Cannot calculate square root of negative number"
        return number ** 0.5
    
    # This will work
    try:
        result = calculate_square_root(16)
        print(f"Square root of 16: {result}")
    except AssertionError as e:
        print(f"AssertionError: {e}")
    
    # This will raise AssertionError
    try:
        result = calculate_square_root(-4)
    except AssertionError as e:
        print(f"AssertionError: {e}")
    
    # Example 2: Assertions in testing scenarios
    def divide_numbers(a, b):
        assert b != 0, "Division by zero is not allowed"
        return a / b
    
    # Test with valid input
    try:
        result = divide_numbers(10, 2)
        assert result == 5, f"Expected 5, got {result}"
        print("Division test passed")
    except AssertionError as e:
        print(f"Test failed: {e}")


class CustomException(Exception):
    """Custom exception class."""
    def __init__(self, message: str, error_code: int = None):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)
    
    def __str__(self):
        if self.error_code:
            return f"{self.message} (Error Code: {self.error_code})"
        return self.message


class ValidationError(CustomException):
    """Exception for validation errors."""
    pass


class DatabaseError(CustomException):
    """Exception for database errors."""
    pass


def custom_exceptions():
    """Demonstrates custom exception classes."""
    print("\n=== Custom Exceptions ===")
    
    # Example 1: Using custom exceptions
    def validate_email(email):
        if not isinstance(email, str):
            raise ValidationError("Email must be a string", 1001)
        if '@' not in email:
            raise ValidationError("Email must contain @ symbol", 1002)
        if '.' not in email.split('@')[1]:
            raise ValidationError("Email must have valid domain", 1003)
        return True
    
    # Test email validation
    test_emails = ["not_an_email", "valid@email.com", 123]
    
    for email in test_emails:
        try:
            validate_email(email)
            print(f"'{email}' is valid")
        except ValidationError as e:
            print(f"Validation error: {e}")
    
    # Example 2: Exception hierarchy
    def connect_database(connection_string):
        if not connection_string:
            raise DatabaseError("Connection string cannot be empty", 2001)
        if "localhost" in connection_string:
            raise DatabaseError("Cannot connect to localhost in production", 2002)
        return "Connected successfully"
    
    try:
        connect_database("")
    except DatabaseError as e:
        print(f"Database error: {e}")


def exception_chaining():
    """Demonstrates exception chaining."""
    print("\n=== Exception Chaining ===")
    
    # Example 1: Implicit exception chaining
    def process_config_file(filename):
        try:
            with open(filename, 'r') as file:
                config = file.read()
                return config
        except FileNotFoundError as e:
            raise RuntimeError(f"Failed to process configuration") from e
    
    try:
        process_config_file("nonexistent.txt")
    except RuntimeError as e:
        print(f"RuntimeError: {e}")
        print(f"Caused by: {e.__cause__}")
    
    # Example 2: Explicit exception chaining
    def parse_user_data(data):
        try:
            user_info = eval(data)  # Dangerous, just for demonstration
            return user_info
        except Exception as e:
            raise ValueError("Invalid user data format") from e
    
    try:
        parse_user_data("invalid_python_code")
    except ValueError as e:
        print(f"ValueError: {e}")
        print(f"Original error: {e.__cause__}")


def exception_objects_and_properties():
    """Demonstrates exception objects and their properties."""
    print("\n=== Exception Objects and Properties ===")
    
    # Example 1: Accessing exception properties
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Exception type: {type(e).__name__}")
        print(f"Exception message: {e}")
        print(f"Exception args: {e.args}")
        print(f"Exception representation: {repr(e)}")
    
    # Example 2: Using exception information
    def analyze_exception():
        try:
            # Simulate different types of errors
            import random
            errors = [
                lambda: int("abc"),
                lambda: [1, 2, 3][10],
                lambda: {"a": 1}["b"],
                lambda: 10 / 0
            ]
            random.choice(errors)()
        except Exception as e:
            print(f"Exception type: {type(e).__name__}")
            print(f"Exception message: {str(e)}")
            print(f"Exception class: {e.__class__}")
            print(f"Exception module: {e.__class__.__module__}")
    
    analyze_exception()


def errno_and_error_values():
    """Demonstrates errno variable and error values."""
    print("\n=== Errno and Error Values ===")
    
    import errno
    
    # Example 1: Common errno values
    print(f"EPERM (Operation not permitted): {errno.EPERM}")
    print(f"ENOENT (No such file or directory): {errno.ENOENT}")
    print(f"EACCES (Permission denied): {errno.EACCES}")
    print(f"EEXIST (File exists): {errno.EEXIST}")
    
    # Example 2: Using errno in exception handling
    def safe_file_operation(filename):
        try:
            with open(filename, 'r') as file:
                return file.read()
        except FileNotFoundError as e:
            if e.errno == errno.ENOENT:
                print(f"File '{filename}' does not exist")
            elif e.errno == errno.EACCES:
                print(f"Permission denied accessing '{filename}'")
            else:
                print(f"File error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
    
    safe_file_operation("nonexistent.txt")


def exception_hierarchy_demo():
    """Demonstrates Python's exception hierarchy."""
    print("\n=== Exception Hierarchy ===")
    
    # Common exception types and their hierarchy
    exceptions = [
        BaseException,
        Exception,
        TypeError,
        ValueError,
        RuntimeError,
        OSError,
        FileNotFoundError,
        PermissionError,
        ZeroDivisionError,
        IndexError,
        KeyError,
        AttributeError,
        NameError,
        SyntaxError,
        ImportError,
        ModuleNotFoundError
    ]
    
    print("Python Exception Hierarchy (partial):")
    for exc in exceptions:
        print(f"  {exc.__name__}")
    
    # Example: Checking exception hierarchy
    try:
        result = 10 / 0
    except ArithmeticError as e:
        print(f"Caught ArithmeticError: {e}")
    except Exception as e:
        print(f"Caught Exception: {e}")


def practical_exception_handling():
    """Demonstrates practical exception handling scenarios."""
    print("\n=== Practical Exception Handling ===")
    
    # Example 1: Robust data processing
    def process_user_list(user_data):
        results = []
        for i, data in enumerate(user_data):
            try:
                # Try to extract user information
                name = data.get('name', 'Unknown')
                age = int(data.get('age', 0))
                email = data.get('email', '')
                
                if age < 0 or age > 150:
                    raise ValueError(f"Invalid age: {age}")
                
                results.append({
                    'name': name,
                    'age': age,
                    'email': email,
                    'status': 'valid'
                })
                
            except (ValueError, TypeError) as e:
                print(f"Error processing user {i}: {e}")
                results.append({
                    'name': data.get('name', 'Unknown'),
                    'age': 0,
                    'email': data.get('email', ''),
                    'status': 'invalid',
                    'error': str(e)
                })
            except Exception as e:
                print(f"Unexpected error processing user {i}: {e}")
                results.append({
                    'name': 'Unknown',
                    'age': 0,
                    'email': '',
                    'status': 'error',
                    'error': str(e)
                })
        
        return results
    
    # Test data with various issues
    test_data = [
        {'name': 'John', 'age': 25, 'email': 'john@example.com'},
        {'name': 'Jane', 'age': 'invalid', 'email': 'jane@example.com'},
        {'name': 'Bob', 'age': -5, 'email': 'bob@example.com'},
        {'name': 'Alice', 'age': 200, 'email': 'alice@example.com'},
        {'age': 30},  # Missing name
        None,  # Invalid data
    ]
    
    results = process_user_list(test_data)
    for i, result in enumerate(results):
        print(f"User {i}: {result}")


if __name__ == "__main__":
    print("Exception Handling Examples")
    print("=" * 50)
    
    # Run all demonstrations
    basic_exception_handling()
    try_except_else_finally()
    multiple_exception_handling()
    raising_exceptions()
    assert_statement()
    custom_exceptions()
    exception_chaining()
    exception_objects_and_properties()
    errno_and_error_values()
    exception_hierarchy_demo()
    practical_exception_handling()
    
    print("\n" + "=" * 50)
    print("Exception handling examples completed!")
