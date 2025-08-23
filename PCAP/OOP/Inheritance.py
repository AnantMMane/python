class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    species = "Canis familiaris"

    def __init__(self, name, age, breed="Unknown", color="Unknown"):
        super().__init__(name)
        self.age = age
        self._breed = breed
        self.__color = color
    
    @property
    def breed(self):
        return self._breed
    
    @property
    def color(self):
        return self.__color
    
    @breed.setter
    def breed(self, value):
        self._breed = value

    @color.setter
    def color(self, value):
        self.__color = value
    
    def speak(self):
        return super().speak() + " Woof!"

class Cat(Animal):
    species = "Felis catus"

    def __init__(self, name, age, breed="Unknown", color="Unknown"):
        super().__init__(name)
        self.age = age
        self._breed = breed
        self.__color = color

    def speak(self):
        return super().speak() + " Meow!"

def animal_sound(animal):
    return animal.speak()

my_dog = Dog("Buddy", 3, "Golden Retriever", "Golden")
# Example usage of the Dog class
print(f"My dog's species is {my_dog.species}.")
print(f"My dog's name is {my_dog.name} and he is {my_dog.age} years old.")
print(f"My dog says: {my_dog.speak()}")
print(f"My dog's breed is {my_dog.breed}.")

animal_sound(my_dog)
animal_sound(Cat("Whiskers", 2))