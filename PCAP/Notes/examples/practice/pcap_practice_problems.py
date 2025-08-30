#!/usr/bin/env python3
"""
PCAP Practice Problems
This file contains practice problems similar to those found in PCAP certification exam.
"""

print("=== PCAP Practice Problems ===")

# ===== PROBLEM 1: LIST OPERATIONS =====
print("\n--- Problem 1: List Operations ---")
# What is the output of this code?
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print("Problem 1 Output:", list1)
# Answer: [1, 2, 3, 4] - because list2 references the same object as list1

# ===== PROBLEM 2: FUNCTION SCOPE =====
print("\n--- Problem 2: Function Scope ---")
x = "global"

def test_scope():
    x = "local"
    return x

result = test_scope()
print("Problem 2 - Function result:", result)
print("Problem 2 - Global x:", x)
# Answer: Function result: "local", Global x: "global"

# ===== PROBLEM 3: LOOP CONTROL =====
print("\n--- Problem 3: Loop Control ---")
# What numbers are printed?
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print("Problem 3:", i)
# Answer: 0, 1, 3

# ===== PROBLEM 4: STRING SLICING =====
print("\n--- Problem 4: String Slicing ---")
text = "Python"
print("Problem 4a:", text[1:4])   # "yth"
print("Problem 4b:", text[::-1])  # "nohtyP"
print("Problem 4c:", text[::2])   # "Pto"

# ===== PROBLEM 5: EXCEPTION HANDLING =====
print("\n--- Problem 5: Exception Handling ---")
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid types"
    finally:
        print("Division attempt completed")

print("Problem 5a:", safe_divide(10, 2))
print("Problem 5b:", safe_divide(10, 0))

# ===== PROBLEM 6: DICTIONARY OPERATIONS =====
print("\n--- Problem 6: Dictionary Operations ---")
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Merge dictionaries (Python 3.5+ unpacking)
merged = {**dict1, **dict2}
print("Problem 6 - Merged dict:", merged)
# Answer: {"a": 1, "b": 3, "c": 4} - dict2 values override dict1

