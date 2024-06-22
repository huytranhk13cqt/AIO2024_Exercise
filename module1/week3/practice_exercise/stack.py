class MyStack():
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def pop(self):
        if self.is_empty():
            raise IndexError("Empty Stack Error")
        return self.stack.pop()

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack Overflow Error")
        self.stack.append(value)

    def top(self):
        if self.is_empty():
            raise IndexError("Empty Stack Error")
        return self.stack[-1]


# simulate pointer
stack = MyStack(capacity=4)
stack.push(31)
print(stack.top())
stack.push(12)
print(stack.top())
stack.push(10)
print(stack.top())
stack.push(20)
print(stack.top())
stack.pop()
print(stack.top())
stack.pop()
print(stack.top())

# simulate example
stack1 = MyStack(capacity=5)
stack1.push(1)
stack1.push(2)
print(stack1.is_full())
print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())
print(stack1.is_empty())
