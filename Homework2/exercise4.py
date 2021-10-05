'''
CLRS 10.1-5
Whereas a stack allows insertion and deletion of elements at only one end, and a
queue allows insertion at one end and deletion at the other end, a deque (doubleended queue) allows insertion and deletion at both ends. Write four O.1/-time
procedures to insert elements into and delete elements from both ends of a deque
implemented by an array
'''

class Dequeue:
    def __init__(self, head=None, tail=None, size=0):
        self.head = head
        self.tail = tail
        self.size = size
    
    def head_enqueue(self, item):
        self.head[self.head] = item
        if self.head == 1:
            self.head = self.size
        else:
            self.head = self.size - 1
    
    def tail_enqueue(self, item):
        self.tail[self.tail] = item
        if self.tail == self.size:
            self.tail = 1
        else:
            self.tail = self.tail + 1
    
    def head_dequeue(self, item):
        item = self.head[self.head]
        if self.head == self.size:
            self.head = 1
        else:
            self.head = self.head + 1
    
    def tail_dequeue(self, item):
        item = self.tail[self.tail]
        if self.tail == 1:
            self.tail = self.size
        else:
            self.tail = self.tail - 1