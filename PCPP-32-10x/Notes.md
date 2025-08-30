# PCPP-32-10x Python Certified Professional Programmer - Comprehensive Study Notes

## Table of Contents
1. [Advanced Object-Oriented Programming](#advanced-object-oriented-programming)
2. [GUI Programming with tkinter](#gui-programming-with-tkinter)
3. [Network Programming](#network-programming)
4. [File Processing & I/O](#file-processing--io)
5. [Design Patterns](#design-patterns)
6. [Testing & Debugging](#testing--debugging)
7. [Code Optimization](#code-optimization)
8. [Useful Resources](#useful-resources)

---

## Advanced Object-Oriented Programming

### 1. Inheritance and Polymorphism

#### Key Concepts:
- **Single Inheritance**: A class inherits from one parent class
- **Multiple Inheritance**: A class inherits from multiple parent classes
- **Method Resolution Order (MRO)**: Python's algorithm for determining method lookup
- **Polymorphism**: Objects of different types responding to the same interface

#### Deep Dive - Method Resolution Order:
```python
class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        print("B method")

class C(A):
    def method(self):
        print("C method")

class D(B, C):
    pass

# Check MRO
print(D.__mro__)
# Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

### 2. Abstract Base Classes (ABC)

#### When to use ABCs:
- Define contracts that concrete classes must follow
- Enforce implementation of specific methods
- Create template for related classes

#### Example Implementation:
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def description(self):
        return f"This is a shape with area {self.area()}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
```

### 3. Special Methods (Magic Methods)

#### Essential Magic Methods:
- `__init__`: Constructor
- `__str__`: String representation for users
- `__repr__`: String representation for developers
- `__len__`: Length of object
- `__eq__`: Equality comparison
- `__lt__`, `__le__`, `__gt__`, `__ge__`: Ordering comparisons

#### Advanced Magic Methods:
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

### 4. Properties and Descriptors

#### Properties for Controlled Access:
```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9
```

### 5. Metaclasses

#### Understanding Metaclasses:
Metaclasses are "classes that create classes". They control the creation and behavior of class objects.

```python
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = "Connected to database"

# Usage
db1 = Database()
db2 = Database()
print(db1 is db2)  # True - same instance
```

---

## GUI Programming with tkinter

### 1. Basic GUI Structure

#### Essential Components:
- **Root Window**: Main application window
- **Widgets**: UI elements (buttons, labels, entries)
- **Layout Managers**: pack(), grid(), place()
- **Event Handling**: Responding to user interactions

#### Basic Application Template:
```python
import tkinter as tk
from tkinter import ttk

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("My Application")
        self.root.geometry("400x300")
        
        self.create_widgets()
        self.arrange_widgets()
        self.bind_events()
    
    def create_widgets(self):
        self.label = ttk.Label(self.root, text="Hello, World!")
        self.button = ttk.Button(self.root, text="Click Me", command=self.on_click)
        self.entry = ttk.Entry(self.root)
    
    def arrange_widgets(self):
        self.label.pack(pady=10)
        self.entry.pack(pady=5)
        self.button.pack(pady=5)
    
    def bind_events(self):
        self.root.bind('<Return>', lambda e: self.on_click())
    
    def on_click(self):
        text = self.entry.get()
        self.label.config(text=f"You entered: {text}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
```

### 2. Advanced Widget Usage

#### Treeview for Data Display:
```python
import tkinter as tk
from tkinter import ttk

class DataViewer:
    def __init__(self, root):
        self.root = root
        self.create_treeview()
    
    def create_treeview(self):
        # Create treeview with columns
        self.tree = ttk.Treeview(self.root, columns=('Name', 'Age', 'City'), show='headings')
        
        # Define headings
        self.tree.heading('#1', text='Name')
        self.tree.heading('#2', text='Age')
        self.tree.heading('#3', text='City')
        
        # Configure column widths
        self.tree.column('#1', width=150)
        self.tree.column('#2', width=100)
        self.tree.column('#3', width=150)
        
        # Add sample data
        data = [
            ('Alice', 30, 'New York'),
            ('Bob', 25, 'San Francisco'),
            ('Charlie', 35, 'Chicago')
        ]
        
        for item in data:
            self.tree.insert('', tk.END, values=item)
        
        self.tree.pack(expand=True, fill='both')
```

### 3. Custom Widgets

#### Creating Reusable Components:
```python
import tkinter as tk
from tkinter import ttk

class LabeledEntry(ttk.Frame):
    def __init__(self, parent, label_text, **kwargs):
        super().__init__(parent)
        
        self.label = ttk.Label(self, text=label_text)
        self.entry = ttk.Entry(self, **kwargs)
        
        self.label.pack(side=tk.LEFT, padx=(0, 5))
        self.entry.pack(side=tk.LEFT, expand=True, fill=tk.X)
    
    def get(self):
        return self.entry.get()
    
    def set(self, value):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)

# Usage
root = tk.Tk()
name_field = LabeledEntry(root, "Name:")
age_field = LabeledEntry(root, "Age:")

name_field.pack(fill=tk.X, padx=10, pady=5)
age_field.pack(fill=tk.X, padx=10, pady=5)
```

---

## Network Programming

### 1. Socket Programming Fundamentals

#### TCP Client-Server Communication:
```python
# Server
import socket
import threading

class TCPServer:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    def start(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")
        
        while True:
            client_socket, addr = self.socket.accept()
            client_thread = threading.Thread(
                target=self.handle_client, 
                args=(client_socket, addr)
            )
            client_thread.start()
    
    def handle_client(self, client_socket, addr):
        print(f"Connection from {addr}")
        try:
            while True:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break
                response = f"Echo: {data}"
                client_socket.send(response.encode('utf-8'))
        except ConnectionResetError:
            print(f"Client {addr} disconnected")
        finally:
            client_socket.close()

# Client
class TCPClient:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
    
    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
    
    def send_message(self, message):
        self.socket.send(message.encode('utf-8'))
        response = self.socket.recv(1024).decode('utf-8')
        return response
    
    def close(self):
        self.socket.close()
```

### 2. HTTP Requests and APIs

#### Using requests library:
```python
import requests
import json

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
    
    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def post(self, endpoint, data=None, json_data=None):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.post(url, data=data, json=json_data)
        response.raise_for_status()
        return response.json()
    
    def with_auth(self, token):
        self.session.headers.update({'Authorization': f'Bearer {token}'})
        return self

# Usage example
api = APIClient("https://api.example.com")
api.with_auth("your-token-here")

users = api.get("users", params={"limit": 10})
new_user = api.post("users", json_data={"name": "John", "email": "john@example.com"})
```

---

## File Processing & I/O

### 1. Advanced File Operations

#### Context Managers for Resource Management:
```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # Return False to propagate exceptions
        return False

# Usage
with FileManager('data.txt', 'w') as f:
    f.write('Hello, World!')
```

### 2. JSON and XML Processing

#### Advanced JSON Handling:
```python
import json
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

class DataProcessor:
    @staticmethod
    def save_json(data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f, cls=DateTimeEncoder, indent=2)
    
    @staticmethod
    def load_json(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    
    @staticmethod
    def process_large_json(filename):
        """Process large JSON files line by line"""
        with open(filename, 'r') as f:
            for line in f:
                try:
                    data = json.loads(line.strip())
                    yield data
                except json.JSONDecodeError:
                    continue
```

---

## Design Patterns

### 1. Creational Patterns

#### Singleton Pattern:
```python
class Singleton:
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self._initialized = True
            # Initialization code here
            self.data = {}
```

#### Factory Pattern:
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return "Drawing a circle"

class Rectangle(Shape):
    def draw(self):
        return "Drawing a rectangle"

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type):
        if shape_type.lower() == 'circle':
            return Circle()
        elif shape_type.lower() == 'rectangle':
            return Rectangle()
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")
```

### 2. Behavioral Patterns

#### Observer Pattern:
```python
class Observable:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self, event):
        for observer in self._observers:
            observer.update(event)

class ConcreteObserver:
    def __init__(self, name):
        self.name = name
    
    def update(self, event):
        print(f"{self.name} received event: {event}")
```

---

## Testing & Debugging

### 1. Unit Testing with unittest

#### Comprehensive Test Suite:
```python
import unittest
from unittest.mock import Mock, patch

class Calculator:
    def add(self, a, b):
        return a + b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_add(self):
        result = self.calc.add(3, 5)
        self.assertEqual(result, 8)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
    
    def test_divide_success(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5.0)
    
    @patch('builtins.print')
    def test_with_mock(self, mock_print):
        # Test code that uses print
        print("Hello, World!")
        mock_print.assert_called_once_with("Hello, World!")

if __name__ == '__main__':
    unittest.main()
```

### 2. Debugging Techniques

#### Custom Decorator for Debugging:
```python
import functools
import time

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        
        print(f"Calling {func.__name__}({signature})")
        
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        print(f"{func.__name__} returned {result!r} in {end_time - start_time:.4f}s")
        return result
    return wrapper

@debug
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

---

## Code Optimization

### 1. Performance Optimization

#### Profiling Code:
```python
import cProfile
import time
from functools import lru_cache

class PerformanceAnalyzer:
    @staticmethod
    def profile_function(func, *args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()
        profiler.print_stats(sort='cumulative')
        return result
    
    @staticmethod
    @lru_cache(maxsize=128)
    def expensive_operation(n):
        """Cached expensive operation"""
        time.sleep(0.1)  # Simulate expensive computation
        return n ** 2
```

### 2. Memory Optimization

#### Using __slots__ for Memory Efficiency:
```python
class RegularClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class OptimizedClass:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Memory usage comparison
import sys
regular = RegularClass(1, 2)
optimized = OptimizedClass(1, 2)

print(f"Regular class size: {sys.getsizeof(regular.__dict__)} bytes")
print(f"Optimized class has no __dict__")
```

---

## Useful Resources

### Official Documentation
- [Python.org](https://www.python.org/)
- [Python Standard Library](https://docs.python.org/3/library/)
- [PEP Index](https://www.python.org/dev/peps/)

### Books
- "Effective Python" by Brett Slatkin
- "Python Tricks" by Dan Bader
- "Fluent Python" by Luciano Ramalho

### Online Resources
- [Real Python](https://realpython.com/)
- [Python Institute](https://pythoninstitute.org/)
- [Stack Overflow Python Tag](https://stackoverflow.com/questions/tagged/python)

### Practice Platforms
- [LeetCode](https://leetcode.com/)
- [HackerRank](https://www.hackerrank.com/domains/python)
- [Codewars](https://www.codewars.com/)

---

## Next Steps

1. **Practice with examples**: Work through the code examples in the `examples/` folder
2. **Build projects**: Apply concepts in real-world scenarios
3. **Take practice tests**: Use official Python Institute practice exams
4. **Join communities**: Participate in Python forums and discussions

Remember: The key to certification success is not just understanding concepts but being able to apply them in practical scenarios. Practice regularly and build projects to reinforce your learning.
