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
        temp.next = self.head
        self.head = temp


    def delete_elem(self, key):
        if self.head.value is None:
             raise Exception('Empty list')

        dummy = Node()
        dummy.next = self.head
        current_node = dummy

        while current_node.next:
            if current_node.next.value == key:
                current_node.next = current_node.next.next
                break
            else:
                current_node = current_node.next

        return dummy.next

    def insert_after(self, key, new_value):

        current_node = self.head

        while current_node:
            if current_node.value == key:
                new_node = Node()
                new_node.value = new_value
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next
        print("Key not found")

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

    def print(self):
        if self.head.value is None:
            print('Empty Linked List')
            return
        print(self.head.value, end=' ')
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            print(current_node.value, end=' ')
        print()

ll = LinkedList()
print(ll.find(0), ll.find(9), ll.find(6), ll.find(19))
print(ll.lenght())
ll.print()
ll.add(9)
print(ll.find(0), ll.find(9), ll.find(6), ll.find(19))
print(ll.lenght())
ll.print()
ll.add(8)
print(ll.find(0), ll.find(9), ll.find(6), ll.find(19))
print(ll.lenght())
ll.print()
ll.add(6)
print(ll.find(0), ll.find(9), ll.find(6), ll.find(19))
print(ll.lenght())
ll.print()
ll.add(4)
print(ll.find(0), ll.find(9), ll.find(6), ll.find(19))
print(ll.lenght())
ll.print()
ll.add(9)
print(ll.find(0), ll.find(9), ll.find(6), ll.find(19))
print(ll.lenght())
ll.print()
ll.add(19)
print(ll.find(0), ll.find(9), ll.find(6), ll.find(19))
print(ll.lenght())
ll.print()
ll.delete_elem(9)
ll.delete_elem(4)
ll.delete_elem(6)
ll.delete_elem(19)
ll.print()
ll.insert_after(9,1)
ll.print()
a = 10


