# Module 4: Functions and Data Structures
## Building Reusable Code and Organizing Data

Welcome to Module 4! This module covers functions and advanced data structures in Python. You'll learn how to create reusable code blocks and work with powerful data structures that make Python programming efficient and elegant.

## 🎯 Module Objectives

By the end of this module, you will be able to:
- Define and call functions with various parameter types
- Understand function scope and variable lifetime
- Work with advanced data structures (lists, dictionaries, tuples, sets)
- Implement list comprehensions and generator expressions
- Use built-in functions and methods effectively
- Create clean, maintainable, and reusable code

## 📋 What You'll Learn

### 1. Function Fundamentals
- Function definition and calling
- Parameters and arguments
- Return values and multiple returns
- Function scope and namespaces

### 2. Advanced Function Features
- Default parameters and keyword arguments
- Variable-length arguments (*args, **kwargs)
- Lambda functions and functional programming
- Decorators and function modification

### 3. Data Structures
- Lists: mutable sequences
- Dictionaries: key-value mappings
- Tuples: immutable sequences
- Sets: unordered unique collections

### 4. Data Structure Operations
- Common methods and operations
- List comprehensions and generator expressions
- Data structure selection guidelines
- Performance considerations

## 🚀 Getting Started

### Prerequisites
- Complete Modules 1-3
- Understanding of control flow and basic syntax
- Familiarity with variables and data types

### Setup
1. Ensure Python 3.8+ is installed
2. Have a text editor or IDE ready
3. Create a practice directory for exercises

## 📚 Core Concepts

### Function Fundamentals

Functions are reusable blocks of code that can accept input and return output:

```python
# Basic function definition
def greet(name):
    """Return a personalized greeting."""
    return f"Hello, {name}!"

# Function call
message = greet("Alice")
print(message)  # Output: Hello, Alice!

# Function with multiple parameters
def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    area = length * width
    return area

# Function with multiple return values
def get_name_and_age():
    """Return name and age as a tuple."""
    return "Bob", 25

# Unpacking multiple return values
name, age = get_name_and_age()
print(f"{name} is {age} years old")
```

### Function Parameters

Python offers flexible parameter handling:

```python
# Default parameters
def greet_user(name="Guest", greeting="Hello"):
    """Greet a user with default values."""
    return f"{greeting}, {name}!"

# Using defaults
print(greet_user())                    # Hello, Guest!
print(greet_user("Alice"))            # Hello, Alice!
print(greet_user("Bob", "Hi"))        # Hi, Bob!

# Keyword arguments
def create_profile(name, age, city, occupation="Student"):
    """Create a user profile."""
    return {
        "name": name,
        "age": age,
        "city": city,
        "occupation": occupation
    }

# Call with keyword arguments (order doesn't matter)
profile = create_profile(
    age=25,
    city="Boston",
    name="Charlie",
    occupation="Developer"
)

# Variable-length arguments
def sum_all(*numbers):
    """Sum all provided numbers."""
    return sum(numbers)

def create_user(**user_data):
    """Create a user with flexible attributes."""
    return user_data

# Using variable-length arguments
total = sum_all(1, 2, 3, 4, 5)  # 15
user = create_user(name="David", age=30, city="Chicago")
```

### Function Scope and Namespaces

Understanding variable scope is crucial for function design:

```python
# Global variable
global_var = "I'm global"

def scope_demo():
    """Demonstrate variable scope."""
    local_var = "I'm local"
    print(f"Inside function: {local_var}")
    print(f"Global variable: {global_var}")
    
    # Modifying global variable
    global global_var
    global_var = "Modified global"
    print(f"Modified global: {global_var}")

def nested_function():
    """Demonstrate nested function scope."""
    outer_var = "Outer variable"
    
    def inner_function():
        inner_var = "Inner variable"
        print(f"Inner: {inner_var}")
        print(f"Outer: {outer_var}")
        # print(f"Global: {global_var}")  # Accessible
    
    inner_function()
    # print(f"Inner var: {inner_var}")  # Not accessible

# Test scope
scope_demo()
nested_function()
```

## 💻 Hands-On Practice

### Exercise 1: Basic Functions

Create utility functions for common operations:

