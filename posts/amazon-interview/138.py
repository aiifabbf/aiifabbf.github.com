"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        sentinel = head # 保存好旧链表头
        oldNewMapping = {
            None: None
        } # key是老节点，value是新节点

        while head: # 第一遍遍历
            oldNewMapping[head] = Node(head.val) # 只要复制出新节点就行，先不要解决引用问题
            head = head.next

        head = sentinel

        while head: # 第二遍遍历，解决引用问题
            oldNewMapping[head].next = oldNewMapping[head.next] # 新节点的next指向旧节点next指向的那个节点对应的新节点
            oldNewMapping[head].random = oldNewMapping[head.random]
            head = head.next # 新节点的random指向旧节点random指向的那个节点对应的新节点

        return oldNewMapping[sentinel] # 返回head对应的新节点