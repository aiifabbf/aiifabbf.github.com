# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        if self.iterator.hasNext():
            self.buffer = self.iterator.next() # 先把内部迭代器的第一个元素取出来放到cache里
        else:
            self.buffer = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.buffer # peek的时候返回cache就好了

    def next(self):
        """
        :rtype: int
        """
        res = self.buffer # 返回cache

        if self.iterator.hasNext():
            self.buffer = self.iterator.next() # 并且把cache设置为内部迭代器的下一个元素
        else:
            self.buffer = None

        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.buffer) # cache不为空，就可以取

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].