from typing import *


import bisect


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if not row:
                continue
            if row[0] <= target <= row[-1]:
                index = bisect.bisect_left(row, target)
                if 0 <= index < len(row):
                    if row[index] == target:
                        return True
                    else:
                        continue
                else:
                    continue
            elif target < row[0]:
                return False
            elif row[-1] < target:
                continue

        return False