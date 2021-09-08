# Linked list data structure implementation in python

# [e1] -> [e2] -> [None]

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
    
    def set_next(self, next):
        self.next = next

class SingleLinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def printList(self):
        node = self.head
        while node:
            print(node.val)
            node = node.next

    # Insert implementation
    '''
    def insert(self, list, index, node):
        if index == 0:
            node.set_next()
            return SingleLinkedList(node)    
    '''
# Linked list example
# [Jan] -> [Feb] -> [March] -> [None]
m1 = Node("Jan")
m2 = Node("Feb")
m3 = Node("March")

m1.set_next(m2)
m2.set_next(m3)

list1 = SingleLinkedList(m1)

list1.printList()
