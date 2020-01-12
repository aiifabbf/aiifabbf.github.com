from typing import *

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0

        while len(arr) != 1:
            largestLeafValue = float("-inf")
            product = float("inf")
            index = -1

            for i in range(0, len(arr) - 1):
                a = arr[i]
                b = arr[i + 1]
                if a * b < product:
                    index = i
                    product = a * b
                    largestLeafValue = max(a, b)

            res += product
            arr[index: index + 2] = [largestLeafValue]

        return res

s = Solution()
print(s.mctFromLeafValues([6, 2, 4])) # 32