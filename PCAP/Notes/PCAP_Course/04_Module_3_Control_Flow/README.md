# Module 3: Control Flow
## Mastering Program Logic and Flow Control

Welcome to Module 3! This module covers control flow in Python, including conditional statements, loops, and program flow control. You'll learn how to make decisions in your code and repeat operations efficiently.

## 🎯 Module Objectives

By the end of this module, you will be able to:
- Understand and implement conditional statements
- Use different types of loops effectively
- Control program flow with break, continue, and pass
- Implement nested control structures
- Write efficient and readable control flow code
- Debug and troubleshoot control flow issues

## 📋 What You'll Learn

### 1. Conditional Statements
- if, elif, and else statements
- Comparison operators
- Logical operators
- Conditional expressions (ternary operators)

### 2. Loops
- for loops and iteration
- while loops and condition-based repetition
- Loop control statements
- Nested loops

### 3. Program Flow Control
- break and continue statements
- pass statement
- Exception handling basics
- Program structure and readability

## 🚀 Getting Started

### Prerequisites
- Complete Modules 1-2
- Understanding of data types and variables
- Basic Python syntax knowledge

### Setup
1. Ensure Python 3.8+ is installed
2. Have a text editor or IDE ready
3. Create a practice directory for exercises

## 📚 Core Concepts

### Conditional Statements

Conditionals allow your program to make decisions based on conditions:

```python
# Basic if statement
age = 18
if age >= 18:
    print("You are an adult")

# if-else statement
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote yet")

# if-elif-else chain
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"Your grade is: {grade}")
```

### Comparison Operators

Python provides several comparison operators:

```python
# Equality operators
x == y    # Equal to
x != y    # Not equal to

# Relational operators
x < y     # Less than
x <= y    # Less than or equal to
x > y     # Greater than
x >= y    # Greater than or equal to

# Identity operators
x is y    # Same object
x is not y # Different objects

# Membership operators
x in y    # x is a member of y
x not in y # x is not a member of y
```

### Logical Operators

Combine conditions with logical operators:

```python
# AND operator (both conditions must be True)
age = 25
income = 50000
if age >= 18 and income >= 30000:
    print("Eligible for loan")

# OR operator (at least one condition must be True)
is_student = True
is_employed = False
if is_student or is_employed:
    print("Eligible for discount")

# NOT operator (inverts the condition)
is_weekend = False
if not is_weekend:
    print("Time to work!")

# Combining multiple conditions
temperature = 75
humidity = 60
if temperature > 70 and humidity < 80 and not is_weekend:
    print("Perfect day for outdoor activities")
```

### Conditional Expressions (Ternary Operators)

Python's concise conditional expressions:

```python
# Traditional if-else
age = 20
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Ternary operator (more concise)
status = "adult" if age >= 18 else "minor"

# Multiple conditions
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
```

## 💻 Hands-On Practice

### Exercise 1: Basic Conditionals

Create a simple grading system:

```python
def calculate_grade(score):
    """Calculate letter grade based on numerical score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def check_eligibility(age, income, credit_score):
    """Check loan eligibility based on multiple criteria."""
    if age >= 18 and income >= 30000 and credit_score >= 650:
        return "Eligible"
    elif age >= 18 and income >= 50000:
        return "Eligible with co-signer"
    else:
        return "Not eligible"

# Test the functions
print(calculate_grade(85))  # Output: B
print(check_eligibility(25, 45000, 700))  # Output: Eligible
```

### Exercise 2: For Loops

Master iteration with for loops:

```python
# Iterating over a range
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"Number: {i}")

# Iterating over a list
fruits = ["apple", "banana", "cherry", "date"]
print("\nFruits in the basket:")
for fruit in fruits:
    print(f"- {fruit}")

# Iterating with enumerate (get index and value)
print("\nFruits with position:")
for index, fruit in enumerate(fruits, 1):
    print(f"{index}. {fruit}")

# Iterating over a dictionary
person = {"name": "Alice", "age": 30, "city": "Boston"}
print("\nPerson details:")
for key, value in person.items():
    print(f"{key}: {value}")

# List comprehension with conditions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"\nSquares of even numbers: {even_squares}")
```

