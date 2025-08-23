class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed="Unknown", color="Unknown"):
        self.name = name
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
    
    def bark(self):
        return "Woof!"

my_dog = Dog("Buddy", 3)
# Example usage of the Dog class
print(f"My dog's species is {my_dog.species}.")
print(f"My dog's name is {my_dog.name} and he is {my_dog.age} years old.")
print(f"My dog says: {my_dog.bark()}")
print(f"My dog's breed is {my_dog.breed}.")
my_dog.breed = "Golden Retriever"   
print(f"My dog's new breed is {my_dog.breed}.")
print(f"My dog's color is {my_dog.color}.") 
my_dog.__color = "Golden"
print(f"My dog's new color is {my_dog.color}.")