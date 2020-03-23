from typing import *


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) >= 1:
            left = 0 # 左闭
            right = 0 # 右开

            while right < len(nums):
                if nums[right] == 0: # 遇到0
                    right += 1 # 吸收
                elif nums[right] != 0: # 遇到非0
                    nums[left], nums[right] = nums[right], nums[left] # 把右边的非0数和水滴的第一个数字交换位置
                    left += 1
                    right += 1

        else:
            return