```python
def calculate_statistics(numbers):
    """Calculate basic statistics for a list of numbers."""
    if not numbers:
        return None
    
    stats = {
        "count": len(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "minimum": min(numbers),
        "maximum": max(numbers)
    }
    
    # Calculate median
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        stats["median"] = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        stats["median"] = sorted_numbers[n//2]
    
    return stats

def validate_password(password):
    """Validate password strength."""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    
    if not all([has_upper, has_lower, has_digit, has_special]):
        return False, "Password must contain uppercase, lowercase, digit, and special character"
    
    return True, "Password is strong"

# Test the functions
sample_numbers = [4, 2, 7, 1, 9, 3, 6, 5, 8]
stats = calculate_statistics(sample_numbers)
print("Statistics:", stats)

passwords = ["weak", "Strong123!", "NoSpecial123", "Perfect@123"]
for pwd in passwords:
    is_valid, message = validate_password(pwd)
    print(f"'{pwd}': {message}")
```

### Exercise 2: Advanced Function Features

Explore advanced function capabilities:

```python
def flexible_calculator(operation, *numbers, **options):
    """Perform various mathematical operations with options."""
    if not numbers:
        return None
    
    result = None
    
    if operation == "add":
        result = sum(numbers)
    elif operation == "multiply":
        result = 1
        for num in numbers:
            result *= num
    elif operation == "average":
        result = sum(numbers) / len(numbers)
    elif operation == "power":
        if len(numbers) >= 2:
            result = numbers[0] ** numbers[1]
        else:
            result = numbers[0] ** 2
    else:
        return f"Unknown operation: {operation}"
    
    # Apply options
    if options.get("round", False):
        result = round(result, options.get("decimals", 2))
    
    if options.get("absolute", False):
        result = abs(result)
    
    return result

def memoize(func):
    """Simple memoization decorator."""
    cache = {}
    
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    
    return wrapper

@memoize
def fibonacci(n):
    """Calculate Fibonacci number with memoization."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Test advanced functions
print("Calculator examples:")
print(f"Add: {flexible_calculator('add', 1, 2, 3, 4, 5)}")
print(f"Multiply: {flexible_calculator('multiply', 2, 3, 4)}")
print(f"Average: {flexible_calculator('average', 10, 20, 30, round=True, decimals=1)}")
print(f"Power: {flexible_calculator('power', 2, 8)}")

print("\nFibonacci with memoization:")
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")
```

### Exercise 3: Working with Lists

Master list operations and comprehensions:

```python
def list_operations_demo():
    """Demonstrate various list operations."""
    
    # Creating lists
    numbers = [1, 2, 3, 4, 5]
    fruits = ["apple", "banana", "cherry"]
    mixed = [1, "hello", 3.14, True]
    
    # List methods
    print("Original numbers:", numbers)
    numbers.append(6)
    print("After append:", numbers)
    
    numbers.insert(0, 0)
    print("After insert at 0:", numbers)
    
    numbers.extend([7, 8, 9])
    print("After extend:", numbers)
    
    # List slicing
    print("First 3:", numbers[:3])
    print("Last 3:", numbers[-3:])
    print("Every 2nd:", numbers[::2])
    print("Reverse:", numbers[::-1])
    
    # List comprehensions
    squares = [x**2 for x in range(10)]
    print("Squares:", squares)
    
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    print("Even squares:", even_squares)
    
    # Nested list comprehension
    matrix = [[i+j for j in range(3)] for i in range(0, 9, 3)]
    print("Matrix:")
    for row in matrix:
        print(row)

def advanced_list_processing():
    """Advanced list processing techniques."""
    
    # Filtering and mapping
    numbers = list(range(1, 21))
    
    # Filter even numbers and square them
    even_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
    print("Even squares (functional):", even_squares)
    
    # Same with list comprehension
    even_squares_comp = [x**2 for x in numbers if x % 2 == 0]
    print("Even squares (comprehension):", even_squares_comp)
    
    # Grouping by remainder
    grouped = {}
    for num in numbers:
        remainder = num % 3
        if remainder not in grouped:
            grouped[remainder] = []
        grouped[remainder].append(num)
    
    print("Grouped by remainder when divided by 3:")
    for remainder, nums in grouped.items():
        print(f"Remainder {remainder}: {nums}")

# Test list operations
list_operations_demo()
print("\n" + "="*50)
advanced_list_processing()
```

