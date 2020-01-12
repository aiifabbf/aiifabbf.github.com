# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentinel = ListNode(None)
        head = sentinel
        carry = 0

        while l1 != None or l2 != None:
            summation = carry
            if l1:
                summation += l1.val
                l1 = l1.next
            if l2:
                summation += l2.val
                l2 = l2.next

            if summation >= 10:
                carry = 1
                summation -= 10
            else:
                carry = 0
            head.next = ListNode(summation)
            head = head.next

        if carry == 1:
            head.next = ListNode(1)

        return sentinel.next