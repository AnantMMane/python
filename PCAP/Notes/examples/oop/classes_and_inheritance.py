#!/usr/bin/env python3
"""
PCAP Examples: Object-Oriented Programming
This file demonstrates classes, inheritance, and OOP concepts for PCAP certification.
"""

# ===== BASIC CLASS DEFINITION =====
print("=== Basic Class Definition ===")

class Person:
    """Basic Person class demonstrating class fundamentals."""
    
    # Class variable (shared by all instances)
    species = "Homo sapiens"
    population = 0
    
    def __init__(self, name, age):
        """Constructor method."""
        self.name = name  # Instance variable
        self.age = age    # Instance variable
        Person.population += 1  # Increment class variable
    
    def introduce(self):
        """Instance method."""
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
    
    def have_birthday(self):
        """Instance method that modifies instance variable."""
        self.age += 1
        print(f"Happy birthday! {self.name} is now {self.age} years old.")
    
    @classmethod
    def get_population(cls):
        """Class method - access class variables."""
        return cls.population
    
    @staticmethod
    def is_adult(age):
        """Static method - doesn't access instance or class variables."""
        return age >= 18

# Creating and using objects
person1 = Person("Alice", 25)
person2 = Person("Bob", 17)

print(person1.introduce())
print(person2.introduce())

person1.have_birthday()

print(f"Population: {Person.get_population()}")
print(f"Is Alice an adult? {Person.is_adult(person1.age)}")
print(f"Is Bob an adult? {Person.is_adult(person2.age)}")

# ===== INHERITANCE =====
print("\n=== Inheritance ===")

class Animal:
    """Base class for all animals."""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_alive = True
    
    def make_sound(self):
        """Method to be overridden by subclasses."""
        return "Some generic animal sound"
    
    def sleep(self):
        """Method inherited by all subclasses."""
        return f"{self.name} is sleeping..."
    
    def info(self):
        """Return basic information about the animal."""
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    """Dog class inheriting from Animal."""
    
    def __init__(self, name, breed):
        super().__init__(name, "Canine")  # Call parent constructor
        self.breed = breed
        self.is_trained = False
    
    def make_sound(self):
        """Override parent method."""
        return "Woof! Woof!"
    
    def fetch(self):
        """Method specific to Dog class."""
        return f"{self.name} is fetching the ball!"
    
    def train(self):
        """Train the dog."""
        self.is_trained = True
        return f"{self.name} has been trained!"

class Cat(Animal):
    """Cat class inheriting from Animal."""
    
    def __init__(self, name, breed):
        super().__init__(name, "Feline")
        self.breed = breed
        self.lives = 9
    
    def make_sound(self):
        """Override parent method."""
        return "Meow!"
    
    def climb(self):
        """Method specific to Cat class."""
        return f"{self.name} is climbing the tree!"

# Using inheritance
my_dog = Dog("Max", "Golden Retriever")
my_cat = Cat("Whiskers", "Persian")

print(my_dog.info())  # Inherited method
print(my_dog.make_sound())  # Overridden method
print(my_dog.fetch())  # Dog-specific method
print(my_dog.sleep())  # Inherited method

print(my_cat.info())
print(my_cat.make_sound())
print(my_cat.climb())

# ===== MULTIPLE INHERITANCE =====
print("\n=== Multiple Inheritance ===")

class Flyable:
    """Mixin class for flying ability."""
    
    def fly(self):
        return "Flying through the sky!"
    
    def land(self):
        return "Landing safely on the ground."

class Swimmable:
    """Mixin class for swimming ability."""
    
    def swim(self):
        return "Swimming gracefully in water!"
    
    def dive(self):
        return "Diving underwater!"

class Duck(Animal, Flyable, Swimmable):
    """Duck class with multiple inheritance."""
    
    def __init__(self, name):
        Animal.__init__(self, name, "Bird")
    
    def make_sound(self):
        return "Quack! Quack!"

# Using multiple inheritance
duck = Duck("Donald")
print(duck.info())      # From Animal
print(duck.make_sound()) # Overridden in Duck
print(duck.fly())       # From Flyable
print(duck.swim())      # From Swimmable
print(duck.dive())      # From Swimmable

# Method Resolution Order (MRO)
print(f"Duck MRO: {Duck.__mro__}")

# ===== ENCAPSULATION =====
print("\n=== Encapsulation ===")

