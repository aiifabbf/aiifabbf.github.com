from typing import *


class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        indices1 = []
        indices2 = []

        for i, v in enumerate(words):
            if v == word1:
                indices1.append(i)
            elif v == word2:
                indices2.append(i)

        return min(abs(i - j) for i in indices1 for j in indices2)