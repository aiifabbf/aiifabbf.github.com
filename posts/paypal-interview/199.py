from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root:
            queue = [root]
            res = []

            while queue:
                size = len(queue)

                for i in range(size):
                    node = queue.pop(0)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                    if i == size - 1: # 如果是最右边的节点
                        res.append(node.val)

            return res
        else:
            return []