### Exercise 4: Dictionary Mastery

Explore dictionary operations and use cases:

```python
def dictionary_operations():
    """Demonstrate dictionary operations."""
    
    # Creating dictionaries
    person = {
        "name": "Alice",
        "age": 30,
        "city": "Boston",
        "skills": ["Python", "JavaScript", "SQL"]
    }
    
    # Accessing and modifying
    print("Original person:", person)
    person["age"] = 31
    person["experience"] = 5
    print("Modified person:", person)
    
    # Dictionary methods
    print("Keys:", list(person.keys()))
    print("Values:", list(person.values()))
    print("Items:", list(person.items()))
    
    # Safe access
    print("Phone:", person.get("phone", "Not provided"))
    
    # Nested dictionaries
    company = {
        "name": "TechCorp",
        "employees": {
            "alice": {"role": "Developer", "salary": 80000},
            "bob": {"role": "Manager", "salary": 100000}
        }
    }
    
    print(f"\nCompany: {company['name']}")
    for emp_id, emp_data in company["employees"].items():
        print(f"{emp_id}: {emp_data['role']} - ${emp_data['salary']:,}")

def dictionary_comprehensions():
    """Show dictionary comprehension examples."""
    
    # Square mapping
    squares = {x: x**2 for x in range(1, 6)}
    print("Squares mapping:", squares)
    
    # Filtered dictionary
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_squares = {x: x**2 for x in numbers if x % 2 == 0}
    print("Even squares:", even_squares)
    
    # Word frequency counter
    text = "hello world hello python world python programming"
    words = text.split()
    word_count = {}
    
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    print("Word frequency:", word_count)
    
    # Using Counter from collections
    from collections import Counter
    word_count_counter = Counter(words)
    print("Using Counter:", dict(word_count_counter))

# Test dictionary operations
dictionary_operations()
print("\n" + "="*50)
dictionary_comprehensions()
```

### Exercise 5: Sets and Tuples

Master immutable and unique collections:

```python
def set_operations_demo():
    """Demonstrate set operations."""
    
    # Creating sets
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    print("Set 1:", set1)
    print("Set 2:", set2)
    
    # Set operations
    print("Union:", set1 | set2)
    print("Intersection:", set1 & set2)
    print("Difference (set1 - set2):", set1 - set2)
    print("Symmetric difference:", set1 ^ set2)
    
    # Set methods
    set1.add(6)
    print("After adding 6:", set1)
    
    set1.remove(1)
    print("After removing 1:", set1)
    
    # Set comprehensions
    even_set = {x for x in range(10) if x % 2 == 0}
    print("Even numbers set:", even_set)

def tuple_operations():
    """Demonstrate tuple operations."""
    
    # Creating tuples
    coordinates = (3, 4)
    person = ("Bob", 25, "Engineer")
    
    print("Coordinates:", coordinates)
    print("Person:", person)
    
    # Tuple unpacking
    x, y = coordinates
    name, age, job = person
    
    print(f"X: {x}, Y: {y}")
    print(f"Name: {name}, Age: {age}, Job: {job}")
    
    # Named tuples
    from collections import namedtuple
    
    Point = namedtuple('Point', ['x', 'y'])
    point = Point(5, 10)
    
    print(f"Point: ({point.x}, {point.y})")
    
    # Tuple as dictionary key
    locations = {
        (0, 0): "Origin",
        (1, 1): "Corner",
        (-1, -1): "Opposite corner"
    }
    
    print("Locations:", locations)

def data_structure_selection():
    """Guidelines for choosing data structures."""
    
    print("Data Structure Selection Guidelines:")
    print("=" * 40)
    
    print("\n1. Lists:")
    print("   - Use when you need ordered, mutable sequences")
    print("   - Good for: shopping lists, to-do items, scores")
    
    print("\n2. Dictionaries:")
    print("   - Use when you need key-value mappings")
    print("   - Good for: user profiles, configuration, counting")
    
    print("\n3. Tuples:")
    print("   - Use when you need immutable, ordered sequences")
    print("   - Good for: coordinates, database records, function returns")
    
    print("\n4. Sets:")
    print("   - Use when you need unique, unordered collections")
    print("   - Good for: removing duplicates, membership testing")

# Test sets and tuples
set_operations_demo()
print("\n" + "="*50)
tuple_operations()
print("\n" + "="*50)
data_structure_selection()
```

