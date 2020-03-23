from typing import *

import itertools


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        queue = list(s)
        rows = [[] for _ in range(numRows)]
        rowIndexIterator = itertools.cycle(itertools.chain(
            range(numRows), reversed(range(1, numRows - 1))))

        for i, v in zip(rowIndexIterator, queue):
            rows[i].append(v)

        return "".join(sum(rows, []))
