# Module 7: String Processing and Manipulation
## Mastering Text Operations in Python

Welcome to Module 7! This module focuses on string processing, manipulation, and analysis. You'll learn advanced string methods, regular expressions, text validation, and efficient text processing techniques.

## 🎯 Module Objectives

By the end of this module, you will be able to:
- Master string methods and operations
- Process and validate text data effectively
- Work with character encoding and Unicode
- Use regular expressions for pattern matching
- Implement text analysis and cleaning
- Handle advanced string formatting

## 📋 What You'll Learn

### 1. String Methods and Operations
- String creation and manipulation
- Built-in string methods
- String slicing and indexing
- String concatenation and repetition

### 2. String Formatting
- f-strings (formatted string literals)
- .format() method
- % operator formatting
- Custom format specifiers

### 3. Character Encoding
- ASCII, Unicode, and UTF-8
- Encoding and decoding
- ord() and chr() functions
- Handling special characters

### 4. Regular Expressions
- Pattern matching and searching
- Regex syntax and metacharacters
- Grouping and capturing
- Text validation and extraction

## 🚀 Getting Started

### Prerequisites
- Completed Module 6 (Modules and Packages)
- Understanding of Python strings and basic operations
- Knowledge of basic data types

### Estimated Time
- **Reading**: 2-3 hours
- **Practice**: 3-4 hours
- **Exercises**: 2-3 hours
- **Total**: 7-10 hours

## 📚 Module Content

### Section 1: String Methods and Operations

#### Basic String Operations
```python
# String creation and basic operations
text = "Hello, World!"
print(f"Original: {text}")
print(f"Length: {len(text)}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Title case: {text.title()}")
print(f"Capitalize: {text.capitalize()}")

# String slicing and indexing
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")
print(f"First 5 characters: {text[:5]}")
print(f"Last 5 characters: {text[-5:]}")
print(f"Characters 2-7: {text[2:7]}")
print(f"Every second character: {text[::2]}")

# String concatenation and repetition
str1 = "Hello"
str2 = "World"
combined = str1 + " " + str2
repeated = str1 * 3
print(f"Combined: {combined}")
print(f"Repeated: {repeated}")
```

#### String Methods
```python
# String search and replacement
text = "Python is a great programming language. Python is versatile."

# Finding substrings
print(f"Contains 'Python': {'Python' in text}")
print(f"Count of 'Python': {text.count('Python')}")
print(f"First 'Python' at: {text.find('Python')}")
print(f"Last 'Python' at: {text.rfind('Python')}")

# Replacing text
new_text = text.replace("Python", "JavaScript")
print(f"Replaced: {new_text}")

# Splitting and joining
words = text.split()
print(f"Words: {words}")
print(f"Word count: {len(words)}")

sentences = text.split('.')
print(f"Sentences: {sentences}")

# Joining strings
joined = '-'.join(words)
print(f"Joined with hyphens: {joined}")

# Stripping whitespace
messy_text = "   Hello World   "
print(f"Original: '{messy_text}'")
print(f"Stripped: '{messy_text.strip()}'")
print(f"Left stripped: '{messy_text.lstrip()}'")
print(f"Right stripped: '{messy_text.rstrip()}'")
```

### Section 2: String Formatting

#### f-strings (Formatted String Literals)
```python
# Basic f-string formatting
name = "Alice"
age = 25
height = 1.75

# Simple variable insertion
print(f"My name is {name}")
print(f"I am {age} years old")
print(f"My height is {height} meters")

# Format specifiers
pi = 3.14159
print(f"Pi to 2 decimal places: {pi:.2f}")
print(f"Pi in scientific notation: {pi:.2e}")
print(f"Pi as percentage: {pi:.1%}")

# Expressions in f-strings
x, y = 10, 5
print(f"{x} + {y} = {x + y}")
print(f"{x} * {y} = {x * y}")
print(f"Square root of {x}: {x ** 0.5:.2f}")

# Formatting with alignment
text = "Python"
print(f"Left aligned: {text:<10}")
print(f"Right aligned: {text:>10}")
print(f"Center aligned: {text:^10}")
print(f"Center aligned with padding: {text:^10}")

# Number formatting
number = 1234567.89
print(f"With commas: {number:,}")
print(f"With 2 decimal places: {number:.2f}")
print(f"Integer: {int(number)}")
```

