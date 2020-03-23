from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root:
            queue = [root]
            res = []

            while queue:
                levelQueue = []

                for v in queue:
                    if v.left:
                        levelQueue.append(v.left)
                    if v.right:
                        levelQueue.append(v.right)

                res.append([v.val for v in queue])
                queue = levelQueue

            return res
        else:
            return []