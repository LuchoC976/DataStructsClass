# Stacks implementation with python

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
    # For stacks there is no set_next()

# Stack class implementation
class Stack:
    def __init__(self, head=None):
        self.head = head
        if self.head:
            self.item_count = 1
        else:
            self.item_count = 0
    
    def printStack(self):
        curr = self.head
        output = ""
        while curr:
            output += str(curr.val) + " -> "
            curr = curr.next
        return output[:-4]

    def size(self):
        return self.item_count

    def empty(self):
        if self.item_count == 0:
            return True
        return False
    
    def top(self):
        if self.empty():
            print("Stack is empty")
        return self.head.val

    def push(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node
        self.item_count += 1

    def pop(self):
        if self.empty():
            print("Stack is empty")
        popped = self.head
        self.head = popped.next
        self.item_count -= 1
        return popped.val

# Stacks test
s1 = Stack(Node("1"))
print("Empty stack: " + str(s1.empty()))
print("Stack size 1: " + str(s1.size()))
print("Stack top 1:", s1.top())
print(s1.printStack())

s1.push(2)
print("Stack size 2: " + str(s1.size()))
print("Stack top 2:", s1.top())
print(s1.printStack())

s1.push(3)
print("Stack size 3: " + str(s1.size()))
print("Stack top 3:", s1.top())
print(s1.printStack())

s1.pop()
print("Stack size 4: " + str(s1.size()))
print("Stack top 4:", s1.top())
print(s1.printStack())

# Stacks exercise: check if string works -> "([{}])({[()]})"

s = "(){[]}({[]})"

def convert(character):
    if character == ")":
        return "("
    elif character == "]":
        return "["
    elif character == "}":
        return "{"
    else:
        return False

def checkString(my_str):
    stack = Stack()
    opening = ['(', '[', '{']
    for c in my_str:
        if c in opening:
            stack.push(c)
        elif (not stack.empty() and stack.top() == convert(c)):
            stack.pop()
        else:
            return False
    return stack.empty()
    
print(checkString(s))