#### .format() Method
```python
# Basic .format() usage
name = "Bob"
age = 30
city = "New York"

# Positional arguments
template1 = "My name is {}, I am {} years old, and I live in {}."
result1 = template1.format(name, age, city)
print(result1)

# Named arguments
template2 = "My name is {n}, I am {a} years old, and I live in {c}."
result2 = template2.format(n=name, a=age, c=city)
print(result2)

# Mixed positional and named
template3 = "My name is {}, I am {a} years old, and I live in {}."
result3 = template3.format(name, city, a=age)
print(result3)

# Format specifiers
price = 19.99
quantity = 3
total = price * quantity

template4 = "Price: ${:.2f}, Quantity: {}, Total: ${:.2f}"
result4 = template4.format(price, quantity, total)
print(result4)

# Dictionary formatting
person = {"name": "Charlie", "age": 35, "occupation": "Engineer"}
template5 = "Name: {name}, Age: {age}, Job: {occupation}"
result5 = template5.format(**person)
print(result5)
```

### Section 3: Character Encoding and Unicode

#### Understanding Encoding
```python
# Character encoding basics
text = "Hello, World! 🐍"

# ASCII characters (0-127)
ascii_chars = "Hello"
print(f"ASCII text: {ascii_chars}")
print(f"ASCII bytes: {ascii_chars.encode('ascii')}")

# Unicode characters
unicode_chars = "Hello 🐍"
print(f"Unicode text: {unicode_chars}")
print(f"UTF-8 bytes: {unicode_chars.encode('utf-8')}")

# ord() and chr() functions
print(f"ASCII 'A': {ord('A')}")
print(f"ASCII 'a': {ord('a')}")
print(f"Unicode '🐍': {ord('🐍')}")

print(f"Character 65: {chr(65)}")
print(f"Character 97: {chr(97)}")
print(f"Character 128053: {chr(128053)}")

# Encoding and decoding
text = "Hello, 世界!"
encoded = text.encode('utf-8')
decoded = encoded.decode('utf-8')

print(f"Original: {text}")
print(f"Encoded: {encoded}")
print(f"Decoded: {decoded}")
print(f"Match: {text == decoded}")

# Handling different encodings
try:
    # Try to encode with ASCII (will fail for non-ASCII)
    ascii_encoded = text.encode('ascii')
except UnicodeEncodeError as e:
    print(f"ASCII encoding failed: {e}")
    # Use UTF-8 instead
    utf8_encoded = text.encode('utf-8')
    print(f"UTF-8 encoding successful: {utf8_encoded}")
```

### Section 4: Regular Expressions

#### Basic Regex Patterns
```python
import re

# Basic pattern matching
text = "The quick brown fox jumps over the lazy dog"

# Simple search
pattern = r"fox"
match = re.search(pattern, text)
if match:
    print(f"Found 'fox' at position {match.start()}-{match.end()}")
    print(f"Matched text: '{match.group()}'")

# Pattern matching with metacharacters
# . matches any character except newline
pattern = r"b..n"  # matches "brown"
matches = re.findall(pattern, text)
print(f"Pattern 'b..n' matches: {matches}")

# * matches 0 or more repetitions
pattern = r"o*"  # matches 0 or more 'o' characters
matches = re.findall(pattern, text)
print(f"Pattern 'o*' matches: {matches}")

# + matches 1 or more repetitions
pattern = r"o+"  # matches 1 or more 'o' characters
matches = re.findall(pattern, text)
print(f"Pattern 'o+' matches: {matches}")

# ? matches 0 or 1 repetition
pattern = r"colou?r"  # matches "color" or "colour"
test_words = ["color", "colour", "colouur"]
for word in test_words:
    if re.match(pattern, word):
        print(f"'{word}' matches pattern")

# Character classes
pattern = r"[aeiou]"  # matches any vowel
vowels = re.findall(pattern, text)
print(f"Vowels found: {vowels}")

pattern = r"[^aeiou\s]"  # matches any non-vowel, non-whitespace
consonants = re.findall(pattern, text)
print(f"Consonants found: {consonants}")

# Quantifiers
pattern = r"\b\w{3,5}\b"  # matches words with 3-5 characters
short_words = re.findall(pattern, text)
print(f"Words with 3-5 characters: {short_words}")
```

