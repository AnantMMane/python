#!/usr/bin/env python3
"""
PCAP Examples: Functions - Comprehensive Guide
This file demonstrates all aspects of Python functions for PCAP certification.
"""

# ===== BASIC FUNCTION DEFINITION =====
print("=== Basic Function Definition ===")

def greet():
    """Simple function with no parameters."""
    print("Hello, World!")

def greet_person(name):
    """Function with one parameter."""
    print(f"Hello, {name}!")

def add_numbers(a, b):
    """Function with return value."""
    return a + b

# Function calls
greet()
greet_person("Alice")
result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# ===== FUNCTION PARAMETERS =====
print("\n=== Function Parameters ===")

def describe_pet(name, animal_type="dog"):
    """Function with default parameter."""
    print(f"I have a {animal_type} named {name}")

# Different ways to call
describe_pet("Max")  # Uses default
describe_pet("Whiskers", "cat")  # Positional arguments
describe_pet(animal_type="bird", name="Tweety")  # Keyword arguments

def calculate_area(length, width, unit="m²"):
    """Function demonstrating parameter types."""
    area = length * width
    return f"{area} {unit}"

print(calculate_area(5, 3))
print(calculate_area(5, 3, "ft²"))

# ===== VARIABLE-LENGTH ARGUMENTS =====
print("\n=== Variable-Length Arguments ===")

def sum_all(*args):
    """Function accepting variable number of arguments."""
    print(f"Arguments received: {args}")
    return sum(args)

print(f"sum_all(1, 2, 3): {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5): {sum_all(1, 2, 3, 4, 5)}")

def print_info(**kwargs):
    """Function accepting keyword arguments."""
    print("Information received:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print_info(name="Bob", age=30, city="New York", job="Engineer")

def complex_function(required, default="default", *args, **kwargs):
    """Function combining all parameter types."""
    print(f"Required: {required}")
    print(f"Default: {default}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

complex_function("must_have", "custom", 1, 2, 3, x=10, y=20)

# ===== FUNCTION SCOPE =====
print("\n=== Function Scope ===")

# Global variable
global_var = "I'm global"

def scope_demo():
    """Demonstrate variable scope."""
    local_var = "I'm local"
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")

scope_demo()
print(f"Outside function - Global: {global_var}")
# print(local_var)  # This would cause NameError

# Modifying global variables
counter = 0

def increment_counter():
    """Modify global variable."""
    global counter
    counter += 1
    print(f"Counter incremented to: {counter}")

increment_counter()
increment_counter()
print(f"Final counter value: {counter}")

# nonlocal keyword
def outer_function():
    """Demonstrate nonlocal keyword."""
    x = 10
    
    def inner_function():
        nonlocal x
        x += 5
        print(f"Inner function - x: {x}")
    
    print(f"Before inner function - x: {x}")
    inner_function()
    print(f"After inner function - x: {x}")

outer_function()

# ===== LAMBDA FUNCTIONS =====
print("\n=== Lambda Functions ===")

# Basic lambda
square = lambda x: x ** 2
print(f"square(5): {square(5)}")

# Lambda with multiple arguments
multiply = lambda x, y: x * y
print(f"multiply(4, 6): {multiply(4, 6)}")

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map() with lambda
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Squared numbers: {squared_numbers}")

# filter() with lambda
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# sorted() with lambda
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("Diana", 96)]
sorted_by_grade = sorted(students, key=lambda student: student[1])
print(f"Students sorted by grade: {sorted_by_grade}")

sorted_by_name = sorted(students, key=lambda student: student[0])
print(f"Students sorted by name: {sorted_by_name}")

# ===== FUNCTION ANNOTATIONS =====
print("\n=== Function Annotations ===")

def calculate_bmi(weight: float, height: float) -> float:
    """Calculate BMI with type annotations."""
    return weight / (height ** 2)

def greet_user(name: str, age: int = 25) -> str:
    """Greet user with type annotations."""
    return f"Hello {name}, you are {age} years old!"

bmi = calculate_bmi(70.0, 1.75)
print(f"BMI: {bmi:.2f}")

greeting = greet_user("Alice", 30)
print(greeting)

# ===== NESTED FUNCTIONS AND CLOSURES =====
print("\n=== Nested Functions and Closures ===")

def outer(x):
    """Demonstrate nested functions and closures."""
    def inner(y):
        return x + y  # x is captured from outer scope
    return inner

add_five = outer(5)
print(f"add_five(10): {add_five(10)}")

def make_multiplier(n):
    """Factory function creating multiplier functions."""
    def multiplier(x):
        return x * n
    return multiplier

times_2 = make_multiplier(2)
times_3 = make_multiplier(3)

print(f"times_2(7): {times_2(7)}")
print(f"times_3(7): {times_3(7)}")

# ===== DECORATORS (BASIC) =====
print("\n=== Basic Decorators ===")

def timing_decorator(func):
    """Simple decorator to demonstrate concept."""
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} completed")
        return result
    return wrapper