class BankAccount:
    """Demonstrate encapsulation with access modifiers."""
    
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number      # Public
        self._balance = initial_balance           # Protected (convention)
        self.__pin = "1234"                      # Private (name mangling)
        self.__transaction_history = []          # Private
    
    def get_balance(self):
        """Public method to access balance."""
        return self._balance
    
    def deposit(self, amount):
        """Public method for depositing money."""
        if amount > 0:
            self._balance += amount
            self.__add_transaction(f"Deposited ${amount}")
            return f"Deposited ${amount}. New balance: ${self._balance}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount, pin):
        """Public method for withdrawing money."""
        if pin != self.__pin:
            return "Invalid PIN"
        
        if self.__validate_withdrawal(amount):
            self._balance -= amount
            self.__add_transaction(f"Withdrew ${amount}")
            return f"Withdrew ${amount}. New balance: ${self._balance}"
        return "Insufficient funds or invalid amount"
    
    def __validate_withdrawal(self, amount):
        """Private method for validation."""
        return amount > 0 and amount <= self._balance
    
    def __add_transaction(self, transaction):
        """Private method to add transaction."""
        self.__transaction_history.append(transaction)
    
    def get_transaction_history(self):
        """Public method to access transaction history."""
        return self.__transaction_history.copy()  # Return copy to prevent modification

# Using encapsulation
account = BankAccount("123456789", 1000)
print(f"Account number: {account.account_number}")  # Public access
print(f"Initial balance: {account.get_balance()}")

print(account.deposit(500))
print(account.withdraw(200, "1234"))
print(account.withdraw(100, "wrong"))  # Wrong PIN

# Direct access examples
print(f"Protected _balance: {account._balance}")  # Can access but shouldn't
# print(account.__pin)  # AttributeError - can't access private directly

# Name mangling makes private attributes accessible with _ClassName__attribute
print(f"Private __pin via name mangling: {account._BankAccount__pin}")

# ===== PROPERTIES =====
print("\n=== Properties ===")

class Temperature:
    """Demonstrate properties for controlled access."""
    
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter for celsius."""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter for celsius with validation."""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Computed property for Fahrenheit."""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Setter for fahrenheit (converts to celsius)."""
        if value < -459.67:
            raise ValueError("Temperature cannot be below absolute zero (-459.67°F)")
        self.celsius = (value - 32) * 5/9
    
    @property
    def kelvin(self):
        """Computed property for Kelvin."""
        return self._celsius + 273.15

# Using properties
temp = Temperature(25)
print(f"Temperature: {temp.celsius}°C")
print(f"In Fahrenheit: {temp.fahrenheit:.1f}°F")
print(f"In Kelvin: {temp.kelvin:.1f}K")

temp.fahrenheit = 86
print(f"After setting to 86°F: {temp.celsius:.1f}°C")

# ===== SPECIAL METHODS (MAGIC METHODS) =====
print("\n=== Special Methods ===")

class Vector:
    """Demonstrate special methods."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """String representation for users."""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """String representation for developers."""
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        """Addition operator."""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Subtraction operator."""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Multiplication with scalar."""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        """Equality operator."""
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        """Length of vector (magnitude)."""
        return int((self.x ** 2 + self.y ** 2) ** 0.5)
    
    def __getitem__(self, index):
        """Index access."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")
    
    def __setitem__(self, index, value):
        """Index assignment."""
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
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
print(f"len(v1): {len(v1)}")
print(f"v1[0]: {v1[0]}")
print(f"v1[1]: {v1[1]}")

v1[0] = 5
print(f"After v1[0] = 5: {v1}")

# ===== POLYMORPHISM =====
print("\n=== Polymorphism ===")

class Shape:
    """Abstract base class for shapes."""
    
    def area(self):
        raise NotImplementedError("Subclass must implement area method")
    
    def perimeter(self):
        raise NotImplementedError("Subclass must implement perimeter method")

class Rectangle(Shape):
    """Rectangle implementation."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"

class Circle(Shape):
    """Circle implementation."""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius
    
    def __str__(self):
        return f"Circle(r={self.radius})"

# Polymorphism in action
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Rectangle(2, 8),
    Circle(2.5)
]

print("Shape calculations:")
for shape in shapes:
    print(f"{shape}: Area = {shape.area():.2f}, Perimeter = {shape.perimeter():.2f}")

if __name__ == "__main__":
    print("\n=== OOP examples completed! ===")
