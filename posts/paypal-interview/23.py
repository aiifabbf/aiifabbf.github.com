from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 删掉所有空链表
        i = 0

        while i < len(lists):
            if lists[i] == None: # 发现空链表
                lists[i], lists[-1] = lists[-1], lists[i] # 就和最后一个交换
                lists.pop() # 然后删掉
            else:
                i += 1

        if not lists: # 如果没有链表了
            return None # 直接返回

        sentinel = ListNode(None)
        head = sentinel

        while len(lists) != 1: # 直到合并成一个大链表为止
            newLists = []

            for i in range(len(lists) // 2):
                newLists.append(self.merge2LinkedLists(lists[i * 2], lists[i * 2 + 1]))

            if len(lists) % 2 != 0:
                newLists.append(lists[-1])

            lists = newLists

        return lists[0]

    def merge2LinkedLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1:
            return list2
        elif not list2:
            return list1

        sentinel = ListNode(None)
        head = sentinel

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next

        if list1 == None:
            head.next = list2
        else:
            head.next = list1

        return sentinel.next