from typing import *


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter1 = dict()

        for v in s:
            if v in counter1:
                counter1[v] += 1
            else:
                counter1[v] = 1

        counter2 = dict()

        for v in t:
            if v in counter2:
                counter2[v] += 1
            else:
                counter2[v] = 1

        return counter1 == counter2