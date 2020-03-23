from typing import *

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productAfter = [1]

        for v in reversed(nums):
            productAfter.append(productAfter[-1] * v)

        productAfter.reverse()

        productBefore = 1 # 其实不需要得到每个productBefore[i]，只需要前一项就够了

        for i, v in enumerate(nums):
            productAfter[i] = productBefore * productAfter[i + 1] # 一边遍历一遍覆盖
            productBefore = productBefore * v

        return productAfter[: -1] # 最后一个是1，不用返回