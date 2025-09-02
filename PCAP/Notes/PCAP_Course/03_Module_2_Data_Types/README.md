# Module 2: Data Types, Variables, and Basic Operations
## Mastering Python's Data Foundation

Welcome to Module 2! This module covers the fundamental building blocks of Python programming: variables, data types, and basic operations. You'll learn how to store, manipulate, and work with different types of data in Python.

## 🎯 Module Objectives

By the end of this module, you will be able to:
- Understand and use Python's core data types
- Create and manipulate variables effectively
- Perform type conversions and checking
- Use input/output operations
- Apply arithmetic, comparison, and logical operators
- Understand operator precedence and associativity

## 📋 What You'll Learn

### 1. Variables and Assignment
- Variable naming conventions
- Assignment operators
- Multiple assignment
- Variable scope basics

### 2. Data Types
- Numeric types (int, float, complex)
- String type and operations
- Boolean type and operations
- Type checking and conversion

### 3. Input and Output
- Input functions and validation
- Output formatting
- String formatting methods

### 4. Operators
- Arithmetic operators
- Comparison operators
- Logical operators
- Assignment operators
- Operator precedence

## 🚀 Getting Started

### Prerequisites
- Completed Module 1 (Python Fundamentals)
- Python 3.8+ installed and working
- Basic understanding of Python syntax

### Estimated Time
- **Reading**: 2-3 hours
- **Practice**: 3-4 hours
- **Exercises**: 2-3 hours
- **Total**: 7-10 hours

## 📚 Module Content

### Section 1: Variables and Assignment

#### What are Variables?
Variables are containers for storing data values. In Python, variables are created when you assign a value to them.

```python
# Variable assignment
name = "John"
age = 25
height = 1.75
is_student = True

# Multiple assignment
x, y, z = 1, 2, 3
a = b = c = 0

# Variable naming conventions
user_name = "john_doe"      # snake_case (recommended)
userName = "johnDoe"        # camelCase
UserName = "JohnDoe"        # PascalCase
```

#### Variable Naming Rules
- **Must start with** a letter (a-z, A-Z) or underscore (_)
- **Can contain** letters, digits, and underscores
- **Case sensitive** (age ≠ Age ≠ AGE)
- **Cannot use** Python keywords (if, for, while, etc.)
- **Descriptive names** are recommended

```python
# Good variable names
first_name = "John"
last_name = "Doe"
age_in_years = 25
is_employed = True

# Avoid these names
1name = "John"      # SyntaxError: cannot start with digit
my-name = "John"    # SyntaxError: cannot use hyphens
if = "condition"    # SyntaxError: cannot use keyword
```

#### Assignment Operators

```python
# Basic assignment
x = 5

# Compound assignment operators
x += 3      # x = x + 3
x -= 2      # x = x - 2
x *= 4      # x = x * 4
x /= 2      # x = x / 2
x //= 2     # x = x // 2 (floor division)
x %= 3      # x = x % 3 (modulo)
x **= 2     # x = x ** 2 (exponentiation)

# Multiple assignment
a, b = 10, 20
a, b = b, a  # Swap values
```

### Section 2: Data Types

#### Numeric Types

**Integer (int)**
```python
# Positive and negative integers
positive_int = 42
negative_int = -17
zero = 0

# Large integers (no size limit)
large_number = 123456789012345678901234567890

# Binary, octal, and hexadecimal
binary = 0b1010        # 10 in decimal
octal = 0o17           # 15 in decimal
hexadecimal = 0xFF     # 255 in decimal
```

**Float (float)**
```python
# Decimal numbers
pi = 3.14159
negative_float = -2.5
scientific = 1.23e-4   # 0.000123

# Float precision
x = 0.1 + 0.2
print(x)                # 0.30000000000000004 (floating point precision)
```

**Complex (complex)**
```python
# Complex numbers
z = 3 + 4j
real_part = z.real      # 3.0
imaginary_part = z.imag # 4.0
conjugate = z.conjugate() # 3 - 4j
```

#### String Type (str)

