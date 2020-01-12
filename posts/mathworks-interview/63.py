from typing import *

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1: # 为了对付屑test case
            return 0

        rowCount = len(obstacleGrid)
        columnCount = len(obstacleGrid[0])
        dp = dict()

        # 初始条件
        dp[0, 0] = 1

        for columnIndex in range(1, columnCount):
            if obstacleGrid[0][columnIndex] == 0:
                dp[0, columnIndex] = dp[0, columnIndex - 1]
            else:
                dp[0, columnIndex] = 0

        for rowIndex in range(1, rowCount):
            if obstacleGrid[rowIndex][0] == 0:
                dp[rowIndex, 0] = dp[rowIndex - 1, 0]
            else:
                dp[rowIndex, 0] = 0

        # 开始填表
        for rowIndex, row in enumerate(obstacleGrid[1: ], 1):

            for columnIndex, box in enumerate(row[1: ], 1):
                if box == 0:
                    dp[rowIndex, columnIndex] = dp[rowIndex - 1, columnIndex] + dp[rowIndex, columnIndex - 1]
                else:
                    dp[rowIndex, columnIndex] = 0

        return dp[rowCount - 1, columnCount - 1]

s = Solution()
print(s.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
])) # 2
print(s.uniquePathsWithObstacles([
    [0, 0, 0],
])) # 1
print(s.uniquePathsWithObstacles([
    [0, 1, 0],
])) # 0
print(s.uniquePathsWithObstacles([[1]])) # 0 屑test case
print(s.uniquePathsWithObstacles([[0]])) # 1 屑test case