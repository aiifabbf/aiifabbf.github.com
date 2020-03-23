from typing import *

import itertools

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        integrals = [0] + list(itertools.accumulate(nums))
        minIntegral = 0 # 至今为止见到的最小的积分值
        res = float("-inf")

        for v in integrals[1: ]:
            res = max(res, v - minIntegral) # 以第i个元素结尾的累加和最大的substring的累加和是第i个积分值减去前面见过的最小的积分值
            minIntegral = min(minIntegral, v)

        return res