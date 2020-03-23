from typing import *


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0: # 绝对值不可能小于0
            return 0
        elif k == 0: # 等于0的时候特殊处理
            counter = dict()

            for v in nums:
                if v in counter:
                    counter[v] += 1
                else:
                    counter[v] = 1

            return sum(1 for k, v in counter.items() if v >= 2) # 数一下有多少个数出现的次数大于等于2的
        else: # k > 0
            seen = set(nums)
            array = sorted(seen)
            res = 0

            for v in array:
                if v + k in seen: # 永远往大的方向看，这样就不会重复计数了
                    res += 1

            return res