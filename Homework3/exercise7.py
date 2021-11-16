# 7. Implemente una clase de Python que defina un arreglo de stacks. La idea de tener este 
# arreglo es que cuando un stack alcance su capacidad máxima, un nuevo stack empieza en el 
# mismo arreglo. Las operación pop() debe retornar el mismo valor que lo haría si estuviéramos 
# usando un stack simple.

class Stack:
    def __init__(self, n):
        self.n = n
        self.item_count = 0
        self.stack = []

    def size(self):
        return self.item_count
    
    def full(self):
        if self.size() == self.n:
            return True
        return False
    
    def empty(self):
        if self.size() == 0:
            return True
        return False
    
    def add(self, item):
        self.stack.append(item)
    
    def pop(self):
        self.stack.pop()

class StackArray:
   def __init__(self, max_array_size=10):
       self.array = []
       self.arr_size = len(self.array)
       self.max_array_size = max_array_size
   
   def size(self):
       return len(self.array)

   def full(self):
       if self.size() == self.max_array_size:
           for i in range(self.size()):
               if not self.array[i].full():
                   return False
           return True
       return False
   
   def empty(self):
       if self.size() == 0:
           return True
       return False
   
   def addStack(self, size=5):
       if self.full():
           print("Array is full")
       else:
           self.array.append(Stack(size))
   
   def push2Arr(self, item):
       for i in range(self.size()):
           if self.array[i].full():
               self.addStack()
               continue
           self.array[i].push(item)
   
   def popFromArr(self):
       for i in range(self.size()):
           if self.array[i].full():
               continue
           self.array[i].pop()