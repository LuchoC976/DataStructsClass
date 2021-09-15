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
    
    # Traverse works like this as well
    def printList(self):
        node = self.head
        while node:
            print(node.val)
            node = node.next

    # Insert implementation
    
    def insert(self, add_node, prev_node=None):
        # Adding to start
        if prev_node == None:
            add_node.set_next(self.head)
            self.head = add_node
        else:
            # Adding to end
            if prev_node.next == None:
                prev_node.next = add_node
            else:
                # Adding in between nodes
                temp = prev_node.next
                prev_node.next = add_node
                add_node.next = temp
            


# Linked list example
# [Jan] -> [Feb] -> [March] -> [None]
m1 = Node("Jan")
m2 = Node("Feb")
m3 = Node("March")

m1.set_next(m2)
m2.set_next(m3)

list1 = SingleLinkedList(m1)

list1.printList()

print("Inserting node at start (December node)")
m4 = Node("Dec")


list1.insert(m4)

list1.printList()

print("Inserting node at end (May node)")

m5 = Node("May")
list1.insert(m5,m3)

list1.printList()

print("Inserting in between nodes (April node)")

m6 = Node("April")
list1.insert(m6,m3)

list1.printList()