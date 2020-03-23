from typing import *

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productBefore = [1]
        
        for v in nums:
            productBefore.append(productBefore[-1] * v)

        productAfter = [1]

        for v in reversed(nums):
            productAfter.append(productAfter[-1] * v)

        productAfter.reverse()

        res = []

        for i, v in enumerate(nums):
            res.append(productBefore[i] * productAfter[i + 1])

        return res