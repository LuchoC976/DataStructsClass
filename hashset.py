# Hash set implementation in Python

class HashSet:
    def __init__(self):
        self.arr = [[] for _ in range(1000000)]
 
    def add(self, key):
        subkey = key % 1000
        if not self.contains(key):
            self.arr[subkey].append(key)

    def remove(self, key):
        subkey = key % 1000
        if self.contains(key):
            self.arr[subkey].remove(key)
    
    def contains(self, key):
        subkey = key % 1000

        return key in self.arr[subkey]

ob = HashSet()
ob.add(1)
ob.add(3)
print(ob.contains(1))
print(ob.contains(2))
ob.add(2)
print(ob.contains(2))
ob.remove(2)
print(ob.contains(2))