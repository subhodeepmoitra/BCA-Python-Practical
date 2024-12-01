class Stack:
    def __init__(self):
        self.container = [] #using a list
    
    def push(self, val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def isEmpty(self):
        return len(self.container) == 0 #returns True is length of stack == 0 else False
    
    def size(self):
        return len(self.container)
    
    def printStack(self):
        return self.container
    
s = Stack()
s.push(5)
s.push(10)
#s.push(15)
#s.push(20)
print(s.printStack())
print(s.peek()) #prints the last element
print(s.pop())
print(s.printStack())
print(s.pop())
print(s.isEmpty())