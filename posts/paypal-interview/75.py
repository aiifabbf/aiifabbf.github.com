from typing import *

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for v in [1, 2]:
            left = 0
            right = 0

            while right < len(nums):
                if nums[right] == v:
                    right += 1
                else:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right += 1