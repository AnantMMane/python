# Module 5: Object-Oriented Programming
## Building Classes and Objects

Welcome to Module 5! This module introduces you to Object-Oriented Programming (OOP) in Python. You'll learn how to create classes, instantiate objects, and use inheritance and polymorphism to build robust, maintainable code.

## 🎯 Module Objectives

By the end of this module, you will be able to:
- Understand OOP principles and concepts
- Create classes and instantiate objects
- Implement inheritance and polymorphism
- Use encapsulation and access control
- Apply special methods and properties
- Use object introspection effectively

## 📋 What You'll Learn

### 1. OOP Fundamentals
- Classes and objects
- Constructors and methods
- Instance vs class variables
- Method types and usage

### 2. Inheritance and Polymorphism
- Single and multiple inheritance
- Method overriding and overloading
- Polymorphic behavior
- Abstract classes and interfaces

### 3. Encapsulation and Access Control
- Private and protected attributes
- Properties and getters/setters
- Data hiding principles
- Interface design

### 4. Advanced OOP Features
- Special methods (magic methods)
- Class methods and static methods
- Object introspection
- Design patterns

## 🚀 Getting Started

### Prerequisites
- Completed Module 4 (Functions and Data Structures)
- Understanding of Python functions and data types
- Basic knowledge of programming concepts

### Estimated Time
- **Reading**: 3-4 hours
- **Practice**: 4-5 hours
- **Exercises**: 3-4 hours
- **Total**: 10-13 hours

## 📚 Module Content

### Section 1: Classes and Objects

#### Basic Class Definition
```python
class Person:
    """A simple class representing a person."""
    
    def __init__(self, name, age):
        """Constructor method."""
        self.name = name
        self.age = age
    
    def introduce(self):
        """Method to introduce the person."""
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
    
    def have_birthday(self):
        """Method to increment age."""
        self.age += 1
        return f"Happy birthday! {self.name} is now {self.age}."

# Creating objects (instances)
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Using object methods
print(person1.introduce())
print(person2.introduce())
print(person1.have_birthday())
```

#### Instance Variables and Methods
```python
class BankAccount:
    """A class representing a bank account."""
    
    def __init__(self, account_number, owner_name, initial_balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = initial_balance
        self.transactions = []
    
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount}")
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds"
    
    def get_balance(self):
        """Get current account balance."""
        return self.balance
    
    def get_transaction_history(self):
        """Get list of transactions."""
        return self.transactions.copy()

# Using the class
account = BankAccount("12345", "John Doe", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(f"Balance: ${account.get_balance()}")
print("Transactions:", account.get_transaction_history())
```

### Section 2: Inheritance and Polymorphism

#### Single Inheritance
```python
class Animal:
    """Base class for animals."""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        """Base method for making sounds."""
        return "Some animal sound"
    
    def get_info(self):
        """Get animal information."""
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    """Dog class inheriting from Animal."""
    
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    
    def make_sound(self):
        """Override the make_sound method."""
        return "Woof!"
    
    def fetch(self):
        """Dog-specific method."""
        return f"{self.name} is fetching the ball"
    
    def get_info(self):
        """Override get_info to include breed."""
        return f"{self.name} is a {self.breed} dog"

class Cat(Animal):
    """Cat class inheriting from Animal."""
    
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color
    
    def make_sound(self):
        """Override the make_sound method."""
        return "Meow!"
    
    def climb(self):
        """Cat-specific method."""
        return f"{self.name} is climbing the tree"

# Using inheritance
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

print(dog.make_sound())  # Polymorphic behavior
print(cat.make_sound())  # Polymorphic behavior
print(dog.fetch())
print(cat.climb())
```

#### Multiple Inheritance
```python
class Flyable:
    """Mixin class for flying ability."""
    
    def fly(self):
        return "Flying high in the sky"

class Swimmable:
    """Mixin class for swimming ability."""
    
    def swim(self):
        return "Swimming in the water"

class Duck(Animal, Flyable, Swimmable):
    """Duck class with multiple inheritance."""
    
    def __init__(self, name):
        super().__init__(name, "Duck")
    
    def make_sound(self):
        return "Quack!"
    
    def get_info(self):
        return f"{self.name} is a duck that can fly and swim"

# Using multiple inheritance
duck = Duck("Donald")
print(duck.make_sound())
print(duck.fly())
print(duck.swim())
print(duck.get_info())
```

### Section 3: Encapsulation and Access Control

