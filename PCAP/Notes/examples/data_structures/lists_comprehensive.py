#!/usr/bin/env python3
"""
PCAP Examples: Lists - Comprehensive Guide
This file demonstrates all aspects of Python lists for PCAP certification.
"""

# ===== CREATING LISTS =====
print("=== Creating Lists ===")

# Empty lists
empty_list1 = []
empty_list2 = list()

# Lists with initial values
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, [1, 2]]
nested = [[1, 2], [3, 4], [5, 6]]

print(f"Numbers: {numbers}")
print(f"Mixed types: {mixed}")
print(f"Nested lists: {nested}")

# List from range
range_list = list(range(5))
range_list2 = list(range(2, 10, 2))
print(f"From range(5): {range_list}")
print(f"From range(2, 10, 2): {range_list2}")

# List comprehensions
squares = [x**2 for x in range(5)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Squares: {squares}")
print(f"Even squares: {even_squares}")

# ===== ACCESSING LIST ELEMENTS =====
print("\n=== Accessing List Elements ===")

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"Fruits: {fruits}")

# Positive indexing
print(f"First fruit (index 0): {fruits[0]}")
print(f"Third fruit (index 2): {fruits[2]}")

# Negative indexing
print(f"Last fruit (index -1): {fruits[-1]}")
print(f"Second to last (index -2): {fruits[-2]}")

# ===== SLICING =====
print("\n=== List Slicing ===")

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original: {numbers}")

# Basic slicing
print(f"numbers[2:6]: {numbers[2:6]}")
print(f"numbers[:4]: {numbers[:4]}")
print(f"numbers[5:]: {numbers[5:]}")
print(f"numbers[:]: {numbers[:]}")  # Copy entire list

# Step slicing
print(f"numbers[::2]: {numbers[::2]}")  # Every 2nd element
print(f"numbers[1::2]: {numbers[1::2]}")  # Every 2nd starting from index 1
print(f"numbers[::-1]: {numbers[::-1]}")  # Reverse

# Negative indices in slicing
print(f"numbers[-3:]: {numbers[-3:]}")  # Last 3 elements
print(f"numbers[:-2]: {numbers[:-2]}")  # All except last 2

# ===== MODIFYING LISTS =====
print("\n=== Modifying Lists ===")

numbers = [1, 2, 3, 4, 5]
print(f"Original: {numbers}")

# Changing single elements
numbers[0] = 10
numbers[-1] = 50
print(f"After changing first and last: {numbers}")

# Changing slices
numbers[1:3] = [20, 30]
print(f"After changing slice [1:3]: {numbers}")

# Replacing with different number of elements
numbers[1:3] = [21, 22, 23, 24]
print(f"After replacing 2 elements with 4: {numbers}")

# ===== ADDING ELEMENTS =====
print("\n=== Adding Elements ===")

fruits = ["apple", "banana"]
print(f"Starting list: {fruits}")

# append() - add single element to end
fruits.append("cherry")
print(f"After append('cherry'): {fruits}")

# insert() - add element at specific position
fruits.insert(1, "apricot")
print(f"After insert(1, 'apricot'): {fruits}")

# extend() - add multiple elements
fruits.extend(["date", "elderberry"])
print(f"After extend(['date', 'elderberry']): {fruits}")

# Using + operator
more_fruits = fruits + ["fig", "grape"]
print(f"Using + operator: {more_fruits}")

# Using += operator
fruits += ["honeydew"]
print(f"After += ['honeydew']: {fruits}")

# ===== REMOVING ELEMENTS =====
print("\n=== Removing Elements ===")

numbers = [1, 2, 3, 2, 4, 5, 2]
print(f"Starting list: {numbers}")

# remove() - remove first occurrence
numbers.remove(2)
print(f"After remove(2): {numbers}")

# pop() - remove and return last element
last = numbers.pop()
print(f"Popped element: {last}, List now: {numbers}")

# pop(index) - remove and return element at index
second = numbers.pop(1)
print(f"Popped element at index 1: {second}, List now: {numbers}")

# del statement - delete by index or slice
del numbers[0]
print(f"After del numbers[0]: {numbers}")

# clear() - remove all elements
copy_numbers = numbers.copy()
copy_numbers.clear()
print(f"After clear(): {copy_numbers}")

# ===== LIST METHODS =====
print("\n=== List Methods ===")

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(f"Original: {numbers}")

# count() - count occurrences
print(f"Count of 1: {numbers.count(1)}")
print(f"Count of 5: {numbers.count(5)}")