#### Advanced Regex Features
```python
# Grouping and capturing
text = "John Doe, Jane Smith, Bob Johnson"

# Named groups
pattern = r"(?P<first>\w+)\s+(?P<last>\w+)"
matches = re.finditer(pattern, text)

for match in matches:
    first_name = match.group('first')
    last_name = match.group('last')
    print(f"First: {first_name}, Last: {last_name}")

# Substitution
text = "Hello World! Hello Python! Hello Everyone!"
pattern = r"Hello"
replacement = "Hi"
new_text = re.sub(pattern, replacement, text)
print(f"Original: {text}")
print(f"Replaced: {new_text}")

# Case-insensitive matching
text = "Python is great, PYTHON is awesome, python is fun"
pattern = r"python"
matches = re.findall(pattern, text, re.IGNORECASE)
print(f"Case-insensitive matches: {matches}")

# Multiline matching
text = """Line 1: Hello
Line 2: World
Line 3: Python"""

pattern = r"^Line \d+: (.+)$"
matches = re.findall(pattern, text, re.MULTILINE)
print(f"Multiline matches: {matches}")

# Complex pattern example
# Match email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
test_emails = [
    "user@example.com",
    "invalid-email",
    "another.user@domain.co.uk",
    "test@test"
]

for email in test_emails:
    if re.match(email_pattern, email):
        print(f"'{email}' is a valid email")
    else:
        print(f"'{email}' is not a valid email")
```

## 💻 Hands-On Practice

### Exercise 1: Text Analyzer
Create a comprehensive text analysis tool:

```python
import re
from collections import Counter

class TextAnalyzer:
    """Comprehensive text analysis tool."""
    
    def __init__(self, text):
        self.text = text
        self.words = self._extract_words()
        self.sentences = self._extract_sentences()
    
    def _extract_words(self):
        """Extract words from text."""
        # Remove punctuation and split into words
        clean_text = re.sub(r'[^\w\s]', '', self.text.lower())
        return clean_text.split()
    
    def _extract_sentences(self):
        """Extract sentences from text."""
        # Split by sentence endings
        return re.split(r'[.!?]+', self.text.strip())
    
    def word_count(self):
        """Get total word count."""
        return len(self.words)
    
    def sentence_count(self):
        """Get total sentence count."""
        return len([s for s in self.sentences if s.strip()])
    
    def character_count(self):
        """Get character count (with and without spaces)."""
        with_spaces = len(self.text)
        without_spaces = len(self.text.replace(" ", ""))
        return {"with_spaces": with_spaces, "without_spaces": without_spaces}
    
    def average_word_length(self):
        """Calculate average word length."""
        if not self.words:
            return 0
        total_length = sum(len(word) for word in self.words)
        return total_length / len(self.words)
    
    def most_common_words(self, n=5):
        """Get most common words."""
        word_counts = Counter(self.words)
        return word_counts.most_common(n)
    
    def word_frequency(self, word):
        """Get frequency of a specific word."""
        return self.words.count(word.lower())
    
    def text_summary(self):
        """Generate comprehensive text summary."""
        summary = {
            "word_count": self.word_count(),
            "sentence_count": self.sentence_count(),
            "character_count": self.character_count(),
            "average_word_length": round(self.average_word_length(), 2),
            "most_common_words": self.most_common_words(),
            "unique_words": len(set(self.words))
        }
        return summary

# Test the text analyzer
if __name__ == "__main__":
    sample_text = """
    Python is a high-level, interpreted programming language. 
    Python was created by Guido van Rossum and was released in 1991. 
    Python is known for its simplicity and readability. 
    Many developers choose Python for web development, data science, and automation.
    """
    
    analyzer = TextAnalyzer(sample_text)
    summary = analyzer.text_summary()
    
    print("Text Analysis Summary:")
    print("=" * 40)
    for key, value in summary.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    
    # Specific analysis
    print(f"\nFrequency of 'python': {analyzer.word_frequency('python')}")
    print(f"Frequency of 'is': {analyzer.word_frequency('is')}")
```

