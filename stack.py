class stack:
    def __init__(self,contents = []):
        self.stack = contents
    
    def is_empty(self):
        return self.stack == []

    def add_card(self, item):
        self.stack.append(item)
    
    def deal_card(self):
        if self.stack != []:
            return self.stack.pop()
        else:
            return self.stack == []
    
    def peek(self):
        return self.stack[len(self.stack)-1]
    
    def size(self):
        return len(self.stack)

    