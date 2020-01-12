# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# class NestedIterator(object):

#     def __init__(self, nestedList):
#         """
#         Initialize your data structure here.
#         :type nestedList: List[NestedInteger]
#         """
#         self.buffer = sum((NestedIterator.flatten(v) for v in nestedList), [])

#     @staticmethod
#     def flatten(array: "NestedIterator") -> "List":
#         if array.isInteger():
#             return [array.getInteger()]
#         else:
#             res = []

#             for v in array.getList():
#                 if v.isInteger():
#                     res.append(v.getInteger())
#                 else:
#                     res.extend(NestedIterator.flatten(v))

#             return res

#     def next(self):
#         """
#         :rtype: int
#         """
#         return self.buffer.pop(0)

#     def hasNext(self):
#         """
#         :rtype: bool
#         """
#         return self.buffer != []

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# 像上面的做法面试里面一定会被批判的，因为太浪费内存了

import collections

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.queue = collections.deque(nestedList) # 搞一个queue

    def next(self) -> int:
        return self.queue.popleft().getInteger() # 只要把第一个元素pop出来就可以了

    def hasNext(self) -> bool:

        while self.queue: # queue当然不能为空
            if self.queue[0].isInteger(): # 如果发现第一个元素已经是integer了
                return True # 那下一次next()就pop这个
            else: # 如果发现第一个元素不是integer
                toExpand = collections.deque(self.queue.popleft().getList()) # 把第一个元素展开
                self.queue = toExpand + self.queue # 展开之后放到最前面。到下一个迭代再来检测第一个元素到底是不是integer，如果还不是的话，继续展开，直到是integer为止

        return False # queue为空说明没有下一个了

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())