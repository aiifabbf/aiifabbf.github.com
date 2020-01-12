# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        queue = [s]

        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            if self.isEqualTree(node, t):
                return True

        return False

    def isEqualTree(self, s: TreeNode, t: TreeNode) -> bool:
        if s == None and t == None:
            return True
        elif s != None and t != None:
            return s.val == t.val and self.isEqualTree(s.left, t.left) and self.isEqualTree(s.right, t.right)
        else:
            return False