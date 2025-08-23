class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed="Unknown", color="Unknown"):
        self.name = name
        self.age = age
        self._breed = breed
        self._color = color
    
    def __str__(self):
        return f"{self.name} is a {self.breed} dog, {self.age} years old, and {self.color} in color."
    
    def __repr__(self):
        return f"Dog(name={self.name}, age={self.age}, breed={self.breed}, color={self.color})"
    
    def __eq__(self, other):
        if isinstance(other, Dog):
            return self.name == other.name and self.age == other.age
        return False
    
    def __lt__(self, other):
        if isinstance(other, Dog):
            return self.age < other.age
        return NotImplemented
    
    def __hash__(self):
        return hash((self.name, self.age, self.breed, self.color))
    
    def __len__(self):
        return self.age
    
    def __getitem__(self, key):
        if key == 'name':
            return self.name
        elif key == 'age':
            return self.age
        elif key == 'breed':
            return self.breed
        elif key == 'color':
            return self.color
        else:
            raise KeyError(f"Invalid key: {key}")
     
    def __setitem__(self, key, value):
        if key == 'name':
            self.name = value
        elif key == 'age':
            self.age = value
        elif key == 'breed':
            self.breed = value
        elif key == 'color':
            self.color = value
        else:
            raise KeyError(f"Invalid key: {key}")
    
    def __delitem__(self, key):
        if key == 'name':
            del self.name
        elif key == 'age':
            del self.age
        elif key == 'breed':
            del self.breed
        elif key == 'color':
            del self.color
        else:
            raise KeyError(f"Invalid key: {key}")
    
    def __contains__(self, item):
        return item in (self.name, self.age, self.breed, self.color)
    
    def __iter__(self):
        yield self.name
        yield self.age
        yield self.breed
        yield self.color

    def __next__(self):
        if not hasattr(self, '_iter_index'):
            self._iter_index = 0
        if self._iter_index < 4:
            result = [self.name, self.age, self.breed, self.color][self._iter_index]
            self._iter_index += 1
            return result
        else:
            raise StopIteration
    
    def __reversed__(self):
        return reversed([self.name, self.age, self.breed, self.color])
    
    def __call__(self, *args, **kwargs):
        return f"{self.name} is called with arguments: {args} and keyword arguments: {kwargs}"
    
    def __del__(self):
        print(f"{self.name} is being deleted.")
        del self.name
        del self.age
        del self._breed
        del self._color

    def __enter__(self):
        print(f"Entering context with {self.name}.")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Exiting context with {self.name}.")
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        return True
    
    def __sizeof__(self):
        return super().__sizeof__() + sum(len(str(attr)) for attr in (self.name, self.age, self.breed, self.color))
    
    def __format__(self, format_spec):
        return f"{self.name} ({self.breed}, {self.age} years old, {self.color})".format(format_spec)
    
    def __getattr__(self, name):
        if name == 'info':
            return f"{self.name} is a {self._breed} dog, {self.age} years old, and {self._color} in color."
        raise AttributeError(f"{name} not found in Dog class.")
    
    def __setattr__(self, name, value):
        if name in ('name', 'age', '_breed', '_color'):
            super().__setattr__(name, value)
        elif name == 'breed':
            super().__setattr__('_breed', value)
        elif name == 'color':
            super().__setattr__('_color', value)
        else:
            raise AttributeError(f"Cannot set attribute {name} in Dog class.")
        
    def __delattr__(self, name):
        if name in ('name', 'age', '_breed', '_color'):
            super().__delattr__(name)
        else:
            raise AttributeError(f"Cannot delete attribute {name} in Dog class.")
        
    def __copy__(self):
        new_dog = Dog(self.name, self.age, self.breed, self.color)
        return new_dog
    
    def __deepcopy__(self, memo):
        from copy import deepcopy
        new_dog = Dog(deepcopy(self.name, memo), deepcopy(self.age, memo), 
                      deepcopy(self.breed, memo), deepcopy(self.color, memo))
        return new_dog
    
    def __reduce__(self):
        return (self.__class__, (self.name, self.age, self.breed, self.color))
    
    def __reduce_ex__(self, protocol):
        return self.__reduce__()
    
    def __dir__(self):
        return super().__dir__() + ['bark', 'breed', 'color', 'species']
    
    def __sizeof__(self):
        return super().__sizeof__() + sum(len(str(attr)) for attr in (self.name, self.age, self.breed, self.color)) 
    
    def __getstate__(self):
        return (self.name, self.age, self.breed, self.color)
    
    def __setstate__(self, state):
        self.name, self.age, self.breed, self.color = state

if __name__ == "__main__":
    print("This runs when the file is executed directly.")
    my_dog = Dog("Buddy", 3, "Golden Retriever", "Golden")
    # Example usage of the Dog class
    print(my_dog)  # Using __str__
    print(repr(my_dog))  # Using __repr__   