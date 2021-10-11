# Linked list data structure implementation in python

# [e1] -> [e2] -> [None]

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None
    
    def set_next(self, next):
        self.next = next

class SingleLinkedList:
    def __init__(self, head=None):
        self.head = head
    
    # Traverse works like this as well
    def traverse(self):
        node = self.head
        while node:
            print(node.val)
            node = node.next

    # Insert implementation
    
    def insert(self, data, prev_node=None):
        # Adding to start
        add_node = Node(data)
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
    
    # Delete implementation

    def delete(self, prev_node):
        del_node = prev_node.next
        prev_node.next = del_node.next
        del_node.next = None


# Linked list example
# [Jan] -> [Feb] -> [March] -> [None]
m1 = Node("Jan")
m2 = Node("Feb")
m3 = Node("March")

m1.set_next(m2)
m2.set_next(m3)

list1 = SingleLinkedList(m1)

list1.traverse()

print("Inserting node at start (December node)")

list1.insert("Dec")

list1.traverse()

print("Inserting node at end (May node)")

list1.insert("May",m3)

list1.traverse()

print("Inserting in between nodes (April node)")

list1.insert("April",m3)

list1.traverse()

print("Deleting elements (March node)")
list1.delete(m2)

list1.traverse()