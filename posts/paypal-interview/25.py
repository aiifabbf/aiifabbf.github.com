from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        sentinel = ListNode(None)
        sentinel.next = head

        length = 0

        while head:
            length += 1
            head = head.next

        segmentCount = length // k

        lastSegmentLastNode = sentinel
        head = sentinel.next

        for i in range(segmentCount):
            thisSegmentSentinel = ListNode(None)
            thisSegmentLastNode = head

            for j in range(k):
                newHead = head.next
                head.next = thisSegmentSentinel.next
                thisSegmentSentinel.next = head
                head = newHead

            lastSegmentLastNode.next = thisSegmentSentinel.next
            lastSegmentLastNode = thisSegmentLastNode

        lastSegmentLastNode.next = head

        return sentinel.next