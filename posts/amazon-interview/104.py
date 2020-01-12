class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            queue = [root]
            depth = 0

            while queue:
                size = len(queue)

                for _ in range(size):
                    node = queue.pop(0)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                
                depth += 1

            return depth
        else:
            return 0