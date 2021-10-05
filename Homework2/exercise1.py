'''
1. Given the following implementation of the class PriorityQueue, implement the methods:
insert(v,k) - add an element v with priority k. Complexity O(n)
deleteMin() - remove the element with the lowest $k$ (highest priority). Complexity O(1)
decreaseKey(v,k) - decrease the value of k (increase priority). Complexity O(n)
'''

import ctypes
class PriorityQueue(object):
    def __init__(self, n):
        self.item_count = 0
        self.n = n
        self.queue = self._create_queue(self.n)        
    
    def _create_queue(self, n):
        return (n * ctypes.py_object)()
    
    def enqueue(self, item):
        if self.item_count == self.n:
            raise ValueError("no more capacity")
        self.queue[self.item_count] = item
        self.item_count += 1

    def insert(self, v, k):
        item = {v: k}
        self.enqueue(item)
    
    def deleteMin(self):
        minVal = 0
        for item in self.queue:
            if (item["v"] == minVal):
                pass # pending
    
    def decreaseKey(self, v, k):
        pass # pending


