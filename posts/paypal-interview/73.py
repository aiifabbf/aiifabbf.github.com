from typing import *

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowCount = len(matrix)
        columnCount = len(matrix[0])

        # 第一行特殊处理
        firstRowClear = False
        if 0 in matrix[0]:
            firstRowClear = True

        # 第一列特殊处理
        firstColumnClear = False
        if any(row[0] == 0 for row in matrix):
            firstColumnClear = True

        for rowIndex, row in enumerate(matrix):

            for columnIndex, box in enumerate(row):
                if box == 0: # 遇到某个0
                    matrix[rowIndex][0] = 0 # 把这行最开头设置成0
                    matrix[0][columnIndex] = 0 # 把这列最开头设置成0

        for rowIndex in range(1, rowCount): # 从第1行开始
            if matrix[rowIndex][0] == 0: # 如果这一行的第一个元素是0

                for columnIndex in range(columnCount): # 整行清零
                    matrix[rowIndex][columnIndex] = 0

        for columnIndex in range(1, columnCount): # 从第1列开始
            if matrix[0][columnIndex] == 0: # 如果这一列的第一个元素是0

                for rowIndex in range(rowCount): # 整列清零
                    matrix[rowIndex][columnIndex] = 0

        # 中间完成之后，再特殊处理第一列和第一行
        if firstColumnClear:

            for rowIndex in range(rowCount):
                matrix[rowIndex][0] = 0

        if firstRowClear:

            for columnIndex in range(columnCount):
                matrix[0][columnIndex] = 0