from typing import *

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []:
            return []

        rowCount = len(matrix)
        columnCount = len(matrix[0])

        if columnCount == 0: # 可能会是 [[], [], []]
            return []

        if rowCount == 1 and columnCount == 1: # 1x1的特殊处理
            return [matrix[0][0]]
        elif rowCount == 1 and columnCount > 1: # 1xn的特殊处理
            return matrix[0]
        elif rowCount > 1 and columnCount == 1: # nx1的特殊处理
            return sum(matrix, [])
        else: # rowCount > 1 and columnCount > 1
            indiceIterator = [(0, i) for i in range(columnCount - 1)]
                + [(i, columnCount - 1) for i in range(rowCount - 1)]
                + [(rowCount - 1, i) for i in reversed(range(1, columnCount))]
                + [(i, 0) for i in reversed(range(1, rowCount))]

            res = []

            for i, j in indiceIterator: # 剥开洋葱的最外层
                res.append(matrix[i][j])

            # 然后要删掉我们刚才已经剥掉的部分

            matrix.pop() # 删掉第一行
            matrix.pop(0) # 删掉最后一行

            for v in matrix: # 删掉每一行的第一个元素和最后一个元素
                v.pop()
                v.pop(0)

            res.extend(self.spiralOrder(matrix)) # 剥开内层
            return res
