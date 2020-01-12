from typing import *

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counter: Dict[Hashable, List[int, int, int]] = {} # key是数字，value是一个list，第一个元素表示key出现的次数、第二个元素表示key第一次出现的位置、第三个元素表示key最后一次出现的位置
        maxFrequency = 0 # 一边构造counter，一边记下最高频次

        for i, v in enumerate(nums):
            if v in counter: # 已经出现过了
                counter[v][0] += 1 # 频次+1
                counter[v][2] = i # 更新最后出现的位置
            else: # 没有见过
                counter[v] = [1, i, i] # 记下来

            maxFrequency = max(maxFrequency, counter[v][0])

        res = float("inf")

        for k, v in counter.items():
            if v[0] == maxFrequency: # 如果是出现频次最高的元素
                res = min(res, v[2] - v[1] + 1) # 最短相同度substring一定是从这个元素第一次出现的位置到最后一次出现的位置之后那个substring

        return res

s = Solution()
print(s.findShortestSubArray([1, 2, 2, 3, 1])) # 2
print(s.findShortestSubArray([1, 2, 2, 3, 1, 4, 2])) # 6