```python
# String creation
single_quotes = 'Hello, World!'
double_quotes = "Python Programming"
triple_quotes = """Multi-line
string with
line breaks"""

# String operations
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # Concatenation
repeated = "Ha" * 3                       # Repetition: "HaHaHa"

# String methods
text = "  Hello, World!  "
print(text.strip())           # "Hello, World!" (remove whitespace)
print(text.upper())           # "  HELLO, WORLD!  "
print(text.lower())           # "  hello, world!  "
print(text.replace("World", "Python"))  # "  Hello, Python!  "
```

#### Boolean Type (bool)

```python
# Boolean values
is_true = True
is_false = False

# Boolean operations
and_result = True and False    # False
or_result = True or False      # True
not_result = not True          # False

# Truthiness
print(bool(0))        # False
print(bool(1))        # True
print(bool(""))       # False
print(bool("Hello"))  # True
print(bool([]))       # False
print(bool([1, 2]))   # True
```

#### Type Checking and Conversion

```python
# Type checking
x = 42
y = "Hello"
z = 3.14

print(type(x))        # <class 'int'>
print(type(y))        # <class 'str'>
print(type(z))        # <class 'float'>

# Type conversion
string_number = "123"
number = int(string_number)    # Convert string to int
float_number = float(number)   # Convert int to float
string_float = str(float_number)  # Convert float to string

# Safe conversions
try:
    number = int("abc")
except ValueError:
    print("Cannot convert 'abc' to integer")

# Boolean conversion
print(bool(0))        # False
print(bool(1))        # True
print(bool(-1))       # True
print(bool(""))       # False
print(bool("Hello"))  # True
```

### Section 3: Input and Output Operations

#### Input Function

```python
# Basic input
name = input("Enter your name: ")
age = input("Enter your age: ")

# Input always returns a string
print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")

# Converting input to appropriate type
age = int(input("Enter your age: "))
height = float(input("Enter your height (meters): "))
is_student = input("Are you a student? (y/n): ").lower() == 'y'

# Input validation
while True:
    try:
        age = int(input("Enter your age: "))
        if 0 <= age <= 150:
            break
        else:
            print("Age must be between 0 and 150")
    except ValueError:
        print("Please enter a valid number")
```

#### Output and Formatting

```python
# Basic print
print("Hello, World!")
print("Multiple", "values", "separated", "by", "commas")

# Print with separator and end
print("Hello", "World", sep="-", end="!\n")

# String formatting methods
name = "John"
age = 25
height = 1.75

# Method 1: f-strings (Python 3.6+)
print(f"My name is {name}, I am {age} years old, and {height}m tall")

# Method 2: .format() method
print("My name is {}, I am {} years old, and {}m tall".format(name, age, height))
print("My name is {n}, I am {a} years old, and {h}m tall".format(n=name, a=age, h=height))

# Method 3: % operator (legacy)
print("My name is %s, I am %d years old, and %.2fm tall" % (name, age, height))

# Formatting numbers
pi = 3.14159
print(f"Pi rounded to 2 decimal places: {pi:.2f}")
print(f"Pi in scientific notation: {pi:.2e}")
```

### Section 4: Operators

#### Arithmetic Operators

```python
# Basic arithmetic
a, b = 10, 3

print(f"{a} + {b} = {a + b}")    # Addition: 10 + 3 = 13
print(f"{a} - {b} = {a - b}")    # Subtraction: 10 - 3 = 7
print(f"{a} * {b} = {a * b}")    # Multiplication: 10 * 3 = 30
print(f"{a} / {b} = {a / b}")    # Division: 10 / 3 = 3.333...
print(f"{a} // {b} = {a // b}")  # Floor division: 10 // 3 = 3
print(f"{a} % {b} = {a % b}")    # Modulo: 10 % 3 = 1
print(f"{a} ** {b} = {a ** b}")  # Exponentiation: 10 ** 3 = 1000

# Special cases
print(f"10 / 0 = Error")          # Division by zero raises error
print(f"10 // 0 = Error")         # Floor division by zero raises error
print(f"10 % 0 = Error")          # Modulo by zero raises error
```

#### Comparison Operators

```python
# Comparison operators
a, b = 5, 10

print(f"{a} == {b}: {a == b}")    # Equal: False
print(f"{a} != {b}: {a != b}")    # Not equal: True
print(f"{a} < {b}: {a < b}")      # Less than: True
print(f"{a} > {b}: {a > b}")      # Greater than: False
print(f"{a} <= {b}: {a <= b}")    # Less than or equal: True
print(f"{a} >= {b}: {a >= b}")    # Greater than or equal: False

# String comparison
print("apple" < "banana")          # True (lexicographic order)
print("Apple" < "apple")           # True (uppercase < lowercase)

# Chained comparisons
x = 5
print(0 <= x <= 10)                # True (equivalent to 0 <= x and x <= 10)
```

