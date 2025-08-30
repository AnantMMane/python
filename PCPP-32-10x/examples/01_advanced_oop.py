#!/usr/bin/env python3
"""
Advanced Object-Oriented Programming Examples
PCPP Certification Study Material

This module demonstrates advanced OOP concepts including:
- Multiple inheritance and MRO
- Abstract base classes
- Magic methods
- Properties and descriptors
- Metaclasses
"""

from abc import ABC, abstractmethod
import functools


# 1. Multiple Inheritance and Method Resolution Order (MRO)
class A:
    def method(self):
        print("Method from class A")
        return "A"

class B(A):
    def method(self):
        print("Method from class B")
        result = super().method()
        return f"B -> {result}"

class C(A):
    def method(self):
        print("Method from class C")
        result = super().method()
        return f"C -> {result}"

class D(B, C):
    def method(self):
        print("Method from class D")
        result = super().method()
        return f"D -> {result}"


# 2. Abstract Base Classes (ABC)
class Vehicle(ABC):
    """Abstract base class for vehicles"""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    @abstractmethod
    def start_engine(self):
        """Abstract method that must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def stop_engine(self):
        """Abstract method that must be implemented by subclasses"""
        pass
    
    def get_info(self):
        """Concrete method available to all subclasses"""
        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type="gasoline"):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
        self.engine_running = False
    
    def start_engine(self):
        if not self.engine_running:
            self.engine_running = True
            return f"Car engine started with {self.fuel_type}"
        return "Engine already running"
    
    def stop_engine(self):
        if self.engine_running:
            self.engine_running = False
            return "Car engine stopped"
        return "Engine already stopped"


class ElectricCar(Vehicle):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity
        self.motor_running = False
    
    def start_engine(self):
        if not self.motor_running:
            self.motor_running = True
            return f"Electric motor started (Battery: {self.battery_capacity}kWh)"
        return "Motor already running"
    
    def stop_engine(self):
        if self.motor_running:
            self.motor_running = False
            return "Electric motor stopped"
        return "Motor already stopped"


# 3. Magic Methods (Dunder Methods)
class Vector:
    """A 2D vector class demonstrating magic methods"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """String representation for end users"""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """String representation for developers"""
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        """Addition operator overloading"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other)
        return NotImplemented
    
    def __sub__(self, other):
        """Subtraction operator overloading"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x - other, self.y - other)
        return NotImplemented
    
    def __mul__(self, scalar):
        """Scalar multiplication"""
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented
    
    def __rmul__(self, scalar):
        """Right multiplication (scalar * vector)"""
        return self.__mul__(scalar)
    
    def __eq__(self, other):
        """Equality comparison"""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False
    
    def __lt__(self, other):
        """Less than comparison (by magnitude)"""
        if isinstance(other, Vector):
            return self.magnitude() < other.magnitude()
        return NotImplemented
    
    def __len__(self):
        """Length of vector (magnitude as integer)"""
        return int(self.magnitude())
    
    def __bool__(self):
        """Boolean conversion (False if zero vector)"""
        return self.x != 0 or self.y != 0
    
    def __getitem__(self, index):
        """Index access: vector[0] = x, vector[1] = y"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")
    
    def __setitem__(self, index, value):
        """Index assignment"""
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Vector index out of range")
    
    def magnitude(self):
        """Calculate vector magnitude"""
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def normalize(self):
        """Return normalized vector"""
        mag = self.magnitude()
        if mag == 0:
            return Vector(0, 0)
        return Vector(self.x / mag, self.y / mag)


