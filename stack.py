class stack:
    def __init__(self,contents = []):
        self.stack = contents
    
    def isEmpty(self):
        return self.stack == []

    def addcard(self, item):
        self.stack.append(item)
    
    def dealCard(self):
        if self.stack != []:
            return self.stack.pop()
        else:
            return self.stack == []
    
    def peek(self):
        return self.stack[len(self.stack)-1]
    
    def size(self):
        return len(self.stack)

    