#### Logical Operators

```python
# Logical operators
a, b = True, False

print(f"{a} and {b}: {a and b}")  # Logical AND: False
print(f"{a} or {b}: {a or b}")    # Logical OR: True
print(f"not {a}: {not a}")        # Logical NOT: False

# Short-circuit evaluation
def expensive_function():
    print("This function is expensive!")
    return True

# Short-circuit: second operand not evaluated if first is False
False and expensive_function()     # Nothing printed
True and expensive_function()      # Function called

# Short-circuit: second operand not evaluated if first is True
True or expensive_function()       # Nothing printed
False or expensive_function()      # Function called
```

#### Assignment Operators

```python
# Assignment operators
x = 10
print(f"Initial value: {x}")

x += 5      # x = x + 5
print(f"After += 5: {x}")         # 15

x -= 3      # x = x - 3
print(f"After -= 3: {x}")         # 12

x *= 2      # x = x * 2
print(f"After *= 2: {x}")         # 24

x /= 4      # x = x / 4
print(f"After /= 4: {x}")         # 6.0

x //= 2     # x = x // 2
print(f"After //= 2: {x}")        # 3.0

x %= 2      # x = x % 2
print(f"After %= 2: {x}")         # 1.0

x **= 3     # x = x ** 3
print(f"After **= 3: {x}")        # 1.0
```

#### Operator Precedence

```python
# Operator precedence (from highest to lowest)
# 1. Parentheses ()
# 2. Exponentiation **
# 3. Unary +, -, ~
# 4. Multiplication *, Division /, Floor //, Modulo %
# 5. Addition +, Subtraction -
# 6. Bitwise shifts <<, >>
# 7. Bitwise AND &
# 8. Bitwise XOR ^
# 9. Bitwise OR |
# 10. Comparison ==, !=, <, <=, >, >=
# 11. Logical NOT not
# 12. Logical AND and
# 13. Logical OR or

# Examples
result1 = 2 + 3 * 4        # 14 (not 20)
result2 = (2 + 3) * 4      # 20
result3 = 2 ** 3 + 1       # 9 (not 16)
result4 = 2 ** (3 + 1)     # 16

# Complex expression
complex_result = 10 + 5 * 2 ** 3 - 15 / 3
# Step by step:
# 1. 2 ** 3 = 8
# 2. 5 * 8 = 40
# 3. 15 / 3 = 5
# 4. 10 + 40 - 5 = 45
print(f"Complex result: {complex_result}")  # 45.0
```

## 💻 Hands-On Practice

### Exercise 1: Variable and Data Type Practice
Create a file called `data_types_practice.py`:

```python
# Data Types Practice Exercise

# 1. Create variables of different types
name = "Your Name"
age = 25
height = 1.75
is_student = True
favorite_numbers = [7, 13, 42]

# 2. Display variable information
print("Variable Information:")
print(f"Name: {name} (Type: {type(name)})")
print(f"Age: {age} (Type: {type(age)})")
print(f"Height: {height} (Type: {type(height)})")
print(f"Is Student: {is_student} (Type: {type(is_student)})")
print(f"Favorite Numbers: {favorite_numbers} (Type: {type(favorite_numbers)})")

# 3. Type conversions
age_string = str(age)
height_integer = int(height)
age_float = float(age)

print(f"\nType Conversions:")
print(f"Age as string: {age_string} (Type: {type(age_string)})")
print(f"Height as integer: {height_integer} (Type: {type(height_integer)})")
print(f"Age as float: {age_float} (Type: {type(age_float)})")

# 4. Basic operations
print(f"\nBasic Operations:")
print(f"Age in 5 years: {age + 5}")
print(f"Height in centimeters: {height * 100}")
print(f"Name length: {len(name)}")
print(f"Name in uppercase: {name.upper()}")
```

### Exercise 2: Calculator Program
Create a simple calculator:

