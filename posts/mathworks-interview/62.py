from typing import *

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rowCount = m
        columnCount = n
        dp = dict()

        dp[0, 0] = 1

        for columnIndex in range(1, columnCount):
            dp[0, columnIndex] = 1

        for rowIndex in range(1, rowCount):
            dp[rowIndex, 0] = 1

        for rowIndex in range(1, rowCount):

            for columnIndex in range(1, columnCount):
                dp[rowIndex, columnIndex] = dp[rowIndex - 1, columnIndex] + dp[rowIndex, columnIndex - 1]

        return dp[rowCount - 1, columnCount - 1]

s = Solution()
print(s.uniquePaths(3, 2)) # 3
print(s.uniquePaths(7, 3)) # 28