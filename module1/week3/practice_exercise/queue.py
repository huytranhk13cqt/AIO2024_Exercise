class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.capacity

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue Underflow Error")
        return self.queue.pop(0)

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue Overflow Error")
        self.queue.append(value)

    def front(self):
        if self.is_empty():
            raise IndexError("Queue Underflow Error")
        return self.queue[0]


# simulate pointers
queue = MyQueue(capacity=4)
queue.enqueue(31)
queue.enqueue(12)
queue.enqueue(10)
queue.enqueue(20)
print(queue.front())
print(queue.dequeue())
print(queue.front())
print(queue.dequeue())
print(queue.front())

# # simulate example
queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
queue1.enqueue(2)
print(queue1.is_full())
print(queue1.front())
print(queue1.dequeue())
print(queue1.front())
print(queue1.dequeue())
print(queue1.is_empty())
