from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head:
            sentinel = ListNode(None) # 假节点

            while head: # 不停的抽出原链表的第一个节点，插入到sentinel的后面
                newHead = head.next # 原链表的第二个节点
                head.next = sentinel.next
                sentinel.next = head
                head = newHead

            return sentinel.next

        else:
            return head