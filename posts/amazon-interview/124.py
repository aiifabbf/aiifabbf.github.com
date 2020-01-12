# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = float("-inf")
        queue = [root]

        while queue:
            size = len(queue)

            for _ in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                res = max(res, self.maxPathSumPassingHere(node))

        return res

    def maxPathSumStartingHere(self, root: TreeNode) -> int:
        if root:
            res = root.val
        else:
            return 0

    def maxPathSumPassingHere(self, root: TreeNode) -> int: