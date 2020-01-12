class DoubleLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.keyNodeMapping = {} # key是key，value不是value，而是节点的引用，不然做不到所有操作都是O(1)
        self.head = DoubleLinkedListNode(None) # 头虚节点
        self.tail = DoubleLinkedListNode(None) # 尾虚节点
        self.head.previous = None
        self.head.next = self.tail
        self.tail.previous = self.head
        self.tail.next = None
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.keyNodeMapping: # 缓存里存在这个key
            node = self.keyNodeMapping[key] # 取出节点
            # 下面的操作是把节点取出来、放到linked list的最前面
            left = node.previous # left先是节点的前面一个节点
            right = node.next # right先是节点的后面一个节点

            left.next = right # left直接指向right，绕过节点
            right.previous = left # right直接指向left，绕过节点
            # 这样节点就从list里删除了
            # 下面要把节点插入到最前面
            left = self.head # left变成最前面的虚节点
            right = self.head.next # right变成第一个节点

            left.next = node # left指向节点
            right.previous = node # right指向节点
            node.next = right # 节点指向left
            node.previous = left # 节点指向right

            return node.value[1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keyNodeMapping: # 如果key在缓存里面了
            self.get(key) # 先取一次，这样间接做到了把节点放到最前面
            self.keyNodeMapping[key].value = (key, value) # 再更新value的值
            return
        else: # 如果key不在缓存里面
            if len(self.keyNodeMapping) >= self.capacity: # 先看下缓存有没有满，如果满了，要先删掉linked list最后那个节点
                node = self.tail.previous
                left = node.previous
                right = self.tail

                left.next = right
                right.previous = left

                del self.keyNodeMapping[node.value[0]]
            # 建一个新节点，放到linked list的最前面
            node = DoubleLinkedListNode((key, value))
            left = self.head
            right = self.head.next

            node.previous = left
            node.next = right

            left.next = node
            right.previous = node

            self.keyNodeMapping[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)