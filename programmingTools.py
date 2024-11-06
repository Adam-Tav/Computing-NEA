import random

class Stack:
#initialises the stack as a list
    def __init__(self):
        self.items = []
#    
    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
    
    def randomise(self):
        random.shuffle(self.items)
        return self.items


def getValuesFromDict(dict:dict, *keys:str):
    values = []
    for key in keys:
        values.append(dict[key])
    return values
