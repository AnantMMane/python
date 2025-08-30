# PCAP - Certified Associate in Python Programming - Comprehensive Study Notes

## Table of Contents

1. [Introduction](#introduction)
2. [Module 1: Computer Programming and Python Fundamentals](#module-1-computer-programming-and-python-fundamentals)
3. [Module 2: Data Types, Variables, Basic Input-Output Operations](#module-2-data-types-variables-basic-input-output-operations)
4. [Module 3: Boolean Values, Conditional Execution, Loops, Lists and List Processing, Logical and Bitwise Operations](#module-3-boolean-values-conditional-execution-loops-lists-and-list-processing-logical-and-bitwise-operations)
5. [Module 4: Functions, Tuples, Dictionaries, Exceptions, and Data Processing](#module-4-functions-tuples-dictionaries-exceptions-and-data-processing)
6. [Module 5: Object-Oriented Programming](#module-5-object-oriented-programming)
7. [Module 6: Modules and Packages](#module-6-modules-and-packages)
8. [Module 7: String Methods and String Processing](#module-7-string-methods-and-string-processing)
9. [Module 8: File Handling](#module-8-file-handling)
10. [Practice Exercises and Certification Tips](#practice-exercises-and-certification-tips)
11. [Useful Resources and Links](#useful-resources-and-links)

---

## Introduction

The **PCAP (Python Institute Certified Associate in Python Programming)** certification validates foundational Python programming skills. This comprehensive guide covers all essential topics needed to pass the PCAP exam and become proficient in Python programming.

### Exam Details
- **Duration**: 65 minutes
- **Questions**: 40 questions
- **Passing Score**: 70%
- **Format**: Multiple choice, gap fill, drag & drop, code insertion, code ordering

---

## Module 1: Computer Programming and Python Fundamentals

### 1.1 Python Language Overview

#### What is Python?
Python is a high-level, interpreted, interactive, and object-oriented programming language. Created by Guido van Rossum in 1991, Python emphasizes code readability and simplicity.

#### Key Features:
- **Interpreted Language**: No compilation step needed
- **Cross-platform**: Runs on Windows, macOS, Linux, Unix
- **Dynamic Typing**: Variable types determined at runtime
- **Automatic Memory Management**: Garbage collection handles memory
- **Rich Standard Library**: "Batteries included" philosophy
- **Object-Oriented**: Supports OOP concepts
- **Interactive**: Python shell for testing code snippets

#### Python Implementations:
- **CPython**: Standard implementation written in C
- **PyPy**: JIT compiler implementation for performance
- **Jython**: Python for Java Virtual Machine
- **IronPython**: Python for .NET framework

### 1.2 Python Installation and Environment Setup

#### Installing Python:
1. Download from [python.org](https://python.org)
2. Choose appropriate version (3.8+ recommended)
3. During installation, check "Add Python to PATH"
4. Verify installation: `python --version`

#### Python IDE Options:
- **IDLE**: Built-in development environment
- **PyCharm**: Professional IDE by JetBrains
- **VS Code**: Lightweight editor with Python extensions
- **Jupyter Notebook**: Interactive computing environment
- **Spyder**: Scientific Python development environment

### 1.3 Running Python Programs

#### Interactive Mode (Python Shell):
```bash
python
>>> print("Hello, World!")
Hello, World!
>>> exit()
```

#### Script Mode:
```bash
python script.py
```

#### Python File Extensions:
- `.py`: Python source files
- `.pyc`: Compiled bytecode files
- `.pyo`: Optimized bytecode files
- `.pyw`: Python script for Windows (no console)

### 1.4 Syntax Fundamentals

#### Indentation:
Python uses indentation to define code blocks instead of braces.

```python
# Correct indentation
if True:
    print("This is indented")
    print("This is also indented")

# Incorrect indentation (IndentationError)
if True:
print("This will cause an error")
```

#### Comments:
```python
# Single line comment

"""
Multi-line comment
or docstring
"""

'''
Another way to write
multi-line comments
'''
```

#### Statement Separators:
```python
# Multiple statements on one line (not recommended)
a = 1; b = 2; c = 3

# Preferred: One statement per line
a = 1
b = 2
c = 3
```

---

## Module 2: Data Types, Variables, Basic Input-Output Operations

### 2.1 Variables and Assignment

#### Variable Naming Rules:
- Must start with letter or underscore
- Can contain letters, numbers, underscores
- Case-sensitive
- Cannot use Python keywords

```python
# Valid variable names
name = "Alice"
age = 25
_private = "hidden"
number1 = 10
camelCase = "valid"
snake_case = "preferred"

# Invalid variable names
# 2name = "invalid"      # Starts with number
# my-var = "invalid"     # Contains hyphen
# class = "invalid"      # Python keyword
```

#### Assignment Operators:
```python
# Basic assignment
x = 10

# Multiple assignment
a, b, c = 1, 2, 3

# Chained assignment
x = y = z = 0

# Augmented assignment
x += 5    # x = x + 5
x -= 3    # x = x - 3
x *= 2    # x = x * 2
x /= 4    # x = x / 4
x //= 2   # x = x // 2
x %= 3    # x = x % 3
x **= 2   # x = x ** 2
```

### 2.2 Data Types

#### Numeric Types:

**Integers (int):**
```python
# Decimal
num = 42

# Binary (prefix 0b)
binary = 0b1010  # 10 in decimal

# Octal (prefix 0o)
octal = 0o12     # 10 in decimal

# Hexadecimal (prefix 0x)
hex_num = 0xA    # 10 in decimal

# Large integers (unlimited precision)
big_num = 123456789012345678901234567890
```

**Floating-Point Numbers (float):**
```python
# Basic float
pi = 3.14159

# Scientific notation
scientific = 1.23e-4  # 0.000123
large_num = 6.02e23   # 6.02 × 10^23

# Special float values
infinity = float('inf')
negative_infinity = float('-inf')
not_a_number = float('nan')
```

**Complex Numbers (complex):**
```python
# Creating complex numbers
z1 = 3 + 4j
z2 = complex(3, 4)
z3 = complex('3+4j')

# Accessing real and imaginary parts
print(z1.real)  # 3.0
print(z1.imag)  # 4.0

# Complex operations
z3 = z1 + z2
magnitude = abs(z1)  # √(3² + 4²) = 5.0
```

#### String Type (str):

**String Creation:**
```python
# Single quotes
single = 'Hello'

# Double quotes
double = "World"

# Triple quotes (multiline)
multiline = """This is a
multiline string"""

# Raw strings (backslashes treated literally)
raw = r"C:\Users\Name\Documents"

# Unicode strings
unicode_str = "Hello, 世界"
```

**String Escape Sequences:**
```python
escaped = "Line 1\nLine 2\tTabbed"
print(escaped)
# Output:
# Line 1
# Line 2    Tabbed

# Common escape sequences:
# \n - newline
# \t - tab
# \\ - backslash
# \' - single quote
# \" - double quote
# \r - carriage return
# \0 - null character
```

#### Boolean Type (bool):
```python
# Boolean values
is_active = True
is_complete = False

# Boolean from other types
bool(1)        # True
bool(0)        # False
bool("text")   # True
bool("")       # False
bool([1,2,3])  # True
bool([])       # False
```

### 2.3 Type Conversion and Checking

#### Type Checking:
```python
x = 42
print(type(x))           # <class 'int'>
print(isinstance(x, int)) # True

# Multiple type checking
isinstance(x, (int, float, str))  # True if x is any of these types
```

#### Type Conversion (Casting):
```python
# To integer
int("123")      # 123
int(3.14)       # 3
int(True)       # 1

# To float
float("3.14")   # 3.14
float(42)       # 42.0
float(True)     # 1.0

# To string
str(123)        # "123"
str(3.14)       # "3.14"
str(True)       # "True"

# To boolean
bool(1)         # True
bool(0)         # False
bool("hello")   # True
bool("")        # False
```

### 2.4 Input and Output Operations

#### Output with print():
```python
# Basic printing
print("Hello, World!")

# Multiple values
print("Name:", "Alice", "Age:", 25)

# Separator and end parameters
print("A", "B", "C", sep="-")      # A-B-C
print("Line 1", end=" ")
print("Line 2")                    # Line 1 Line 2

# Formatted output
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old")
print("My name is {} and I am {} years old".format(name, age))
print("My name is %s and I am %d years old" % (name, age))
```

#### Input with input():
```python
# String input (always returns string)
name = input("Enter your name: ")

# Converting input to other types
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

# Multiple inputs on one line
a, b = input("Enter two numbers: ").split()
a, b = int(a), int(b)

# Or more concisely
a, b = map(int, input("Enter two numbers: ").split())
```

### 2.5 Operators

#### Arithmetic Operators:
```python
a, b = 10, 3

print(a + b)   # Addition: 13
print(a - b)   # Subtraction: 7
print(a * b)   # Multiplication: 30
print(a / b)   # Division: 3.3333...
print(a // b)  # Floor division: 3
print(a % b)   # Modulus: 1
print(a ** b)  # Exponentiation: 1000

# Unary operators
print(+a)      # Unary plus: 10
print(-a)      # Unary minus: -10
```

#### Comparison Operators:
```python
a, b = 10, 5

print(a == b)   # Equal: False
print(a != b)   # Not equal: True
print(a > b)    # Greater than: True
print(a < b)    # Less than: False
print(a >= b)   # Greater than or equal: True
print(a <= b)   # Less than or equal: False

# Chained comparisons
x = 5
print(1 < x < 10)  # True (equivalent to 1 < x and x < 10)
```

#### Logical Operators:
```python
# and, or, not
a, b = True, False

print(a and b)     # False
print(a or b)      # True
print(not a)       # False

# Short-circuit evaluation
x = 5
result = x > 0 and x < 10  # If x > 0 is False, x < 10 won't be evaluated
```

---

## Module 3: Boolean Values, Conditional Execution, Loops, Lists and List Processing, Logical and Bitwise Operations

### 3.1 Boolean Values and Operations

#### Truth Values in Python:
```python
# Falsy values (evaluate to False)
bool(False)     # False
bool(None)      # False
bool(0)         # False
bool(0.0)       # False
bool("")        # False
bool([])        # False
bool(())        # False
bool({})        # False
bool(set())     # False

# Truthy values (evaluate to True)
bool(True)      # True
bool(1)         # True
bool(-1)        # True
bool("hello")   # True
bool([1, 2])    # True
bool((1, 2))    # True
bool({"a": 1})  # True
```

### 3.2 Conditional Execution

#### if-elif-else Statements:
```python
# Basic if statement
age = 18
if age >= 18:
    print("You are an adult")

# if-else statement
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# if-elif-else statement
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")
```

#### Conditional Expression (Ternary Operator):
```python
# Syntax: value_if_true if condition else value_if_false
age = 20
status = "adult" if age >= 18 else "minor"

# Multiple conditions
x = 10
result = "positive" if x > 0 else "zero" if x == 0 else "negative"
```

### 3.3 Loops

#### while Loop:
```python
# Basic while loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# while with else (executes if loop completes normally)
x = 0
while x < 3:
    print(x)
    x += 1
else:
    print("Loop completed normally")

# Infinite loop (use with caution)
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == 'quit':
        break
    print(f"You entered: {user_input}")
```

#### for Loop:
```python
# Iterating over sequences
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using range()
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 8):       # 2, 3, 4, 5, 6, 7
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8
    print(i)

# for with else
for i in range(3):
    print(i)
else:
    print("Loop completed")

# Iterating with index using enumerate()
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Iterating over multiple sequences with zip()
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

#### Loop Control Statements:
```python
# break: exits the loop
for i in range(10):
    if i == 5:
        break
    print(i)  # Prints 0, 1, 2, 3, 4

# continue: skips the rest of the current iteration
for i in range(5):
    if i == 2:
        continue
    print(i)  # Prints 0, 1, 3, 4

# pass: does nothing (placeholder)
for i in range(5):
    if i == 2:
        pass  # TODO: implement something here
    print(i)  # Prints 0, 1, 2, 3, 4
```

### 3.4 Lists and List Processing

#### Creating Lists:
```python
# Empty list
empty_list = []
empty_list2 = list()

# List with initial values
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4], [5, 6]]

# List comprehensions - powerful and concise way to create lists
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
even_squares = [x**2 for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]
```

#### Accessing List Elements:
```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Positive indexing (0-based)
print(fruits[0])    # apple
print(fruits[2])    # cherry

# Negative indexing (-1 is last element)
print(fruits[-1])   # elderberry
print(fruits[-2])   # date

# Slicing
print(fruits[1:4])    # ['banana', 'cherry', 'date']
print(fruits[:3])     # ['apple', 'banana', 'cherry']
print(fruits[2:])     # ['cherry', 'date', 'elderberry']
print(fruits[:])      # Copy of entire list
print(fruits[::2])    # ['apple', 'cherry', 'elderberry'] (every 2nd)
print(fruits[::-1])   # Reverse the list
```

#### Modifying Lists:
```python
numbers = [1, 2, 3, 4, 5]

# Changing elements
numbers[0] = 10       # [10, 2, 3, 4, 5]
numbers[-1] = 50      # [10, 2, 3, 4, 50]

# Changing slices
numbers[1:3] = [20, 30]  # [10, 20, 30, 4, 50]

# Adding elements
numbers.append(60)         # Add to end: [10, 20, 30, 4, 50, 60]
numbers.insert(0, 0)       # Insert at index: [0, 10, 20, 30, 4, 50, 60]
numbers.extend([70, 80])   # Add multiple: [0, 10, 20, 30, 4, 50, 60, 70, 80]

# Removing elements
numbers.remove(4)          # Remove first occurrence of 4
last = numbers.pop()       # Remove and return last element
first = numbers.pop(0)     # Remove and return element at index 0
del numbers[1]             # Delete element at index 1
del numbers[1:3]           # Delete slice
numbers.clear()            # Remove all elements
```

#### List Methods:
```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Finding elements
print(numbers.index(4))      # 2 (index of first occurrence)
print(numbers.count(1))      # 2 (number of occurrences)

# Sorting
numbers.sort()               # Sort in place: [1, 1, 2, 3, 4, 5, 6, 9]
numbers.sort(reverse=True)   # Sort descending: [9, 6, 5, 4, 3, 2, 1, 1]
sorted_copy = sorted(numbers)  # Return new sorted list

# Reversing
numbers.reverse()            # Reverse in place
reversed_copy = numbers[::-1]  # Create reversed copy

# Copying
shallow_copy = numbers.copy()
shallow_copy2 = numbers[:]
shallow_copy3 = list(numbers)
```

#### List Operations:
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
combined = list1 + list2      # [1, 2, 3, 4, 5, 6]

# Repetition
repeated = list1 * 3          # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Membership testing
print(2 in list1)             # True
print(7 not in list1)         # True

# Length
print(len(list1))             # 3

# Min, max, sum (for numeric lists)
numbers = [3, 1, 4, 1, 5]
print(min(numbers))           # 1
print(max(numbers))           # 5
print(sum(numbers))           # 14
```

#### Advanced List Comprehensions:
List comprehensions provide a concise way to create lists based on existing sequences.

**Basic Syntax:**
```
[expression for item in iterable]
[expression for item in iterable if condition]
```

**Simple Examples:**
```python
# Basic list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]  # [1, 4, 9, 16, 25]

# With transformation
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]  # ['HELLO', 'WORLD', 'PYTHON']

# From range
evens = [x for x in range(20) if x % 2 == 0]  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

**Conditional List Comprehensions:**
```python
# Filter with if condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x**2 for x in numbers if x % 2 == 0]  # [4, 16, 36, 64, 100]

# Multiple conditions
big_evens = [x for x in range(50) if x % 2 == 0 and x > 20]  # [22, 24, 26, ..., 48]

# Conditional expression within comprehension
abs_diff = [x if x >= 0 else -x for x in [-3, -1, 0, 2, 4]]  # [3, 1, 0, 2, 4]

# More complex conditions
words = ["apple", "banana", "cherry", "date", "elderberry"]
long_words = [word for word in words if len(word) > 5]  # ['banana', 'cherry', 'elderberry']
```

**Working with Strings:**
```python
sentence = "The quick brown fox jumps"
words = sentence.split()

# Extract first letters
first_letters = [word[0] for word in words]  # ['T', 'q', 'b', 'f', 'j']

# Filter and transform
long_words_upper = [word.upper() for word in words if len(word) > 4]  # ['QUICK', 'BROWN', 'JUMPS']

# Character-level operations
vowels = [char for char in sentence.lower() if char in 'aeiou']  # ['e', 'u', 'i', 'o', 'o', 'u']
```

**Nested List Comprehensions:**
```python
# 2D list creation
matrix = [[i*j for j in range(3)] for i in range(3)]
# [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# Flattening nested lists
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in nested for item in sublist]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Matrix operations
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Get all elements greater than 5
big_elements = [item for row in matrix for item in row if item > 5]  # [6, 7, 8, 9]

# Transpose matrix
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

**Dictionary and Set Comprehensions:**
```python
# Dictionary comprehensions
numbers = [1, 2, 3, 4, 5]
squares_dict = {n: n**2 for n in numbers}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With conditional
even_squares_dict = {n: n**2 for n in numbers if n % 2 == 0}  # {2: 4, 4: 16}

# From existing dictionary
prices = {'apple': 0.50, 'banana': 0.30, 'cherry': 1.20}
expensive = {item: price for item, price in prices.items() if price > 0.40}
# {'apple': 0.5, 'cherry': 1.2}

# Set comprehensions
words = ["apple", "banana", "apple", "cherry", "banana"]
unique_lengths = {len(word) for word in words}  # {5, 6}

# First letters (unique)
first_letters_set = {word[0].upper() for word in words}  # {'A', 'B', 'C'}
```

**Practical Examples:**
```python
# File processing example
lines = ["  hello world  ", "python programming", "  data science  "]
cleaned = [line.strip().title() for line in lines if line.strip()]
# ['Hello World', 'Python Programming', 'Data Science']

# Number processing
grades = [85, 92, 78, 96, 88, 76, 94]
letter_grades = ['A' if g >= 90 else 'B' if g >= 80 else 'C' if g >= 70 else 'F' 
                for g in grades]
# ['B', 'A', 'C', 'A', 'B', 'C', 'A']

# Parsing data
data = "1,2,3,4,5"
numbers = [int(x) for x in data.split(',')]  # [1, 2, 3, 4, 5]

# Working with functions
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Find primes using comprehension
primes = [n for n in range(2, 50) if is_prime(n)]
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# Generator expressions (memory efficient)
squares_gen = (x**2 for x in range(1000000))  # Creates generator, not list
# Use next(squares_gen) or list(squares_gen) to get values
```

**Performance Comparison:**
```python
import time

# Traditional approach
def traditional_squares(n):
    result = []
    for i in range(n):
        result.append(i**2)
    return result

# List comprehension approach
def comprehension_squares(n):
    return [i**2 for i in range(n)]

# Timing comparison (comprehensions are typically faster)
n = 100000
start = time.time()
traditional_squares(n)
traditional_time = time.time() - start

start = time.time()
comprehension_squares(n)
comprehension_time = time.time() - start

print(f"Traditional: {traditional_time:.4f}s")
print(f"Comprehension: {comprehension_time:.4f}s")
```

### 3.5 Logical and Bitwise Operations

#### Logical Operators:
```python
# and: Returns True if both operands are True
True and True    # True
True and False   # False
False and True   # False
False and False  # False

# or: Returns True if at least one operand is True
True or True     # True
True or False    # True
False or True    # True
False or False   # False

# not: Returns opposite boolean value
not True         # False
not False        # True

# Short-circuit evaluation
x = 5
y = 0
result = y != 0 and x / y > 2  # y / x is not evaluated because y != 0 is False
```

#### Bitwise Operators:
```python
# Work on binary representations of integers
a = 60   # 0011 1100 in binary
b = 13   # 0000 1101 in binary

# Bitwise AND (&)
print(a & b)     # 12 (0000 1100)

# Bitwise OR (|)
print(a | b)     # 61 (0011 1101)

# Bitwise XOR (^)
print(a ^ b)     # 49 (0011 0001)

# Bitwise NOT (~)
print(~a)        # -61 (complement)

# Left shift (<<)
print(a << 2)    # 240 (shift left by 2 bits)

# Right shift (>>)
print(a >> 2)    # 15 (shift right by 2 bits)
```

#### Boolean Context and Truthiness:
```python
# Using values in boolean context
values = [0, 1, "", "hello", [], [1, 2], None, False, True]

for value in values:
    if value:
        print(f"{value} is truthy")
    else:
        print(f"{value} is falsy")

# all() and any() functions
numbers = [2, 4, 6, 8]
print(all(n % 2 == 0 for n in numbers))  # True (all are even)

numbers = [1, 3, 5, 7]
print(any(n % 2 == 0 for n in numbers))  # False (none are even)
```

---

## Module 4: Functions, Tuples, Dictionaries, Exceptions, and Data Processing

### 4.1 Functions
Python functions are reusable blocks of code that perform specific tasks.

#### Function Definition and Basic Usage:
```python
# Basic function definition
def greet(name):
    """Function to greet a person"""
    return f"Hello, {name}!"

# Function call
message = greet("Alice")
print(message)  # Hello, Alice!

# Function with multiple parameters
def add_numbers(a, b):
    """Add two numbers and return the result"""
    result = a + b
    return result

# Function without return (returns None)
def print_info(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

print_info("Bob", 25)
```

#### Parameters and Arguments:
```python
# Positional arguments
def describe_person(name, age, city):
    return f"{name} is {age} years old and lives in {city}"

info = describe_person("Alice", 30, "New York")

# Default parameters
def greet_person(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet_person("Bob"))           # Hello, Bob!
print(greet_person("Bob", "Hi"))     # Hi, Bob!

# Keyword arguments
print(describe_person(age=25, name="Charlie", city="London"))

# *args - variable positional arguments
def sum_all(*args):
    """Sum all provided arguments"""
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3, 4, 5))      # 15
print(sum_all(10, 20))             # 30

# **kwargs - variable keyword arguments
def create_profile(**kwargs):
    """Create a profile from keyword arguments"""
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile

profile = create_profile(name="David", age=28, job="Engineer", city="Boston")
print(profile)  # {'name': 'David', 'age': 28, 'job': 'Engineer', 'city': 'Boston'}

# Combining all parameter types
def complex_function(required, default_param="default", *args, **kwargs):
    print(f"Required: {required}")
    print(f"Default: {default_param}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

complex_function("test", "custom", 1, 2, 3, key1="value1", key2="value2")
```

#### Variable Scope:
```python
# Global scope
global_var = "I'm global"

def demonstrate_scope():
    # Local scope
    local_var = "I'm local"
    print(f"Inside function: {global_var}")  # Can access global
    print(f"Inside function: {local_var}")   # Can access local

demonstrate_scope()
# print(local_var)  # Error: local_var not accessible outside function

# Global keyword
counter = 0

def increment():
    global counter  # Declare that we want to modify global variable
    counter += 1

increment()
print(counter)  # 1

# Nonlocal keyword (for nested functions)
def outer_function():
    x = "outer"
    
    def inner_function():
        nonlocal x  # Refer to the outer function's x
        x = "modified by inner"
    
    inner_function()
    print(x)  # "modified by inner"

outer_function()

# LEGB Rule: Local, Enclosing, Global, Built-in
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(f"Inner x: {x}")  # local
    
    inner()
    print(f"Outer x: {x}")  # enclosing

outer()
print(f"Global x: {x}")  # global
```

#### Lambda Functions:
Anonymous functions for simple operations.

```python
# Basic lambda syntax: lambda arguments: expression
square = lambda x: x**2
print(square(5))  # 25

# Lambda with multiple arguments
add = lambda x, y: x + y
print(add(3, 4))  # 7

# Lambda in list operations
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16, 25]

# Lambda with conditional expression
max_value = lambda a, b: a if a > b else b
print(max_value(10, 15))  # 15

# Lambda for sorting
students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
# Sort by grade (second element)
students.sort(key=lambda student: student[1])
print(students)  # [('Charlie', 78), ('Alice', 85), ('Bob', 90)]

# Sort by name (first element)
students.sort(key=lambda student: student[0])
print(students)  # [('Alice', 85), ('Bob', 90), ('Charlie', 78)]

# Lambda in filter operations
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4, 6, 8, 10]
odds = list(filter(lambda x: x % 2 == 1, numbers))   # [1, 3, 5, 7, 9]

# Lambda for data processing
data = [
    {"name": "Alice", "age": 30, "salary": 50000},
    {"name": "Bob", "age": 25, "salary": 45000},
    {"name": "Charlie", "age": 35, "salary": 60000}
]

# Sort by salary
data.sort(key=lambda person: person["salary"])

# Filter high earners
high_earners = list(filter(lambda person: person["salary"] > 50000, data))

# Extract names
names = list(map(lambda person: person["name"], data))
```

#### Functions as First-Class Objects:
```python
# Functions can be assigned to variables
def say_hello():
    return "Hello!"

greeting_function = say_hello
print(greeting_function())  # Hello!

# Functions can be passed as arguments
def apply_operation(func, x, y):
    return func(x, y)

def multiply(a, b):
    return a * b

def add(a, b):
    return a + b

result1 = apply_operation(multiply, 4, 5)  # 20
result2 = apply_operation(add, 4, 5)       # 9

# Functions can return other functions
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15

# Functions can be stored in data structures
operations = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
    "divide": lambda x, y: x / y if y != 0 else "Cannot divide by zero"
}

print(operations["add"](10, 5))      # 15
print(operations["multiply"](3, 4))  # 12
```

#### Advanced Function Features:
```python
# Function decorators (basic example)
def my_decorator(func):
    def wrapper():
        print("Something before the function")
        func()
        print("Something after the function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something before the function
# Hello!
# Something after the function

# Recursive functions
def factorial(n):
    """Calculate factorial using recursion"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120

def fibonacci(n):
    """Calculate nth Fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print([fibonacci(i) for i in range(10)])  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Generator functions
def count_up_to(max_count):
    """Generator that yields numbers from 1 to max_count"""
    count = 1
    while count <= max_count:
        yield count
        count += 1

# Using the generator
for num in count_up_to(5):
    print(num)  # Prints 1, 2, 3, 4, 5

# Generator expression with functions
def square(x):
    return x**2

squares_gen = (square(x) for x in range(10))
print(list(squares_gen))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

#### Built-in Functions: map() and filter():
Powerful functions for data processing with functional programming approach.

**map() Function:**
Applies a function to every item in an iterable.

```python
# Basic map usage
numbers = [1, 2, 3, 4, 5]

# Using map with built-in function
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# Using map with regular function
def cube(x):
    return x**3

cubes = list(map(cube, numbers))
print(cubes)  # [1, 8, 27, 64, 125]

# Map with multiple iterables
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
sums = list(map(lambda x, y: x + y, list1, list2))
print(sums)  # [11, 22, 33, 44]

# Map with string operations
words = ["hello", "world", "python", "programming"]
upper_words = list(map(str.upper, words))
print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON', 'PROGRAMMING']

# Map with type conversion
string_numbers = ["1", "2", "3", "4", "5"]
int_numbers = list(map(int, string_numbers))
print(int_numbers)  # [1, 2, 3, 4, 5]

# Map with custom function
def format_name(name):
    return name.strip().title()

names = ["  alice  ", "BOB", "charlie"]
formatted_names = list(map(format_name, names))
print(formatted_names)  # ['Alice', 'Bob', 'Charlie']

# Map for mathematical operations
temperatures_celsius = [0, 20, 30, 40, 100]
temperatures_fahrenheit = list(map(lambda c: (c * 9/5) + 32, temperatures_celsius))
print(temperatures_fahrenheit)  # [32.0, 68.0, 86.0, 104.0, 212.0]
```

**filter() Function:**
Filters items from an iterable based on a function that returns True/False.

```python
# Basic filter usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Filter odd numbers
odds = list(filter(lambda x: x % 2 == 1, numbers))
print(odds)  # [1, 3, 5, 7, 9]

# Filter with custom function
def is_positive(x):
    return x > 0

mixed_numbers = [-3, -1, 0, 2, 4, -5, 7]
positive_numbers = list(filter(is_positive, mixed_numbers))
print(positive_numbers)  # [2, 4, 7]

# Filter strings by length
words = ["cat", "elephant", "dog", "butterfly", "ant"]
long_words = list(filter(lambda word: len(word) > 3, words))
print(long_words)  # ['elephant', 'butterfly']

# Filter with None (removes falsy values)
mixed_data = [1, 0, "hello", "", None, False, True, [], [1, 2]]
truthy_values = list(filter(None, mixed_data))
print(truthy_values)  # [1, 'hello', True, [1, 2]]

# Filter dictionary data
people = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Boston"},
    {"name": "Charlie", "age": 35, "city": "New York"},
    {"name": "David", "age": 28, "city": "Chicago"}
]

# Filter by age
adults_over_30 = list(filter(lambda person: person["age"] > 30, people))
print([p["name"] for p in adults_over_30])  # ['Alice', 'Charlie']

# Filter by city
ny_residents = list(filter(lambda person: person["city"] == "New York", people))
print([p["name"] for p in ny_residents])  # ['Alice', 'Charlie']
```

**Combining map() and filter():**
```python
# Chain operations: filter then map
numbers = range(1, 21)  # 1 to 20

# Get squares of even numbers
even_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(even_squares)  # [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

# Map then filter: get even squares
all_squares = map(lambda x: x**2, numbers)
even_squares2 = list(filter(lambda x: x % 2 == 0, all_squares))
print(even_squares2)  # [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

# Complex data processing
sales_data = [
    {"product": "laptop", "price": 1200, "quantity": 5},
    {"product": "mouse", "price": 25, "quantity": 50},
    {"product": "keyboard", "price": 80, "quantity": 30},
    {"product": "monitor", "price": 300, "quantity": 15}
]

# Filter expensive items and calculate total value
expensive_items = filter(lambda item: item["price"] > 50, sales_data)
total_values = list(map(lambda item: item["price"] * item["quantity"], expensive_items))
print(total_values)  # [6000, 2400, 4500]

# Alternative using list comprehensions (often more readable)
total_values_lc = [item["price"] * item["quantity"] 
                  for item in sales_data 
                  if item["price"] > 50]
print(total_values_lc)  # [6000, 2400, 4500]
```

**Advanced Usage with Custom Functions:**
```python
# Using map and filter with user-defined functions
def clean_and_validate_email(email):
    """Clean email and return if valid"""
    cleaned = email.strip().lower()
    return cleaned if "@" in cleaned and "." in cleaned else None

def is_valid_email(email):
    """Check if email is valid (not None)"""
    return email is not None

# Process email list
raw_emails = ["  Alice@Example.COM  ", "bob@test", "charlie@domain.com", "invalid-email"]

# Clean emails
cleaned_emails = map(clean_and_validate_email, raw_emails)
# Filter valid emails
valid_emails = list(filter(is_valid_email, cleaned_emails))
print(valid_emails)  # ['alice@example.com', 'charlie@domain.com']

# Using reduce (from functools) with map and filter
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Sum of squares of even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)
squares = map(lambda x: x**2, even_numbers)
total = reduce(lambda x, y: x + y, squares)
print(total)  # 220 (4 + 16 + 36 + 64 + 100)

# More concise version
total_concise = reduce(lambda x, y: x + y, 
                      map(lambda x: x**2, 
                          filter(lambda x: x % 2 == 0, numbers)))
print(total_concise)  # 220
```

**Performance Considerations:**
```python
# Map and filter return iterators (Python 3), not lists
# This is memory efficient for large datasets

numbers = range(1000000)

# This creates an iterator, not a list in memory
squares_iter = map(lambda x: x**2, numbers)
print(type(squares_iter))  # <class 'map'>

# Only convert to list when you need all values
# squares_list = list(squares_iter)  # This would use a lot of memory

# You can iterate without creating the full list
for i, square in enumerate(squares_iter):
    if i >= 5:  # Only process first 5
        break
    print(square)  # 0, 1, 4, 9, 16

# Generator expressions are often more pythonic
squares_gen = (x**2 for x in numbers if x % 2 == 0)
# This is often preferred over: map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))
```

#### Closures:
Closures are functions that capture and "close over" variables from their enclosing scope.

```python
# Basic closure example
def outer_function(x):
    # Variable in enclosing scope
    def inner_function(y):
        # Inner function accesses variable from outer scope
        return x + y  # x is captured from outer scope
    
    return inner_function

# Create closure
add_10 = outer_function(10)
print(add_10(5))  # 15 - x=10 is "remembered"

add_100 = outer_function(100)
print(add_100(5))  # 105 - different x value is captured

# The enclosing variable persists even after outer function returns
print(add_10(20))  # 30 - x=10 is still remembered
```

**Closure with State:**
```python
def make_counter(start=0):
    """Create a counter function that remembers its count"""
    count = start
    
    def counter():
        nonlocal count  # Allows modification of enclosing variable
        count += 1
        return count
    
    return counter

# Create different counters
counter1 = make_counter()
counter2 = make_counter(100)

print(counter1())  # 1
print(counter1())  # 2
print(counter2())  # 101
print(counter1())  # 3
print(counter2())  # 102

# Each closure maintains its own state
print(f"Counter1 called again: {counter1()}")  # 4
print(f"Counter2 called again: {counter2()}")  # 103
```

**Closures with Multiple Functions:**
```python
def make_account(initial_balance):
    """Create account functions that share state"""
    balance = initial_balance
    
    def deposit(amount):
        nonlocal balance
        balance += amount
        return f"Deposited ${amount}. Balance: ${balance}"
    
    def withdraw(amount):
        nonlocal balance
        if amount <= balance:
            balance -= amount
            return f"Withdrew ${amount}. Balance: ${balance}"
        else:
            return f"Insufficient funds. Balance: ${balance}"
    
    def get_balance():
        return f"Current balance: ${balance}"
    
    # Return dictionary of functions
    return {
        'deposit': deposit,
        'withdraw': withdraw,
        'balance': get_balance
    }

# Create account
account = make_account(1000)

print(account['balance']())      # Current balance: $1000
print(account['deposit'](200))   # Deposited $200. Balance: $1200
print(account['withdraw'](150))  # Withdrew $150. Balance: $1050
print(account['withdraw'](2000)) # Insufficient funds. Balance: $1050
```

**Closures in Loops (Common Pitfall):**
```python
# WRONG WAY - Common mistake
functions = []
for i in range(3):
    # This captures the final value of i (2) for all functions
    functions.append(lambda: i)

# All functions return 2 (the final value of i)
for func in functions:
    print(func())  # 2, 2, 2

# CORRECT WAY - Capture current value
functions = []
for i in range(3):
    # Use default argument to capture current value of i
    functions.append(lambda x=i: x)

# Each function returns its correct value
for func in functions:
    print(func())  # 0, 1, 2

# ALTERNATIVE CORRECT WAY - Using closure properly
def make_function(value):
    return lambda: value

functions = []
for i in range(3):
    functions.append(make_function(i))

for func in functions:
    print(func())  # 0, 1, 2
```

**Practical Closure Applications:**
```python
# 1. Configuration and Settings
def make_validator(min_length, max_length):
    """Create custom validation function"""
    def validate(text):
        if len(text) < min_length:
            return f"Too short. Minimum {min_length} characters."
        elif len(text) > max_length:
            return f"Too long. Maximum {max_length} characters."
        else:
            return "Valid"
    
    return validate

# Create different validators
username_validator = make_validator(3, 20)
password_validator = make_validator(8, 50)

print(username_validator("ab"))      # Too short. Minimum 3 characters.
print(username_validator("alice"))   # Valid
print(password_validator("abc"))     # Too short. Minimum 8 characters.

# 2. Event Handlers and Callbacks
def make_event_handler(event_name):
    """Create event handler with captured event name"""
    def handler(data):
        print(f"Handling {event_name} event with data: {data}")
    
    return handler

click_handler = make_event_handler("click")
hover_handler = make_event_handler("hover")

click_handler("button1")  # Handling click event with data: button1
hover_handler("menu")     # Handling hover event with data: menu

# 3. Memoization using closures
def memoize(func):
    """Decorator that caches function results"""
    cache = {}
    
    def memoized_func(*args):
        if args in cache:
            print(f"Cache hit for {args}")
            return cache[args]
        
        result = func(*args)
        cache[args] = result
        print(f"Computed and cached result for {args}")
        return result
    
    return memoized_func

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Computes and caches intermediate results
print(fibonacci(8))   # Uses cached results

# 4. Factory functions
def make_multiplier(factor):
    """Create multiplication function with specific factor"""
    return lambda x: x * factor

def make_formatter(prefix, suffix):
    """Create string formatter with specific format"""
    return lambda text: f"{prefix}{text}{suffix}"

# Use factory functions
double = make_multiplier(2)
triple = make_multiplier(3)

html_bold = make_formatter("<b>", "</b>")
parentheses = make_formatter("(", ")")

print(double(15))           # 30
print(triple(10))           # 30
print(html_bold("Hello"))   # <b>Hello</b>
print(parentheses("note"))  # (note)
```

**Closure Introspection:**
```python
def outer(x):
    y = 20
    
    def inner(z):
        return x + y + z
    
    return inner

closure_func = outer(10)

# Examine closure properties
print(f"Function name: {closure_func.__name__}")           # inner
print(f"Closure cells: {closure_func.__closure__}")        # Closure cell objects
print(f"Free variables: {closure_func.__code__.co_freevars}")  # ('x', 'y')

# Access closure values
if closure_func.__closure__:
    for i, cell in enumerate(closure_func.__closure__):
        var_name = closure_func.__code__.co_freevars[i]
        print(f"Closure variable '{var_name}': {cell.cell_contents}")

# Result: Closure variable 'x': 10, Closure variable 'y': 20

print(closure_func(5))  # 35 (10 + 20 + 5)

# Practical debugging closure function
def debug_closure(func):
    """Debug function to examine closure contents"""
    print(f"\n=== Closure Debug: {func.__name__} ===")
    
    if func.__closure__:
        print("Captured variables:")
        for i, cell in enumerate(func.__closure__):
            var_name = func.__code__.co_freevars[i]
            print(f"  {var_name}: {cell.cell_contents}")
    else:
        print("No closure variables")
    
    print(f"Free variables: {func.__code__.co_freevars}")

# Test debugging
counter = make_counter(50)
debug_closure(counter)
```

### 4.2 Tuples
Immutable sequences that can store multiple items. See `examples/data_structures/tuples.py`.

**Key operations:**
- Creation: `tuple()`, `(1, 2, 3)`
- Indexing and slicing
- Tuple unpacking
- Methods: `count()`, `index()`

### 4.3 Dictionaries
Mutable key-value data structures. See `examples/data_structures/dictionaries.py`.

**Key operations:**
- Creation: `{}`, `dict()`
- Accessing: `dict[key]`, `dict.get(key)`
- Methods: `keys()`, `values()`, `items()`
- Dictionary comprehensions

### 4.4 Exception Handling
Robust error handling using try-except blocks for managing runtime errors.

#### Exception Hierarchy:
All exceptions in Python inherit from BaseException. Understanding the hierarchy helps with proper exception handling.

```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- ArithmeticError
      |    +-- ZeroDivisionError
      |    +-- OverflowError
      |    +-- FloatingPointError
      +-- AttributeError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- FileNotFoundError
      |    +-- PermissionError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      +-- Warning
           +-- UserWarning
           +-- DeprecationWarning
```

#### Basic Exception Handling Structure:
```python
try:
    # risky code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # handle specific error
    print("Cannot divide by zero!")
except Exception as e:
    # handle any other exception
    print(f"An error occurred: {e}")
else:
    # runs only if no exception occurred
    print("Operation successful")
finally:
    # always runs, regardless of exceptions
    print("Cleanup complete")
```

#### Multiple Exception Handling:
```python
# Handle multiple specific exceptions
try:
    value = input("Enter a number: ")
    number = int(value)
    result = 10 / number
    my_list = [1, 2, 3]
    print(my_list[number])
except (ValueError, TypeError):
    print("Invalid input - not a number")
except ZeroDivisionError:
    print("Cannot divide by zero")
except IndexError:
    print("List index out of range")
except Exception as e:
    print(f"Unexpected error: {type(e).__name__}: {e}")

# Exception with else and finally
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
    content = ""
except PermissionError:
    print("Permission denied")
    content = ""
else:
    print("File read successfully")
finally:
    # Clean up - close file if it was opened
    try:
        file.close()
    except NameError:
        pass  # file was never opened
```

#### Raising Exceptions:
```python
# Raise built-in exceptions
def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numbers")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Re-raise the same exception
try:
    result = divide(10, 0)
except ValueError as e:
    print(f"Caught error: {e}")
    # Do some cleanup, then re-raise
    raise  # Re-raises the same exception

# Raise exception with custom message
def validate_age(age):
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    if age > 150:
        raise ValueError(f"Age seems unrealistic: {age}")
    return True
```

#### Assert Statement:
The `assert` statement is used for debugging and testing assumptions.

```python
# Basic assert
def calculate_average(numbers):
    assert len(numbers) > 0, "Cannot calculate average of empty list"
    assert all(isinstance(n, (int, float)) for n in numbers), "All items must be numbers"
    return sum(numbers) / len(numbers)

# Assert examples
assert 2 + 2 == 4, "Math is broken!"  # Passes silently
# assert 2 + 2 == 5, "This will fail"  # AssertionError: This will fail

# Assert for preconditions
def square_root(x):
    assert x >= 0, f"Cannot calculate square root of negative number: {x}"
    return x ** 0.5

# Assert for postconditions
def factorial(n):
    assert isinstance(n, int) and n >= 0, "n must be a non-negative integer"
    
    if n <= 1:
        result = 1
    else:
        result = n * factorial(n - 1)
    
    assert result >= 1, "Factorial result should be positive"
    return result

# Disable assertions with python -O script.py
# In production, assertions can be disabled for performance
```

#### Exception Objects and Properties:
```python
try:
    # Create a scenario with multiple types of errors
    data = {"name": "John", "age": "not_a_number"}
    age = int(data["age"])
except ValueError as e:
    # Exception object properties
    print(f"Exception type: {type(e)}")
    print(f"Exception message: {str(e)}")
    print(f"Exception args: {e.args}")
    
    # Some exceptions have additional attributes
    print(f"Exception repr: {repr(e)}")

try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError as e:
    print(f"Index error: {e}")
    print(f"Error args: {e.args}")

# Working with exception information
import sys
import traceback

try:
    1 / 0
except:
    # Get exception information
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print(f"Exception type: {exc_type}")
    print(f"Exception value: {exc_value}")
    
    # Print full traceback
    traceback.print_exc()
```

#### Self-Defined Exceptions:
Creating custom exception classes for specific application needs.

```python
# Basic custom exception
class CustomError(Exception):
    """Base exception for our application"""
    pass

# Custom exception with additional attributes
class ValidationError(Exception):
    """Raised when data validation fails"""
    
    def __init__(self, message, field_name=None, value=None):
        super().__init__(message)
        self.field_name = field_name
        self.value = value
        
    def __str__(self):
        if self.field_name:
            return f"Validation error in '{self.field_name}': {super().__str__()}"
        return super().__str__()

# Using custom exceptions
def validate_email(email):
    if not isinstance(email, str):
        raise ValidationError("Email must be a string", "email", email)
    if "@" not in email:
        raise ValidationError("Email must contain @ symbol", "email", email)
    if "." not in email.split("@")[1]:
        raise ValidationError("Email domain must contain a dot", "email", email)
    return True

# Exception hierarchy for an application
class DatabaseError(Exception):
    """Base database exception"""
    pass

class ConnectionError(DatabaseError):
    """Database connection failed"""
    pass

class QueryError(DatabaseError):
    """SQL query failed"""
    
    def __init__(self, message, query=None, error_code=None):
        super().__init__(message)
        self.query = query
        self.error_code = error_code

class RecordNotFoundError(DatabaseError):
    """Requested record not found"""
    
    def __init__(self, table, record_id):
        message = f"Record with ID {record_id} not found in table '{table}'"
        super().__init__(message)
        self.table = table
        self.record_id = record_id

# Using custom exception hierarchy
def get_user(user_id):
    if user_id <= 0:
        raise ValidationError("User ID must be positive", "user_id", user_id)
    
    # Simulate database lookup
    if user_id == 999:
        raise RecordNotFoundError("users", user_id)
    
    return {"id": user_id, "name": f"User{user_id}"}

# Exception handling with custom exceptions
try:
    validate_email("invalid-email")
except ValidationError as e:
    print(f"Validation failed: {e}")
    print(f"Field: {e.field_name}, Value: {e.value}")

try:
    user = get_user(-1)
except ValidationError as e:
    print(f"Input validation error: {e}")
except RecordNotFoundError as e:
    print(f"Database error: {e}")
    print(f"Table: {e.table}, ID: {e.record_id}")
except DatabaseError as e:
    print(f"General database error: {e}")

# Best practices for custom exceptions
class APIError(Exception):
    """Base API exception with HTTP status code support"""
    
    def __init__(self, message, status_code=500, details=None):
        super().__init__(message)
        self.status_code = status_code
        self.details = details or {}
        
    def to_dict(self):
        return {
            "error": str(self),
            "status_code": self.status_code,
            "details": self.details
        }

class BadRequestError(APIError):
    def __init__(self, message, details=None):
        super().__init__(message, status_code=400, details=details)

class NotFoundError(APIError):
    def __init__(self, message, details=None):
        super().__init__(message, status_code=404, details=details)

# Exception chaining (Python 3.0+)
def process_data(data):
    try:
        result = risky_operation(data)
    except ValueError as e:
        # Chain the original exception
        raise ProcessingError("Failed to process data") from e

def risky_operation(data):
    if not data:
        raise ValueError("Data cannot be empty")
    return data.upper()

class ProcessingError(Exception):
    pass

# Example with exception chaining
try:
    process_data("")
except ProcessingError as e:
    print(f"Processing error: {e}")
    print(f"Original cause: {e.__cause__}")
    print(f"Cause type: {type(e.__cause__)}")
```

---

## Module 5: Object-Oriented Programming

### 5.1 Classes and Objects
Python supports full object-oriented programming with classes, objects, inheritance, and polymorphism.

#### Basic Class Definition and Instantiation:
```python
# Basic class definition
class Person:
    """A simple Person class"""
    
    # Class variable (shared by all instances)
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        """Constructor method"""
        # Instance variables (unique to each instance)
        self.name = name
        self.age = age
    
    def introduce(self):
        """Instance method"""
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
    
    def have_birthday(self):
        """Method that modifies instance state"""
        self.age += 1
        return f"Happy birthday! {self.name} is now {self.age} years old."

# Creating objects (instantiation)
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Accessing attributes and methods
print(person1.name)         # Alice
print(person1.introduce())  # Hi, I'm Alice and I'm 30 years old.
print(person1.species)      # Homo sapiens

# Modifying instance
print(person1.have_birthday())  # Happy birthday! Alice is now 31 years old.
```

#### Instance vs Class Variables:
```python
class BankAccount:
    # Class variables (shared by all instances)
    bank_name = "Python Bank"
    interest_rate = 0.02
    total_accounts = 0
    
    def __init__(self, owner, initial_balance=0):
        # Instance variables (unique to each instance)
        self.owner = owner
        self.balance = initial_balance
        self.account_number = BankAccount.total_accounts + 1
        
        # Modify class variable
        BankAccount.total_accounts += 1
    
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"
    
    def get_info(self):
        return f"Account {self.account_number}: {self.owner} - ${self.balance}"

# Creating accounts
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

print(f"Total accounts: {BankAccount.total_accounts}")  # 2
print(f"Bank name: {account1.bank_name}")  # Python Bank
print(f"Interest rate: {account2.interest_rate}")  # 0.02

# Modifying class variable affects all instances
BankAccount.interest_rate = 0.03
print(f"New interest rate for Alice: {account1.interest_rate}")  # 0.03
print(f"New interest rate for Bob: {account2.interest_rate}")    # 0.03
```

#### The __dict__ Property:
The `__dict__` attribute stores an object's attributes in a dictionary.

```python
class Student:
    school_name = "Python University"
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.courses = []
    
    def add_course(self, course):
        self.courses.append(course)

# Create student instance
student = Student("Charlie", 20, "A")
student.add_course("Python Programming")

# Examine __dict__ for instance
print("Instance __dict__:")
print(student.__dict__)
# {'name': 'Charlie', 'age': 20, 'grade': 'A', 'courses': ['Python Programming']}

# Examine __dict__ for class
print("\nClass __dict__:")
print(Student.__dict__)
# Contains class methods, variables, and metadata

# Modifying attributes through __dict__
student.__dict__['age'] = 21  # Same as student.age = 21
print(f"Modified age: {student.age}")  # 21

# Adding new attributes dynamically
student.__dict__['email'] = 'charlie@example.com'
print(f"New email: {student.email}")  # charlie@example.com

# Iterating through instance attributes
print("\nAll instance attributes:")
for key, value in student.__dict__.items():
    print(f"{key}: {value}")

# Difference between instance and class __dict__
print(f"\nInstance has 'name': {'name' in student.__dict__}")      # True
print(f"Class has 'name': {'name' in Student.__dict__}")           # False
print(f"Instance has 'school_name': {'school_name' in student.__dict__}")  # False
print(f"Class has 'school_name': {'school_name' in Student.__dict__}")     # True
```

#### Method Types:
```python
class MathUtils:
    class_var = "I'm a class variable"
    
    def __init__(self, value):
        self.value = value
    
    # Instance method (needs self)
    def instance_method(self):
        return f"Instance method called with value: {self.value}"
    
    # Class method (needs cls, can access class variables)
    @classmethod
    def class_method(cls):
        return f"Class method called. Class var: {cls.class_var}"
    
    # Static method (no self or cls, independent function)
    @staticmethod
    def static_method(a, b):
        return f"Static method: {a} + {b} = {a + b}"
    
    # Alternative class method with parameters
    @classmethod
    def from_string(cls, value_string):
        """Alternative constructor"""
        value = int(value_string)
        return cls(value)  # Return new instance

# Using different method types
math_obj = MathUtils(42)

# Instance method
print(math_obj.instance_method())  # Instance method called with value: 42

# Class method (can call on class or instance)
print(MathUtils.class_method())    # Class method called. Class var: I'm a class variable
print(math_obj.class_method())     # Same result

# Static method (can call on class or instance)
print(MathUtils.static_method(5, 3))  # Static method: 5 + 3 = 8
print(math_obj.static_method(5, 3))   # Same result

# Alternative constructor using class method
math_obj2 = MathUtils.from_string("100")
print(math_obj2.value)  # 100
```

#### Object Introspection:
Python provides several built-in functions for examining objects.

```python
class Vehicle:
    wheels = 4
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start_engine(self):
        return f"{self.brand} {self.model} engine started!"

car = Vehicle("Toyota", "Camry")

# hasattr() - check if object has an attribute
print(hasattr(car, 'brand'))        # True
print(hasattr(car, 'wheels'))       # True
print(hasattr(car, 'color'))        # False
print(hasattr(car, 'start_engine')) # True

# getattr() - get attribute value with optional default
print(getattr(car, 'brand'))                    # Toyota
print(getattr(car, 'color', 'Unknown'))         # Unknown (default)
print(getattr(car, 'wheels'))                   # 4

# setattr() - set attribute value
setattr(car, 'color', 'Blue')
print(car.color)  # Blue

setattr(car, 'year', 2020)
print(car.year)   # 2020

# delattr() - delete attribute
delattr(car, 'year')
print(hasattr(car, 'year'))  # False

# isinstance() - check if object is instance of class
print(isinstance(car, Vehicle))    # True
print(isinstance(car, str))        # False
print(isinstance(car, object))     # True (all classes inherit from object)

# Check multiple types
print(isinstance(42, (int, float, str)))     # True
print(isinstance("hello", (int, float)))     # False

# type() vs isinstance()
print(type(car))                   # <class '__main__.Vehicle'>
print(type(car) == Vehicle)        # True
print(isinstance(car, Vehicle))    # True (preferred for inheritance)

# Object properties and methods
print(f"Object ID: {id(car)}")           # Memory address
print(f"Object type: {type(car)}")       # Class type
print(f"Object dir: {len(dir(car))}")    # Number of attributes/methods
```

#### Advanced Introspection:
```python
import inspect

class Employee:
    company = "Tech Corp"
    
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self._salary = salary  # Protected
        self.__id = hash(name)  # Private
    
    def get_info(self):
        return f"{self.name} - {self.position}"
    
    @classmethod
    def get_company(cls):
        return cls.company
    
    @staticmethod
    def validate_salary(salary):
        return salary > 0

emp = Employee("Alice", "Developer", 75000)

# Get all attributes and methods
all_attributes = dir(emp)
print(f"Total attributes/methods: {len(all_attributes)}")

# Filter by type
instance_attributes = [attr for attr in dir(emp) 
                      if not callable(getattr(emp, attr)) 
                      and not attr.startswith('__')]
print(f"Instance attributes: {instance_attributes}")

methods = [method for method in dir(emp) 
          if callable(getattr(emp, method)) 
          and not method.startswith('__')]
print(f"Methods: {methods}")

# Inspect specific attributes
print(f"Name attribute: {inspect.getattr_static(emp, 'name')}")
print(f"Company class var: {inspect.getattr_static(Employee, 'company')}")

# Check if attribute is method, property, etc.
print(f"get_info is method: {inspect.ismethod(emp.get_info)}")
print(f"name is method: {inspect.ismethod(emp.name)}")

# Get class hierarchy
print(f"MRO (Method Resolution Order): {Employee.__mro__}")

# Object properties: __name__, __module__, __bases__
print(f"Class name: {Employee.__name__}")           # Employee
print(f"Module: {Employee.__module__}")             # __main__
print(f"Base classes: {Employee.__bases__}")        # (<class 'object'>,)

# For inheritance
class Manager(Employee):
    def __init__(self, name, position, salary, team_size):
        super().__init__(name, position, salary)
        self.team_size = team_size

print(f"Manager bases: {Manager.__bases__}")        # (<class '__main__.Employee'>,)
print(f"Manager MRO: {Manager.__mro__}")           # Method Resolution Order

# Practical introspection example
def analyze_object(obj):
    """Analyze any Python object"""
    print(f"\n=== Analysis of {obj} ===")
    print(f"Type: {type(obj)}")
    print(f"Class: {obj.__class__.__name__}")
    print(f"Module: {obj.__class__.__module__}")
    
    # Instance variables
    if hasattr(obj, '__dict__'):
        print(f"Instance variables: {list(obj.__dict__.keys())}")
    
    # Methods
    methods = [m for m in dir(obj) if callable(getattr(obj, m)) and not m.startswith('_')]
    print(f"Public methods: {methods[:5]}...")  # Show first 5
    
    # Check common capabilities
    print(f"Iterable: {hasattr(obj, '__iter__')}")
    print(f"Callable: {callable(obj)}")
    print(f"Has length: {hasattr(obj, '__len__')}")

# Test the analyzer
analyze_object(emp)
analyze_object("hello")
analyze_object([1, 2, 3])
```

### 5.2 Inheritance
Code reusability through inheritance hierarchies with comprehensive examples.

#### Single Inheritance:
```python
# Base class (parent/superclass)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.energy = 100
    
    def eat(self):
        self.energy += 20
        return f"{self.name} is eating. Energy: {self.energy}"
    
    def sleep(self):
        self.energy += 50
        return f"{self.name} is sleeping. Energy: {self.energy}"
    
    def __str__(self):
        return f"{self.name} the {self.species}"

# Derived class (child/subclass)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # Call parent constructor
        self.breed = breed
    
    def bark(self):
        self.energy -= 5
        return f"{self.name} barks! Woof! Energy: {self.energy}"
    
    # Method overriding
    def eat(self):
        self.energy += 25  # Dogs get more energy from eating
        return f"{self.name} the dog is eating happily. Energy: {self.energy}"
    
    # Overriding __str__ method
    def __str__(self):
        return f"{self.name} the {self.breed} dog"

# Usage
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog)           # Buddy the Golden Retriever dog
print(my_dog.eat())     # Buddy the dog is eating happily. Energy: 125
print(my_dog.bark())    # Buddy barks! Woof! Energy: 120
```

#### Identity Operators: `is` and `not is`:
```python
# is vs == operators
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)       # True (same content)
print(a is b)       # False (different objects)
print(a is c)       # True (same object)
print(a is not b)   # True (not the same object)

# Using with inheritance
class Parent:
    pass

class Child(Parent):
    pass

parent_obj = Parent()
child_obj = Child()

print(type(parent_obj) is Parent)    # True
print(type(child_obj) is Child)     # True
print(type(child_obj) is Parent)    # False
print(isinstance(child_obj, Parent)) # True (recommended for inheritance)

# None checking (common use case)
def process_data(data):
    if data is None:
        return "No data provided"
    elif data is not None:
        return f"Processing: {data}"

print(process_data(None))     # No data provided
print(process_data("test"))   # Processing: test
```

#### Multiple Inheritance and Diamond Problem:
```python
# Multiple inheritance example
class Flyable:
    def fly(self):
        return f"{self.__class__.__name__} is flying"

class Swimmable:
    def swim(self):
        return f"{self.__class__.__name__} is swimming"

class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        super().__init__(name, "Duck")
    
    def quack(self):
        return f"{self.name} says quack!"

# Diamond problem demonstration
class A:
    def method(self):
        return "A method"

class B(A):
    def method(self):
        return "B method"

class C(A):
    def method(self):
        return "C method"

class D(B, C):  # Diamond inheritance: D -> B -> A, D -> C -> A
    pass

# Method Resolution Order (MRO) solves diamond problem
diamond_obj = D()
print(diamond_obj.method())  # "B method" (B comes first in MRO)
print(D.__mro__)             # Shows resolution order

# Complex diamond problem with super()
class Vehicle:
    def __init__(self, max_speed):
        self.max_speed = max_speed
        print(f"Vehicle init: max_speed={max_speed}")

class LandVehicle(Vehicle):
    def __init__(self, max_speed, wheels):
        super().__init__(max_speed)
        self.wheels = wheels
        print(f"LandVehicle init: wheels={wheels}")

class WaterVehicle(Vehicle):
    def __init__(self, max_speed, displacement):
        super().__init__(max_speed)
        self.displacement = displacement
        print(f"WaterVehicle init: displacement={displacement}")

class AmphibiousVehicle(LandVehicle, WaterVehicle):
    def __init__(self, max_speed, wheels, displacement):
        # Cooperative inheritance using super()
        LandVehicle.__init__(self, max_speed, wheels)
        WaterVehicle.__init__(self, max_speed, displacement)
        print("AmphibiousVehicle init complete")

# Create amphibious vehicle
amphibious = AmphibiousVehicle(60, 4, 1000)
print(f"MRO: {AmphibiousVehicle.__mro__}")
```

#### Polymorphism:
```python
# Polymorphism through inheritance
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area method")
    
    def perimeter(self):
        raise NotImplementedError("Subclass must implement perimeter method")
    
    def __str__(self):
        return f"{self.__class__.__name__}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius
    
    def __str__(self):
        return f"Circle(radius={self.radius})"

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    
    def area(self):
        # Heron's formula
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def __str__(self):
        return f"Triangle({self.a}, {self.b}, {self.c})"

# Polymorphic behavior
shapes = [
    Rectangle(5, 10),
    Circle(7),
    Triangle(3, 4, 5)
]

# Same interface, different implementations
for shape in shapes:
    print(f"{shape}:")
    print(f"  Area: {shape.area():.2f}")
    print(f"  Perimeter: {shape.perimeter():.2f}")
    print()

# Polymorphic function
def calculate_total_area(shapes_list):
    """Calculate total area of different shapes"""
    total = 0
    for shape in shapes_list:
        total += shape.area()  # Polymorphic method call
    return total

total_area = calculate_total_area(shapes)
print(f"Total area of all shapes: {total_area:.2f}")

# Duck typing (Python's approach to polymorphism)
class Duck:
    def quack(self):
        return "Quack!"
    
    def fly(self):
        return "Flying like a duck"

class Airplane:
    def fly(self):
        return "Flying like an airplane"

def make_it_fly(flying_object):
    """If it can fly, make it fly (duck typing)"""
    try:
        return flying_object.fly()
    except AttributeError:
        return f"{flying_object} cannot fly"

duck = Duck()
plane = Airplane()
car = "Car"

print(make_it_fly(duck))    # Flying like a duck
print(make_it_fly(plane))   # Flying like an airplane
print(make_it_fly(car))     # Car cannot fly
```

**Types:**
- Single inheritance
- Multiple inheritance
- Method overriding
- `super()` function
- Diamond problem resolution
- Polymorphism and duck typing

### 5.3 Encapsulation
Data hiding and access control.

**Access levels:**
- Public: `attribute`
- Protected: `_attribute` (convention)
- Private: `__attribute` (name mangling)
- Properties with `@property` decorator

---

## Module 6: Modules and Packages

### 6.1 Modules
Reusable Python files containing functions, classes, and variables. See `examples/modules/`.

**Import methods:**
- `import module`
- `from module import function`
- `import module as alias`
- `from module import *` (not recommended)

#### Module Introspection with dir():
The `dir()` function returns a list of names in the current local scope or attributes of an object.

```python
# List all built-in functions and variables
print(dir())  # Shows current namespace

# List all attributes of a module
import math
print(dir(math))  # Shows all math module functions and constants

# Example output: ['acos', 'asin', 'atan', 'ceil', 'cos', 'e', 'exp', 'floor', 'log', 'pi', 'sin', 'sqrt', 'tan']

# Check what's available in any object
my_list = [1, 2, 3]
print(dir(my_list))  # Shows all list methods

# Filter to see only non-private attributes
math_functions = [name for name in dir(math) if not name.startswith('_')]
print(math_functions)
```

**Practical uses:**
- Discovering available functions in unfamiliar modules
- Debugging and exploration during development
- Interactive learning about object capabilities

#### Module Search Path with sys.path:
The `sys.path` variable is a list of directories that Python searches when importing modules.

```python
import sys

# View current module search paths
print(sys.path)
# Output: ['', '/usr/lib/python3.9', '/usr/lib/python3.9/lib-dynload', ...]

# Add a custom directory to the search path
sys.path.append('/path/to/my/modules')

# Insert at the beginning (highest priority)
sys.path.insert(0, '/path/to/priority/modules')

# View the modified path
for i, path in enumerate(sys.path):
    print(f"{i}: {path}")

# Remove a path
if '/some/path' in sys.path:
    sys.path.remove('/some/path')
```

**Understanding the search order:**
1. Current directory (empty string `''`)
2. PYTHONPATH environment variable directories
3. Standard library directories
4. Site-packages directory
5. Added paths via `sys.path.append()`

**Common use cases:**
- Adding project-specific module directories
- Debugging import issues
- Understanding why certain modules are found or not found

### 6.2 Packages
Collections of modules organized in directories with `__init__.py` files.

**Key concepts:**
- Package structure
- Relative vs absolute imports
- `__all__` variable
- Package installation with pip

#### Advanced Import Qualifying for Nested Modules:
```python
# Basic nested module structure:
# myproject/
# ├── main.py
# ├── utils/
# │   ├── __init__.py
# │   ├── math_tools.py
# │   └── string_tools.py
# └── data/
#     ├── __init__.py
#     └── processors/
#         ├── __init__.py
#         └── csv_processor.py

# Advanced qualifying examples
import utils.math_tools
from utils import string_tools
from utils.math_tools import calculate_average
from data.processors.csv_processor import process_csv

# Relative imports (within packages)
# In utils/string_tools.py:
from . import math_tools          # Import sibling module
from ..data import processors     # Import from parent's sibling
from .math_tools import add       # Import specific function from sibling

# Absolute vs relative imports
from myproject.utils import math_tools    # Absolute import
from . import math_tools                  # Relative import (same package)
```

#### Public and Private Variables in Modules:
```python
# In my_module.py

# Public variables (normal names)
public_constant = 42
public_function = lambda x: x * 2

# Protected variables (single underscore - convention only)
_internal_cache = {}
_helper_function = lambda x: x + 1

# Private variables (double underscore - not imported with "from module import *")
__private_secret = "hidden"
__private_function = lambda x: x - 1

# Special variables
__version__ = "1.0.0"
__author__ = "Python Developer"
__all__ = ['public_constant', 'public_function']  # Controls "from module import *"

# Usage example:
# >>> from my_module import *
# >>> print(public_constant)      # 42 - works
# >>> print(_internal_cache)      # NameError - not imported
# >>> print(__private_secret)     # NameError - not imported

# Direct import still works for all
# >>> import my_module
# >>> print(my_module.__private_secret)  # "hidden" - works
```

#### Detailed __init__.py File Usage:
```python
# Package structure:
# mypackage/
# ├── __init__.py
# ├── module1.py
# ├── module2.py
# └── subpackage/
#     ├── __init__.py
#     └── submodule.py

# mypackage/__init__.py
"""
Main package initialization file
"""
# Import commonly used functions to package level
from .module1 import important_function
from .module2 import utility_class
from .subpackage import submodule

# Define package-level variables
__version__ = "1.2.3"
__author__ = "Package Author"

# Control what gets imported with "from mypackage import *"
__all__ = [
    'important_function',
    'utility_class', 
    'submodule',
    'package_constant'
]

# Package-level constants
package_constant = "Available at package level"

# Package initialization code
print(f"Initializing mypackage version {__version__}")

# Conditional imports based on dependencies
try:
    import numpy
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

# Usage after this setup:
# >>> import mypackage
# >>> mypackage.important_function()  # Available directly
# >>> mypackage.__version__           # "1.2.3"
```

#### Searching for/through Modules and Packages:
```python
import sys
import os
from importlib import util

# How Python searches for modules
def show_module_search_path():
    print("Python searches for modules in this order:")
    for i, path in enumerate(sys.path):
        print(f"{i+1}. {path}")

show_module_search_path()

# Find where a module is located
def find_module_location(module_name):
    try:
        import importlib
        spec = importlib.util.find_spec(module_name)
        if spec:
            return spec.origin
        return None
    except ImportError:
        return None

print(f"math module location: {find_module_location('math')}")
print(f"os module location: {find_module_location('os')}")

# Check if module exists without importing
def module_exists(module_name):
    return util.find_spec(module_name) is not None

print(f"numpy exists: {module_exists('numpy')}")
print(f"nonexistent exists: {module_exists('nonexistent_module')}")

# Dynamically import modules
def dynamic_import(module_name):
    try:
        module = __import__(module_name)
        return module
    except ImportError as e:
        print(f"Failed to import {module_name}: {e}")
        return None

# Import module by file path
def import_from_path(name, path):
    spec = util.spec_from_file_location(name, path)
    if spec:
        module = util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    return None
```

#### Nested Packages vs. Directory Trees:
```python
# Regular directory tree (NOT a Python package):
# project/
# ├── data.txt
# ├── scripts/
# │   ├── process.py
# │   └── analyze.py
# └── results/
#     └── output.txt

# Python package structure (WITH __init__.py files):
# myproject/
# ├── __init__.py          # Makes myproject a package
# ├── core/
# │   ├── __init__.py      # Makes core a subpackage
# │   ├── engine.py
# │   └── utils.py
# ├── plugins/
# │   ├── __init__.py      # Makes plugins a subpackage
# │   ├── loader.py
# │   └── validator.py
# └── tests/
#     ├── __init__.py      # Makes tests a subpackage
#     └── test_core.py

# Key differences demonstration:
import os

def analyze_structure(path, level=0):
    """Analyze if directory structure is a Python package"""
    indent = "  " * level
    name = os.path.basename(path)
    
    if os.path.isfile(os.path.join(path, '__init__.py')):
        print(f"{indent}{name}/ [PACKAGE]")
    else:
        print(f"{indent}{name}/ [DIRECTORY]")
    
    if os.path.isdir(path):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                analyze_structure(item_path, level + 1)
            elif item.endswith('.py'):
                print(f"{indent}  {item} [MODULE]")

# Package import behavior
try:
    # This works if core is a package (has __init__.py)
    from myproject.core import engine
    print("Successfully imported from package")
except ImportError:
    print("Failed to import - not a proper package structure")

# Namespace packages (Python 3.3+) - no __init__.py required
# But regular packages with __init__.py are still recommended
```

#### Understanding __pycache__:
When Python imports a module, it compiles the source code to bytecode and stores it in `__pycache__` directories for faster loading.

```python
# When you import a module for the first time:
import my_module  # Creates __pycache__/my_module.cpython-39.pyc

# File structure after import:
# my_project/
# ├── my_module.py
# └── __pycache__/
#     └── my_module.cpython-39.pyc
```

**Key points:**
- `.pyc` files contain compiled bytecode (not source code)
- Filename format: `module.cpython-{version}.pyc`
- Python automatically manages these files
- Speeds up subsequent imports
- Safe to delete (will be recreated when needed)

**Bytecode compilation process:**
1. Python reads `.py` source file
2. Compiles to bytecode
3. Stores in `__pycache__/module.cpython-version.pyc`
4. Future imports load bytecode directly (if source unchanged)

```python
# You can manually compile modules
import py_compile

# Compile a single file
py_compile.compile('my_module.py')

# Compile all files in a directory
import compileall
compileall.compile_dir('my_package/')
```

#### The __name__ Variable:
The `__name__` variable is a built-in variable that contains the name of the current module.

```python
# In a file called my_module.py
print(f"Module name: {__name__}")

# When imported: prints "Module name: my_module"
# When run directly: prints "Module name: __main__"
```

**Common usage pattern - Script vs Module:**
```python
# my_script.py
def main_function():
    print("This is the main function")

def helper_function():
    return "I'm a helper"

# This block only runs when file is executed directly
if __name__ == "__main__":
    print("Running as main script")
    main_function()
else:
    print("Imported as module")

# Usage examples:
# python my_script.py          → "Running as main script"
# import my_script             → "Imported as module"
```

**Practical applications:**
```python
# test_module.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# Testing code that only runs when executed directly
if __name__ == "__main__":
    # Test the functions
    assert add(2, 3) == 5
    assert multiply(4, 5) == 20
    print("All tests passed!")
    
    # Interactive examples
    print(f"2 + 3 = {add(2, 3)}")
    print(f"4 * 5 = {multiply(4, 5)}")
```

**In package context:**
```python
# In package/submodule.py
print(f"Full module name: {__name__}")  # "package.submodule"

# Check if running from specific package
if __name__.startswith('mypackage'):
    print("Running from mypackage")
```

### 6.3 Standard Library Modules

#### Math Module:
The `math` module provides mathematical functions and constants.

```python
import math

# Rounding and truncation functions
print(math.ceil(4.2))    # 5 - smallest integer >= x
print(math.floor(4.8))   # 4 - largest integer <= x
print(math.trunc(4.8))   # 4 - truncate to integer (towards zero)

# Mathematical functions
print(math.sqrt(16))     # 4.0 - square root
print(math.factorial(5)) # 120 - factorial (5! = 5*4*3*2*1)
print(math.hypot(3, 4))  # 5.0 - Euclidean distance sqrt(x*x + y*y)

# Mathematical constants
print(math.pi)           # 3.141592653589793
print(math.e)            # 2.718281828459045

# Trigonometric functions
print(math.sin(math.pi/2))  # 1.0
print(math.cos(0))          # 1.0
print(math.tan(math.pi/4))  # 1.0

# Logarithmic functions
print(math.log(math.e))     # 1.0 - natural logarithm
print(math.log10(100))      # 2.0 - base-10 logarithm

# Power and exponential
print(math.pow(2, 3))       # 8.0 - x raised to power y
print(math.exp(1))          # 2.718... - e raised to power x
```

#### Random Module:
The `random` module provides functions for generating random numbers and making random choices.

```python
import random

# Basic random number generation
print(random.random())        # Random float between 0.0 and 1.0

# Set seed for reproducible results
random.seed(42)               # Same seed = same sequence
print(random.random())        # Will always be same with seed 42

# Random integers
print(random.randint(1, 10))  # Random integer between 1 and 10 (inclusive)
print(random.randrange(0, 10, 2))  # Random even number between 0 and 8

# Random choice from sequence
fruits = ['apple', 'banana', 'cherry', 'date']
print(random.choice(fruits))  # Random single item

# Multiple random choices (with replacement)
print(random.choices(fruits, k=3))  # List of 3 random items

# Random sample (without replacement)
print(random.sample(fruits, 2))     # List of 2 unique items

# Shuffle a list in place
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)                # List is now shuffled

# Random float in range
print(random.uniform(1.5, 10.5))  # Random float between 1.5 and 10.5
```

#### Platform Module:
The `platform` module provides information about the underlying platform.

```python
import platform

# System information
print(platform.platform())      # Complete platform string
print(platform.system())        # OS name (Windows, Linux, Darwin)
print(platform.machine())       # Machine type (x86_64, AMD64)
print(platform.processor())     # Processor name

# Version information
print(platform.version())       # OS version
print(platform.release())       # OS release

# Python-specific information
print(platform.python_implementation())  # CPython, PyPy, Jython
print(platform.python_version())         # Python version string
print(platform.python_version_tuple())   # Version as tuple ('3', '9', '7')

# Architecture information
print(platform.architecture())   # Architecture and linkage info

# Example usage for cross-platform code
if platform.system() == 'Windows':
    print("Running on Windows")
    # Windows-specific code
elif platform.system() == 'Linux':
    print("Running on Linux")
    # Linux-specific code
elif platform.system() == 'Darwin':
    print("Running on macOS")
    # macOS-specific code
```

---

## Module 7: String Methods and String Processing

### 7.1 String Operations
Comprehensive string manipulation. See `examples/strings/`.

**Categories:**
- Case methods: `upper()`, `lower()`, `title()`
- Search: `find()`, `index()`, `count()`
- Split/Join: `split()`, `join()`
- Formatting: f-strings, `format()`, `%` formatting
- Validation: `isdigit()`, `isalpha()`, `isalnum()`

#### Character Encoding and ord()/chr() Functions:
Understanding how characters are represented as numbers.

```python
# ord() - convert character to Unicode code point
print(ord('A'))        # 65
print(ord('a'))        # 97
print(ord('0'))        # 48
print(ord('€'))        # 8364
print(ord('世'))       # 19990

# chr() - convert Unicode code point to character
print(chr(65))         # 'A'
print(chr(97))         # 'a'
print(chr(8364))       # '€'
print(chr(19990))      # '世'

# Practical examples
def caesar_cipher(text, shift):
    """Simple Caesar cipher using ord() and chr()"""
    result = ""
    for char in text:
        if char.isalpha():
            # Handle uppercase and lowercase separately
            if char.isupper():
                shifted = (ord(char) - ord('A') + shift) % 26
                result += chr(shifted + ord('A'))
            else:
                shifted = (ord(char) - ord('a') + shift) % 26
                result += chr(shifted + ord('a'))
        else:
            result += char
    return result

print(caesar_cipher("Hello World!", 3))  # "Khoor Zruog!"

# Character ranges
print("ASCII digits:", [chr(i) for i in range(ord('0'), ord('9') + 1)])
print("ASCII uppercase:", [chr(i) for i in range(ord('A'), ord('Z') + 1)])
print("ASCII lowercase:", [chr(i) for i in range(ord('a'), ord('z') + 1)])
```

#### Encoding Standards:
Understanding different character encoding systems.

**ASCII (American Standard Code for Information Interchange):**
- 7-bit encoding (0-127)
- Basic English characters, digits, punctuation
- Limited to 128 characters

**Unicode:**
- Universal character set
- Supports all world languages
- Code points from U+0000 to U+10FFFF
- Over 1 million possible characters

**UTF-8 (Unicode Transformation Format - 8-bit):**
- Variable-length encoding of Unicode
- 1-4 bytes per character
- Backward compatible with ASCII
- Most common Unicode encoding

```python
# Encoding and decoding examples
text = "Hello, 世界! 🌍"

# Encode string to bytes
utf8_bytes = text.encode('utf-8')
ascii_bytes = "Hello".encode('ascii')

print(f"UTF-8 bytes: {utf8_bytes}")
print(f"ASCII bytes: {ascii_bytes}")

# Decode bytes to string
decoded_text = utf8_bytes.decode('utf-8')
print(f"Decoded: {decoded_text}")

# Different encodings
try:
    # This will fail - emoji can't be encoded in ASCII
    text.encode('ascii')
except UnicodeEncodeError as e:
    print(f"Encoding error: {e}")

# Handle encoding errors
safe_ascii = text.encode('ascii', errors='ignore')  # Skip problematic chars
print(f"ASCII with errors ignored: {safe_ascii}")

# Check encoding of bytes
import chardet
detected = chardet.detect(utf8_bytes)
print(f"Detected encoding: {detected}")
```

#### Comprehensive String Methods:

**Validation Methods:**
```python
text = "Hello123"

# Character type checking
print(text.isalnum())     # True - alphanumeric
print(text.isalpha())     # False - contains digits
print(text.isdigit())     # False - contains letters
print(text.isnumeric())   # False - contains letters
print(text.isdecimal())   # False - contains letters

# Case checking
print("HELLO".isupper())  # True
print("hello".islower())  # True
print("Hello".istitle())  # True

# Whitespace checking
print("   ".isspace())    # True
print("Hello World".isspace())  # False

# Specific examples
examples = ["123", "12.3", "Hello", "HELLO", "hello", "Hello World", "   ", ""]
for ex in examples:
    print(f"'{ex}': digit={ex.isdigit()}, alpha={ex.isalpha()}, "
          f"alnum={ex.isalnum()}, space={ex.isspace()}")
```

**Search and Find Methods:**
```python
text = "The quick brown fox jumps over the lazy dog"

# find() vs index() - both search for substring
print(text.find("fox"))      # 16 - returns index
print(text.find("cat"))      # -1 - not found
print(text.index("fox"))     # 16 - returns index
# print(text.index("cat"))   # ValueError - not found

# rfind() - find from right
print(text.rfind("the"))     # 31 - last occurrence of "the"
print(text.find("the"))      # 0 - first occurrence of "the"

# count() - count occurrences
print(text.count("o"))       # 4
print(text.count("the"))     # 1 (case-sensitive)
print(text.lower().count("the"))  # 2 (case-insensitive)

# Practical search example
def find_all_positions(text, substring):
    """Find all positions of substring in text"""
    positions = []
    start = 0
    while True:
        pos = text.find(substring, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1
    return positions

print(find_all_positions("hello world hello", "l"))  # [2, 3, 9, 10, 15]
```

### 7.2 String Processing
Advanced text processing techniques.

**Topics:**
- Regular expressions with `re` module
- Text parsing and validation
- Character encoding (UTF-8)

---

## Module 8: File Handling

### 8.1 File Operations
Python provides comprehensive file handling capabilities for reading, writing, and manipulating files.

#### File Opening and Modes:
```python
# Basic file opening syntax: open(filename, mode, encoding)

# Text modes (default)
file = open("example.txt", "r")          # Read mode
file = open("example.txt", "w")          # Write mode (overwrites)
file = open("example.txt", "a")          # Append mode
file = open("example.txt", "x")          # Exclusive creation (fails if exists)

# Binary modes
file = open("image.jpg", "rb")           # Read binary
file = open("data.bin", "wb")            # Write binary
file = open("log.bin", "ab")             # Append binary

# Read and write modes
file = open("data.txt", "r+")            # Read and write
file = open("data.txt", "w+")            # Write and read (overwrites)
file = open("data.txt", "a+")            # Append and read

# With encoding specification
file = open("unicode.txt", "r", encoding="utf-8")
file = open("latin.txt", "w", encoding="latin1")

# Always close files (manual way)
file.close()
```

#### The with Statement (Context Manager):
```python
# Recommended approach - automatic file closing
with open("example.txt", "r") as file:
    content = file.read()
    # File is automatically closed when exiting the with block

# Multiple files
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    data = infile.read()
    outfile.write(data.upper())

# Exception handling with context manager
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
```

#### Reading Files:
```python
# 1. Read entire file
with open("data.txt", "r") as file:
    content = file.read()           # Returns entire file as string
    print(content)

# 2. Read specific number of characters
with open("data.txt", "r") as file:
    first_10_chars = file.read(10)  # Read first 10 characters
    print(first_10_chars)

# 3. Read line by line
with open("data.txt", "r") as file:
    line1 = file.readline()         # Read first line
    line2 = file.readline()         # Read second line
    print(f"Line 1: {line1.strip()}")
    print(f"Line 2: {line2.strip()}")

# 4. Read all lines into a list
with open("data.txt", "r") as file:
    lines = file.readlines()        # Returns list of lines
    for i, line in enumerate(lines):
        print(f"Line {i+1}: {line.strip()}")

# 5. Iterate through file (memory efficient)
with open("data.txt", "r") as file:
    for line_number, line in enumerate(file, 1):
        print(f"Line {line_number}: {line.strip()}")
```

#### Writing Files:
```python
# 1. Write string to file (overwrites existing content)
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.\n")

# 2. Write multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)

# 3. Append to existing file
with open("output.txt", "a") as file:
    file.write("This line is appended.\n")

# 4. Write with formatting
data = {"name": "Alice", "age": 30, "city": "New York"}
with open("person.txt", "w") as file:
    file.write(f"Name: {data['name']}\n")
    file.write(f"Age: {data['age']}\n")
    file.write(f"City: {data['city']}\n")

# 5. Write using print() function
with open("output.txt", "w") as file:
    print("Hello, World!", file=file)
    print("Line 2", file=file)
    print("Multiple", "values", "separated", file=file)
```

#### errno Variable and Error Values:
```python
import errno
import os

# errno provides error codes for system calls
def safe_file_operation_with_errno(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except OSError as e:
        if e.errno == errno.ENOENT:
            return f"File not found: {filename}"
        elif e.errno == errno.EACCES:
            return f"Permission denied: {filename}"
        elif e.errno == errno.EISDIR:
            return f"Is a directory: {filename}"
        elif e.errno == errno.EMFILE:
            return "Too many open files"
        elif e.errno == errno.ENOSPC:
            return "No space left on device"
        else:
            return f"OS error {e.errno}: {e.strerror}"

# Common errno values
print(f"ENOENT (No such file): {errno.ENOENT}")
print(f"EACCES (Permission denied): {errno.EACCES}")
print(f"EISDIR (Is a directory): {errno.EISDIR}")
print(f"ENOSPC (No space left): {errno.ENOSPC}")

# Test with different error conditions
print(safe_file_operation_with_errno("nonexistent.txt"))
print(safe_file_operation_with_errno("/etc/shadow"))  # Permission denied on Unix
```

#### Predefined Streams:
```python
import sys

# Python has three predefined streams
print("Standard streams in Python:")
print(f"stdin: {sys.stdin}")   # Standard input
print(f"stdout: {sys.stdout}") # Standard output  
print(f"stderr: {sys.stderr}") # Standard error

# Using predefined streams
def demonstrate_streams():
    # Write to stdout (normal output)
    sys.stdout.write("This goes to stdout\n")
    
    # Write to stderr (error output)
    sys.stderr.write("This goes to stderr\n")
    
    # Read from stdin (but don't actually do this in demo)
    # user_input = sys.stdin.read()
    
    # Flush output buffers
    sys.stdout.flush()
    sys.stderr.flush()

demonstrate_streams()

# Redirecting streams
import io

def redirect_output_example():
    # Capture stdout
    old_stdout = sys.stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    # This will go to captured_output instead of console
    print("This output is captured")
    print("So is this")
    
    # Restore stdout
    sys.stdout = old_stdout
    
    # Get captured content
    output = captured_output.getvalue()
    print(f"Captured: {repr(output)}")

redirect_output_example()

# Stream properties
def analyze_stream(stream, name):
    print(f"\n{name} properties:")
    print(f"  Readable: {stream.readable()}")
    print(f"  Writable: {stream.writable()}")
    print(f"  Seekable: {stream.seekable()}")
    print(f"  Closed: {stream.closed}")

analyze_stream(sys.stdin, "stdin")
analyze_stream(sys.stdout, "stdout")
analyze_stream(sys.stderr, "stderr")
```

#### Handles vs Streams:
```python
# Understanding the difference between handles and streams

# File handle (low-level, OS specific)
import os

def demonstrate_file_handles():
    # Open file and get file descriptor (handle)
    fd = os.open("test_handle.txt", os.O_CREAT | os.O_WRONLY | os.O_TRUNC)
    print(f"File descriptor (handle): {fd}")
    
    # Write using handle
    os.write(fd, b"Hello from file handle\n")
    
    # Close handle
    os.close(fd)
    
    # Verify content
    with open("test_handle.txt", "r") as f:
        print(f"Content: {f.read()}")

# File stream (high-level, Python file object)
def demonstrate_file_streams():
    # Open file and get stream object
    stream = open("test_stream.txt", "w")
    print(f"Stream object: {stream}")
    print(f"Stream fileno (underlying handle): {stream.fileno()}")
    
    # Write using stream
    stream.write("Hello from file stream\n")
    
    # Close stream
    stream.close()

demonstrate_file_handles()
demonstrate_file_streams()

# Key differences:
print("\nHandles vs Streams:")
print("Handles (file descriptors):")
print("  - Low-level OS concept")
print("  - Integer numbers")
print("  - Used with os.open(), os.read(), os.write()")
print("  - Platform specific")

print("\nStreams (file objects):")
print("  - High-level Python concept")
print("  - File-like objects")
print("  - Used with open(), .read(), .write()")
print("  - Cross-platform")
print("  - Built on top of handles")

# Stream wrapping handles
def wrap_handle_in_stream():
    # Open with handle
    fd = os.open("wrapped.txt", os.O_CREAT | os.O_RDWR | os.O_TRUNC)
    
    # Wrap handle in stream
    stream = os.fdopen(fd, "w+")
    
    # Now use as normal stream
    stream.write("Handle wrapped in stream\n")
    stream.seek(0)
    content = stream.read()
    print(f"Read from wrapped stream: {content}")
    
    stream.close()  # This also closes the underlying handle

wrap_handle_in_stream()
```

#### bytearray as Input/Output Buffer:
```python
# bytearray for efficient I/O operations

def demonstrate_bytearray_io():
    # Create bytearray buffer
    buffer = bytearray(1024)  # 1KB buffer
    print(f"Empty buffer: {len(buffer)} bytes")
    
    # Write data to file
    data = b"Hello, World! This is binary data.\n" * 10
    with open("binary_data.bin", "wb") as file:
        file.write(data)
    
    # Read into bytearray buffer
    with open("binary_data.bin", "rb") as file:
        bytes_read = file.readinto(buffer)
        print(f"Read {bytes_read} bytes into buffer")
        print(f"First 50 bytes: {buffer[:50]}")
    
    # Modify buffer contents
    buffer[0:5] = b"HELLO"
    
    # Write buffer back to different file
    with open("modified_data.bin", "wb") as file:
        file.write(buffer[:bytes_read])
    
    print("Buffer operations completed")

demonstrate_bytearray_io()

# Advanced bytearray I/O
def efficient_file_copying_with_bytearray(source, destination, buffer_size=8192):
    """Copy file using bytearray for efficiency"""
    buffer = bytearray(buffer_size)
    
    with open(source, "rb") as src, open(destination, "wb") as dst:
        while True:
            bytes_read = src.readinto(buffer)
            if bytes_read == 0:
                break
            dst.write(buffer[:bytes_read])
    
    print(f"Copied {source} to {destination} using {buffer_size} byte buffer")

# Create test file and copy it
with open("source_file.txt", "w") as f:
    f.write("Test data for copying\n" * 1000)

efficient_file_copying_with_bytearray("source_file.txt", "copied_file.txt")

# bytearray manipulation for data processing
def process_binary_data():
    # Read binary data into bytearray
    with open("binary_data.bin", "rb") as file:
        data = bytearray(file.read())
    
    print(f"Original data size: {len(data)} bytes")
    
    # Process data (example: XOR encryption)
    key = 0x42
    for i in range(len(data)):
        data[i] ^= key
    
    # Write processed data
    with open("encrypted_data.bin", "wb") as file:
        file.write(data)
    
    print("Data processed and saved")
    
    # Decrypt (XOR again with same key)
    for i in range(len(data)):
        data[i] ^= key
    
    # Verify decryption
    with open("decrypted_data.bin", "wb") as file:
        file.write(data)
    
    print("Data decrypted and verified")

process_binary_data()

# Memory-mapped file simulation with bytearray
def simulate_memory_mapped_file():
    # Create large data
    large_data = bytearray(b"Data chunk " * 1000)
    
    # Simulate reading/writing specific sections
    chunk_size = 100
    
    # Read chunk from "file" (bytearray)
    start = 500
    chunk = large_data[start:start + chunk_size]
    print(f"Read chunk: {chunk[:20]}...")
    
    # Modify chunk
    modified_chunk = bytearray(b"Modified! " * 10)
    large_data[start:start + len(modified_chunk)] = modified_chunk
    
    print("Simulated memory-mapped file operations")

simulate_memory_mapped_file()

# Cleanup
import os
for filename in ["test_handle.txt", "test_stream.txt", "wrapped.txt", 
                "binary_data.bin", "modified_data.bin", "source_file.txt", 
                "copied_file.txt", "encrypted_data.bin", "decrypted_data.bin"]:
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass
```

### 8.2 File Types
Working with different file formats.

**Supported types:**
- Text files
- CSV files (with `csv` module)
- JSON files (with `json` module)
- Binary files

---

## Practice Exercises and Certification Tips

### Key Areas to Focus On:
1. **Data Types and Operations** - Lists, tuples, dictionaries, sets
2. **Control Flow** - if/elif/else, loops, break/continue
3. **Functions** - Parameters, scope, lambda functions
4. **OOP Basics** - Classes, inheritance, encapsulation
5. **Exception Handling** - try/except/else/finally
6. **File I/O** - Reading/writing files, error handling
7. **String Processing** - Methods, formatting, validation

### Common Exam Patterns:
- Code output prediction
- Error identification
- Code completion
- Best practice selection

### Study Strategy:
1. **Practice coding daily** - Use examples in `examples/` folder
2. **Take practice tests** - Focus on time management
3. **Review error patterns** - Common mistakes and solutions
4. **Understand built-in functions** - `len()`, `range()`, `enumerate()`, etc.

---

## Useful Resources and Links

### Official Documentation:
- **Python.org**: [docs.python.org](https://docs.python.org/3/)
- **Python Tutorial**: [docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/)

### PCAP Certification:
- **Python Institute**: [pythoninstitute.org](https://pythoninstitute.org)
- **PCAP Details**: [pythoninstitute.org/pcap](https://pythoninstitute.org/pcap)

### Practice Platforms:
- **LeetCode**: [leetcode.com](https://leetcode.com)
- **HackerRank**: [hackerrank.com](https://hackerrank.com)
- **Codewars**: [codewars.com](https://codewars.com)

### Learning Resources:
- **Real Python**: [realpython.com](https://realpython.com)
- **Automate the Boring Stuff**: [automatetheboringstuff.com](https://automatetheboringstuff.com)

---

## Code Examples

All practical examples are organized in the `examples/` folder:

```
examples/
├── basics/           # Variables, data types, operators
├── control_flow/     # if/else, loops, logical operations
├── functions/        # Function definitions, parameters, scope
├── data_structures/  # Lists, tuples, dictionaries, sets
├── oop/             # Classes, inheritance, polymorphism
├── modules/         # Module creation and imports
├── strings/         # String methods and processing
├── files/           # File I/O operations
├── exceptions/      # Error handling examples
└── practice/        # PCAP-style practice problems
```

---

**Good luck with your PCAP certification!** 🐍

*This comprehensive guide covers all PCAP exam objectives. Practice regularly with the provided examples and focus on understanding concepts rather than memorizing syntax.*
