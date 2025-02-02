#Stacks

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self): # Look at the last item
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
data = Stack()
data.push(5)
data.push(10)
data.push(15)
data.push(20)

print(data.)

# data = []
# data.append(5)
# data.append(10)
# data.append(15)
# data.append(20)

# print(data)

# data.pop()
# print(data)



#Queues

animals = []
animals.append("cat")
animals.append("dog")
animals.append("fish")
print(animals)

animals.pop(0)
print(animals)

#Using Deque

from collections import deque

numbers = deque()
numbers.append(5)
numbers.append(10)
numbers.append(15)
numbers.append(20)

print(numbers)

value = numbers.popleft()
print(value,numbers)