### Exercise 3: While Loops

Use while loops for condition-based repetition:

```python
def countdown(n):
    """Countdown from n to 1."""
    while n > 0:
        print(f"Countdown: {n}")
        n -= 1
    print("Blast off!")

def find_factorial(n):
    """Calculate factorial using while loop."""
    if n < 0:
        return "Factorial not defined for negative numbers"
    
    result = 1
    i = n
    while i > 1:
        result *= i
        i -= 1
    
    return result

def password_checker():
    """Simple password checker with retry limit."""
    correct_password = "secret123"
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        password = input("Enter password: ")
        if password == correct_password:
            print("Access granted!")
            return True
        else:
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Wrong password. {remaining} attempts remaining.")
            else:
                print("Access denied. Too many failed attempts.")
    
    return False

# Test the functions
countdown(5)
print(f"Factorial of 5: {find_factorial(5)}")
# password_checker()  # Uncomment to test interactively
```

### Exercise 4: Nested Control Structures

Combine conditionals and loops:

```python
def analyze_numbers(numbers):
    """Analyze a list of numbers with nested control structures."""
    if not numbers:
        print("No numbers to analyze")
        return
    
    positive_count = 0
    negative_count = 0
    zero_count = 0
    even_sum = 0
    odd_sum = 0
    
    for num in numbers:
        # Count positive, negative, and zero
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1
        
        # Sum even and odd numbers
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    
    # Print analysis
    print("Number Analysis:")
    print(f"Positive numbers: {positive_count}")
    print(f"Negative numbers: {negative_count}")
    print(f"Zeros: {zero_count}")
    print(f"Sum of even numbers: {even_sum}")
    print(f"Sum of odd numbers: {odd_sum}")

def multiplication_table(n):
    """Print multiplication table with nested loops."""
    if n <= 0:
        print("Please enter a positive number")
        return
    
    print(f"Multiplication table for {n}:")
    print("-" * 20)
    
    for i in range(1, 11):
        result = n * i
        print(f"{n} x {i:2d} = {result:3d}")

# Test the functions
sample_numbers = [1, -2, 3, -4, 0, 6, -7, 8, 0, -10]
analyze_numbers(sample_numbers)
print()
multiplication_table(7)
```

### Exercise 5: Loop Control Statements

Master break, continue, and pass:

```python
def find_first_even(numbers):
    """Find the first even number in a list."""
    for num in numbers:
        if num % 2 == 0:
            print(f"First even number found: {num}")
            break
    else:
        print("No even numbers found")

def skip_negative_numbers(numbers):
    """Sum positive numbers, skipping negative ones."""
    total = 0
    for num in numbers:
        if num < 0:
            continue  # Skip negative numbers
        total += num
        print(f"Added {num}, total: {total}")
    return total

def process_data(data):
    """Process data with different actions based on type."""
    for item in data:
        if isinstance(item, str):
            # Process strings
            if item.startswith('#'):
                continue  # Skip comments
            print(f"Processing string: {item}")
        elif isinstance(item, int):
            # Process integers
            if item == 0:
                pass  # Do nothing for zero
            else:
                print(f"Processing integer: {item}")
        else:
            # Handle other types
            print(f"Unknown type: {type(item).__name__}")

# Test the functions
print("Finding first even number:")
find_first_even([1, 3, 5, 7, 8, 9, 10])

print("\nSumming positive numbers:")
total = skip_negative_numbers([1, -2, 3, -4, 5])
print(f"Final total: {total}")

print("\nProcessing mixed data:")
mixed_data = ["hello", "#comment", 42, 0, "world", 3.14]
process_data(mixed_data)
```

