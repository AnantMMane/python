#!/usr/bin/env python3
"""
PCAP Examples: Variables and Data Types
This file demonstrates basic Python data types and variable operations.
"""

# ===== VARIABLES AND NAMING =====
print("=== Variables and Naming ===")

# Valid variable names
name = "Alice"
age = 25
_private = "hidden"
number1 = 10
CONSTANT = 100
snake_case = "preferred style"

print(f"Name: {name}, Age: {age}")
print(f"Constant: {CONSTANT}")

# ===== NUMERIC TYPES =====
print("\n=== Numeric Types ===")

# Integers
decimal = 42
binary = 0b1010  # 10 in decimal
octal = 0o12     # 10 in decimal
hexadecimal = 0xA  # 10 in decimal

print(f"Decimal: {decimal}")
print(f"Binary 0b1010 = {binary}")
print(f"Octal 0o12 = {octal}")
print(f"Hex 0xA = {hexadecimal}")

# Floating-point numbers
pi = 3.14159
scientific = 1.23e-4  # 0.000123
large_num = 6.02e23   # Avogadro's number

print(f"Pi: {pi}")
print(f"Scientific notation 1.23e-4 = {scientific}")
print(f"Large number 6.02e23 = {large_num}")

# Complex numbers
z1 = 3 + 4j
z2 = complex(5, 12)

print(f"Complex z1: {z1}")
print(f"Complex z2: {z2}")
print(f"z1 real part: {z1.real}")
print(f"z1 imaginary part: {z1.imag}")
print(f"z1 magnitude: {abs(z1)}")

# ===== STRING TYPES =====
print("\n=== String Types ===")

# Different string literals
single_quotes = 'Hello'
double_quotes = "World"
multiline = """This is a
multiline string
with line breaks"""

# Raw strings (escape sequences not processed)
raw_string = r"C:\Users\Name\Documents"
normal_string = "C:\\Users\\Name\\Documents"

print(f"Single quotes: {single_quotes}")
print(f"Double quotes: {double_quotes}")
print(f"Raw string: {raw_string}")
print(f"Normal string: {normal_string}")

# String escape sequences
escaped = "Line 1\nLine 2\tTabbed text\nQuote: \"Hello\""
print(f"Escaped string:\n{escaped}")

# ===== BOOLEAN TYPE =====
print("\n=== Boolean Type ===")

# Boolean values
is_active = True
is_complete = False

# Boolean conversion
print(f"bool(1): {bool(1)}")
print(f"bool(0): {bool(0)}")
print(f"bool('text'): {bool('text')}")
print(f"bool(''): {bool('')}")
print(f"bool([1,2,3]): {bool([1,2,3])}")
print(f"bool([]): {bool([])}")

# ===== TYPE CHECKING AND CONVERSION =====
print("\n=== Type Checking and Conversion ===")

x = 42
print(f"x = {x}")
print(f"type(x): {type(x)}")
print(f"isinstance(x, int): {isinstance(x, int)}")
print(f"isinstance(x, (int, float)): {isinstance(x, (int, float))}")

# Type conversion examples
print(f"int('123'): {int('123')}")
print(f"int(3.14): {int(3.14)}")
print(f"float('3.14'): {float('3.14')}")
print(f"str(123): {str(123)}")
print(f"bool('hello'): {bool('hello')}")

# ===== ARITHMETIC OPERATORS =====
print("\n=== Arithmetic Operators ===")

a, b = 10, 3
print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}")  # Addition
print(f"a - b = {a - b}")  # Subtraction
print(f"a * b = {a * b}")  # Multiplication
print(f"a / b = {a / b}")  # Division (float)
print(f"a // b = {a // b}")  # Floor division
print(f"a % b = {a % b}")  # Modulus
print(f"a ** b = {a ** b}")  # Exponentiation

# ===== ASSIGNMENT OPERATORS =====
print("\n=== Assignment Operators ===")

x = 10
print(f"Initial x: {x}")

x += 5
print(f"After x += 5: {x}")

x *= 2
print(f"After x *= 2: {x}")

x //= 3
print(f"After x //= 3: {x}")

# Multiple assignment
a, b, c = 1, 2, 3
print(f"Multiple assignment: a={a}, b={b}, c={c}")

# Chained assignment
x = y = z = 0
print(f"Chained assignment: x={x}, y={y}, z={z}")

# ===== COMPARISON OPERATORS =====
print("\n=== Comparison Operators ===")

x, y = 10, 5
print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x > y: {x > y}")
print(f"x < y: {x < y}")
print(f"x >= y: {x >= y}")
print(f"x <= y: {x <= y}")

# Chained comparisons
z = 7
print(f"z = {z}")
print(f"y < z < x: {y < z < x}")  # True because 5 < 7 < 10

if __name__ == "__main__":
    print("\n=== Script completed successfully! ===")
