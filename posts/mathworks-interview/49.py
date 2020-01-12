from typing import *

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()

        for v in strs:
            root = "".join(sorted(v))
            if root in res:
                res[root].append(v)
            else:
                res[root] = [v]

        return list(res.values())