### Exercise 2: Data Validation System
Create a system for validating different types of data:

```python
import re
from typing import Dict, Any, List

class DataValidator:
    """System for validating different types of data."""
    
    def __init__(self):
        self.patterns = {
            'email': r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$',
            'phone': r'^\+?1?\d{9,15}$',
            'url': r'^https?://(?:[-\w.])+(?:[:\d]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:#(?:[\w.])*)?)?$',
            'date': r'^\d{4}-\d{2}-\d{2}$',
            'time': r'^([01]?[0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?$',
            'zip_code': r'^\d{5}(-\d{4})?$',
            'credit_card': r'^\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}$',
            'ip_address': r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
        }
    
    def validate(self, data_type: str, value: str) -> bool:
        """Validate a value against a specific pattern."""
        if data_type not in self.patterns:
            raise ValueError(f"Unknown data type: {data_type}")
        
        pattern = self.patterns[data_type]
        return bool(re.match(pattern, value))
    
    def validate_multiple(self, validations: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Validate multiple values at once."""
        results = {
            'valid': [],
            'invalid': [],
            'summary': {'total': 0, 'passed': 0, 'failed': 0}
        }
        
        for validation in validations:
            data_type = validation['type']
            value = validation['value']
            description = validation.get('description', f'{data_type} validation')
            
            is_valid = self.validate(data_type, value)
            
            result_item = {
                'description': description,
                'type': data_type,
                'value': value,
                'valid': is_valid
            }
            
            if is_valid:
                results['valid'].append(result_item)
                results['summary']['passed'] += 1
            else:
                results['invalid'].append(result_item)
                results['summary']['failed'] += 1
            
            results['summary']['total'] += 1
        
        return results
    
    def clean_phone_number(self, phone: str) -> str:
        """Clean and format phone number."""
        # Remove all non-digit characters
        cleaned = re.sub(r'\D', '', phone)
        
        # Format as (XXX) XXX-XXXX
        if len(cleaned) == 10:
            return f"({cleaned[:3]}) {cleaned[3:6]}-{cleaned[6:]}"
        elif len(cleaned) == 11 and cleaned[0] == '1':
            return f"+1 ({cleaned[1:4]}) {cleaned[4:7]}-{cleaned[7:]}"
        else:
            return cleaned
    
    def extract_emails(self, text: str) -> List[str]:
        """Extract all email addresses from text."""
        pattern = self.patterns['email']
        return re.findall(pattern, text)
    
    def extract_urls(self, text: str) -> List[str]:
        """Extract all URLs from text."""
        pattern = self.patterns['url']
        return re.findall(pattern, text)

# Test the data validator
if __name__ == "__main__":
    validator = DataValidator()
    
    # Test individual validations
    test_cases = [
        {'type': 'email', 'value': 'user@example.com', 'description': 'Valid email'},
        {'type': 'email', 'value': 'invalid-email', 'description': 'Invalid email'},
        {'type': 'phone', 'value': '+1-555-123-4567', 'description': 'Valid phone'},
        {'type': 'phone', 'value': '123', 'description': 'Invalid phone'},
        {'type': 'date', 'value': '2024-01-15', 'description': 'Valid date'},
        {'type': 'date', 'value': '01/15/2024', 'description': 'Invalid date format'},
        {'type': 'zip_code', 'value': '12345-6789', 'description': 'Valid ZIP code'},
        {'type': 'zip_code', 'value': '12345', 'description': 'Valid ZIP code'},
    ]
    
    # Validate all test cases
    results = validator.validate_multiple(test_cases)
    
    print("Validation Results:")
    print("=" * 50)
    
    print(f"Total: {results['summary']['total']}")
    print(f"Passed: {results['summary']['passed']}")
    print(f"Failed: {results['summary']['failed']}")
    
    print("\nValid Items:")
    for item in results['valid']:
        print(f"✓ {item['description']}: {item['value']}")
    
    print("\nInvalid Items:")
    for item in results['invalid']:
        print(f"✗ {item['description']}: {item['value']}")
    
    # Test phone number cleaning
    phone_numbers = ["555-123-4567", "(555) 123-4567", "555.123.4567"]
    print("\nPhone Number Cleaning:")
    for phone in phone_numbers:
        cleaned = validator.clean_phone_number(phone)
        print(f"Original: {phone} -> Cleaned: {cleaned}")
    
    # Test extraction
    sample_text = "Contact us at info@company.com or visit https://company.com"
    emails = validator.extract_emails(sample_text)
    urls = validator.extract_urls(sample_text)
    
    print(f"\nExtracted emails: {emails}")
    print(f"Extracted URLs: {urls}")
```

