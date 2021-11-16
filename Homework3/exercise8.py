# 8. Implemente los métodos enqueue y decreaseKey, tal que ambos métodos tengan complejidad O(log(n)),
# sin utilizar funciones nativas de Python. Por ejemplo, si necesita hacer una búsqueda, 
# no use la función de Python que implementa esto, programe la función usando for o while loops.

import ctypes

class PriorityQueue(object):

    """

    Implementation of the queue data structure

    """

    def __init__(self, n):

        self.item_count = 0

        self.n = n

        self.queue = self._create_queue(self.n)

    def _create_queue(self, n):

        """

        Creates a new stack of capacity n

        """
        return (n * ctypes.py_object)()

    def dequeue(self):

        """

        Remove an element from the queue

        """

        c = self.queue[0]

        for i in range(1,self.item_count):

            self.queue[i-1] = self.queue[i]

            self.queue[self.item_count - 1] = ctypes.py_object

            self.item_count -= 1

        return c

    def enqueue(self, k, v):
        if self.item_count == self.n:
            print("No capacity")
        self.queue[self.item_count] = (k, v)
        self.item_count += 1

    def decreaseKey(self, k, v):
        for i in range(self.item_count):
            if k == self.queue[i]:
                self.queue[i] = (k-1, v)
            else:
                "No existe el valor" 
