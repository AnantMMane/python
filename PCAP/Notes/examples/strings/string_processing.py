#!/usr/bin/env python3
"""
PCAP Examples: String Processing and Methods
This file demonstrates comprehensive string operations for PCAP certification.
"""

# ===== STRING CREATION =====
print("=== String Creation ===")

# Different ways to create strings
single_quotes = 'Hello'
double_quotes = "World"
triple_quotes = """This is a
multiline string
with line breaks"""

# Raw strings
normal_path = "C:\\Users\\Name\\Documents"  # Need to escape backslashes
raw_path = r"C:\Users\Name\Documents"       # Raw string - no escaping needed

print(f"Single quotes: {single_quotes}")
print(f"Double quotes: {double_quotes}")
print(f"Normal path: {normal_path}")
print(f"Raw path: {raw_path}")

# Unicode strings
unicode_text = "Hello, 世界! 🐍"
print(f"Unicode: {unicode_text}")

# ===== STRING INDEXING AND SLICING =====
print("\n=== String Indexing and Slicing ===")

text = "Python Programming"
print(f"Original text: '{text}'")

# Indexing
print(f"First character [0]: '{text[0]}'")
print(f"Last character [-1]: '{text[-1]}'")
print(f"Character at index 7: '{text[7]}'")

# Slicing
print(f"First 6 characters [0:6]: '{text[0:6]}'")
print(f"From index 7 [7:]: '{text[7:]}'")
print(f"Last 11 characters [-11:]: '{text[-11:]}'")
print(f"Every 2nd character [::2]: '{text[::2]}'")
print(f"Reversed [::-1]: '{text[::-1]}'")

# ===== CASE METHODS =====
print("\n=== Case Methods ===")

sample_text = "hello WORLD python"
print(f"Original: '{sample_text}'")

print(f"upper(): '{sample_text.upper()}'")
print(f"lower(): '{sample_text.lower()}'")
print(f"capitalize(): '{sample_text.capitalize()}'")
print(f"title(): '{sample_text.title()}'")
print(f"swapcase(): '{sample_text.swapcase()}'")

# Case checking
test_strings = ["HELLO", "hello", "Hello World", "Hello"]
for s in test_strings:
    print(f"'{s}' -> isupper: {s.isupper()}, islower: {s.islower()}, istitle: {s.istitle()}")

# ===== SEARCH AND FIND METHODS =====
print("\n=== Search and Find Methods ===")

text = "Python is awesome. Python is powerful. Python is easy."
print(f"Text: '{text}'")

# Finding substrings
print(f"find('Python'): {text.find('Python')}")  # First occurrence
print(f"find('Java'): {text.find('Java')}")      # Not found (-1)
print(f"rfind('Python'): {text.rfind('Python')}")  # Last occurrence
print(f"count('Python'): {text.count('Python')}")  # Count occurrences
print(f"count('is'): {text.count('is')}")

# Using index (raises ValueError if not found)
try:
    index = text.index("awesome")
    print(f"index('awesome'): {index}")
except ValueError as e:
    print(f"index error: {e}")

# Checking string properties
print(f"startswith('Python'): {text.startswith('Python')}")
print(f"endswith('easy.'): {text.endswith('easy.')}")

# ===== CHARACTER TYPE CHECKING =====
print("\n=== Character Type Checking ===")

test_strings = ["123", "abc", "abc123", "ABC", "Hello World", "   ", ""]

for s in test_strings:
    print(f"'{s}' -> isdigit: {s.isdigit()}, isalpha: {s.isalpha()}, "
          f"isalnum: {s.isalnum()}, isspace: {s.isspace()}")

# ===== SPLIT AND JOIN =====
print("\n=== Split and Join ===")

# Basic splitting
csv_data = "apple,banana,cherry,date"
fruits = csv_data.split(",")
print(f"CSV data: '{csv_data}'")
print(f"Split by comma: {fruits}")

# Splitting with maxsplit
sentence = "Hello world python programming"
words = sentence.split()  # Default: split by whitespace
print(f"Split by whitespace: {words}")

limited_split = sentence.split(" ", 2)  # Split only first 2 spaces
print(f"Split with maxsplit=2: {limited_split}")

# Special split methods
lines = "Line1\nLine2\nLine3\nLine4"
line_list = lines.splitlines()
print(f"splitlines(): {line_list}")

# Joining strings
fruits = ['apple', 'banana', 'cherry']
result = ", ".join(fruits)
print(f"Join with ', ': '{result}'")

words = ['Hello', 'world', 'from', 'Python']
sentence = " ".join(words)
print(f"Join with space: '{sentence}'")

# Join numbers (convert to string first)
numbers = [1, 2, 3, 4, 5]
number_string = "-".join(str(n) for n in numbers)
print(f"Join numbers: '{number_string}'")

# ===== STRIP AND PADDING =====
print("\n=== Strip and Padding ===")

# Removing whitespace
messy_text = "   Hello World   "
print(f"Original: '{messy_text}'")
print(f"strip(): '{messy_text.strip()}'")
print(f"lstrip(): '{messy_text.lstrip()}'")
print(f"rstrip(): '{messy_text.rstrip()}'")

# Removing specific characters
bordered_text = "***Hello World***"
print(f"Remove asterisks: '{bordered_text.strip('*')}'")

# Padding and alignment
text = "Python"
print(f"Original: '{text}'")
print(f"ljust(15): '{text.ljust(15)}'")
print(f"rjust(15): '{text.rjust(15)}'")
print(f"center(15): '{text.center(15)}'")
print(f"center(15, '-'): '{text.center(15, '-')}'")
print(f"zfill(10): '{text.zfill(10)}'")