## 📝 Module Quiz

### Quiz Questions
1. What is the difference between `find()` and `index()` methods for strings?
2. How do you format a number to show 2 decimal places in an f-string?
3. What does the `r` prefix before a string literal do?
4. How do you match the beginning of a line in a regular expression?
5. What is the purpose of the `ord()` function?

### Quiz Answers
1. `find()` returns -1 if not found, `index()` raises an exception
2. Use `{number:.2f}` format specifier
3. It creates a raw string where backslashes are treated literally
4. Use the `^` metacharacter
5. `ord()` returns the Unicode code point of a character

## 🔍 Key Concepts Review

### String Processing Best Practices
- Use f-strings for modern string formatting
- Choose appropriate string methods for your task
- Handle encoding issues gracefully
- Use raw strings for regular expressions
- Validate input data before processing

### Regular Expression Guidelines
- Start with simple patterns and build complexity
- Use raw strings (`r"pattern"`) for regex
- Test patterns with various inputs
- Use appropriate flags (case-insensitive, multiline)
- Group related patterns for clarity

### Performance Considerations
- String concatenation with `+` is fine for small operations
- Use `join()` for combining many strings
- Compile regex patterns if used repeatedly
- Consider string methods over regex for simple operations

## 🎯 Module Checklist

- [ ] Master string methods and operations
- [ ] Understand string formatting techniques
- [ ] Work with character encoding and Unicode
- [ ] Use regular expressions effectively
- [ ] Implement text validation and cleaning
- [ ] Complete hands-on exercises
- [ ] Take module quiz
- [ ] Review key concepts

## 🚀 Next Steps

1. **Complete Exercises**: Work through all hands-on exercises
2. **Practice Text Processing**: Work with real text data
3. **Master Regex**: Practice with various patterns
4. **Move to Module 8**: File Handling

## 💡 Pro Tips

- **Use f-strings** for most string formatting needs
- **Learn regex gradually** - start with simple patterns
- **Handle encoding** properly for international text
- **Validate input** before processing strings
- **Use appropriate methods** for your specific task
- **Test edge cases** in your string processing

---

**Congratulations on completing Module 7! You now have a solid understanding of string processing and manipulation in Python. In the next module, you'll learn about file handling and I/O operations. Keep practicing and happy coding! 🐍✨**