@timing_decorator
def say_hello(name):
    """Function with decorator."""
    return f"Hello, {name}!"

message = say_hello("World")
print(message)

# ===== RECURSIVE FUNCTIONS =====
print("\n=== Recursive Functions ===")

def factorial(n):
    """Calculate factorial recursively."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"factorial(5): {factorial(5)}")
print(f"factorial(0): {factorial(0)}")

def fibonacci(n):
    """Calculate Fibonacci number recursively."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci sequence (first 10 numbers):")
for i in range(10):
    print(f"fib({i}): {fibonacci(i)}")

# ===== PRACTICAL EXAMPLES =====
print("\n=== Practical Examples ===")

def validate_email(email):
    """Simple email validation."""
    if "@" not in email:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    username, domain = parts
    return len(username) > 0 and "." in domain

emails = ["user@example.com", "invalid.email", "test@domain.org", "@missing.com"]
for email in emails:
    is_valid = validate_email(email)
    print(f"{email}: {'Valid' if is_valid else 'Invalid'}")

def calculate_grade_statistics(grades):
    """Calculate statistics for a list of grades."""
    if not grades:
        return {"error": "No grades provided"}
    
    return {
        "count": len(grades),
        "average": sum(grades) / len(grades),
        "min": min(grades),
        "max": max(grades),
        "passed": len([g for g in grades if g >= 60])
    }

student_grades = [85, 92, 78, 96, 88, 73, 89, 94]
stats = calculate_grade_statistics(student_grades)
print(f"\nGrade Statistics:")
for key, value in stats.items():
    if key == "average":
        print(f"  {key}: {value:.2f}")
    else:
        print(f"  {key}: {value}")

def create_calculator():
    """Factory function returning calculator functions."""
    def add(x, y):
        return x + y
    
    def subtract(x, y):
        return x - y
    
    def multiply(x, y):
        return x * y
    
    def divide(x, y):
        if y == 0:
            return "Error: Division by zero"
        return x / y
    
    return {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }

calc = create_calculator()
print(f"\nCalculator operations:")
print(f"10 + 5 = {calc['add'](10, 5)}")
print(f"10 - 5 = {calc['subtract'](10, 5)}")
print(f"10 * 5 = {calc['multiply'](10, 5)}")
print(f"10 / 5 = {calc['divide'](10, 5)}")
print(f"10 / 0 = {calc['divide'](10, 0)}")

# ===== FUNCTION INTROSPECTION =====
print("\n=== Function Introspection ===")

def sample_function(a, b=10, *args, **kwargs):
    """Sample function for introspection."""
    pass

print(f"Function name: {sample_function.__name__}")
print(f"Function docstring: {sample_function.__doc__}")
print(f"Function defaults: {sample_function.__defaults__}")

# Function as first-class objects
functions = [len, max, min, sum]
data = [1, 5, 3, 9, 2]

print(f"\nApplying functions to {data}:")
for func in functions:
    try:
        result = func(data)
        print(f"{func.__name__}({data}): {result}")
    except TypeError:
        print(f"{func.__name__}: Not applicable to this data")

if __name__ == "__main__":
    print("\n=== Function examples completed! ===")