# ===== PROBLEM 7: LIST COMPREHENSION =====
print("\n--- Problem 7: List Comprehension ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create list of squares of even numbers
even_squares = [x**2 for x in numbers if x % 2 == 0]
print("Problem 7:", even_squares)
# Answer: [4, 16, 36, 64, 100]

# ===== PROBLEM 8: FUNCTION ARGUMENTS =====
print("\n--- Problem 8: Function Arguments ---")
def mystery_function(*args, **kwargs):
    return len(args) + len(kwargs)

result1 = mystery_function(1, 2, 3)
result2 = mystery_function(1, 2, x=3, y=4)
result3 = mystery_function(a=1, b=2, c=3)

print("Problem 8a:", result1)  # 3
print("Problem 8b:", result2)  # 4 (2 args + 2 kwargs)
print("Problem 8c:", result3)  # 3

# ===== PROBLEM 9: CLASS INHERITANCE =====
print("\n--- Problem 9: Class Inheritance ---")
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

class Cat(Animal):
    pass  # Inherits speak method

dog = Dog("Rex")
cat = Cat("Whiskers")

print("Problem 9a:", dog.speak())    # "Rex barks"
print("Problem 9b:", cat.speak())    # "Whiskers makes a sound"

# ===== PROBLEM 10: MUTABLE DEFAULT ARGUMENTS =====
print("\n--- Problem 10: Mutable Default Arguments ---")
def add_item(item, target_list=[]):  # BAD: mutable default
    target_list.append(item)
    return target_list

list1 = add_item("apple")
list2 = add_item("banana")
list3 = add_item("cherry", [])

print("Problem 10a:", list1)  # ["apple", "banana"]
print("Problem 10b:", list2)  # ["apple", "banana"]
print("Problem 10c:", list3)  # ["cherry"]
# Explanation: list1 and list2 share the same default list!

# ===== PROBLEM 11: BOOLEAN OPERATIONS =====
print("\n--- Problem 11: Boolean Operations ---")
# What are the results?
print("Problem 11a:", bool([]))        # False
print("Problem 11b:", bool([0]))       # True
print("Problem 11c:", bool(""))        # False
print("Problem 11d:", bool("0"))       # True
print("Problem 11e:", bool(None))      # False

# Short-circuit evaluation
x = 0
y = 5
result = x and y  # Returns x (0) because x is falsy
print("Problem 11f:", result)  # 0

result = x or y   # Returns y (5) because x is falsy
print("Problem 11g:", result)  # 5

# ===== PROBLEM 12: NESTED LOOPS =====
print("\n--- Problem 12: Nested Loops ---")
# What is printed?
for i in range(3):
    for j in range(2):
        if i == 1 and j == 1:
            break
        print(f"Problem 12: i={i}, j={j}")
# Answer: (0,0), (0,1), (1,0), (2,0), (2,1)

# ===== PROBLEM 13: STRING METHODS =====
print("\n--- Problem 13: String Methods ---")
text = "  Hello World  "
operations = [
    text.strip().upper(),           # "HELLO WORLD"
    text.replace(" ", "-"),         # "--Hello-World--"
    text.strip().split(),           # ["Hello", "World"]
    "".join(text.strip().split())   # "HelloWorld"
]

for i, op in enumerate(operations, 1):
    print(f"Problem 13{chr(96+i)}: {op}")

# ===== PROBLEM 14: TUPLE UNPACKING =====
print("\n--- Problem 14: Tuple Unpacking ---")
data = (1, 2, 3, 4, 5)

# Various unpacking patterns
a, b, *rest = data
print("Problem 14a:", a, b, rest)    # 1 2 [3, 4, 5]

*start, y, z = data
print("Problem 14b:", start, y, z)   # [1, 2, 3] 4 5

x, *middle, w = data
print("Problem 14c:", x, middle, w)  # 1 [2, 3, 4] 5

# ===== PROBLEM 15: SET OPERATIONS =====
print("\n--- Problem 15: Set Operations ---")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Problem 15a - Union:", set1 | set2)         # {1, 2, 3, 4, 5, 6}
print("Problem 15b - Intersection:", set1 & set2)  # {3, 4}
print("Problem 15c - Difference:", set1 - set2)    # {1, 2}
print("Problem 15d - Symmetric diff:", set1 ^ set2) # {1, 2, 5, 6}

# ===== PROBLEM 16: LAMBDA FUNCTIONS =====
print("\n--- Problem 16: Lambda Functions ---")
# Sort list of tuples by second element
students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
sorted_students = sorted(students, key=lambda x: x[1])
print("Problem 16:", sorted_students)
# Answer: [("Charlie", 78), ("Alice", 85), ("Bob", 90)]

# ===== PROBLEM 17: GENERATOR EXPRESSIONS =====
print("\n--- Problem 17: Generator vs List Comprehension ---")
# What's the difference?
numbers = [1, 2, 3, 4, 5]

list_comp = [x**2 for x in numbers]    # List comprehension
gen_exp = (x**2 for x in numbers)      # Generator expression

print("Problem 17a - List comp type:", type(list_comp))
print("Problem 17b - Generator type:", type(gen_exp))
print("Problem 17c - List comp result:", list_comp)
print("Problem 17d - Generator result:", list(gen_exp))

# ===== PROBLEM 18: GLOBAL VS LOCAL =====
print("\n--- Problem 18: Global vs Local Variables ---")
counter = 0

def increment():
    global counter
    counter += 1

def local_increment():
    counter = 1  # Creates local variable
    return counter

increment()
local_result = local_increment()
print("Problem 18a - Global counter:", counter)      # 1
print("Problem 18b - Local result:", local_result)   # 1
print("Problem 18c - Global after local:", counter)  # Still 1

# ===== PROBLEM 19: FILE OPERATIONS =====
print("\n--- Problem 19: File Operations ---")
# Create a temporary file for demonstration
filename = "temp_test.txt"

try:
    # Write to file
    with open(filename, "w") as f:
        f.write("Line 1\nLine 2\nLine 3")
    
    # Read entire file
    with open(filename, "r") as f:
        content = f.read()
        print("Problem 19a - Full content:", repr(content))
    
    # Read lines
    with open(filename, "r") as f:
        lines = f.readlines()
        print("Problem 19b - Lines count:", len(lines))
        print("Problem 19c - First line:", repr(lines[0]))

except Exception as e:
    print("Problem 19 - Error:", e)

# Clean up
try:
    import os
    os.remove(filename)
except:
    pass

# ===== PROBLEM 20: COMPLEX EXPRESSION =====
print("\n--- Problem 20: Complex Expression ---")
# What is the result?
result = [i for i in range(10) if i % 2 == 0 if i % 3 == 0]
print("Problem 20:", result)
# Answer: [0, 6] - numbers divisible by both 2 and 3

# ===== PRACTICAL PROBLEMS =====
print("\n=== PRACTICAL PROBLEMS ===")

# Practical Problem 1: Count word frequency
def word_frequency(text):
    """Count frequency of words in text."""
    words = text.lower().split()
    frequency = {}
    for word in words:
        word = word.strip(".,!?;:")  # Remove punctuation
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

sample_text = "Python is great. Python is powerful. Python is easy."
freq = word_frequency(sample_text)
print("Practical 1 - Word frequency:", freq)

# Practical Problem 2: Find missing number in sequence
def find_missing_number(numbers):
    """Find missing number in sequence 1 to n+1."""
    n = len(numbers) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum

sequence = [1, 2, 3, 5, 6, 7, 8]  # Missing 4
missing = find_missing_number(sequence)
print("Practical 2 - Missing number:", missing)

# Practical Problem 3: Validate parentheses
def validate_parentheses(s):
    """Check if parentheses are balanced."""
    stack = []
    pairs = {"(": ")", "[": "]", "{": "}"}
    
    for char in s:
        if char in pairs:
            stack.append(char)
        elif char in pairs.values():
            if not stack or pairs[stack.pop()] != char:
                return False
    
    return len(stack) == 0

test_strings = ["()", "()[]{}", "([)]", "((", ""])
for s in test_strings:
    result = validate_parentheses(s)
    print(f"Practical 3 - '{s}': {result}")

