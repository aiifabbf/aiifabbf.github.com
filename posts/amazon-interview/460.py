class DoubleLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

class LFUCache:

    def __init__(self, capacity: int):
        self.keyNodeMapping = {}
        self.capacity = capacity
        self.head = DoubleLinkedListNode(None)
        self.tail = DoubleLinkedListNode(None)
        self.head.next = self.tail
        self.tail.previous = self.head

    def get(self, key: int) -> int:
        if key in self.keyNodeMapping:
            node = self.keyNodeMapping[key]
            left = node.previous
            right = node.next

            left.next = right
            right.previous = left

            node.value[-1] += 1

            while True:
                if left.previous == None:
                    break
                elif left.value[-1] > node.value[-1]:
                    break
                else:
                    left = left.previous

            left = left
            right = left.next

            node.next = right
            node.previous = left
            left.next = node
            right.previous = node

            return node.value[1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.keyNodeMapping:
            self.get(key)
            self.keyNodeMapping[key].value[1] = value
            return
        else:
            if len(self.keyNodeMapping) >= self.capacity:
                node = self.tail.previous
                left = node.previous
                right = node.next

                left.next = right
                right.previous = left

                del self.keyNodeMapping[node.value[0]]

            node = DoubleLinkedListNode([key, value, 0])
            left = self.tail.previous
            right = self.tail

            left.next = node
            right.previous = node
            node.previous = left
            node.next = right
            self.keyNodeMapping[key] = node
            self.get(key)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)