#Стэк
from time import sleep

class Stack:
    def __init__(self):
        self.elems = list()
    
    def add(self, value):
        #self.elems.append(value)
        self.elems.insert(0, value)

    def get(self):
        #val = self.elems.pop()
        val = self.elems.pop(0)
        return val
    
    def size(self):
        size = len(self.elems)
        return size
    

queue = Stack()
for i in range(10):
    queue.add(i)

for i in range(queue.size()):
    val = queue.get()
    print(val)
    sleep(val)
    