# index() - find first occurrence
print(f"Index of 4: {numbers.index(4)}")
print(f"Index of 5: {numbers.index(5)}")

# Sorting
numbers_copy = numbers.copy()
numbers_copy.sort()
print(f"After sort(): {numbers_copy}")

numbers_copy.sort(reverse=True)
print(f"After sort(reverse=True): {numbers_copy}")

# sorted() - returns new sorted list
sorted_asc = sorted(numbers)
sorted_desc = sorted(numbers, reverse=True)
print(f"Original unchanged: {numbers}")
print(f"sorted() ascending: {sorted_asc}")
print(f"sorted() descending: {sorted_desc}")

# reverse() - reverse in place
numbers_copy = numbers.copy()
numbers_copy.reverse()
print(f"After reverse(): {numbers_copy}")

# ===== LIST OPERATIONS =====
print("\n=== List Operations ===")

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
combined = list1 + list2
print(f"list1 + list2: {combined}")

# Repetition
repeated = list1 * 3
print(f"list1 * 3: {repeated}")

# Membership testing
print(f"2 in list1: {2 in list1}")
print(f"7 in list1: {7 in list1}")
print(f"7 not in list1: {7 not in list1}")

# Length
print(f"len(list1): {len(list1)}")

# Min, max, sum (for numeric lists)
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Numbers: {numbers}")
print(f"min(numbers): {min(numbers)}")
print(f"max(numbers): {max(numbers)}")
print(f"sum(numbers): {sum(numbers)}")

# ===== COPYING LISTS =====
print("\n=== Copying Lists ===")

original = [1, 2, [3, 4]]
print(f"Original: {original}")

# Shallow copies (references to nested objects are shared)
copy1 = original.copy()
copy2 = original[:]
copy3 = list(original)

# Modify the nested list
original[2][0] = 99
print(f"After modifying original[2][0] = 99:")
print(f"Original: {original}")
print(f"Copy1: {copy1}")
print(f"Copy2: {copy2}")
print(f"Copy3: {copy3}")

# Deep copy (for completely independent copy)
import copy
deep_copy = copy.deepcopy(original)
original[2][1] = 88
print(f"After modifying original[2][1] = 88:")
print(f"Original: {original}")
print(f"Deep copy: {deep_copy}")

# ===== LIST COMPREHENSIONS =====
print("\n=== List Comprehensions ===")

# Basic comprehension
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# Comprehension with condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Comprehension with if-else
pos_neg = [x if x > 0 else -x for x in [-2, -1, 0, 1, 2]]
print(f"Absolute values: {pos_neg}")

# Nested comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
print(f"Multiplication matrix: {matrix}")

# String processing with comprehension
words = ["hello", "world", "python"]
uppercase = [word.upper() for word in words]
print(f"Uppercase words: {uppercase}")

# ===== PRACTICAL EXAMPLES =====
print("\n=== Practical Examples ===")

# Example 1: Filter and transform data
temperatures_f = [32, 68, 86, 104, 122]
temperatures_c = [(f - 32) * 5/9 for f in temperatures_f]
print(f"Fahrenheit: {temperatures_f}")
print(f"Celsius: {[round(c, 1) for c in temperatures_c]}")

# Example 2: Find duplicates
numbers = [1, 2, 3, 2, 4, 5, 1, 6]
seen = []
duplicates = []
for num in numbers:
    if num in seen and num not in duplicates:
        duplicates.append(num)
    else:
        seen.append(num)
print(f"Numbers: {numbers}")
print(f"Duplicates: {duplicates}")

# Example 3: Matrix operations
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Matrix: {matrix}")

# Get diagonal elements
diagonal = [matrix[i][i] for i in range(len(matrix))]
print(f"Diagonal: {diagonal}")

# Transpose matrix
transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print(f"Transposed: {transposed}")

# Example 4: Group data
students = [
    ("Alice", 85), ("Bob", 92), ("Charlie", 78), 
    ("Diana", 96), ("Eve", 83)
]

# Group by grade ranges
grade_a = [name for name, grade in students if grade >= 90]
grade_b = [name for name, grade in students if 80 <= grade < 90]
grade_c = [name for name, grade in students if grade < 80]

print(f"Grade A students: {grade_a}")
print(f"Grade B students: {grade_b}")
print(f"Grade C students: {grade_c}")

if __name__ == "__main__":
    print("\n=== List examples completed! ===")
