class ExampleClass:
    __counter = 0
    def __init__(self, val = 1):
        self.first = val
        ExampleClass.__counter += 1

    def set_second(self, val):
        self.second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5

print(example_object_1.__dict__, "Counter:", ExampleClass.__counter)
print(example_object_2.__dict__, "Counter:", ExampleClass.__counter)
print(example_object_3.__dict__, "Counter:", ExampleClass.__counter)

ExampleClass.__counter = 10
print("After changing class variable:", ExampleClass.__counter)