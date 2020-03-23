from typing import *

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def detach(self):
        previous = self.previous
        next = self.next

        if previous == None and next == None:
            return
        elif previous == None and next != None:
            next.previous = None
            self.next = None
        elif previous != None and next == None:
            previous.next = None
            self.previous = None
        else:
            next.previous = previous.next
            previous.next = next.previous
            self.previous = None
            self.next = None

    def insertAfter(self, node: LinkedListNode):
        if not node:
            return

        previous = node
        next = previous.next

        previou.next = self
        self.previous = previous
        if next:
            next.previous = self
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.mapping = {}
        self.head = LinkedListNode(None)
        self.tail = LinkedListNode(None)
        self.tail.insertAfter(self.head)
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1
        else:
            res = key
            node = self.mapping[key]
            node.detach()
            node.insertAfter(self.head)

    def put(self, key: int, value: int) -> None:
        if len(self.mapping) == capacity:
            lastNode = self.tail.previous
            self.mapping.pop(lastNode.value)
            lastNode.detach()

            node = LinkedListNode(value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)