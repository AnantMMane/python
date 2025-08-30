#!/usr/bin/env python3
"""
PCAP Examples: Control Flow - Conditionals and Loops
This file demonstrates if statements, loops, and control flow structures.
"""

# ===== BASIC IF STATEMENTS =====
print("=== Basic If Statements ===")

age = 18
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# if-elif-else chain
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

print(f"Score: {score}, Grade: {grade}")

# ===== CONDITIONAL EXPRESSIONS (TERNARY) =====
print("\n=== Conditional Expressions ===")

temperature = 25
weather = "warm" if temperature > 20 else "cold"
print(f"Temperature: {temperature}°C, Weather: {weather}")

# Nested conditional expressions
x = 10
result = "positive" if x > 0 else "zero" if x == 0 else "negative"
print(f"x = {x}, result: {result}")

# ===== WHILE LOOPS =====
print("\n=== While Loops ===")

# Basic while loop
print("Counting to 5:")
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

# While loop with else
print("\nWhile loop with else:")
i = 0
while i < 3:
    print(f"i = {i}")
    i += 1
else:
    print("While loop completed normally")

# Infinite loop with break
print("\nInfinite loop with break:")
counter = 0
while True:
    print(f"Counter: {counter}")
    counter += 1
    if counter >= 3:
        break
print("Broke out of infinite loop")

# ===== FOR LOOPS =====
print("\n=== For Loops ===")

# Iterating over a list
fruits = ["apple", "banana", "cherry"]
print("Fruits:")
for fruit in fruits:
    print(f"- {fruit}")

# Using range()
print("\nUsing range():")
for i in range(5):
    print(f"i = {i}")

print("\nRange with start and stop:")
for i in range(2, 8):
    print(f"i = {i}")

print("\nRange with step:")
for i in range(0, 10, 2):
    print(f"i = {i}")

# For loop with else
print("\nFor loop with else:")
for i in range(3):
    print(f"Loop iteration: {i}")
else:
    print("For loop completed normally")

# ===== ENUMERATE AND ZIP =====
print("\n=== Enumerate and Zip ===")

# Enumerate for index and value
colors = ["red", "green", "blue"]
print("Using enumerate:")
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")

print("\nUsing enumerate with start:")
for index, color in enumerate(colors, start=1):
    print(f"Color {index}: {color}")

# Zip for multiple sequences
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Tokyo"]

print("\nUsing zip:")
for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")

# ===== LOOP CONTROL STATEMENTS =====
print("\n=== Loop Control Statements ===")

# break statement
print("Using break:")
for i in range(10):
    if i == 5:
        print(f"Breaking at i = {i}")
        break
    print(f"i = {i}")

# continue statement
print("\nUsing continue:")
for i in range(8):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {i}")

# pass statement
print("\nUsing pass:")
for i in range(3):
    if i == 1:
        pass  # Placeholder - do nothing
    print(f"Processing i = {i}")

# ===== NESTED LOOPS =====
print("\n=== Nested Loops ===")

# Multiplication table
print("Multiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        product = i * j
        print(f"{i} x {j} = {product}", end="  ")
    print()  # New line after each row

# ===== LOGICAL OPERATORS =====
print("\n=== Logical Operators ===")

# and, or, not
a, b = True, False
print(f"a = {a}, b = {b}")
print(f"a and b: {a and b}")
print(f"a or b: {a or b}")
print(f"not a: {not a}")
print(f"not b: {not b}")

# Short-circuit evaluation
x = 5
y = 0
print(f"\nShort-circuit evaluation:")
print(f"x = {x}, y = {y}")

# This won't cause division by zero because first condition is False
result = y != 0 and x / y > 2
print(f"y != 0 and x / y > 2: {result}")

# ===== TRUTHINESS AND BOOLEAN CONTEXT =====
print("\n=== Truthiness in Boolean Context ===")

values = [0, 1, "", "hello", [], [1, 2], None, False, True]

for value in values:
    if value:
        print(f"{repr(value)} is truthy")
    else:
        print(f"{repr(value)} is falsy")

# ===== PRACTICAL EXAMPLES =====
print("\n=== Practical Examples ===")

# Find all even numbers in a range
print("Even numbers from 1 to 20:")
even_numbers = []
for num in range(1, 21):
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)

# Count vowels in a string
text = "Hello World"
vowels = "aeiouAEIOU"
vowel_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1

print(f"\nVowels in '{text}': {vowel_count}")

# Simple number guessing game simulation
import random
target = random.randint(1, 10)
guess = 5  # Simulated guess

print(f"\nNumber guessing game (target: {target}, guess: {guess}):")
if guess == target:
    print("Correct!")
elif guess < target:
    print("Too low!")
else:
    print("Too high!")

# Menu system example
print("\n=== Menu System Example ===")
menu_choice = 2  # Simulated user choice

if menu_choice == 1:
    print("You selected: View Profile")
elif menu_choice == 2:
    print("You selected: Settings")
elif menu_choice == 3:
    print("You selected: Logout")
else:
    print("Invalid choice")

if __name__ == "__main__":
    print("\n=== Control flow examples completed! ===")