## 🧪 Module Quiz

Test your understanding with these questions:

### Question 1
What is the output of this code?
```python
x = 5
if x > 3:
    print("A")
elif x > 2:
    print("B")
else:
    print("C")
```
- A) A
- B) B
- C) C
- D) A and B

**Answer: A** - Only the first true condition executes.

### Question 2
Which loop is best for iterating over a list when you need the index?
- A) `for item in list:`
- B) `for i in range(len(list)):`
- C) `for index, item in enumerate(list):`
- D) `while i < len(list):`

**Answer: C** - `enumerate()` provides both index and value efficiently.

### Question 3
What does the `break` statement do in a loop?
- A) Skips the current iteration
- B) Exits the loop completely
- C) Continues to the next iteration
- D) Pauses the loop

**Answer: B** - `break` exits the loop immediately.

### Question 4
What is the purpose of the `pass` statement?
- A) To exit a function
- B) To skip an iteration
- C) To do nothing (placeholder)
- D) To raise an exception

**Answer: C** - `pass` is a placeholder that does nothing.

### Question 5
Which operator has the highest precedence?
- A) `and`
- B) `or`
- C) `not`
- D) `==`

**Answer: C** - `not` has the highest precedence among logical operators.

## 🔑 Key Concepts Review

### Control Flow Best Practices
1. **Use clear, descriptive conditions** for readability
2. **Avoid deeply nested structures** (use functions to break complexity)
3. **Choose appropriate loop types** for your use case
4. **Use break and continue sparingly** to maintain code clarity
5. **Always handle edge cases** in your conditions

### Loop Selection Guidelines
- **for loops**: When you know the number of iterations or iterating over collections
- **while loops**: When you don't know the number of iterations in advance
- **List comprehensions**: For simple transformations and filtering
- **Nested loops**: Use when necessary, but consider if there's a better approach

### Performance Considerations
- **Avoid unnecessary computations** in loop conditions
- **Use appropriate data structures** for efficient iteration
- **Consider using generators** for large datasets
- **Profile your code** if performance is critical

## ✅ Module Checklist

Before moving to the next module, ensure you can:

- [ ] Write conditional statements with if, elif, and else
- [ ] Use comparison and logical operators correctly
- [ ] Implement for loops for iteration
- [ ] Use while loops for condition-based repetition
- [ ] Apply break, continue, and pass statements
- [ ] Create nested control structures
- [ ] Write readable and efficient control flow code
- [ ] Debug control flow issues

## 🚀 Next Steps

After completing this module:

1. **Practice control flow** with different scenarios
2. **Build simple programs** using conditionals and loops
3. **Experiment with nested structures** to understand complexity
4. **Move to Module 4** to learn about functions and data structures
5. **Review control flow** in your previous code examples

## 💡 Pro Tips

### Code Readability
- Use meaningful variable names in conditions
- Keep conditions simple and readable
- Use parentheses to clarify operator precedence
- Break complex conditions into multiple lines

### Debugging Control Flow
- Use print statements to trace execution
- Check your loop conditions carefully
- Verify that your break/continue logic is correct
- Test edge cases in your conditions

### Performance Optimization
- Move invariant calculations outside loops
- Use appropriate loop constructs for your use case
- Consider using built-in functions when possible
- Profile your code to identify bottlenecks

### Common Pitfalls
- Infinite loops with while statements
- Off-by-one errors in range() functions
- Forgetting to update loop variables
- Incorrect operator precedence in conditions

## 🔗 Related Topics

- **Module 2**: Data Types (for condition evaluation)
- **Module 4**: Functions and Data Structures (for organizing control flow)
- **Module 5**: OOP (for method control flow)
- **Module 8**: File Handling (for file processing loops)

---

**Ready to control your program flow?** Start with the exercises above and practice building programs that make decisions and repeat operations. Control flow is the foundation of all programming logic!
