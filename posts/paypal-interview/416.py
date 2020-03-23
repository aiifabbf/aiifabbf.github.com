from typing import *


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summation = sum(nums)
        if summation % 2 != 0:
            return False
        target = summation // 2
        summations = set() # dp[i - 1]

        for v in nums:
            newSummations = {v} # 没有办法一边遍历、一边插入，所以只能先建临时的

            for w in summations:
                if v + w <= target: # 大于t的没必要放进去
                    newSummations.add(v + w)

            summations.update(newSummations)
            if target in summations:
                return True

        return False