# 4. Properties and Descriptors
class Temperature:
    """Temperature class demonstrating properties"""
    
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Get temperature in Celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius with validation"""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit"""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature in Fahrenheit"""
        self.celsius = (value - 32) * 5/9
    
    @property
    def kelvin(self):
        """Get temperature in Kelvin"""
        return self._celsius + 273.15
    
    @kelvin.setter
    def kelvin(self, value):
        """Set temperature in Kelvin"""
        if value < 0:
            raise ValueError("Temperature in Kelvin cannot be negative")
        self.celsius = value - 273.15
    
    def __str__(self):
        return f"{self._celsius:.1f}°C"


class ValidatedAttribute:
    """Descriptor for validated attributes"""
    
    def __init__(self, validator=None, default=None):
        self.validator = validator
        self.default = default
        self.name = None
    
    def __set_name__(self, owner, name):
        self.name = f"_{name}"
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.name, self.default)
    
    def __set__(self, obj, value):
        if self.validator:
            value = self.validator(value)
        setattr(obj, self.name, value)


def positive_number(value):
    """Validator for positive numbers"""
    if not isinstance(value, (int, float)) or value <= 0:
        raise ValueError("Value must be a positive number")
    return value


def non_empty_string(value):
    """Validator for non-empty strings"""
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Value must be a non-empty string")
    return value.strip()


class Product:
    """Product class using descriptors for validation"""
    
    name = ValidatedAttribute(validator=non_empty_string)
    price = ValidatedAttribute(validator=positive_number)
    quantity = ValidatedAttribute(validator=positive_number, default=1)
    
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_value(self):
        return self.price * self.quantity
    
    def __str__(self):
        return f"{self.name}: ${self.price:.2f} x {self.quantity} = ${self.total_value():.2f}"


# 5. Metaclasses
class SingletonMeta(type):
    """Metaclass that creates singleton instances"""
    
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class DatabaseConnection(metaclass=SingletonMeta):
    """Database connection using singleton pattern"""
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.connection_string = "postgresql://localhost:5432/mydb"
            self.is_connected = False
            print("Database connection instance created")
    
    def connect(self):
        if not self.is_connected:
            self.is_connected = True
            print(f"Connected to {self.connection_string}")
        else:
            print("Already connected")
    
    def disconnect(self):
        if self.is_connected:
            self.is_connected = False
            print("Disconnected from database")
        else:
            print("Not connected")


class AutoPropertyMeta(type):
    """Metaclass that automatically creates properties for private attributes"""
    
    def __new__(mcs, name, bases, namespace):
        # Create properties for attributes starting with underscore
        for attr_name, attr_value in list(namespace.items()):
            if attr_name.startswith('_') and not attr_name.startswith('__'):
                prop_name = attr_name[1:]  # Remove leading underscore
                if prop_name not in namespace:
                    namespace[prop_name] = mcs.create_property(attr_name)
        
        return super().__new__(mcs, name, bases, namespace)
    
    @staticmethod
    def create_property(attr_name):
        """Create a property for the given attribute name"""
        def getter(self):
            return getattr(self, attr_name)
        
        def setter(self, value):
            setattr(self, attr_name, value)
        
        return property(getter, setter)


class Person(metaclass=AutoPropertyMeta):
    """Person class with automatic properties"""
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"


# Demonstration functions
def demonstrate_mro():
    """Demonstrate Method Resolution Order"""
    print("=== Method Resolution Order (MRO) ===")
    print(f"D's MRO: {[cls.__name__ for cls in D.__mro__]}")
    
    d = D()
    result = d.method()
    print(f"Final result: {result}")
    print()


def demonstrate_abc():
    """Demonstrate Abstract Base Classes"""
    print("=== Abstract Base Classes ===")
    
    # This would raise TypeError: Can't instantiate abstract class Vehicle
    # vehicle = Vehicle("Generic", "Model", 2023)
    
    car = Car("Toyota", "Camry", 2023)
    electric_car = ElectricCar("Tesla", "Model 3", 2023, 75)
    
    for vehicle in [car, electric_car]:
        print(f"{vehicle.get_info()}")
        print(f"Start: {vehicle.start_engine()}")
        print(f"Stop: {vehicle.stop_engine()}")
        print()


def demonstrate_magic_methods():
    """Demonstrate Magic Methods"""
    print("=== Magic Methods ===")
    
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 2 = {v1 * 2}")
    print(f"3 * v1 = {3 * v1}")
    print(f"v1 == v2: {v1 == v2}")
    print(f"v1 < v2: {v1 < v2}")
    print(f"len(v1): {len(v1)}")
    print(f"bool(v1): {bool(v1)}")
    print(f"bool(Vector(0, 0)): {bool(Vector(0, 0))}")
    print(f"v1[0] = {v1[0]}, v1[1] = {v1[1]}")
    
    v1[0] = 5
    print(f"After v1[0] = 5: {v1}")
    print()


def demonstrate_properties():
    """Demonstrate Properties and Descriptors"""
    print("=== Properties and Descriptors ===")
    
    # Temperature properties
    temp = Temperature(25)
    print(f"Temperature: {temp}")
    print(f"Fahrenheit: {temp.fahrenheit:.1f}°F")
    print(f"Kelvin: {temp.kelvin:.1f}K")
    
    temp.fahrenheit = 98.6
    print(f"After setting to 98.6°F: {temp}")
    
    # Product with descriptors
    try:
        product = Product("Laptop", 999.99, 2)
        print(f"Product: {product}")
        
        # This will raise ValueError
        # product.price = -100
    except ValueError as e:
        print(f"Validation error: {e}")
    
    print()


def demonstrate_metaclasses():
    """Demonstrate Metaclasses"""
    print("=== Metaclasses ===")
    
    # Singleton pattern
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    print(f"db1 is db2: {db1 is db2}")
    db1.connect()
    
    # Auto-properties
    person = Person("Alice", 30)
    print(f"Person: {person}")
    print(f"Name: {person.name}")
    print(f"Age: {person.age}")
    
    person.name = "Bob"
    person.age = 25
    print(f"Updated person: {person}")
    print()


if __name__ == "__main__":
    print("Advanced Object-Oriented Programming Examples")
    print("=" * 50)
    
    demonstrate_mro()
    demonstrate_abc()
    demonstrate_magic_methods()
    demonstrate_properties()
    demonstrate_metaclasses()
    
    print("All demonstrations completed!")
