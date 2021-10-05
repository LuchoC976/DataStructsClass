
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def addTwoNumbers(l1, l2):
    
    head = None
    temp = None
    carry = 0

    while l1 or l2:
        
        sum_value = carry

        if l1:
            sum_value += l1.val
            l1 = l1.next
        if l2:
            sum_value += l2.val
            l2 = l2.next

        node = ListNode(sum_value % 10)
        carry = sum_value // 10

        if temp:
            temp = head = node
        else:
            temp.next = node
            temp = temp.next
            
    if carry > 0:
        temp.next = ListNode(carry)
    return head


list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)

list2 = ListNode(4)
list2.next = ListNode(3)
list2.next.next = ListNode(2)

result = addTwoNumbers(list1, list2)

print("L3: ", end="")
while result:
    print("[" + str(result.val) + "] ->", end="")
    result = result.next