```python
# Simple Calculator

print("Simple Calculator")
print("Operations: +, -, *, /, //, %, **")

# Get input
num1 = float(input("Enter first number: "))
operator = input("Enter operator: ")
num2 = float(input("Enter second number: "))

# Perform calculation
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero!")
        exit()
elif operator == "//":
    if num2 != 0:
        result = num1 // num2
    else:
        print("Error: Division by zero!")
        exit()
elif operator == "%":
    if num2 != 0:
        result = num1 % num2
    else:
        print("Error: Modulo by zero!")
        exit()
elif operator == "**":
    result = num1 ** num2
else:
    print("Error: Invalid operator!")
    exit()

# Display result
print(f"Result: {num1} {operator} {num2} = {result}")
```

### Exercise 3: Type Conversion and Validation
Create a data validation program:

```python
# Data Validation Program

def get_valid_integer(prompt, min_value=None, max_value=None):
    """Get a valid integer from user input."""
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}")
                continue
            if max_value is not None and value > max_value:
                print(f"Value must be at most {max_value}")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer")

def get_valid_float(prompt, min_value=None, max_value=None):
    """Get a valid float from user input."""
    while True:
        try:
            value = float(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}")
                continue
            if max_value is not None and value > max_value:
                print(f"Value must be at most {max_value}")
                continue
            return value
        except ValueError:
            print("Please enter a valid number")

def get_valid_string(prompt, min_length=None, max_length=None):
    """Get a valid string from user input."""
    while True:
        value = input(prompt).strip()
        if min_length is not None and len(value) < min_length:
            print(f"String must be at least {min_length} characters long")
            continue
        if max_length is not None and len(value) > max_length:
            print(f"String must be at most {max_length} characters long")
            continue
        if value:  # Check if not empty
            return value
        else:
            print("String cannot be empty")

# Test the functions
print("Data Validation Test")
print("=" * 30)

age = get_valid_integer("Enter your age: ", 0, 150)
height = get_valid_float("Enter your height (meters): ", 0.5, 3.0)
name = get_valid_string("Enter your name: ", 2, 50)

print(f"\nValidated Data:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}m")
```

## 📝 Module Quiz

### Quiz Questions
1. What is the difference between `=` and `==` in Python?
2. What happens when you divide an integer by zero in Python?
3. What is the result of `"Hello" * 3`?
4. What is the difference between `/` and `//` operators?
5. How do you check the type of a variable in Python?

### Quiz Answers
1. `=` is assignment operator, `==` is comparison operator
2. ZeroDivisionError is raised
3. "HelloHelloHello" (string repetition)
4. `/` performs true division, `//` performs floor division
5. Use the `type()` function

## 🔍 Key Concepts Review

### Variable Best Practices
- Use descriptive names that explain the purpose
- Follow naming conventions (snake_case recommended)
- Initialize variables before using them
- Use meaningful default values

### Data Type Selection
- Use `int` for whole numbers
- Use `float` for decimal numbers
- Use `str` for text data
- Use `bool` for true/false values
- Use appropriate types for your data

### Operator Precedence
- Parentheses have highest precedence
- Exponentiation has higher precedence than multiplication
- Multiplication/division have higher precedence than addition/subtraction
- Use parentheses to make expressions clear

## 🎯 Module Checklist

- [ ] Understand variable creation and naming
- [ ] Master all basic data types
- [ ] Learn type conversion and checking
- [ ] Practice input/output operations
- [ ] Understand all operator types
- [ ] Learn operator precedence
- [ ] Complete hands-on exercises
- [ ] Take module quiz
- [ ] Review key concepts

## 🚀 Next Steps

1. **Complete Exercises**: Work through all hands-on exercises
2. **Practice Daily**: Write small programs using different data types
3. **Experiment**: Try different type conversions and operations
4. **Move to Module 3**: Control Flow and Data Structures

## 💡 Pro Tips

- **Use f-strings** for modern string formatting
- **Validate input** before converting types
- **Understand precedence** to avoid unexpected results
- **Choose appropriate types** for your data
- **Practice type checking** to debug issues
- **Use meaningful variable names** for better code readability

---

**Congratulations on completing Module 2! You now have a solid understanding of Python's data types and operations. In the next module, you'll learn about control flow, loops, and data structures. Keep practicing and happy coding! 🐍✨**
