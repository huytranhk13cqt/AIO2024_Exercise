# Q1. -> C

```python
import torch
import torch.nn as nn

data = torch.Tensor([1, 2, 3])
softmax_function = nn.Softmax(dim=0)
output = softmax_function(data)
assert round(output[0].item(), 2) == 0.09
print(output)
```

# Q2 -> B

```python
import torch
import torch.nn as nn


class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return nn.functional.softmax(x, dim=0)


data = torch.Tensor([5, 2, 4])
my_softmax = MySoftmax()
output = my_softmax(data)
assert round(output[-1].item(), 2) == 0.26
print(output)
```

# Q3 -> C

```python
import torch
import torch.nn as nn


class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        exp_x = torch.exp(x - torch.max(x))
        return exp_x / exp_x.sum(dim=0)


data = torch.Tensor([1, 2, 300000000])
my_softmax = MySoftmax()
output = my_softmax(data)
assert round(output[0].item(), 2) == 0.0
print(output)
```

# Q4 -> B

```python
import torch
import torch.nn as nn


class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_max = torch.max(x, dim=0, keepdim=True)
        x_exp = torch.exp(x - x_max.values)
        partition = x_exp.sum(0, keepdim=True)
        return x_exp / partition


data = torch.Tensor([1, 2, 3])
softmax_stable = SoftmaxStable()
output = softmax_stable(data)
assert round(output[-1].item(), 2) == 0.67
print(output)
```

# Q5 -> A

```python
from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        print(
            f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}")


student1 = Student(name="studentZ2023", yob=2011, grade="6")
assert student1._yob == 2011
student1.describe()
```

# Q6 -> B

```python
from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self._subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}")


teacher1 = Teacher(name="teacherZ2023", yob=1991, subject="History")
assert teacher1._yob == 1991
teacher1.describe()
```

# Q7 -> A

```python
from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name, yob)
        self._specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}")


doctor1 = Doctor(name="doctorZ2023", yob=1981, specialist="Endocrinologists")
assert doctor1._yob == 1981
doctor1.describe()
```

# Q8 -> C

```python
from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        print(
            f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}")


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self._subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}")


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name, yob)
        self._specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}")


class Ward:
    def __init__(self, name: str):
        self._name = name
        self._listPeople = []

    def add_person(self, person: Person):
        self._listPeople.append(person)

    def describe(self):
        print(f"Ward Name: {self._name}")
        for p in self._listPeople:
            p.describe()

    def count_doctor(self):
        return sum(1 for p in self._listPeople if isinstance(p, Doctor))


student1 = Student(name="studentA", yob=2010, grade="7")
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")

ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)

ward1.describe()
print(f"Number of doctors: {ward1.count_doctor()}")
```

# Q9 -> B

```python
class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack is full")
        self.__stack.append(value)

stack1 = MyStack(capacity=5)
stack1.push(1)
assert stack1.is_full() == False
stack1.push(2)
print(stack1.is_full())
```

# Q10 -> B

```python
class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_empty(self):
        return len(self.__stack) == 0

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack is full")
        self.__stack.append(value)

    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.__stack[-1]


stack1 = MyStack(capacity=5)
stack1.push(1)
assert stack1.is_full() == False
stack1.push(2)
print(stack1.top())
```

# Q11 -> A

```python
class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue is full")
        self.__queue.append(value)

queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
assert queue1.is_full() == False
queue1.enqueue(2)
print(queue1.is_full())
```

# Q12 -> D

```python
class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def isEmpty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        return self.__queue.pop(0)

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue is full")
        self.__queue.append(value)

    def front(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        return self.__queue[0]


queue1 = MyQueue(capacity=5)
queue1.enqueue(1)
assert queue1.is_full() == False
queue1.enqueue(2)
print(queue1.front())
```
