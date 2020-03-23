from typing import *

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        middle = 0
        right = 0

        while right < len(nums):
            if nums[right] == 0:
                if left == right == middle:
                    pass
                elif left == middle < right:
                    nums[left], nums[right] = nums[right], nums[left]
                elif left < middle == right:
                    nums[left], nums[right] = nums[right], nums[left]
                else: # left < middle < right
                    nums[left], nums[middle], nums[right] = nums[right], nums[left], nums[middle]

                left += 1
                middle += 1
                right += 1
            elif nums[right] == 1:
                if left == right == middle:
                    pass
                elif left == middle < right:
                    nums[left], nums[right] = nums[right], nums[left]
                elif left < middle == right:
                    pass
                else: # left < middle < right
                    nums[middle], nums[right] = nums[right], nums[middle]

                middle += 1
                right += 1
            elif nums[right] == 2:
                right += 1