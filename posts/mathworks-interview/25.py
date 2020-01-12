from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head != None and k != 1: # 如果k是1的话，等于不需要颠倒
            sentinel = ListNode(None) # 假节点
            sentinel.next = head
            length = 0

            while head != None: # 先遍历一遍链表，得到长度
                head = head.next
                length += 1

            segmentCount = length // k # 需要颠倒的段的数量
            previousSegmentEnd = sentinel # 前一段的最后一个节点

            for segmentIndex in range(segmentCount): # 颠倒那么多段
                head = previousSegmentEnd.next.next
                previous = previousSegmentEnd.next

                for index in range(k - 1): # 因为是分段颠倒，所以每段只需要颠倒k - 1个链
                    temp = head.next
                    head.next = previous

                    previous = head
                    head = temp
                # 颠倒完这一段了，出for之后，head指向的是下一段的第一个节点、previous指向的是当前段颠倒之后的第一个节点

                temp = previousSegmentEnd.next # temp现在是当前段颠倒后的最后一个节点
                previousSegmentEnd.next = previous # 把上一段最后一个节点的下一个节点指向当前段颠倒后的第一个节点
                temp.next = head # 当前段颠倒后的最后一个节点的下一个节点指向下一段的第一个节点
                previousSegmentEnd = temp # 把当前段颠倒后的最后一个节点设置为上一段最后一个节点，进入下一个段

            return sentinel.next
        elif head != None and k == 1:
            return head
        else:
            return head

    # 用于测试
    def linkedListToList(self, head: ListNode) -> List:
        res = []

        while head:
            res.append(head.val)
            head = head.next

        return res

    def listToLinkedList(self, array: List) -> ListNode:
        sentinel = ListNode(None)
        head = sentinel

        for v in array:
            head.next = ListNode(v)
            head = head.next

        return sentinel.next

s = Solution()
print(s.linkedListToList(s.reverseKGroup(s.listToLinkedList([1, 2, 3, 4, 5]), 3))) # 3 2 1 4 5
print(s.linkedListToList(s.reverseKGroup(s.listToLinkedList([1, 2, 3, 4, 5, 6]), 3))) # 3 2 1 6 5 4
print(s.linkedListToList(s.reverseKGroup(s.listToLinkedList([1, 2, 3, 4, 5]), 2))) # 2 1 4 3 5