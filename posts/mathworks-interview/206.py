from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head:
            previous = head # previous指向第一个节点
            head = head.next # head指向第二个节点

            previous.next = None # 第一个节点颠倒之后变成最后一个节点，最后一个节点后面没有节点了

            while head:
                temp = head.next
                head.next = previous
                
                previous = head
                head = temp

            # 出while之后，head是null，previous是颠倒后的第一个节点

            return previous # 所以返回previous
        else:
            return head