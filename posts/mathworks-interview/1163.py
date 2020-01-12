from typing import *

# import heapq

# class Node:
#     def __init__(self):
#         self.children: Dict[str, Node] = {}
#         self.heap: List[str] = []
#         heapq.heapify(self.heap)
#         self.value: Any = None

# class Solution:
#     def lastSubstring(self, s: str) -> str:
#         suffixTree = self.getSuffixTree(s)
#         res = []
#         head = suffixTree

#         while len(head.children) != 0:
#             largest = heapq.nlargest(1, head.heap)[0]
#             res.append(largest)
#             head = head.children[largest]

#         return "".join(res)[: -1]

#     def getSuffixTree(self, s: str) -> Node:
#         root = Node()

#         for i in reversed(range(0, len(s))):
#             suffix = s[i: ]
#             head = root

#             for v in suffix + "\x00":
#                 if v not in head.children:
#                     head.children[v] = Node()
#                     heapq.heappush(head.heap, v)
#                 head = head.children[v]

#         return root
# 后缀树构造太慢了

class Solution:
    def lastSubstring(self, s: str) -> str:
        ranks = self.getRankArray(s) # ranks[i]表示s[i: ]按字典序从小到大排序后的排名
        
        for i, v in enumerate(ranks):
            if v == len(s) - 1:
                return s[i: ]

    def getRankArray(self, s: str) -> List[int]:
        k = 1
        xy = list(s)
        rankMapping = dict((v, i) for i, v in enumerate(sorted(set(xy))))

        while True:
            # rank = [rankMapping[v] for v in xy]
            # if len(rank) == len(set(rank)):
            if len(rankMapping) == len(s):
                return [rankMapping[v] for v in xy]
            else:

                for i in range(len(xy)):
                    if i + k < len(s):
                        # xy[i] = (rank[i], rank[i + k])
                        xy[i] = (rankMapping[xy[i]], rankMapping[xy[i + k]])
                    else:
                        # xy[i] = (rank[i], 0)
                        xy[i] = (rankMapping[xy[i]], 0)

                # rankMapping = dict((v, i) for i, v in enumerate(sorted(set(xy))))
                rankMapping.clear()

                for i, v in enumerate(sorted(set(xy))):
                    rankMapping[v] = i

                k += 1

s = Solution()
print(s.lastSubstring("abab")) # bab
print(s.lastSubstring("leetcode")) # tcode