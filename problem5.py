class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, items):
        self.items.append(items)
        
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "stack is Empty"
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is Empty"
    
    
    
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def display(self):
        return self.items
    

class parenthecis:
    def __init__(self, expr):
        
        self.expr = expr
        self.stack = Stack()
        
    
    def 
        
    