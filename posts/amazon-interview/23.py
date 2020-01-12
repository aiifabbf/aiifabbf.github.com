# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None

        res = lists

        while len(res) != 1:
            temp = []
            if len(res) % 2 == 0:

                for i in range(len(res) // 2):
                    list1 = res[2 * i]
                    list2 = res[2 * i + 1]
                    temp.append(self.merge2Lists(list1, list2))

            else:

                for i in range((len(res) - 1) // 2):
                    list1 = res[2 * i]
                    list2 = res[2 * i + 1]
                    temp.append(self.merge2Lists(list1, list2))

                temp.append(res[-1])
            res = temp

        return res[0]

    def merge2Lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentinel = ListNode(None)
        head = sentinel

        while l1 != None and l2 != None:
            if l1.val > l2.val:
                head.next = l2
                l2 = l2.next
            else:
                head.next = l1
                l1 = l1.next
            head = head.next

        if l1 == None:
            head.next = l2
        else:
            head.next = l1

        return sentinel.next