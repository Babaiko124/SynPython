# Односвязный список

class Node:
    def __init__(self):
        self.value = None
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = Node()

    def add(self, value):
        if self.head.value is None:
            self.head.value = value
            return
        
        temp = Node()
        temp.value = value
        # current_node = self.head
        # while current_node.next is not None:
        #     current_node = current_node.next
        # current_node.next = temp
        temp.next = self.head
        self.head = temp

    def lenght(self):
        current_node = self.head
        if self.head.value is None:
            size = 0
        else:
            size = 1
        while current_node.next is not None:
            current_node = current_node.next
            size += 1
        return size
    # def get(self):
    #     pass
    def find(self, value):
        if self.head.value is not None:
            if self.head.value == value:
                return True
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            if current_node.value == value:
                return True
        return False

ll = LinkedList()
print(ll.find(0), ll.find(9), ll.find(6), ll.find(19))
print(ll.lenght())
ll.add(9)
print(ll.find(0), ll.find(9), ll.find(6), ll.find(19))
print(ll.lenght())
ll.add(8)
print(ll.find(0), ll.find(9), ll.find(6), ll.find(19))
print(ll.lenght())
ll.add(6)
print(ll.find(0), ll.find(9), ll.find(6), ll.find(19))
print(ll.lenght())
ll.add(4)
print(ll.find(0), ll.find(9), ll.find(6), ll.find(19))
print(ll.lenght())
ll.add(9)
print(ll.find(0), ll.find(9), ll.find(6), ll.find(19))
print(ll.lenght())
ll.add(19)
print(ll.find(0), ll.find(9), ll.find(6), ll.find(19))
print(ll.lenght())
a = 10


