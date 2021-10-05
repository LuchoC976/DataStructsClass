'''
3. Given a linked list, detect if the list has a cycle. 
If a cycle is detected, return the position of the node 
(with respect to the head) where the cycle starts.
'''

class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node
    
    # Traverse works like this as well
    def traverse(self):
        node = self.head
        while node:
            print(node.val, end="")
            node = node.next
    
    def detectLoop(self):
        temp_set = set()
        node = self.head
        i = 0
        while node:
            if (node in temp_set):
                return True, i - 1
            temp_set.add(node)
            i += 1
            node = node.next
        
        return False

llist = LinkedList()
llist.push("Jan")
llist.push("Feb")
llist.push("Mar")
llist.push("Dec")
 
# Create a loop for testing
llist.head.next.next.next = llist.head

found, index = llist.detectLoop()

print("Found: " + str(found) + ", Index: " + str(index))