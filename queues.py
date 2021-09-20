# Queues implementation in Python
    
class Queue:
    def __init__(self, n):
        self.items = []
        self.item_count = 0
        self.n = n
        for i in range(n):
            self.items.append(None)
    
    def printQueue(self):
        if self.empty():
            print("Queue is empty")
        num = 0
        output = ""
        while (num != self.item_count):
            output += str(self.items[num]) + " <- "
            num += 1
        return output[:-4]

    def enqueue(self, item):
        self.items[self.item_count] = item
        self.item_count += 1

    def dequeue(self):
        deq_value = self.items[0]
        for i in range(1, self.item_count):
             self.items[i-1] = self.items[i]

        self.item_count -= 1
        return deq_value
    
    def first(self):
        return self.items[0]

    def full(self):
        if self.item_count == self.n:
            return True
        return False

    def empty(self):
        if self.item_count == 0:
            return True
        return False

    def size(self):
        return self.item_count

# Queues test
q = Queue(10)

# Enqueue
q.enqueue(1)
q.enqueue(2)
q.enqueue(4)

print("Enqueue test: " + q.printQueue())

# Dequeue
q.dequeue()

print("Dequeue test: " + q.printQueue())

# First
print("First test: " + str(q.first()))
print("Queue: " + q.printQueue())

# Empty and full
print("Empty queue: " + str(q.empty()))

print("Full queue: " + str(q.full()))

q.enqueue(5)
q.enqueue(6)

print("Queue: " + q.printQueue())

# Size
print("Queue size: " + str(q.size()))