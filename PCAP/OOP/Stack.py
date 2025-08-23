class Stack:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return len(self.__items) == 0

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.__items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.__items[-1]
        raise IndexError("peek from empty stack")

    def size(self):
        return len(self.__items)

    def __str__(self):
        return str(self.__items)

stack = Stack()
stack.push(1)
stack.push(2)
print(stack)  # Output: [1, 2]
print(stack.pop())  # Output: 2
print(stack.peek())  # Output: 1
print(stack.size())  # Output: 1
print(stack.is_empty())  # Output: False
print(stack)  # Output: [1]
print(stack.pop())  # Output: 1
print(stack.is_empty())  # Output: True