from typing import *

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        queue = []

        while self.stack:
            queue.append(self.stack.pop())

        res = queue.pop()

        while queue:
            self.stack.append(queue.pop())

        return res

    def peek(self) -> int:
        """
        Get the front element.
        """
        queue = []

        while self.stack:
            queue.append(self.stack.pop())

        res = queue.pop()
        queue.append(res)

        while queue:
            self.stack.append(queue.pop())

        return res

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()