#### Private and Protected Attributes
```python
class Student:
    """Student class demonstrating encapsulation."""
    
    def __init__(self, name, student_id):
        self.name = name          # Public attribute
        self._student_id = student_id  # Protected attribute
        self.__grades = {}        # Private attribute
    
    def add_grade(self, subject, grade):
        """Add a grade with validation."""
        if 0 <= grade <= 100:
            self.__grades[subject] = grade
            return True
        return False
    
    def get_grade(self, subject):
        """Get grade for a subject."""
        return self.__grades.get(subject, "No grade recorded")
    
    def get_average(self):
        """Calculate average grade."""
        if not self.__grades:
            return 0
        return sum(self.__grades.values()) / len(self.__grades)
    
    def get_student_id(self):
        """Getter for protected attribute."""
        return self._student_id

# Using encapsulation
student = Student("Alice", "S001")
student.add_grade("Math", 95)
student.add_grade("Science", 88)

print(f"Student: {student.name}")
print(f"ID: {student.get_student_id()}")
print(f"Math Grade: {student.get_grade('Math')}")
print(f"Average: {student.get_average():.1f}")

# Note: Private attributes can still be accessed (Python doesn't enforce true privacy)
# But it's a convention that indicates "don't access this directly"
```

#### Properties and Getters/Setters
```python
class Temperature:
    """Temperature class using properties."""
    
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter for celsius temperature."""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter for celsius temperature with validation."""
        if value < -273.15:  # Absolute zero
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Property for fahrenheit temperature."""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Setter for fahrenheit temperature."""
        self.celsius = (value - 32) * 5/9
    
    @property
    def kelvin(self):
        """Property for kelvin temperature."""
        return self._celsius + 273.15
    
    @kelvin.setter
    def kelvin(self, value):
        """Setter for kelvin temperature."""
        self.celsius = value - 273.15

# Using properties
temp = Temperature(25)
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit}°F")
print(f"Kelvin: {temp.kelvin}K")

# Setting temperatures
temp.fahrenheit = 68
print(f"After setting to 68°F: {temp.celsius}°C")

temp.kelvin = 300
print(f"After setting to 300K: {temp.celsius}°C")
```

### Section 4: Special Methods and Advanced Features

#### Special Methods (Magic Methods)
```python
class Vector:
    """Vector class demonstrating special methods."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """String representation."""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """Detailed string representation."""
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        """Vector addition."""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __sub__(self, other):
        """Vector subtraction."""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented
    
    def __mul__(self, scalar):
        """Vector scalar multiplication."""
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented
    
    def __eq__(self, other):
        """Equality comparison."""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False
    
    def __len__(self):
        """Vector magnitude."""
        return (self.x**2 + self.y**2)**0.5
    
    def __getitem__(self, index):
        """Index-based access."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")

# Using special methods
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 - v2: {v1 - v2}")
print(f"v1 * 2: {v1 * 2}")
print(f"v1 == v2: {v1 == v2}")
print(f"Length of v1: {len(v1):.2f}")
print(f"v1[0]: {v1[0]}, v1[1]: {v1[1]}")
```

#### Class Methods and Static Methods
```python
class Date:
    """Date class demonstrating class and static methods."""
    
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_string):
        """Create Date object from string (YYYY-MM-DD)."""
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)
    
    @classmethod
    def today(cls):
        """Create Date object for today."""
        from datetime import date
        today = date.today()
        return cls(today.year, today.month, today.day)
    
    @staticmethod
    def is_valid_date(year, month, day):
        """Check if date is valid."""
        if year < 1 or month < 1 or month > 12 or day < 1:
            return False
        
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Handle leap year for February
        if month == 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            days_in_month[1] = 29
        
        return day <= days_in_month[month - 1]
    
    def __str__(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"

# Using class and static methods
date1 = Date.from_string("2024-01-15")
date2 = Date.today()

print(f"Date from string: {date1}")
print(f"Today's date: {date2}")
print(f"Is 2024-02-30 valid? {Date.is_valid_date(2024, 2, 30)}")
print(f"Is 2024-02-29 valid? {Date.is_valid_date(2024, 2, 29)}")
```

## 💻 Hands-On Practice

### Exercise 1: Bank Account System
Create a comprehensive banking system:

