# class Queue:
#     def __init__(self):
#         self.items = []
#     def enqueue(self, items):
#         self.items.append(items)
        
#     def dedueue(self):
#         if not self.is_empty():
#             return self.items.pop(0)
#         return "Stack is Empty"
    
#     def peek(self):
#         if not self.is_empty():
#             return self.items[0]
#         return "Queue is Empty"
    
      
#     def is_empty(self):
#         return len(self.items) == 0
    
    
#     def size(self):
#         return len(self.items)
#     def  display(self):
#         return self.items
        
    
    

# q = Queue()

# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# q.enqueue(40)
# print(q.display())
# print("Front:", q.peek())
# print(q.dedueue())
# print(q.dedueue())
# print(q.display())

# print(q.peek())
# print(q.display())
# print(q.size())











class Queue:
    def __init__(self):
        self.items = []
    
    def Enqueue(self, item):
        self.items.append(item)
        
    def Dequeue(self):
        if not self.is_empty():
            return self.items.pop(2)
        
        
    def peek(self):
        if not self.is_empty():
            return self.is_empty[0]
        
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def display(self):
        return self.items
    
    
    
q = Queue()

q.Enqueue(10)
q.Enqueue(20)
q.Enqueue(30)
q.Enqueue(40)
q.Enqueue(50)


print(q.display())
print(q.Dequeue())
print(q.display())


    