# Practical Problem 4: Matrix transpose
def transpose_matrix(matrix):
    """Transpose a 2D matrix."""
    return [[matrix[j][i] for j in range(len(matrix))] 
            for i in range(len(matrix[0]))]

matrix = [[1, 2, 3], [4, 5, 6]]
transposed = transpose_matrix(matrix)
print("Practical 4 - Original:", matrix)
print("Practical 4 - Transposed:", transposed)

# Practical Problem 5: Group anagrams
def group_anagrams(words):
    """Group words that are anagrams of each other."""
    anagram_groups = {}
    
    for word in words:
        # Sort characters to create a key
        key = "".join(sorted(word.lower()))
        if key not in anagram_groups:
            anagram_groups[key] = []
        anagram_groups[key].append(word)
    
    return list(anagram_groups.values())

words_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagram_groups = group_anagrams(words_list)
print("Practical 5 - Anagram groups:", anagram_groups)

if __name__ == "__main__":
    print("\n=== PCAP practice problems completed! ===")
    print("Review your answers and understanding of each concept.")
    print("These problems cover key PCAP exam topics:")
    print("- Data types and operations")
    print("- Control flow and loops") 
    print("- Functions and scope")
    print("- Object-oriented programming")
    print("- Exception handling")
    print("- File operations")
    print("- String processing")
    print("- Data structures")
