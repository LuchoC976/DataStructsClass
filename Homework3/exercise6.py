# 6. Dada una lista enlazada que represente un número. Por ejemplo, 123 es representado 
# por la lista 1->2->3 si la lista es simple o con doble enlace si es doble. Escriba un 
# programa que haga lo siguiente:
#   1. Reciba dos números A y B como input
#   2. Transforme estos números a listas enlazadas como la definida arriba
#   3. Implemente la resta de los números descritos por esas listas enlazadas. 
#       El resultado (A-B) debe ser almacenado en una lista enlazada.
#   4. Imprima el resultado concatenando el valor de los nodos de la lista enlazada resultante
from typing import List, final


def reverseList(head):
    if head == None or head.next == None:
        return head
    prev, curr = None, head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def substractLists(l1, l2):
    
    head1 = reverseList(l1)
    head2 = reverseList(l2)

    final = None

    while head1 or head2:
        if head1.val > head2.val:
            head1.val += 10
            head2.next.val -= 1
            res = head1.val - head2.val
        else:
            res = head1.val - head2.val

        temp = ListNode(res)

        if final:
            final = temp
        else:
            final.next = temp
            temp = final.next
    
    return final


list1 = ListNode(3)
list1.next = ListNode(4)
list1.next.next = ListNode(2)

list2 = ListNode(1)
list2.next = ListNode(8)
list2.next.next = ListNode(3)

result = substractLists(list1, list2)

print("L3: ", end="")
while result:
    print("[" + str(result.val) + "] ->", end="")
    result = result.next