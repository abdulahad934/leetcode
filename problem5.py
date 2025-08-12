class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is Empty  "
    
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
    


class Stringreverse:
    
    def __init__(self, text):
        
        self.text = text
        self.stack = Stack()
        
    
    def reverse(self):
        for char in self.text:
            self.stack.push(char)
            
        reversed_str = ""
        
        while not self.stack.is_empty():
            reversed_str += self.stack.pop()
            
        return reversed_str


sr = Stringreverse("Hello")

print(sr.reverse())
        
        