## 🧪 Module Quiz

Test your understanding with these questions:

### Question 1
What is the output of this code?
```python
def func(a, b=2, c=3):
    return a + b + c

print(func(1, c=5))
```
- A) 6
- B) 8
- C) Error
- D) 9

**Answer: B** - a=1, b=2 (default), c=5, so 1+2+5=8.

### Question 2
Which data structure is best for storing unique values?
- A) List
- B) Dictionary
- C) Set
- D) Tuple

**Answer: C** - Sets automatically handle uniqueness.

### Question 3
What does the `*args` parameter do?
- A) Accepts keyword arguments
- B) Accepts variable number of positional arguments
- C) Accepts only one argument
- D) Accepts no arguments

**Answer: B** - `*args` collects all positional arguments into a tuple.

### Question 4
Which method removes an item from a list and returns it?
- A) `remove()`
- B) `pop()`
- C) `delete()`
- D) `clear()`

**Answer: B** - `pop()` removes and returns the item.

### Question 5
What is a list comprehension?
- A) A way to create lists using loops
- A way to create lists using loops
- B) A way to sort lists
- C) A way to merge lists
- D) A way to copy lists

**Answer: A** - List comprehensions create lists using concise syntax with loops and conditions.

## 🔑 Key Concepts Review

### Function Design Principles
1. **Single Responsibility**: Each function should do one thing well
2. **Clear Naming**: Use descriptive function and parameter names
3. **Documentation**: Always include docstrings for complex functions
4. **Default Values**: Provide sensible defaults for optional parameters
5. **Error Handling**: Validate inputs and handle edge cases

### Data Structure Guidelines
- **Lists**: Ordered, mutable sequences for dynamic collections
- **Dictionaries**: Key-value mappings for structured data
- **Tuples**: Immutable sequences for fixed data
- **Sets**: Unordered unique collections for membership testing

### Performance Considerations
- **List comprehensions** are generally faster than equivalent loops
- **Sets** provide O(1) membership testing vs O(n) for lists
- **Dictionaries** offer O(1) key-based access
- **Generator expressions** save memory for large datasets

## ✅ Module Checklist

Before moving to the next module, ensure you can:

- [ ] Define functions with various parameter types
- [ ] Use default parameters and keyword arguments
- [ ] Implement variable-length arguments (*args, **kwargs)
- [ ] Work with function scope and namespaces
- [ ] Create and manipulate lists, dictionaries, tuples, and sets
- [ ] Use list comprehensions and generator expressions
- [ ] Choose appropriate data structures for different use cases
- [ ] Write clean, maintainable, and reusable functions

## 🚀 Next Steps

After completing this module:

1. **Practice function design** with different scenarios
2. **Build data processing tools** using various data structures
3. **Experiment with advanced features** like decorators and lambdas
4. **Move to Module 5** to learn about Object-Oriented Programming
5. **Review function usage** in your previous code examples

## 💡 Pro Tips

### Function Design
- Keep functions small and focused
- Use type hints for better code documentation
- Return early to reduce nesting
- Use meaningful variable names

### Data Structure Selection
- Choose based on your access patterns
- Consider memory usage for large datasets
- Use built-in methods when available
- Profile performance for critical operations

### Code Organization
- Group related functions together
- Use consistent naming conventions
- Document complex algorithms
- Test edge cases thoroughly

### Performance Tips
- Use sets for membership testing
- Prefer list comprehensions over loops
- Use generators for memory efficiency
- Cache expensive computations

## 🔗 Related Topics

- **Module 3**: Control Flow (for function logic)
- **Module 5**: OOP (for class methods)
- **Module 6**: Modules and Packages (for function organization)
- **Module 8**: File Handling (for data persistence)

---

**Ready to build reusable code?** Start with the exercises above and practice creating functions that solve real problems. Functions and data structures are the building blocks of all Python applications!
