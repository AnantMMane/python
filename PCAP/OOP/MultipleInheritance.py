class A:
    def do(self):
        return "A's do()"

class B:
    def do(self):
        return "B's do()"

class C(A, B):
    pass

c = C()
print(c.do())  # This will call A's do() method due to method resolution order
print(C.__mro__)  # This will show the method resolution order, confirming A is first
print(c.__class__.__mro__)  # This will also show the method resolution order for the instance
print(c.__class__.__bases__)  # This will show the base classes of the class C
print(c.__class__.__name__)  # This will print the name of the class C
print(c.__class__.__module__)  # This will print the module where class C is defined
print(c.__class__.__dict__)  # This will print the class dictionary of C, showing