# ===== REPLACE AND TRANSLATE =====
print("\n=== Replace and Translate ===")

text = "I love Java. Java is great. Java programming."
print(f"Original: '{text}'")

# Replace all occurrences
replaced = text.replace("Java", "Python")
print(f"replace('Java', 'Python'): '{replaced}'")

# Replace with count limit
limited_replace = text.replace("Java", "Python", 2)
print(f"replace with count=2: '{limited_replace}'")

# Translation table
text = "Hello World 123"
translation_table = str.maketrans("aeiou", "AEIOU", "123")
translated = text.translate(translation_table)
print(f"translate (vowels to uppercase, remove digits): '{translated}'")

# ===== STRING FORMATTING =====
print("\n=== String Formatting ===")

name = "Alice"
age = 25
score = 95.7

# f-strings (Python 3.6+)
f_string = f"My name is {name}, I'm {age} years old, and my score is {score:.1f}"
print(f"f-string: {f_string}")

# format() method
format_string = "My name is {}, I'm {} years old, and my score is {:.1f}".format(name, age, score)
print(f"format(): {format_string}")

# Named placeholders
named_format = "My name is {name}, I'm {age} years old".format(name=name, age=age)
print(f"Named format: {named_format}")

# % formatting (older style)
percent_format = "My name is %s, I'm %d years old" % (name, age)
print(f"% format: {percent_format}")

# Advanced formatting
pi = 3.14159265359
print(f"Pi to 2 decimals: {pi:.2f}")
print(f"Pi in scientific notation: {pi:.2e}")
print(f"Number with padding: {42:05d}")
print(f"Percentage: {0.875:.1%}")

# ===== STRING VALIDATION =====
print("\n=== String Validation ===")

def validate_input(text, input_type):
    """Validate different types of input."""
    if input_type == "email":
        return "@" in text and "." in text.split("@")[-1]
    elif input_type == "phone":
        digits_only = "".join(char for char in text if char.isdigit())
        return len(digits_only) == 10
    elif input_type == "password":
        return (len(text) >= 8 and 
                any(c.isupper() for c in text) and 
                any(c.islower() for c in text) and 
                any(c.isdigit() for c in text))
    return False

# Test validation
test_inputs = [
    ("alice@example.com", "email"),
    ("invalid.email", "email"),
    ("123-456-7890", "phone"),
    ("12345", "phone"),
    ("Password123", "password"),
    ("password", "password")
]

for text, validation_type in test_inputs:
    is_valid = validate_input(text, validation_type)
    print(f"{validation_type} '{text}': {'Valid' if is_valid else 'Invalid'}")

# ===== REGULAR EXPRESSIONS (BASIC) =====
print("\n=== Regular Expressions (Basic) ===")

import re

text = "Contact John at john.doe@email.com or call (555) 123-4567"
print(f"Text: {text}")

# Find email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(email_pattern, text)
print(f"Emails found: {emails}")

# Find phone numbers
phone_pattern = r'\(\d{3}\)\s\d{3}-\d{4}'
phones = re.findall(phone_pattern, text)
print(f"Phones found: {phones}")

# Replace sensitive information
masked_text = re.sub(email_pattern, '[EMAIL]', text)
masked_text = re.sub(phone_pattern, '[PHONE]', masked_text)
print(f"Masked text: {masked_text}")

# ===== PRACTICAL STRING PROCESSING =====
print("\n=== Practical String Processing ===")

# Parse CSV-like data
csv_data = """Name,Age,City,Salary
Alice,25,New York,50000
Bob,30,Los Angeles,60000
Charlie,35,Chicago,55000"""

lines = csv_data.strip().split('\n')
header = lines[0].split(',')
data = []

for line in lines[1:]:
    values = line.split(',')
    record = dict(zip(header, values))
    record['Age'] = int(record['Age'])
    record['Salary'] = int(record['Salary'])
    data.append(record)

print("Parsed CSV data:")
for person in data:
    print(f"  {person['Name']}: {person['Age']} years old, "
          f"lives in {person['City']}, earns ${person['Salary']:,}")

# Text analysis
def analyze_text(text):
    """Analyze text and return statistics."""
    words = text.lower().split()
    word_count = {}
    
    for word in words:
        # Remove punctuation
        word = word.strip(".,!?;:\"'")
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    
    return {
        'total_chars': len(text),
        'total_words': len(words),
        'unique_words': len(word_count),
        'most_common': max(word_count, key=word_count.get) if word_count else None,
        'word_frequency': word_count
    }

sample_text = """Python is a powerful programming language. 
Python is easy to learn and Python is versatile."""

analysis = analyze_text(sample_text)
print(f"\nText analysis:")
print(f"Total characters: {analysis['total_chars']}")
print(f"Total words: {analysis['total_words']}")
print(f"Unique words: {analysis['unique_words']}")
print(f"Most common word: {analysis['most_common']}")

# Log parsing example
log_entries = [
    "2023-12-01 10:30:15 [INFO] User login successful",
    "2023-12-01 10:35:22 [ERROR] Database connection failed",
    "2023-12-01 10:36:01 [WARNING] High memory usage detected",
    "2023-12-01 10:40:18 [INFO] User logout"
]

print(f"\nLog analysis:")
for entry in log_entries:
    parts = entry.split(' ', 2)
    date = parts[0]
    time = parts[1]
    message = parts[2]
    
    # Extract log level
    level_start = message.find('[') + 1
    level_end = message.find(']')
    level = message[level_start:level_end]
    content = message[level_end + 2:]
    
    print(f"Date: {date}, Time: {time}, Level: {level}, Message: {content}")

if __name__ == "__main__":
    print("\n=== String processing examples completed! ===")
