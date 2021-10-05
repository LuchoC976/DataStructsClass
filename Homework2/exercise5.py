'''
CLRS 10.1-6
Show how to implement a queue using two stacks. Analyze the running time of the
queue operations.
'''

class StackedQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
 
    # Enqueue into s1
    def enqueue(self, x):
         
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
 
        self.s1.append(x)
 
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()
 
    # Dequeue from s2
    def dequeue(self):

        if len(self.s1) == 0:
            print("Q is Empty")
     
        x = self.s1[-1]
        self.s1.pop()
        return x