```python
class BankAccount:
    """Bank account class with transaction history."""
    
    def __init__(self, account_number, owner_name, initial_balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = initial_balance
        self.transactions = []
        self.is_active = True
    
    def deposit(self, amount):
        """Deposit money into account."""
        if not self.is_active:
            return "Account is inactive"
        if amount <= 0:
            return "Invalid amount"
        
        self.balance += amount
        self.transactions.append({
            'type': 'deposit',
            'amount': amount,
            'balance': self.balance,
            'timestamp': '2024-01-15'  # Simplified timestamp
        })
        return f"Deposited ${amount}. New balance: ${self.balance}"
    
    def withdraw(self, amount):
        """Withdraw money from account."""
        if not self.is_active:
            return "Account is inactive"
        if amount <= 0:
            return "Invalid amount"
        if amount > self.balance:
            return "Insufficient funds"
        
        self.balance -= amount
        self.transactions.append({
            'type': 'withdrawal',
            'amount': amount,
            'balance': self.balance,
            'timestamp': '2024-01-15'
        })
        return f"Withdrew ${amount}. New balance: ${self.balance}"
    
    def transfer(self, other_account, amount):
        """Transfer money to another account."""
        if not self.is_active or not other_account.is_active:
            return "One or both accounts are inactive"
        
        withdrawal_result = self.withdraw(amount)
        if "Insufficient funds" in withdrawal_result:
            return withdrawal_result
        
        other_account.deposit(amount)
        return f"Transferred ${amount} to {other_account.owner_name}"
    
    def get_balance(self):
        """Get current balance."""
        return self.balance
    
    def get_transaction_history(self):
        """Get transaction history."""
        return self.transactions.copy()
    
    def deactivate(self):
        """Deactivate the account."""
        self.is_active = False
        return "Account deactivated"
    
    def activate(self):
        """Activate the account."""
        self.is_active = True
        return "Account activated"

# Test the banking system
if __name__ == "__main__":
    # Create accounts
    alice_account = BankAccount("A001", "Alice Johnson", 1000)
    bob_account = BankAccount("B001", "Bob Smith", 500)
    
    # Perform transactions
    print(alice_account.deposit(200))
    print(alice_account.withdraw(100))
    print(alice_account.transfer(bob_account, 150))
    
    # Check balances
    print(f"Alice's balance: ${alice_account.get_balance()}")
    print(f"Bob's balance: ${bob_account.get_balance()}")
    
    # View transaction history
    print(f"Alice's transactions: {alice_account.get_transaction_history()}")
```

### Exercise 2: Shape Calculator with Inheritance
Create a shape hierarchy:

```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract base class for shapes."""
    
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def area(self):
        """Calculate area of the shape."""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate perimeter of the shape."""
        pass
    
    def get_info(self):
        """Get shape information."""
        return f"{self.name}: Area = {self.area():.2f}, Perimeter = {self.perimeter():.2f}"

class Circle(Shape):
    """Circle class."""
    
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """Rectangle class."""
    
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    """Triangle class."""
    
    def __init__(self, a, b, c):
        super().__init__("Triangle")
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        # Heron's formula
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        return self.a + self.b + self.c

# Test the shape system
if __name__ == "__main__":
    shapes = [
        Circle(5),
        Rectangle(4, 6),
        Triangle(3, 4, 5)
    ]
    
    for shape in shapes:
        print(shape.get_info())
```

## 📝 Module Quiz

### Quiz Questions
1. What is the difference between a class and an object?
2. What does the `super()` function do in inheritance?
3. How do you make an attribute private in Python?
4. What is polymorphism in OOP?
5. What is the purpose of the `__init__` method?

### Quiz Answers
1. A class is a blueprint/template, an object is an instance of that class
2. `super()` calls methods from the parent class
3. Use double underscore prefix: `__attribute_name`
4. Polymorphism allows objects of different classes to respond to the same method call
5. `__init__` is the constructor method that initializes object attributes

## 🔍 Key Concepts Review

### OOP Principles
- **Encapsulation**: Bundling data and methods together
- **Inheritance**: Creating new classes from existing ones
- **Polymorphism**: Different objects responding to the same method call
- **Abstraction**: Hiding complex implementation details

### Best Practices
- Use meaningful class and method names
- Keep classes focused on a single responsibility
- Use inheritance for "is-a" relationships
- Implement proper encapsulation with getters/setters
- Document your classes and methods

## 🎯 Module Checklist

- [ ] Understand OOP principles and concepts
- [ ] Create classes and instantiate objects
- [ ] Implement inheritance and polymorphism
- [ ] Use encapsulation and access control
- [ ] Apply special methods and properties
- [ ] Complete hands-on exercises
- [ ] Take module quiz
- [ ] Review key concepts

## 🚀 Next Steps

1. **Complete Exercises**: Work through all hands-on exercises
2. **Practice OOP**: Create classes for real-world entities
3. **Build Hierarchies**: Design inheritance relationships
4. **Move to Module 6**: Modules and Packages

## 💡 Pro Tips

- **Start simple** and add complexity gradually
- **Use composition over inheritance** when appropriate
- **Follow the Single Responsibility Principle**
- **Use abstract base classes** for common interfaces
- **Implement proper error handling** in your methods
- **Test your classes** with various scenarios

---

**Congratulations on completing Module 5! You now have a solid understanding of Object-Oriented Programming in Python. In the next module, you'll learn about modules, packages, and code organization. Keep practicing and happy coding! 🐍✨**
