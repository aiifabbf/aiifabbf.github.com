from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root:
            graph = {root: root}
            queue = [root]

            while queue:
                size = len(queue)

                for i in range(size):
                    node = queue[i]
                    if node.left:
                        queue.append(node.left)
                        graph[node.left] = node
                    if node.right:
                        queue.append(node.right)
                        graph[node.right] = node

                queue = queue[size: ]

            # head = p
            # pathFromP = []

            # while head != graph[head]:
            #     pathFromP.append(head)
            #     head = graph[head]

            # pathFromP.append(root)

            # head = q
            # pathFromQ = []

            # while head != graph[head]:
            #     pathFromQ.append(head)
            #     head = graph[head]

            # pathFromQ.append(root)

            # pathToP = list(reversed(pathFromP))
            # pathToQ = list(reversed(pathFromQ))

            # for i in range(min(len(pathToP), len(pathToQ))):
            #     v = pathToP[i]
            #     w = pathToQ[i]
            #     if v != w:
            #         return pathToP[i - 1]

            # if len(pathToP) <= len(pathToQ):
            #     return pathToP[-1]
            # else:
            #     return pathToQ[-1]
            # diff做法

            nodesOnPathToP = {root} # 把root到p经过的所有节点都记下来
            head = p

            while head != graph[head]:
                nodesOnPathToP.add(head)
                head = graph[head]

            head = q

            while head != graph[head]: # 然后从q开始顺着往上走
                if head in nodesOnPathToP: # 遇到的第一个也是p的祖宗的节点就是p和q最近的公共祖宗
                    return head
                else: # 不是
                    head = graph[head] # 继续往上翻家谱

            return root # 没找到，那只能是root了
        else:
            return None